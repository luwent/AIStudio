from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from RemoteServer.IVRPC import RPCMessageID
from RemoteServer.IVGrpc_pb2 import *
from RemoteServer.IVGrpc_pb2_grpc import *
from RemoteServer.IVModel_pb2 import *
from RemoteServer.IVModel_pb2_grpc import *
from RemoteServer.rpc_service import *

data_service = None
