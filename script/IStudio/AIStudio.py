from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import IVStudio as iv
import re
import importlib

def load_class(full_class_string):
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_str)

def MakeColor(r, g, b, a = 255):
    return (a << 24) | (r << 16) | (g << 8) | b

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
        self.Framework = load_class("AIPlatform." + name + "." + name + "_framework." + name + "framework")(self)

    def AddRecordVariable(self, var, name = None):
        self.Framework.AddRecordVariable(var, name)

    def RecordVariable(self, var, name = None):
        if (isinstance(var, np.ndarray)):
            self.RecordNArray(name, AIDataType.Variable, var)
            return
        data, vname = self.Framework.RecordVariable(var, name)
        self.RecordNArray(vname, AIDataType.Variable, var)

    def AddRecordScalar(self, value, name = None):
        self.Framework.AddRecordScalar(value, name)

    def RecordScalar(self, value, name):
        data, vname = self.Framework.RecordScalar(value, name)
        if(not isinstance(data, np.float64) and
           not isinstance(data, np.float32) and
           not isinstance(data, np.int32) and
           not isinstance(data, np.int16) and
           not isinstance(data, np.uint16) and
           not isinstance(data, np.int8) and
           not isinstance(data, np.uint8)):
                raise TypeError('RecordScalar has invalid data type')
                return
        self.SaveScalar(vname, data.item())

    def AddRecordImage(self, image, name = None):
        self.Framework.AddRecordImage(image, name)

    def RecordImage(self, image, name):
        if(isinstance(image, np.ndarray)):
            self.RecordNArray(name, AIDataType.Image, image)
            return
        else:
            data, vname = self.Framework.RecordImage(image, name)
            self.RecordNArray(vname, AIDataType.Image, data)

    def AddRecordWaveform(self, waveform, name = None):
        self.Framework.AddRecordWaveform(waveform, name)

    def RecordWaveform(self, waveform, name, samplerate):
        if(isinstance(waveform, np.ndarray)):
            data = waveform
        else:
            data = self.Framework.RecordWaveform(waveform)
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

    def AddRecordTensor(self, tensor, name = None):
        self.Framework.AddRecordTensor(tensor, name)

    def RecordTensor(self, tensor, name):
        if(isinstance(tensor, np.ndarray)):
            data = tensor
        else:
            data = self.Framework.RecordTensor(tensor, name)
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

    def RecordGraphDef(self, graph, name, para = None):
        self.Framework.ViewGraphDef(graph, name, para)

    def GetRecordList(self):
        return self.Framework.GetRecordList()

    def SaveRecordList(self, summary):
        self.Framework.SaveRecordList(summary)

    def SetupCheckpoint(self, var_list=None):
        self.Framework.SetupCheckpoint(var_list)

    def SaveCheckpoint(self, sess, name):
        fullname = self.DataFolder + name + "_PT_"
        self.Framework.SaveCheckpoint(sess, fullname)

    def RestoreCheckpoint(self, sess, name):
        fullname = self.DataFolder + name + "_PT_"
        self.Framework.RestoreCheckpoint(sess, fullname)

    def LoadGraphDef(self, name):
        self.Framework.LoadGraphDef(name)