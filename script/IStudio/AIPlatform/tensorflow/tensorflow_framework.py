from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow.python.framework import tensor_shape
from tensorflow.core.framework import types_pb2, tensor_pb2
from AICommon.framework import AIFramework

def GetFramework(backend):
    return tensorflowframework(backend)

class tensorflowframework(AIFramework):
    
    def __init__(self, backend):
        super(tensorflowframework, self).__init__()
        self.studio = backend
        self.saver = None 
        self.VarRecordList = {}
        self.ImageRecordList = {}
        self.ScalarRecordList = {}
        self.WaveformRecordList = {}
        self.TensorRecordList = {}

    def GetRecordList(self):
        summary = list(self.VarRecordList.values())
        summary = summary + list(self.ImageRecordList.values())
        summary = summary + list(self.ScalarRecordList.values())
        summary = summary + list(self.WaveformRecordList.values())
        summary = summary + list(self.TensorRecordList.values())
        return summary

    def SaveRecordList(self, summary):
        index = 0
        for v in list(self.VarRecordList.keys()):
            self.studio.RecordVariable(summary[index], v)
            index = index + 1

        for v in list(self.ImageRecordList.keys()):
            self.studio.RecordImage(summary[index], v)
            index = index + 1
            
        for v in list(self.ScalarRecordList.keys()):
            self.studio.RecordScalar(summary[index], v)
            index = index + 1
            
        for v in list(self.WaveformRecordList.keys()):
            self.studio.RecordWaveform(summary[index], v)
            index = index + 1
            
        for v in list(self.TensorRecordList.keys()):
            self.studio.RecordTensor(summary[index], v)
            index = index + 1

    def AddRecordVariable(self, var, name = None):
        if isinstance(var, tf.Variable):
            if(name is None):
                name = var.name
            self.VarRecordList[name] = var
        else:
             raise TypeError('AddRecordVariable must be a tf.Variable, but got %s' % type(var))

    def RecordVariable(self, var, name = None):
        if isinstance(var, tf.Variable):
            if(name is None):
                name = var.name
            data = var.eval()
            return data, name
        else:
             raise TypeError('RecordVariable must be a tf.Variable or narray, but got %s' % type(var))

    def AddRecordScalar(self, value, name = None):
        if(isinstance(value, tf.Variable)):
            if(name is None):
                name = value.name
            self.ScalarRecordList[name] = value
        elif(isinstance(value, tf.Tensor)):
            self.ScalarRecordList[name] = value
        else:
             raise TypeError('AddRecordScalar must be a tf.Variable or tensor, but got %s' % type(var))

    def RecordScalar(self, value, name):
        if(isinstance(value, tf.Variable)):
            if(name is None):
                name = value.name
            return value.eval(), name
        elif(isinstance(value, tf.Tensor)):
            return value.eval(), name
        else:
            return value, name

    def AddRecordImage(self, image, name = None):
        if(isinstance(image, tf.Variable)):
            if(name is None):
                name = image.name
            self.ImageRecordList[name] = image
        elif(isinstance(image, tf.Tensor)):
            self.ImageRecordList[name] = image
        else:
             raise TypeError('AddRecordImage must be a tf.Variable or tensor, but got %s' % type(var))

    def RecordImage(self, image, name):
        if(isinstance(image, tf.Variable)):
            if(name is None):
                name = image.name
            return image.eval(), name
        elif(isinstance(image, tf.Tensor)):
            return image.eval(), name
        else:
            raise TypeError('RecordImage has invalid data type')
            return

    def AddRecordWaveform(self, waveform, name = None):
        if(isinstance(waveform, tf.Tensor)):
            self.WaveformRecordList[name] = waveform
        else:
             raise TypeError('AddRecordWavefor must be a tensor, but got %s' % type(var))

    def RecordWaveform(self, waveform):
        if(isinstance(waveform, tf.Tensor)):
            return waveform.eval()
        else:
            raise TypeError('RecordWaveform has invalid data type')
   
    def AddRecordTensor(self, var, name = None):
        if(isinstance(value, tf.Tensor)):
            self.TensorRecordList[name] = var
        else:
             raise TypeError('AddRecordTensor must be a tensor, but got %s' % type(var))

    def RecordTensor(self, tensor, name):
        if(isinstance(tensor, tf.Tensor)):
            return tensor.eval()
        elif(not isinstance(tensor, np.narray)):
            return tensor;
        else:
            raise TypeError('RecordTensor has invalid data type')
 
    def ViewGraphDef(self, graph_or_graph_def, name, para = None):
        if isinstance(graph_or_graph_def, tf.Graph):
            tfgraph = graph_or_graph_def.as_graph_def()
        else:
            tfgraph = graph_or_graph_def
        self.studio.StartSaveGraphDef(name)
        for node in tfgraph.node:
            self.studio.AddNodeGraphDef(node.name, node.op)
            for input_full_name in node.input:
                self.studio.AddNodeInputGraphDef(input_full_name)
            for key, val in node.attr.items():
                if val.HasField('s'):
                    self.studio.AddNodeAttrStringGraphDef(key, str(val.s))
                elif val.HasField('i'):
                    self.studio.AddNodeAttrIntGraphDef(key, val.i)
                elif val.HasField('f'):
                    self.studio.AddNodeAttrFloatGraphDef(key, val.f)
                elif val.HasField('b'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val.b)
                elif val.HasField('type'):
                    self.studio.AddNodeAttrStringGraphDef(key, tf.as_dtype(val.type).name)
                elif val.HasField('shape'):
                    sh = self.GetShapeData(val.shape)
                    shstr = ':'.join(str(e) for e in sh)
                    self.studio.AddNodeAttrStringGraphDef(key, shstr)
                elif val.HasField('tensor'):
                    tensor = self.GetTensorData(val.tensor)
                    tensordatastr = ':'.join(str(e) for e in tensor)
                    self.studio.AddNodeAttrStringGraphDef(key, tensordatastr)
                elif val.HasField('list'):
                    self.studio.AddNodeAttrStringGraphDef(key, self.GetListValue(val))
                elif val.HasField('func'):
                    self.studio.AddNodeAttrStringGraphDef(key, 'func')
                elif val.HasField('placeholder'):
                    self.studio.AddNodeAttrStringGraphDef(key, 'placeholder')
        self.studio.CloseNodeGraphDef()
        self.studio.CloseSaveGraphDef()


    def GetListValue(self,  val):
        list = val.list
        if (list.s):
            return "string list"
        elif (list.i):
            return "int list"
        elif (list.f):
            return "float list"
        elif (list.type):
            return "type list"
        elif (list.shape):
            return "shape list"
        return "unknow list"

    def GetShapeData(self,  shape):
        if(tensor_shape.as_shape(shape).dims != None):
             return  tensor_shape.as_shape(shape).as_list()
        else:
             return [0]

    def GetTensorData(self,  tensor):
        """Get data from tensor."""
        assert isinstance(tensor, tensor_pb2.TensorProto)
        is_raw = False
        if tensor.tensor_content:
            data = tensor.tensor_content
            is_raw = True
        elif tensor.float_val:
            data = tensor.float_val
        elif tensor.dcomplex_val:
            data = tensor.dcomplex_val
        elif tensor.int_val:
            data = tensor.int_val
        elif tensor.bool_val:
            data = tensor.bool_val
        elif tensor.dtype == tf.int32:
            data = [0]
        elif tensor.dtype == tf.int64:
            data = [0]
        elif tensor.dtype == tf.float32:
            data = [0.]
        elif tensor.string_val:
            data = tensor.string_val
        else:
            raise ValueError('tensor data not supported')
        return ["Tensor: raw=", is_raw, data]

    def SetupCheckpoint(self,  var_list=None):
       self.saver = tf.train.Saver(var_list)

    def SaveCheckpoint(self,  sess, name):
        if(self.saver != None):
            self.saver.save(sess, name+ ".chpt")

    def RestoreCheckpoint(self,  sess, name):
        if(self.saver != None):
            self.saver.restore(sess, name + ".chpt")

    def LoadGraphDef(self, name):
        od_graph_def = tf.GraphDef()
        with tf.gfile.Open(name, 'rb') as fid:
            serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')