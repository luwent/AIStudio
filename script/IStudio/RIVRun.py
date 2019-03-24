from concurrent import futures
import numpy as np
import os, sys
import grpc
import RemoteServer as rs
from RemoteServer import  RPCMessageID

class IPRun:

    console_output_ = None

    def __init__(self, port, name):
        self.instance_key = name
        self.port_ = port
        self.start_serve()
        self.breakpoints = {}
        self.watch_variables = set()
        self.watch_update_status = -1
        self.watch_update_name = ""
        self.watch_update_value = ""
        rs.config.is_remote_run = True
 
    def start_serve(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
          ('grpc.max_send_message_length', 50 * 1024 * 1024),
          ('grpc.max_receive_message_length', 50 * 1024 * 1024)
        ])
        rs.data_service = rs.IVDataService()
        rs.IVGrpc_pb2_grpc.add_DataRPCServicer_to_server(rs.data_service, self.server)
        data_server = rs.config.ftp_server_address + ":" + str(self.port_)
        self.server.add_insecure_port(data_server)     
        self.server.start()
        rs.data_service.get_ready()
    
    def stop_serve(self):
        rs.data_service.stop_link()
        self.server.stop(1000)

    def DebugStart(self):
        self.RunOutput(0, "Loading debug information\n")
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = RPCMessageID.IPCMsg_PY_LoadDebugInfo;
        msg.recever_name = "AIAcq"
        msg.int_data.append(0);
        debuginfo = rs.data_service.GetResponse(msg, 20)
        if (debuginfo != None):
            self.DecodeDebugBreak(debuginfo)
            self.RunOutput(0, "Debug information loaded\n")
        msg.msgID = RPCMessageID.IPCMsg_PY_LoadDebugInfo;
        msg.int_data[0] = 1; 
        debuginfo = rs.data_service.GetResponse(msg, 20)
        if (debuginfo != None):
            self.DecodeWatchInfo(debuginfo)
            self.RunOutput(0, "Watch variable loaded\n")
        rs.data_service.SetCallback(self.DebugInfoCallback)

    def DebugInfoCallback(self, msg):
        try:
            if ((msg.msgID & 0xFFFF) == RPCMessageID.IPCMsg_Debug_PostInfo):
                mode = msg.int_data[0]
                if (mode == 3001): #debug break
                    self.breakpoints.clear()
                    del(msg.int_data[0])
                    self.DecodeDebugBreak(msg)
                elif (mode == 3000): #update watch variable
                    if (self.watch_update_status != -1):
                        return
                    self.watch_variables.add(msg.string_data[0])  #variable name
                    self.watch_update_name = msg.string_data[0]
                    self.watch_update_status = 1
                elif (mode == 3002): #update watch variable value
                    if (self.watch_update_status != -1):
                        return
                    self.watch_variables.add(msg.string_data[0]) #vairable name
                    self.watch_update_name = msg.string_data[0]
                    self.watch_update_value = msg.string_data[1] #variable value
                    self.watch_update_status = 2
        except:
            print("except in get debug information:", sys.exc_info()[0])
                

    def DecodeDebugBreak(self, debuginfo):
        n = 0
        m = 0
        i = 0
        for s in debuginfo.string_data:
            m += debuginfo.uint_data[i]
            self.breakpoints[s] = debuginfo.int_data[n:m]
            n = m
            i += 1  
 
    def DecodeWatchInfo(self, debuginfo):
        for s in debuginfo.string_data:
            self.watch_variables.add(s)

    def GetWatchVariable(self, index):
        if (index >= 0 and index < len(self.watch_variables)):
            return self.watch_variables
        elif (index == -1):
            if (self.watch_update_status == 1):
                self.watch_update_status = -1
                print(self.watch_update_name)
                return self.watch_update_name
            elif(self.watch_update_status == 2):
                self.watch_update_status = -1
                return self.watch_update_name + "=" + self.watch_update_value
        return ""

    def RunOutput(self, type, name):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.recever_name = "AIAcq"
        msg.int_data.append(0)
        msg.string_data.append(name)
        if(type == 0):
            msg.msgID = RPCMessageID.IPCMsg_Log_Info;
            rs.data_service.PostMsgToClient(msg)
        else:
            msg.msgID = RPCMessageID.IPCMsg_Log_Error;
            rs.data_service.PostMsgToClient(msg)
        #IPRun.console_output_.write(name)
    
    def DebugInfoOutput(self, type, data):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = RPCMessageID.IPCMsg_Debug_Info;
        msg.recever_name = "AIAcq"
        msg.int_data.append(type)
        if(len(data) <= 2048):
           msg.string_data.append(data)
        else: #truncate length to 2k
           msg.string_data.append(data[:2048])
        rs.data_service.PostMsgToClient(msg)
 
    def DebugInfoStatus(self, type, status): #verify need to show stack, locals, global and watch
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.recever_name = "AIAcq"
        msg.msgID = RPCMessageID.IPCMsg_Debug_Status;
        msg.int_data.append(type)
        msg.int_data.append(status)
        r = rs.data_service.GetInt(msg)
        if (r == None or r <= 0):
            return 0
        return r

    def IsBreakPoint(self, name, line):
        if name in self.breakpoints:
            if (line < 0):
                return True
            for it in self.breakpoints[name]:
                if (it + 1 == line):
                    return True
        return False
    
    def GetBreakPoint(self):
        if (not self.breakpoints):
             return "", -1
        for key, value in self.breakpoints.items() :
            return key, value[0] + 1

    alive_check = 0
    alive_valid = 0
    def WaitAtBreakPoint(self, name, line):
        try:
            if (self.watch_update_status >= 0):
                return 3000 + self.watch_update_status
            status = 0
            if(line >= 0):
                status = rs.data_service.DebugWait(RPCMessageID.IPCMsg_PY_DebugWait, name, line - 1, 1)
            else:
                status = rs.data_service.DebugWait(RPCMessageID.IPCMsg_PY_DebugWait, None, 0, 1)
            IPRun.alive_check = 0
            IPRun.alive_valid = 0
            while (status == None or status == 0):
                if (IPRun.alive_check >= 4): #check server is alive
                    if (rs.data_service.Is_Alive(1) != 1):
                        if(IPRun.alive_valid > 200):
                            return -99
                        else:
                            return status
                    IPRun.alive_check = 0
                    IPRun.alive_valid += 1
                else:
                    IPRun.alive_check += 1
                if (self.watch_update_status >= 0):
                        return 3000 + self.watch_update_status
                status = rs.data_service.DebugWait(RPCMessageID.IPCMsg_PY_DebugWait, None, 0, 1)
            IPRun.alive_check = 0
            return status
        except:
            print("except in waiting debug:", sys.exc_info()[0])
     
