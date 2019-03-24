import os
import sys
import time
from collections import deque
from threading import Condition
import grpc
from . import IVGrpc_pb2
from . import IVGrpc_pb2_grpc
from .authorizer import IVAuthorizer
from .IVRPC import RPCMessageID

class IVFTPService(IVGrpc_pb2_grpc.FTPRPCServicer):

    def __init__(self):
        self.auth = IVAuthorizer()

    def Login(self, request, context):
        response = IVGrpc_pb2.PResponse(retID = 0, result="")
        response.retID,  response.result = self.auth.login_user(request.name, request.psw)
        return response

    def Logout(self, request, context):
        return IVGrpc_pb2.PString(value = self.auth.logout_user(request.name, request.psw))

    def FTPCmd(self, request, context):
        metadata = context.invocation_metadata()
        ftp = self.auth.get_ftp_handler(metadata[0].value, metadata[1].value)
        response = IVGrpc_pb2.PResponse(retID = 0, result="not login")
        if(ftp):
            response.retID,  response.result = ftp.ftp_CMD(request.msgID, request.msg)
        return response 

    def FTPList(self, request, context):    
        metadata = context.invocation_metadata()
        ftp = self.auth.get_ftp_handler(metadata[0].value, metadata[1].value)
        response = IVGrpc_pb2.PFileList(result="not login")
        if(ftp):
            response.result = ftp.ftp_LIST(request.msgID, request.msg, response.files)
        return response 

    def FTPDownload(self, request, context):
        metadata = context.invocation_metadata()
        ftp = self.auth.get_ftp_handler(metadata[0].value, metadata[1].value)
        if(ftp):        
            return ftp.ftp_RETR(request.value, context)
        return 
           
    def FTPUpload(self, request_iterator, context):
        metadata = context.invocation_metadata()
        ftp = self.auth.get_ftp_handler(metadata[0].value, metadata[1].value)
        name = metadata[2].value
        response = IVGrpc_pb2.PResponse(retID = 0, result="not login")
        if(ftp):
            response.retID,  response.result = ftp.ftp_STOR(request_iterator, name)
        if(response.retID == 0):
            print("Upload " + name + ":"  + response.result)
        return response    

class locked_deque:
    def __init__(self):
        self._queue = deque()
        self.cv = Condition()
        return

    def isempty(self):
       return not bool(self._queue)

    def pop(self):
        with self.cv:
            if(self.isempty()):
                self.cv.wait()
            if(self.isempty()):
                return None
            return self._queue.popleft()

    def append(self, item):
        with self.cv:
            self._queue.append(item)
            self.cv.notifyAll()
    
    def wait(self, t):
        with self.cv:
            self.cv.wait(t)
  

