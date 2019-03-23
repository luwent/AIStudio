from __future__ import print_function
import time
import grpc

import IVGrpc_pb2
import IVGrpc_pb2_grpc


CHUNK_SIZE = 1024 * 1024  # 1MB


def get_file_chunks(filename):
    with open(filename, 'rb') as f:
        while True:
            piece = f.read(CHUNK_SIZE);
            if len(piece) == 0:
                return
            yield IVGrpc_pb2.PArray(value=piece)


def save_chunks_to_file(chunks, filename):
    if(chunks is None):
        return
    with open(filename, 'wb') as f:
        for chunk in chunks:
            f.write(chunk.value)
    
def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        print(channel._connectivity_state)
        stub = IVGrpc_pb2_grpc.RPCStub(channel)
        try:
            while True:
                response = stub.Login(IVGrpc_pb2.PUser(name="me", psw="123"))
                print("Login client received: " + str(response.retID) + response.result)
                context = [("1", "me"), ("2", response.result)]

                print("Test LIST__________________________________")
                response =stub.FTPList(IVGrpc_pb2.PCommand(msgID=1, msg="c:\\"), metadata = context)
                print("FTPCmd 1 client received: " + response.result + response.result)

                print("Test NLST__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=1, msg="c:\\"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)

                print("Test MLST__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=2, msg="c:\\"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)

                print("Test MLSD__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=3, msg="c:\\"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)
                
                print("Test SIZE__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=4, msg="c:\\eula.1028.txt"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)

                print("Test MDTM__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=5, msg="c:\\eula.1028.txt"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)

                print("Test MKD__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=6, msg="c:\\test1"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)                

                print("Test RMD__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=7, msg="c:\\test2"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)  

                print("Test DELE__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=8, msg="c:\\test\\test121.txt"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)  

                print("Test RNFR__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=9, msg="c:\\test\\test122.txt"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)  
                print("Test RNTO__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=10, msg="c:\\test\\test123.txt"), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)  
                
                print("Test PWD__________________________________")                
                response =stub.FTPCmd(IVGrpc_pb2.PCommand(msgID=11, msg=""), metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)  
                
                print("Test Upload file_________________________________")       
                context.append(("3", "c:\\test\\test125.txt"))   
                chunks_generator = get_file_chunks("c:\\test\\test124.txt")                
                response =stub.FTPUpload(chunks_generator, metadata = context)
                print("FTPCmd 1 client received: " + str(response.retID) + response.result)  
                
                print("Test Download file_________________________________")       
                response =stub.FTPDownload(IVGrpc_pb2.PString(value="c:\\test\\test125.txt"), metadata = context)
                print("FTPCmd 1 client received: ")
                save_chunks_to_file(response, "c:\\test\\test126.txt")
                
                break
                time.sleep(1)
        except KeyboardInterrupt:
            return		
        


if __name__ == '__main__':
    run()