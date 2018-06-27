from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import IVStudio as iv
import re
import importlib

def load_class(full_class_string):
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_str)

class AIDataType:
    Variable = 1
    Image = 2
    Waveform = 3
    Scalar = 4
    Tensor = 5
    Text = 6

class AIStudio(iv.IPStudio):
    def __init__(self, name):
        iv.IPStudio.__init__(self)
        self.Framework = load_class("AIPlatform.tensorflow.tensorflow_graph.TensorflowGraph")(self)
    def RecordVariable(self, vname, var):
        if vname is None:
            if(not isinstance(var, tf.Variable)):
                raise TypeError('RecordVariable must be a tf.Variable, but got %s' % type(var))
            name = var.name
            data = var.eval()
            self.RecordNArray(name, AIDataType.Variable, data)
        else:
            if(not isinstance(var, np.ndarray)):
                raise TypeError('RecordVariable must be a np.narray, but got %s' % type(var))
            name = vname
            self.RecordNArray(name, AIDataType.Variable, var)

    def RecordScalar(self, name, value):
        if(isinstance(value, tf.Variable)):
            data = value.eval()
        elif(isinstance(value, tf.Tensor)):
            data = value.eval()
        else:
            data = value
        if(not isinstance(data, np.float64) and
           not isinstance(data, np.float32) and
           not isinstance(data, np.int32) and
           not isinstance(data, np.int16) and
           not isinstance(data, np.uint16) and
           not isinstance(data, np.int8) and
           not isinstance(data, np.uint8)):
                raise TypeError('RecordScalar has invalid data type')
                return
        self.SaveScalar(name, data.item())

    def RecordImage(self, name, image):
        if(isinstance(image, tf.Variable)):
            data = image.eval()
        elif(isinstance(image, np.ndarray)):
            data = image
        elif(isinstance(image, tf.Tensor)):
            data = image.eval()
        else:
            raise TypeError('RecordImage has invalid data type')
            return
        self.RecordNArray(name, AIDataType.Image, data)

    def RecordWaveform(self, name, waveform, samplerate):
        if(isinstance(waveform, np.ndarray)):
            data = waveform
        elif(isinstance(waveform, tf.Tensor)):
            data = waveform.eval()
        else:
            raise TypeError('RecordWaveform has invalid data type')
            return
        if data.ndim == 1:
            if data.dtype == np.float64:
                self.SaveWaveform1(name, data, samplerate)
            elif data.dtype == np.float32:
                self.SaveWaveform1_F(name, data, samplerate)
            elif data.dtype == np.int32:
                self.SaveWaveform1_I(name, data, samplerate)
            elif data.dtype == np.int16 or data.dtype == np.uint16:
                self.SaveWaveform1_S(name, data, samplerate)
            elif data.dtype == np.int8 or data.dtype == np.uint8:
                self.SaveWaveform1_C(name, data, sampleratea)
            else:
                self.SaveWaveform1(name, type, data)
        elif data.ndim == 2:
            if data.dtype == np.float64:
                self.SaveWaveform2(name, data, samplerate)
            elif data.dtype == np.float32:
                self.SaveWaveform2_F(name, data, samplerate)
            elif data.dtype == np.int32:
                self.SaveWaveform2_I(name, data, samplerate)
            elif data.dtype == np.int16 or data.dtype == np.uint16:
                self.SaveWaveform2_S(name, data, samplerate)
            elif data.dtype == np.int8 or data.dtype == np.uint8:
                self.SaveWaveform2_C(name, data, samplerate)
            else:
                self.SaveWaveform2(name, data, samplerate)
        else:
            raise TypeError('RecordWaveform has invalid data shape')
            return
   
    def RecordText(self, name, text):
        self.SaveText(name, text)

    def RecordTensor(self, name, tensor):
        if(isinstance(tensor, tf.Tensor)):
            data = tensor.eval()
        elif(not isinstance(tensor, np.narray)):
            data = tensor;
        else:
            raise TypeError('RecordTensor has invalid data type')
            return
        self.RecordNArray(name, AIDataType.Tensor, data)

    def RecordNArray(self, name, type, data):
        if data.ndim == 1:
            if data.dtype == np.float64:
                self.SaveTensor1(name, type, data)
            elif data.dtype == np.float32:
                studio.SaveTensor1_F(name, type, data)
            elif data.dtype == np.int32:
                self.SaveTensor1_I(name, type, data)
            elif data.dtype == np.int16 or data.dtype == np.uint16:
                self.SaveTensor1_S(name, type, data)
            elif data.dtype == np.int8 or data.dtype == np.uint8:
                self.SaveTensor1_C(name, type, data)
            else:
                self.SaveTensor1(name, type, data)
        elif data.ndim == 2:
            if data.dtype == np.float64:
                self.SaveTensor2(name, type, data)
            elif data.dtype == np.float32:
                self.SaveTensor2_F(name, type, data)
            elif data.dtype == np.int32:
                self.SaveTensor2_I(name, type, data)
            elif data.dtype == np.int16 or data.dtype == np.uint16:
                self.SaveTensor2_S(name, type, data)
            elif data.dtype == np.int8 or data.dtype == np.uint8:
                self.SaveTensor2_C(name, type, data)
            else:
                self.SaveTensor2(name, type, data)
        elif data.ndim == 3:
            if data.dtype == np.float64:
                self.SaveTensor3(name, type, data)
            elif data.dtype == np.float32:
                self.SaveTensor3_F(name, type, data)
            elif data.dtype == np.int32:
                self.SaveTensor3_I(name, type, data)
            elif data.dtype == np.int16 or data.dtype == np.uint16:
                self.SaveTensor3_S(name, type, data)
            elif data.dtype == np.int8 or data.dtype == np.uint8:
                self.SaveTensor3_C(name, type, data)
            else:
                self.SaveTensor3(name, type, data)
        elif data.ndim == 4:
            if data.dtype == np.float64:
                self.SaveTensor4(name, type, data)
            elif data.dtype == np.float32:
                self.SaveTensor4_F(name, type, data)
            elif data.dtype == np.int32:
                self.SaveTensor4_I(name, type, data)
            elif data.dtype == np.int16 or data.dtype == np.uint16:
                self.SaveTensor4_S(name, type, data)
            elif data.dtype == np.int8 or data.dtype == np.uint8:
                self.SaveTensor4_C(name, type, data)
            else:
                self.SaveTensor4(name, type, data)

    def RecordGraphDef(self, graph):
        self.Framework.ViewGraphDef(graph)