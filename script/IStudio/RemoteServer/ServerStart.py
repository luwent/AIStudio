from concurrent import futures
import time
import grpc

import IVGrpc_pb2
import IVGrpc_pb2_grpc
import IVAuthorizers

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    IVGrpc_pb2_grpc.add_RPCServicer_to_server(PYIVServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()