class IVDataService(IVGrpc_pb2_grpc.DataRPCServicer):

    def __init__(self):
        self.client_queue = locked_deque()
        self.continue_link = True
        self.msg_response_list = {}
        self.msg_response_list[RPCMessageID.IPCMsg_PY_DebugWait] = self.ResponseDebugMsg
        self.msg_response_list[RPCMessageID.IPCMsg_Debug_Info] = self.ResponseDebugMsg
        self.msg_response_list[RPCMessageID.IPCMsg_Debug_PostInfo] = self.PostDebugMsg
        self.msg_response_list[RPCMessageID.IPCMsg_PY_ReadLine] = self.ResponseReadlineMsg
        self.response_msg = None
        self.stream_msg_callback = None
        self.stream_msg = None
        self.send_msg = None
        self.current_rsp_id = 0
        self.current_debug_rsp = 0
        self.callback_func = None
        self.rpc_send_cv = Condition()
        self.rpc_rev_cv = Condition()
        self.rpc_res_cv = Condition()

    def stop_link(self): 
        self.continue_link = False
        with self.rpc_send_cv:
            self.rpc_send_cv.notifyAll()
        with self.rpc_rev_cv:
            self.rpc_rev_cv.notifyAll()
        with self.rpc_res_cv:
            self.rpc_res_cv.notifyAll() 

    def get_ready(self):
        with self.rpc_rev_cv:
            self.rpc_rev_cv.wait()

    def PostDebugMsg(self, msg):
        if (self.callback_func):
            self.callback_func(msg)

    def ResponseDebugMsg(self, msg):
        with self.rpc_res_cv:
            if(len(msg.int_data) == 1):
                self.current_debug_rsp = msg.int_data[0]
            self.rpc_res_cv.notifyAll()

    def ResponseReadlineMsg(self, msg):
        with self.rpc_res_cv:
            self.response_msg = msg
            self.rpc_res_cv.notifyAll()

    def SetCallback(self, callback):
        self.callback_func = callback

    #send to client no response
    def PostMsgToClient(self, msg):
        with self.rpc_send_cv:
            while((self.send_msg or self.stream_msg) and self.continue_link):
                self.rpc_send_cv.wait(0.2)
            self.send_msg = msg
            self.rpc_send_cv.notifyAll()

    def PostMsgStreamToClient(self, msg, msg_stream_call):
        with self.rpc_send_cv:
            while((self.send_msg or self.stream_msg) and self.continue_link):
                self.rpc_send_cv.wait(0.2)
            self.stream_msg_callback = msg_stream_call
            self.stream_msg = msg
            self.rpc_send_cv.notifyAll()
        while(self.stream_msg and self.continue_link):
            time.sleep(0.1)

    #send to client with response
    def GetResponse(self, msg, timeout = 4000):
        id = msg.msgID
        with self.rpc_rev_cv:
            with self.rpc_send_cv:
                while((self.send_msg or self.stream_msg) and self.continue_link):
                    self.rpc_send_cv.wait(0.2)
                msg.msgID |= RPCMessageID.IPCMsg_Need_Response
                self.response_msg = None
                self.stream_msg = None
                self.send_msg = msg
                self.rpc_send_cv.notifyAll()
            self.rpc_rev_cv.wait(timeout)
            if (self.response_msg != None):
                if((self.response_msg.msgID & 0xFFFF) == id):
                    msg = self.response_msg
                    return msg
        return None

    def GetInt(self, msg, timeout = 40):
        res = self.GetResponse(msg, timeout)
        if (res != None):
            if(len(res.int_data) == 1):
                return res.int_data[0];
        return None

    def GetDouble(self, msg, timeout = 40):
        res = self.GetResponse(msg, timeout)
        if (res != None):
            if(len(res.double_data) == 1):
                return res.double_data[0];
        return None

    def GetString(self, msg, timeout = 40):
        res = self.GetResponse(msg, timeout)
        if (res != None):
            if(len(res.string_data) > 0):
                return res.string_data[0]
        return None

    def GetByteBuff(self, msg, timeout = 40):
        res = self.GetResponse(msg, timeout)
        if (res != None):
            if(len(res.byte_data) == 1):
                return res.byte_data[0];
        return None

    def Is_Alive(self, timeout_ms):
        msg = IVGrpc_pb2.RPCMessage()
        msg.recever_name = "AIAcq"
        msg.msgID = RPCMessageID.IPCMsg_Channel_IsAlive
        r = self.GetInt(msg, timeout_ms)
        return r

    def DebugWait(self, id, name, line, timeout):
        if (self.current_debug_rsp > 0):
            b = self.current_debug_rsp
            self.current_debug_rsp = 0
            return b
        if(name):
            msg = IVGrpc_pb2.RPCMessage()
            msg.recever_name = "AIAcq"
            msg.msgID = id | RPCMessageID.IPCMsg_Need_Response;
            msg.string_data.append("@" + name)
            msg.int_data.append(line)
            self.current_debug_rsp = 0
            self.PostMsgToClient(msg)
        with self.rpc_res_cv:
            self.rpc_res_cv.wait(0.1)
        if(self.current_debug_rsp > 0):
            b = self.current_debug_rsp
            self.current_debug_rsp = 0
            return b
        return None

    #send message to client stream and response
    def RPCServerSendMsg(self, request_iterator, context):
        with self.rpc_rev_cv:
            self.rpc_rev_cv.notifyAll()
        try:
            while(self.continue_link):
                need_resp = False
                with self.rpc_send_cv:
                    if(self.stream_msg):
                        if(self.stream_msg.msgID & RPCMessageID.IPCMsg_Need_Response):
                            need_resp = True
                        for msg in self.stream_msg_callback():
                            yield msg
                        self.send_msg = None
                        self.stream_msg = None
                        self.stream_msg_callback = None
                        self.rpc_send_cv.notifyAll()
                    elif(self.send_msg):
                        if(self.send_msg.msgID & RPCMessageID.IPCMsg_Need_Response):
                            need_resp = True
                        msg = self.send_msg
                        self.send_msg = None
                        self.rpc_send_cv.notifyAll()
                        yield msg
                    else:
                        self.rpc_send_cv.wait(1)
                if(need_resp):
                        rmsg = next(request_iterator)
                        with self.rpc_rev_cv:
                            self.response_msg = rmsg
                            self.rpc_rev_cv.notifyAll() 
        except grpc.RpcError as e:
            print("except in grpc:", e.code())

    #reponse message from client
    def RPCServerReceiveMsg(self, request_iterator, context):
        for msg in request_iterator:
            with self.rpc_rev_cv:
                self.response_msg = msg
                self.rpc_rev_cv.notifyAll() 
      
    #send from client one message
    def RPCClientSendMsg(self, msg, context):
        msg_id = msg.msgID & 0xFFFF
        fun = self.msg_response_list.get(msg_id)
        if(fun):
             return fun(msg)
        return None

    #send from client stream message
    def RPCClientStreamMsg(self, request_iterator, context):
        for msg in request_iterator:
            msg_id = msg.msgID & 0xFFFF
            fun = self.msg_response_list.get(msg_id)
            if(fun):
                return fun(msg)
            return None