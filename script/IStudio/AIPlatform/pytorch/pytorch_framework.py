from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch
from torch.autograd import Variable
from AICommon.framework import AIFramework
from AIPlatform.pytorch.pytorchviz import make_dot, make_dot_from_trace

def GetFramework(backend):
    return pytorchframework(backend)

class pytorchframework(AIFramework):
    
    def __init__(self, backend):
        super(pytorchframework, self).__init__()
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

    def AddRecordScalar(self, value, name = None):
        if(isinstance(value, torch.Tensor)):
            self.ScalarRecordList[name] = value
        else:
             raise TypeError('AddRecordScalar must be a torch.tensor, but got %s' % type(var))

    def RecordScalar(self, value, name):
        if(isinstance(value, torch.Tensor)):
            return value.numpy(), name
        else:
            return value, name

    def AddRecordImage(self, image, name = None):
        if(isinstance(image, torch.Tensor)):
            if(name is None):
                name = image.name
            self.ImageRecordList[name] = image
        elif(isinstance(image, torch.Tensor)):
            self.ImageRecordList[name] = image
        else:
             raise TypeError('AddRecordImage must be a tf.Variable or tensor, but got %s' % type(var))

    def RecordImage(self, image, name):
        if(isinstance(image, torch.Tensor)):
            if(name is None):
                name = image.name
            return image.numpy(), name
        elif(isinstance(image, torch.Tensor)):
            return image.numpy(), name
        else:
            raise TypeError('RecordImage has invalid data type')
            return

    def AddRecordWaveform(self, waveform, name = None):
        if(isinstance(waveform, torch.Tensor)):
            self.WaveformRecordList[name] = waveform
        else:
             raise TypeError('AddRecordWavefor must be a tensor, but got %s' % type(var))

    def RecordWaveform(self, waveform):
        if(isinstance(waveform, torch.Tensor)):
            return waveform.numpy()
        else:
            raise TypeError('RecordWaveform has invalid data type')
   
    def AddRecordTensor(self, var, name = None):
        if(isinstance(value, torch.Tensor)):
            self.TensorRecordList[name] = var
        else:
             raise TypeError('AddRecordTensor must be a tensor, but got %s' % type(var))

    def RecordTensor(self, tensor, name):
        if(isinstance(tensor, torch.Tensor)):
            return tensor.numpy()
        elif(not isinstance(tensor, np.narray)):
            return tensor;
        else:
            raise TypeError('RecordTensor has invalid data type')
 
    def ViewGraphDef(self, model, name, input = None):
        self.studio.StartSaveGraphDef(name)
        if(isinstance(model, torch.Tensor)):
            params=input
            make_dot(self.studio, model, params)
        else:
            with torch.onnx.set_training(model, False):
                trace, _ = torch.jit.get_trace_graph(model, args = (input,))
                make_dot_from_trace(self.studio, trace)
        self.studio.CloseNodeGraphDef()
        self.studio.CloseSaveGraphDef()


    def SaveCheckpoint(self,  model, name):
        torch.save(model, name+ ".chpt")

    def RestoreCheckpoint(self, name):
        return torch.load(name)
 
    def LoadGraphDef(self, name):
        return torch.load(name)
