"""
This module implement functions for remote debug
"""
import numpy as np
import os, sys
import RemoteServer as rs
from RemoteServer import  RPCMessageID

moduleDir =os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + os.sep + "../../binary")
sys.path.append(moduleDir)

class IVDataType():
    IVData_Float = 1
    IVData_Double = 2
    IVData_Int32 = 3
    IVData_UInt8 = 4
    IVData_Int16 = 5
    IVData_Int8 = 6
    IVData_String = 7
    IVData_Complex64 = 8
    IVData_Int64 =  9
    IVData_Bool =  10

class TensorType():
    Unknown = 0
    Variable = 1
    Image = 2
    Waveform = 3
    Scalar = 4
    Tensor = 5
    Text = 6

class IPPlot():
    """Plot class for graph, plot is identified by its name or index.
    """
    def __init__(self, index, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "i" + str(index)

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        if((not (id & RPCMessageID.IPCMsg_Has_Stream)) or (id & RPCMessageID.IPCMsg_Has_EndStream)):
            msg.string_data.append(self.context_)
        return msg

    def __StreamData(self, id, array):
        if(len(array) * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(id | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 8)
            n = int(len(array) / step)
            def SteamMsg():
                for i in range(n):
                    del msg.double_data[:]
                    msg.double_data.extend(array[i * step:(i + 1) * step])
                    yield msg
                del msg.double_data[:]
                if n * step < len(array):
                    msg.double_data.extend(array[n * step:])
                yield msg
            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(id | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(len(array))
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(id)
            msg.int_data.append(len(array))
            msg.double_data.extend(array)
            rs.data_service.PostMsgToClient(msg)

    def __StreamMultiData(self, id, data_list):
        nd = len(data_list)
        nn = len(data_list[0])
        for array in data_list:
            if(array is not None and nn < len(array)):
                nn = len(array)
        if(nn * nd * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(id | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 8)
            n = int(nn / step)
            msg.int_data.append(nd)
            def SteamMsg():
                for array in data_list:
                    if array != None:
                        msg.int_data.append(nn * 8)
                        for i in range(n):
                            if(i != 0):
                                del msg.int_data[:]
                            del msg.double_data[:]
                            msg.double_data.extend(array[i * step:(i + 1) * step])
                            yield msg
                        del msg.double_data[:]
                        if n * step < nn:
                            msg.double_data.extend(array[n * step:])
                        yield msg
                    else:
                        msg.int_data.append(0)
                        yield msg
            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(id | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(4)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(id)
            msg.int_data.append(nd)
            msg.int_data.append(nd)
            for array in data_list:
                if array is not None:
                    msg.int_data.append(nn * 8)
                    msg.double_data.extend(array)
                else:
                    msg.int_data.append(0)
            rs.data_service.PostMsgToClient(msg)

    def SetVisible(self, bVisible):
        """
        Hide or show a plot

        :param bVisible: set True or False to show or hide plot 
        """
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotVisible)
        msg.bool_data.append(bVisible)
        rs.data_service.PostMsgToClient(msg)

    def ModifyOption(self, plotOptions, bAdd):
        """
        Modify plot options see PlotStyle class

        :param bAdd: set True or False to add or remove options 
        """
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotOption)
        msg.uint_data.append(plotOptions)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetName(self, name):
        """
        Set plot name

        :param bVisible: set True or False to show or hide plot 
        """
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotSetName)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
         
    def SetPlotStyle(self, plotStyle):
        """
        Set plot type

        :param plotStyle: select type from PlotStyle enum
        """
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotStyle)
        msg.int_data.append(plotStyle)
        rs.data_service.PostMsgToClient(msg)

    def SetLineStyle(self, type):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotLineStyle)
        msg.int_data.append(type)
        rs.data_service.PostMsgToClient(msg)

    def SetLineColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotLineColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetLineWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotLineWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def SetPointStyle(self, iconType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPointerStyle)
        msg.int_data.append(iconType)
        rs.data_service.PostMsgToClient(msg)

    def SetPointColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPointerColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetPointBorderWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPointerWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def SetPointFillColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPointerFillColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetPointSize(self, size):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPointerSize)
        msg.int_data.append(size)
        rs.data_service.PostMsgToClient(msg)

    def SetXAxis(self, axis_name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotSetXAxis)
        msg.string_data.append(axis_name)
        rs.data_service.PostMsgToClient(msg)

    def SetYAxis(self, axis_name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotSetYAxis)
        msg.string_data.append(axis_name)
        rs.data_service.PostMsgToClient(msg)

    def PlotY(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_PlotY, array)

    def PlotXRange(self, dataStart, dataInc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotXRange)
        msg.double_data.append(dataStart)
        msg.double_data.append(dataInc)
        rs.data_service.PostMsgToClient(msg)

    def PlotX(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_PlotX, array)

    def PlotYRange(self, dataStart, dataInc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotYRange)
        msg.double_data.append(dataStart)
        msg.double_data.append(dataInc)
        rs.data_service.PostMsgToClient(msg)

    def PlotXY(self, xData, yData):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_PlotXY, [xData, yData])

    def ChartY(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_ChartY, array)

    def ChartXRange(self, dataStart, dataInc, chartLength, bScroll=True, scrollPercent=1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ChartXRange)
        msg.double_data.append(dataStart)
        msg.double_data.append(dataInc)
        msg.double_data.append(scrollPercent)
        msg.bool_data.append(bScroll)
        msg.uint_data.append(chartLength)
        rs.data_service.PostMsgToClient(msg)

    def ChartRollbackY(self, n):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ChartRollbackX)
        msg.int_data.append(n)
        rs.data_service.PostMsgToClient(msg)

    def ChartX(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_ChartX, array)

    def ChartYRange(self, dataStart, dataInc, chartLength, bScroll=True, scrollPercent=1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ChartYRange)
        msg.double_data.append(dataStart)
        msg.double_data.append(dataInc)
        msg.double_data.append(scrollPercent)
        msg.bool_data.append(bScroll)
        msg.uint_data.append(chartLength)
        rs.data_service.PostMsgToClient(msg)

    def ChartRollbackX(self, n):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ChartRollbackY)
        msg.int_data.append(n)
        rs.data_service.PostMsgToClient(msg)

    def ChartXY(self, xData, yData):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_ChartXY, [xData, yData])

    def ChartXYRange(self, chartLength, bXScroll=True, bYScroll=False, scrollPercent=1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ChartXYRange)
        msg.double_data.append(scrollPercent)
        msg.bool_data.append(bXScroll)
        msg.bool_data.append(bYScroll)
        msg.uint_data.append(chartLength)
        rs.data_service.PostMsgToClient(msg)

    def SetDataOffset(self, offsetX, offsetY):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotDataOffset)
        msg.double_data.append(offsetX)
        msg.double_data.append(offsetY)
        rs.data_service.PostMsgToClient(msg)

    def ImageRange(self, x0, xinc, y0, yinc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ImageRange)
        msg.double_data.append(x0)
        msg.double_data.append(xinc)
        msg.double_data.append(y0)
        msg.double_data.append(yinc)
        rs.data_service.PostMsgToClient(msg)
              
    def ImageColor(self, images, nx = 0, ny = 0, channel = 1, batch = 1):
        if not isinstance(images, np.ndarray):
            return
        if images.ndim == 2:
            nx =images.shape[1]
            ny = images.shape[0]
        elif images.ndim == 4:
            nx = images.shape[2]
            ny = images.shape[1]
            channel = 3
            batch = images.shape[0]
        images = images.flatten()
        datatype = 2
        if(len(images) * images.itemsize > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ImageXY | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / images.itemsize)
            n = int(len(images) / step)
            def SteamMsg():
                for i in range(n):
                    if images.dtype == np.float64:
                        datatype = 2
                        del msg.double_data[:]
                        msg.double_data.extend(images[i * step:(i + 1) * step])
                    elif images.dtype == np.float32:
                        datatype = 1
                        del msg.float_data[:]
                        msg.float_data.extend(images[i * step:(i + 1) * step])
                    elif images.dtype == np.int32:
                        datatype = 3
                        del msg.int_data[:]
                        msg.int_data.extend(images[i * step:(i + 1) * step])
                    elif images.dtype == np.int16 or images.dtype == np.uint16:
                        datatype = 5
                        del msg.int_data[:]
                        msg.int_data.extend(images[i * step:(i + 1) * step])
                    elif images.dtype == np.int8 or images.dtype == np.uint8:
                        datatype = 6
                        del msg.byte_data[:]
                        msg.byte_data.append(images[i * step:(i + 1) * step])
                    #sys.__stdout__.write("stream-" + str(i))
                    yield msg
                if n * step < len(images):
                    if images.dtype == np.float64:
                        del msg.double_data[:]
                        msg.double_data.extend(images[n * step:])
                    elif images.dtype == np.float32:
                        del msg.float_data[:]
                        msg.float_data.extend(images[n * step:])
                    elif images.dtype == np.int32:
                        del msg.int_data[:]
                        msg.int_data.extend(images[n * step:])
                    elif images.dtype == np.int16 or images.dtype == np.uint16:
                        del msg.int_data[:]
                        msg.int_data.extend(images[n * step:])
                    elif images.dtype == np.int8 or images.dtype == np.uint8:
                        del msg.byte_data[:]
                        msg.byte_data.append(images[n * step:])
                    yield msg
            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ImageXY | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(nx)
            msg.int_data.append(ny)
            msg.int_data.append(datatype)
            msg.int_data.append(channel)
            msg.int_data.append(batch)
            rs.data_service.PostMsgToClient(msg) 	
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ImageXY)
            msg.int_data.append(nx)
            msg.int_data.append(ny)
            if images.dtype == np.float64:
                datatype = 2
                msg.int_data.append(datatype)
                msg.int_data.append(channel)
                msg.int_data.append(batch)
                msg.double_data.extend(images)
            elif images.dtype == np.float32:
                datatype = 1
                msg.int_data.append(datatype)
                msg.int_data.append(channel)
                msg.int_data.append(batch)
                msg.float_data.extend(images)
            elif images.dtype == np.int32:
                datatype = 3
                msg.int_data.append(datatype)
                msg.int_data.append(channel)
                msg.int_data.append(batch)
                msg.int_data.extend(images)
            elif images.dtype == np.int16 or images.dtype == np.uint16:
                datatype = 5
                msg.int_data.append(datatype)
                msg.int_data.append(channel)
                msg.int_data.append(batch)
                msg.int_data.extend(images)
            elif images.dtype == np.int8 or images.dtype == np.uint8:
                datatype = 6
                msg.int_data.append(datatype)
                msg.int_data.append(channel)
                msg.int_data.append(batch)
                msg.byte_data.append(images)
            rs.data_service.PostMsgToClient(msg)

    def Bar(self, labels, array):
        nd = min(len(labels), len(array))
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotBar)
        msg.int_data.append(nd)
        msg.int_data.append(1)
 
        msg.int_data.append(nd)
        for i in range(nd):
            msg.int_data.append(len(labels[i]) + 1)
            msg.string_data.append(labels[i])

        msg.int_data.append(1)
        msg.int_data.append(nd * 8)
        msg.double_data.extend(array[:nd])
        rs.data_service.PostMsgToClient(msg)

    def BarLabel(self, labels):
        nd = len(labels)
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotBarLabel)
        msg.int_data.append(nd)
   
        msg.int_data.append(nd)
        for i in range(nd):
            msg.int_data.append(len(labels[i]) + 1)
            msg.string_data.append(labels[i])

        rs.data_service.PostMsgToClient(msg)

    def BarData(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_PlotBarData, array)

    def BarColor(self, fillType, fillColor, borderWidth, borderColor):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotBarColor)
        msg.int_data.append(fillType)
        msg.uint_data.append(fillColor)
        msg.int_data.append(borderWidth)
        msg.uint_data.append(borderColor)
        rs.data_service.PostMsgToClient(msg)

    def SetBarPara(self, barSize, stackonplot=-1, barpadding=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotBarPara)
        msg.double_data.append(barSize)
        msg.int_data.append(stackonplot)
        msg.int_data.append(barpadding)
        rs.data_service.PostMsgToClient(msg)

    def Pie(self, labels, array, color):
        nd = min(len(labels), len(array, len(color)))
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPie)
        msg.int_data.append(nd)
        msg.int_data.append(2)
 
        msg.int_data.append(nd)
        for i in range(nd):
            msg.int_data.append(len(labels[i]) + 1)
            msg.string_data.append(labels[i])

        msg.int_data.append(2)
        msg.int_data.append(nd * 8)
        msg.double_data.extend(array[:nd])
        msg.int_data.append(nd * 4)
        msg.uint_data.extend(color[:nd])
        rs.data_service.PostMsgToClient(msg)

    def PieLabel(self, labels):
        nd = len(labels)
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieLabel)
        msg.int_data.append(nd)
   
        msg.int_data.append(nd)
        for i in range(nd):
            msg.int_data.append(len(labels) + 1)
            msg.string_data.append(labels[i])

        rs.data_service.PostMsgToClient(msg)

    def PieData(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_PlotPieData, array)

    def PieColor(self, color):
        if(len(color) * 4 > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieColor | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 4)
            n = int(len(color) / step)
            def SteamMsg():
                for i in range(n):
                    del msg.uint_data[:]
                    msg.uint_data.extend(color[i * step:(i + 1) * step])
                    yield msg
                del msg.uint_data[:]
                if n * step < len(color):
                    msg.uint_data.extend(color[n * step:])
                yield msg
            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieColor | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(len(color))
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieColor)
            msg.int_data.append(len(color))
            msg.uint_data.extend(color)
            rs.data_service.PostMsgToClient(msg)

    def SetPieColor(self, highlight, bkgrColor):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieParaColor)
        msg.uint_data.append(highlight)
        msg.uint_data.append(bkgrColor)
        rs.data_service.PostMsgToClient(msg)

    def SetPieOffset(self, pie, offset):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieParaOffset)
        msg.int_data.append(pie)
        msg.double_data.append(offset)
        rs.data_service.PostMsgToClient(msg)

    def SetPieLabelOffset(self, pie, offsetX, offsetY):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPieParaLabelOffset)
        msg.int_data.append(pie)
        msg.double_data.append(offsetX)
        msg.double_data.append(offsetY)
        rs.data_service.PostMsgToClient(msg)

    def SetPiePara(self, angleStart, doughnutRatio):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPiePara)
        msg.double_data.append(angleStart)
        msg.double_data.append(doughnutRatio)
        rs.data_service.PostMsgToClient(msg)

    def SetPie3DPara(self, inclneAngle, pieDepth):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotPiePara3D)
        msg.double_data.append(inclneAngle)
        msg.double_data.append(pieDepth)
        rs.data_service.PostMsgToClient(msg)

    def VectorXY(self, data1, data2, data3, data4):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_PlotVectorXY, [data1, data2, data3, data4])

    def VectorAL(self, data1, data2, data3, data4):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_PlotVectorAL, [data1, data2, data3, data4])

    def SetVectorPara(self, arrowSize, lenScale):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotVectorPara)
        msg.double_data.append(arrowSize)
        msg.double_data.append(lenScale)
        rs.data_service.PostMsgToClient(msg)

    def BubbleXY(self, data1, data2, data3):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_PlotBubleXY, [data1, data2, data3])

    def SetBubblePara(self, bubbleScale):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotBublePara)
        msg.double_data.append(bubbleScale)
        rs.data_service.PostMsgToClient(msg)

    def SetErrorPercent(self, err):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotErrPer)
        msg.double_data.append(err)
        rs.data_service.PostMsgToClient(msg)

    def SetErrorUpData(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_PlotErrUp, array)

    def SetErrorLowData(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_PlotErrLow, array)

    def SetErrorStyle(self, errBarSource, direction, display, lineWidth, capWidth, barColor):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotErrStyle)
        msg.int_data.append(errBarSource)
        msg.int_data.append(direction)
        msg.int_data.append(display)
        msg.int_data.append(lineWidth)
        msg.int_data.append(capWidth)
        msg.uint_data.append(barColor)
        rs.data_service.PostMsgToClient(msg)

    def PlotZ(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_Plot3DZ, array)

    def PlotZRange(self, dataStart, dataInc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DZRange)
        msg.double_data.append(dataStart)
        msg.double_data.append(dataInc)
        rs.data_service.PostMsgToClient(msg)

    def ChartZ(self, array):
        self.__StreamData(RPCMessageID.IPCMsg_Widget_Chart3DZ, array)

    def ChartZRange(self, dataStart, dataInc, chartLength, bScroll=True, scrollPercent=1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DZRange)
        msg.double_data.append(dataStart)
        msg.double_data.append(dataInc)
        msg.uint_data.append(chartLength)
        msg.bool_data.append(bScroll)
        msg.double_data.append(scrollPercent)
        rs.data_service.PostMsgToClient(msg)

    def ChartRollbackZ(self, n):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Chart3DZRollback)
        msg.uint_data.append(n)
        rs.data_service.PostMsgToClient(msg)

    def ChartXYZ(self, data1, data2, data3):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_Chart3DXYZ, [data1, data2, data3])

    def ChartXYZRange(self, chartLength, bXScroll=True, bYScroll=False, bZScroll=False, scrollPercent=1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Chart3DXYZRange)
        msg.uint_data.append(chartLength)
        msg.bool_data.append(bXScroll)
        msg.bool_data.append(bYScroll)
        msg.bool_data.append(bZScroll)
        msg.double_data.append(scrollPercent)
        rs.data_service.PostMsgToClient(msg)

    def PlotXYZCurve(self, data1, data2, data3, data4 = None):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_Plot3DXYZ, [data1, data2, data3, data4])

    def SurfaceXYZ(self, x, y, z, c):
        nd = 4
        nn = len(x) + len(y) + len(z)
        if(c is not None):
            nn = nn + len(c)
        if(nn * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceXYZ | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 8)
            msg.int_data.append(nd)
            def SteamMsg():
                for array in [x, y, z, c]:
                    if(array is None):
                        msg.int_data.append(0)
                        yield msg
                    else:
                        nn = len(array)
                        n = int(nn / step)
                        msg.int_data.append(len(array) * 8)
                        for i in range(n):
                            if(i != 0):
                                del msg.int_data[:]
                            del msg.double_data[:]
                            msg.double_data.extend(array[i * step:(i + 1) * step])
                            yield msg
                        del msg.double_data[:]
                        if n * step < nn:
                            msg.double_data.extend(array[n * step:])
                        yield msg

            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceXYZ | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(4)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceXYZ)
            msg.int_data.append(nd)
            msg.int_data.append(nd)
            for array in [x, y, z, c]:
                if(array is not None):
                    nn = len(array)
                    msg.int_data.append(nn * 8)
                    msg.double_data.extend(array)
                else:
                    msg.int_data.append(0)
            rs.data_service.PostMsgToClient(msg)

    def SurfaceXYZ2(self, x, y, z2, c2 = None):
        z = z2.flatten()
        c = None
        if c2 is not None:
            c = c2.flatten()
        self.SurfaceXYZ(x, y, z, c)

    def SurfaceXYZParametric(self, x, y, z, c, nu, nv):
        if(len(x) != nu * nv or len(y) != nu * nv or len(z) != nu * nv):
            return
        if(c != None and len(c) != nu * nv):
            return
        nd = 5
        if(nu * nv * 3 * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfacePara | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 8)
            msg.int_data.append(nd)
            def SteamMsg():
                msg.int_data.append(2 * 4)
                msg.int_data.append(nu)
                msg.int_data.append(nv)
                yield msg
                for array in [x, y, z, c]:
                    if(array == None):
                        continue
                    nn = len(array)
                    n = int(nn / step)
                    msg.int_data.append(len(array) * 8)
                    for i in range(n):
                        if(i != 0):
                            del msg.int_data[:]
                        del msg.double_data[:]
                        msg.double_data.extend(array[i * step:(i + 1) * step])
                        yield msg
                    del msg.double_data[:]
                    if n * step < nn:
                        msg.double_data.extend(array[n * step:])
                    yield msg

            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfacePara | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(4)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfacePara)
            msg.int_data.append(nd)
            msg.int_data.append(nd)
            msg.int_data.append(2 * 4)
            msg.int_data.append(nu)
            msg.int_data.append(nv)
            for array in [x, y, z, c]:
                if(aray == None):
                    continue
                nn = len(array)
                msg.int_data.append(nn * 8)
                msg.double_data.extend(array)
            rs.data_service.PostMsgToClient(msg)

    def SurfaceZ(self, array, nx, ny):
        if (len(array) != nx * ny):
            return 
        if(nx * ny * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceZ | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 8)
            def SteamMsg():
                nn = len(array)
                n = int(nn / step)
                msg.int_data.append(len(array) * 8)
                for i in range(n):
                    if(i != 0):
                        del msg.int_data[:]
                    del msg.double_data[:]
                    msg.double_data.extend(array[i * step:(i + 1) * step])
                    yield msg
                del msg.double_data[:]
                if n * step < nn:
                    msg.double_data.extend(array[n * step:])
                yield msg

            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceZ | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(nx)
            msg.int_data.append(ny)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceZ)
            msg.int_data.append(nx)
            msg.int_data.append(ny)
            nn = len(array)
            msg.double_data.extend(array)
            rs.data_service.PostMsgToClient(msg)

    def SurfaceRange(self, x0, xinc, y0, yinc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DSurfaceRange)
        msg.double_data.append(x0)
        msg.double_data.append(xinc)
        msg.double_data.append(y0)
        msg.double_data.append(yinc)
        rs.data_service.PostMsgToClient(msg)

    def SurfaceImage(self, image, x0, y0, z0, cx, cy, cz, plotCubicPlane):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SurfaceImage)
        msg.string_data.append(image)
        msg.double_data.append(x0)
        msg.double_data.append(y0)
        msg.double_data.append(z0)
        msg.double_data.append(cx)
        msg.double_data.append(cy)
        msg.double_data.append(cz)
        msg.int_data.append(plotCubicPlane)
        rs.data_service.PostMsgToClient(msg)

    def VolumnRange(self, x0, xinc, y0, yinc, z0, zinc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DVolRange)
        msg.double_data.append(x0)
        msg.double_data.append(xinc)
        msg.double_data.append(y0)
        msg.double_data.append(yinc)
        msg.double_data.append(z0)
        msg.double_data.append(zinc)
        rs.data_service.PostMsgToClient(msg)

    def VolumnData(self, slices, image = None):
        shape = slices.shape
        if(slices.size * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DVolData | RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 8)
            msg.int_data.append(nd)
            array = slices.flatten()
            def SteamMsg():
                nn = len(array)
                n = int(nn / step)
                msg.int_data.append(len(array) * 8)
                for i in range(n):
                    if(i != 0):
                        del msg.int_data[:]
                    del msg.float_data[:]
                    msg.float_data.extend(array[i * step:(i + 1) * step])
                    yield msg
                del msg.float_data[:]
                if n * step < nn:
                    msg.float_data.extend(array[n * step:])
                yield msg

            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DVolData | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(shape[0])
            msg.int_data.append(shape[1])
            msg.int_data.append(shape[2])
            msg.int_data.append(2)
            if image == None:
                msg.string_data.append("")
            else:
                msg.string_data.append(image)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DVolData)
            msg.int_data.append(shape[0])
            msg.int_data.append(shape[1])
            msg.int_data.append(shape[2])
            msg.int_data.append(2)
            if image == None:
                msg.string_data.append("")
            else:
                msg.string_data.append(image)
            array = slices.flatten()
            msg.float_data.extend(array)
            rs.data_service.PostMsgToClient(msg)

    def SetVolumnDisplayType(self, plotVolumnDisplayType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DVolType)
        msg.int_data.append(plotVolumnDisplayType)
        rs.data_service.PostMsgToClient(msg)

    def SetVolumeCutPosition(self, x, y, z):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DVolCut)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        rs.data_service.PostMsgToClient(msg)

    def Bar3D(self, labelx, labely, array, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Plot3DBar)
        nx = len(labelx)
        ny = len(labely)
        msg.int_data.append(nx)
        msg.int_data.append(ny)
        msg.int_data.append(len(array))
        msg.int_data.append(len(color))

        msg.int_data.append(nx)
        for i in range(nx):
            msg.int_data.append(len(labelx[i]) + 1)
            msg.string_data.append(labelx[i])

        msg.int_data.append(ny)
        for i in range(ny):
            msg.int_data.append(len(labely) + 1)
            msg.string_data.append(labely[i])

        msg.int_data.append(len(array))
        msg.double_data.extend(array)
        msg.int_data.append(len(color))
        msg.uint_data.extend(color)
        rs.data_service.PostMsgToClient(msg)

    def BarLabel3D(self, labelx, labely):
        nd = len(labels)
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PlotBarLabel)
        nx = len(labelx)
        ny = len(labely)
        msg.int_data.append(nx)
        msg.int_data.append(ny)
  
        msg.int_data.append(nx)
        for i in range(nx):
            msg.int_data.append(len(labelx[i]) + 1)
            msg.string_data.append(labelx[i])

        msg.int_data.append(ny)
        for i in range(ny):
            msg.int_data.append(len(labely) + 1)
            msg.string_data.append(labely[i])

        rs.data_service.PostMsgToClient(msg)

    def VectorXYZ(self, x0, y0, z0, x1, y1, z1):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_Plot3DVector, [x0, y0, z0, x1, y1, z1])

    def VectorABL(self, x0, y0, z0, theta, azimuthal, length):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_Plot3DVectorABL, [x0, y0, z0, theta, azimuthal, length])

    def BubbleXYZ(self, x, y, z, r):
        self.__StreamMultiData(RPCMessageID.IPCMsg_Widget_Plot3DBubble, [x, y, z, r])

class IPAxis():

    def __init__(self, index, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "i" + str(index)

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        msg.string_data.append(self.context_)
        return msg

    def SetTitle(self, caption):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisSetTitle)
        msg.string_data.append(caption)
        rs.data_service.PostMsgToClient(msg)

    def SetTitleColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def ModifyOption(self, axisOptions, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisOption)
        msg.uint_data.append(axisOptions)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetAxisType(self, axisType, bInitialize):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisType)
        msg.int_data.append(axisType)
        msg.bool_data.append(bInitialize)
        rs.data_service.PostMsgToClient(msg)

    def SetMinimum(self, min):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisSetMinimum)
        msg.double_data.append(min)
        rs.data_service.PostMsgToClient(msg)

    def SetMaximum(self, max):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisSetMaximum)
        msg.double_data.append(max)
        rs.data_service.PostMsgToClient(msg)

    def GetMinimum(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGetMinimum)
        return rs.data_service.GetDouble(msg)

    def GetMaximum(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGetMaximum)
        return rs.data_service.GetDouble(msg)

    def SetTickLabelFont(self, name, size, orientation=0, style=0, offsetX=0, offsetY=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisLabelFont)
        msg.string_data.append(name)
        msg.int_data.append(size)
        msg.float_data.append(orientation)
        msg.uint_data.append(style)
        msg.int_data.append(offsetX)
        msg.int_data.append(offsetY)
        rs.data_service.PostMsgToClient(msg)

    def SetTickColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisLabelColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetTickPadding(self, padding):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickPad)
        msg.int_data.append(padding)
        rs.data_service.PostMsgToClient(msg)

    def SetTickMajorSize(self, size):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickMajorSize)
        msg.int_data.append(size)
        rs.data_service.PostMsgToClient(msg)

    def SetTickMinorSize(self, size):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickMinorSize)
        msg.int_data.append(size)
        rs.data_service.PostMsgToClient(msg)

    def SetTickScaling(self, scale):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickScale)
        msg.double_data.append(size)
        rs.data_service.PostMsgToClient(msg)

    def SetMajorTickRange(self, base, step):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickRange)
        msg.double_data.append(base)
        msg.double_data.append(step)
        rs.data_service.PostMsgToClient(msg)

    def SetMajorTickNumber(self, number):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickMajorNumber)
        msg.int_data.append(number)
        rs.data_service.PostMsgToClient(msg)

    def SetMinorTickNumber(self, number):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisTickMinorNumber)
        msg.int_data.append(number)
        rs.data_service.PostMsgToClient(msg)

    def SetMajorGridColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGridColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetMajorGridStyle(self, lineType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGridStyle)
        msg.int_data.append(lineType)
        rs.data_service.PostMsgToClient(msg)

    def SetMajorGridWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGridWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def SetMinorGridColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGridMinorColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetMinorGridStyle(self, lineType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGridMinorStyle)
        msg.int_data.append(lineType)
        rs.data_service.PostMsgToClient(msg)

    def SetMinorGridWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisGridMinorWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def ModifyValuePairOption(self, valuePairOption, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisVPOption)
        msg.uint_data.append(valuePairOption)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def AddValuePair(self, name, value, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisVPAdd)
        msg.string_data.append(name)
        msg.double_data.append(value)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetValuePair(self, index, name, value, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisVPSet)
        msg.int_data.append(index)
        msg.string_data.append(name)
        msg.double_data.append(value)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def RemoveVaulePair(self, index):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisVPRemove)
        msg.int_data.append(index)
        rs.data_service.PostMsgToClient(msg)

    def RemoveVaulePairAll(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisVPRemoveAll)
        rs.data_service.PostMsgToClient(msg)

    def SetTickLabelOrientation(self, textOrientationStyle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AxisLabelOrientation)
        msg.int_data.append(textOrientationStyle)
        rs.data_service.PostMsgToClient(msg)

class IPCursor():

    def __init__(self, index, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "i" + str(index)

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        msg.string_data.append(self.context_)
        return msg

    def ModifyOption(self, cursorOptions, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorOption)
        msg.uint_data.append(cursorOptions)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def GetCursorPos(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorPos)
        res = rs.data_service.GetResponse(msg, 4000)
        if (res != None):
            if(len(res.double_data) == 2):
                return res.double_data;

    def SetCursorPos(self, x, y):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorSetPosition)
        msg.double_data.append(x)
        msg.double_data.append(y)
        rs.data_service.PostMsgToClient(msg)

    def SetColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetLineStyle(self, lineType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorLineStyle)
        msg.int_data.append(lineType)
        rs.data_service.PostMsgToClient(msg)

    def SetLineWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorLineWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def SetCursorStyle(self, cursorLineShape):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorStyle)
        msg.int_data.append(cursorLineShape)
        rs.data_service.PostMsgToClient(msg)

    def SetWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def SetHeight(self, height):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorHeight)
        msg.int_data.append(height)
        rs.data_service.PostMsgToClient(msg)

    def SetLabelColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorLabelColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetLabelFont(self, name, size, orientation=0, style=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorLabelFont)
        msg.string_data.append(name)
        msg.int_data.append(size)
        msg.float_data.append(orientation)
        msg.uint_data.append(style)
        rs.data_service.PostMsgToClient(msg)

    def SetLabelDecimal(self, decimal):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorLabelDecimal)
        msg.int_data.append(decimal)
        rs.data_service.PostMsgToClient(msg)

    def SetSnapMode(self, snapModes):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorSnapMode)
        msg.int_data.append(snapModes)
        rs.data_service.PostMsgToClient(msg)

    def SetSnapPlot(self, plotIndex):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorPlotIndex)
        msg.int_data.append(plotIndex)
        rs.data_service.PostMsgToClient(msg)

    def GetCursorPos3D(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorPos3D)
        res = rs.data_service.GetResponse(msg, 4000)
        if (res != None):
            if(len(res.double_data) == 3):
                return res.double_data;

    def SetCursorPos3D(self, x, y, z):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorSetPos3D)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        rs.data_service.PostMsgToClient(msg)

    def SetLength(self, length):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorLength)
        msg.double_data.append(length)
        rs.data_service.PostMsgToClient(msg)

    def SetTextOrientation(self, textOrientationStyle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_CursorOrientation)
        msg.int_data.append(textOrientationStyle)
        rs.data_service.PostMsgToClient(msg)

class IPDrawItem():
    def __init__(self, index, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "i" + str(index)

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        msg.string_data.append(self.context_)
        return msg

    def GetType(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemType)
        return rs.data_service.GetInt()

    def SetLineStyle(self, lineType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemLineStyle)
        msg.int_data.append(lineType)
        rs.data_service.PostMsgToClient(msg)

    def SetLineWidth(self, lineWidth):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemLineWidth)
        msg.int_data.append(lineWidth)
        rs.data_service.PostMsgToClient(msg)

    def SetLineColor(self, lineColor):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemLineColor)
        msg.uint_data.append(lineColor)
        rs.data_service.PostMsgToClient(msg)

    def SetLineBeginCap(self, lineCapType, size):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemLineBCap)
        msg.int_data.append(lineCapType)
        msg.int_data.append(size)
        rs.data_service.PostMsgToClient(msg)

    def SetLineEndCap(self, lineCapType, size):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemLineECap)
        msg.int_data.append(lineCapType)
        msg.int_data.append(size)
        rs.data_service.PostMsgToClient(msg)

    def SetFillStyle(self, fillType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemFillStyle)
        msg.int_data.append(fillType)
        rs.data_service.PostMsgToClient(msg)

    def SetFillColor(self, fillColor):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemFillColor)
        msg.uint_data.append(fillColor)
        rs.data_service.PostMsgToClient(msg)

    def SetFont(self, name, size, orientation=0, style=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemFont)
        msg.string_data.append(name)
        msg.int_data.append(size)
        msg.float_data.append(orientation)
        msg.uint_data.append(style)
        rs.data_service.PostMsgToClient(msg)

    def SetTextColor(self, textColor):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemTextColor)
        msg.uint_data.append(textColor)
        rs.data_service.PostMsgToClient(msg)

    def SetOptions(self, bVisible, bRender3D):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemOption)
        msg.bool_data.append(bVisible)
        msg.bool_data.append(bRender3D)
        rs.data_service.PostMsgToClient(msg)

    def SetText(self, text):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemText)
        msg.string_data.append(text)
        rs.data_service.PostMsgToClient(msg)

    def SetAlignment(self, horizontalAlignment, verticalAlignment):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemAlign)
        msg.int_data.append(horizontalAlignment)
        msg.int_data.append(verticalAlignment)
        rs.data_service.PostMsgToClient(msg)

    def SetCoordinates(self, x, y, type, annotationCoordinate = 0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemCoord)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.int_data.append(type)
        msg.int_data.append(annotationCoordinate)
        rs.data_service.PostMsgToClient(msg)

    def SetCoordinates3D(self, x, y, z, type, annotationCoordinate = 0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemCoord3D)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        msg.int_data.append(type)
        msg.int_data.append(annotationCoordinate)
        rs.data_service.PostMsgToClient(msg)

    def SetRotation(self, rx, ry, rz):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawItemRotation)
        msg.double_data.append(rx)
        msg.double_data.append(ry)
        msg.double_data.append(rz)
        rs.data_service.PostMsgToClient(msg)

class IPDrawGroup():

    def __init__(self, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "s"

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        msg.string_data.append(self.context_)
        return msg

    def AddGroup(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupAddGroup)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPDrawGroup(name, self.graph_);

    def RemoveGroup(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupRemoveGroup)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def FindGroup(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupFindGroup)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPDrawGroup(name, self.graph_);

    def AddItem(self, drawItemType, name=None):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupAddItem)
        msg.int_data.append(drawItemType)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPDrawItem(name, self.graph_);

    def FindItem(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupFindItem)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPDrawGroup(name, self.graph_);

    def DeleteItem(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupDeleteItem)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def RemoveAllItems(self, bDelete):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawGroupRemoveAll)
        msg.bool_data.append(bDelete)
        rs.data_service.PostMsgToClient(msg)

class IPAnnotation():
    def __init__(self, index, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "i" + str(index)

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        msg.string_data.append(self.context_)
        return msg

    def SetCaption(self, text, horizontalAlignment=0, verticalAlignment=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationCaption)
        msg.string_data.append(text)
        msg.int_data.append(horizontalAlignment)
        msg.int_data.append(verticalAlignment)
        rs.data_service.PostMsgToClient(msg)

    def SetCaptionColor(self, textcolor, backgroundColor=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationCaptionColor)
        msg.uint_data.append(textcolor)
        msg.uint_data.append(backgroundColor)
        rs.data_service.PostMsgToClient(msg)

    def SetCaptionBorder(self, borderType, borderColor = 0xFF000000, width = 1, paddingSpace = 2):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationCaptionBorder)
        msg.int_data.append(borderType)
        msg.uint_data.append(borderColor)
        msg.int_data.append(width)
        msg.int_data.append(paddingSpace)
        rs.data_service.PostMsgToClient(msg)

    def SetCaptionLocation(self, x, y, coorType=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationCaptionLoc)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.int_data.append(coorType)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowLineWidth(self, width):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowLineWidth)
        msg.int_data.append(width)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowLineColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowLineColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowLineStyle(self, lineType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowLineStyle)
        msg.int_data.append(lineType)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowTailStyle(self, lineCapType, width=5, height=10):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowLineECap)
        msg.int_data.append(lineCapType)
        msg.int_data.append(width)
        msg.int_data.append(height)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowHeadStyle(self, lineCapType, width=5, height=10):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowLineBCap)
        msg.int_data.append(lineCapType)
        msg.int_data.append(width)
        msg.int_data.append(height)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowHeadPos(self, x, y, coorType=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowPos)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.int_data.append(coorType)
        rs.data_service.PostMsgToClient(msg)

    def SetDrawType(self, drawItemType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationType)
        msg.int_data.append(drawItemType)
        rs.data_service.PostMsgToClient(msg)
        name = self.context_
        if(name is not None):
            name = name[1:]
        return IPDrawItem(self.index_, name, self.graph_)

    def SetCaptionLocation3D(self, x, y, z, annotationCoordinate=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationCaptionLoc3D)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        msg.int_data.append(annotationCoordinate)
        rs.data_service.PostMsgToClient(msg)

    def SetCaptionOrientation(self, textOrientationStyle, rotationX=0, rotationY=0, rotationZ=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationCaptionOrientation)
        msg.uint_data.append(textOrientationStyle)
        msg.double_data.append(rotationX)
        msg.double_data.append(rotationY)
        msg.double_data.append(rotationZ)
        rs.data_service.PostMsgToClient(msg)

    def SetArrowHeadPos3D(self, x, y, z, annotationCoordinate=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AnnotationArrowPos3D)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        msg.int_data.append(annotationCoordinate)
        rs.data_service.PostMsgToClient(msg)

class IPLight3D():
    def __init__(self, index, name, graph):
        self.index_ = index
        self.graph_ = graph
        if(name is not None):
            self.context_ = "s" + name
        else:
            self.context_ = "i" + str(index)
         
    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        msg.string_data.append(self.context_)
        return msg

    def ModifyOption(self, lightOptions, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightOption)
        msg.uint_data.append(lightOptions)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetDirection(self, nx, ny, nz, cutoffAngle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightOption)
        msg.double_data.append(nx)
        msg.double_data.append(ny)
        msg.double_data.append(nz)
        msg.double_data.append(cutoffAngle)
        rs.data_service.PostMsgToClient(msg)

    def SetPosition(self, px, py, pz):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightPos)
        msg.double_data.append(px)
        msg.double_data.append(py)
        msg.double_data.append(pz)
        rs.data_service.PostMsgToClient(msg)

    def SetDirectionLight(self, nx, ny, nz):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightDirLight)
        msg.double_data.append(nx)
        msg.double_data.append(ny)
        msg.double_data.append(nz)
        rs.data_service.PostMsgToClient(msg)

    def SetPointLight(self, px, py, pz):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightPointLight)
        msg.double_data.append(px)
        msg.double_data.append(py)
        msg.double_data.append(pz)
        rs.data_service.PostMsgToClient(msg)

    def SetSpotLight(self, px, py, pz, nx, ny, nz, cutoffAngle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightSpotLight)
        msg.double_data.append(px)
        msg.double_data.append(py)
        msg.double_data.append(pz)
        msg.double_data.append(nx)
        msg.double_data.append(ny)
        msg.double_data.append(nz)
        msg.double_data.append(cutoffAngle)
        rs.data_service.PostMsgToClient(msg)

    def SetColor(self, diffuse, ambient, specular):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightColor)
        msg.uint_data.append(diffuse)
        msg.uint_data.append(ambient)
        msg.uint_data.append(specular)
        rs.data_service.PostMsgToClient(msg)

    def SetAttenuation(self, constant, linear, quadratic):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LightAtt)
        msg.float_data.append(constant)
        msg.float_data.append(linear)
        msg.float_data.append(quadratic)
        rs.data_service.PostMsgToClient(msg)
 
class IPPalette():
    def __init__(self, graph):
        self.graph_ = graph

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        return msg

    def ModifyOption(self, paletteOptions, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteOption)
        msg.uint_data.append(paletteOptions)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetTitle(self, title, bShortTitle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteTitle)
        msg.string_data.append(title)
        msg.bool_data.append(bShortTitle)
        rs.data_service.PostMsgToClient(msg)

    def SetAlign(self, locationSide):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteAlign)
        msg.int_data.append(locationSide)
        rs.data_service.PostMsgToClient(msg)

    def SetTransparency(self, tran, startCValue, endCValue, bAllValue):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteTransparency)
        msg.int_data.append(tran)
        msg.double_data.append(startCValue)
        msg.double_data.append(endCValue)
        msg.bool_data.append(bAllValue)
        rs.data_service.PostMsgToClient(msg)

    def SetMaximumScale(self, maxScale):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteMax)
        msg.double_data.append(maxScale)
        rs.data_service.PostMsgToClient(msg)

    def SetMinimumScale(self, minScale):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteMin)
        msg.double_data.append(minScale)
        rs.data_service.PostMsgToClient(msg)

    def GetColor(self, index):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteGetColor)
        msg.int_data.append(index)
        rs.data_service.GetInt(msg)

    def SetColor(self, index, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteSetColor)
        msg.int_data.append(index)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetLevelNum(self, numThreshold):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteLevelNum)
        msg.int_data.append(numThreshold)
        rs.data_service.PostMsgToClient(msg)

    def SetLevelValue(self, level, value):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteLevelValue)
        msg.int_data.append(level)
        msg.double_data.append(value)
        rs.data_service.PostMsgToClient(msg)

    def SetLevelType(self, level, type):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_PaletteLevelType)
        msg.int_data.append(level)
        msg.int_data.append(type)
        rs.data_service.PostMsgToClient(msg)

class IPLegend():
    def __init__(self, graph):
        self.graph_ = graph

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_.graph_id
        return msg

    def SetVisible(self, bVisible):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LegendVisible)
        msg.bool_data.append(bVisible)
        rs.data_service.PostMsgToClient(msg)

    def SetLength(self, length):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LegendLength)
        msg.int_data.append(length)
        rs.data_service.PostMsgToClient(msg)

    def SetSpace(self, space, padding):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LegendPad)
        msg.int_data.append(space)
        msg.int_data.append(padding)
        rs.data_service.PostMsgToClient(msg)

    def SetLocationSide(self, locationSide):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LegenLoc)
        msg.int_data.append(locationSide)
        rs.data_service.PostMsgToClient(msg)

    def SetFont(self, name, size, orientation=0, style=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_LegenFont)
        msg.string_data.append(name)
        msg.int_data.append(size)
        msg.float_data.append(orientation)
        msg.uint_data.append(style)
        rs.data_service.PostMsgToClient(msg)
 
class IPGraph():
    def __init__(self, name):
        self.graph_id = name

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.graph_id
        return msg

    def SetGraphQuality(self, graphQualityType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetGraphQuality)
        msg.int_data.append(graphQualityType)
        rs.data_service.PostMsgToClient(msg)

    def SetGraphCategory(self, graphCategory, plotStyle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetGraphCategory)
        msg.int_data.append(graphCategory)
        msg.int_data.append(plotStyle)
        rs.data_service.PostMsgToClient(msg)

    def RedrawPlotArea(self, updatenow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RedrawPlotArea)
        msg.bool_data.append(updatenow)
        rs.data_service.PostMsgToClient(msg)

    def RedrawGraph(self, bRedrawBord=False):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_Redraw)
        msg.bool_data.append(bRedrawBord)
        rs.data_service.PostMsgToClient(msg)

    def SetDisplayOrder(self, graphDisplayOrder):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetDisplayOrder)
        msg.int_data.append(graphDisplayOrder)
        rs.data_service.PostMsgToClient(msg)

    def SetMouseTrackingMode(self, graphMouseTrackingMode, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_TrackMode)
        msg.int_data.append(graphMouseTrackingMode)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetFrameColor(self, fillType, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetFrameColor)
        msg.int_data.append(fillType)
        msg.int_data.append(len(color))
        msg.uint_data.extend(color)
        rs.data_service.PostMsgToClient(msg)

    def SetPlotAreaColor(self, fillStyle, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetPlotAreaColor)
        msg.int_data.append(fillStyle)
        msg.int_data.append(len(color))
        msg.uint_data.extend(color)
        rs.data_service.PostMsgToClient(msg)

    def SetCaption(self, caption):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetCaption)
        msg.string_data.append(caption)
        rs.data_service.PostMsgToClient(msg)

    def SetCaptionAlign(self, align):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetCaptionAlign)
        msg.int_data.append(align)
        rs.data_service.PostMsgToClient(msg)

    def SetCaptionColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetCaptionColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def GetAxisCount(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetAxisCount)
        return rs.data_service.GetInt(msg)

    def Axes(self, index_or_name):
        if(isinstance(index_or_name, str)):
            return IPAxis(-1, index_or_name, self)
        else:
            return IPAxis(index_or_name, None, self)

    def NewAxis(self, name, type):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddAxis)
        msg.string_data.append(name)
        msg.int_data.append(type)
        rs.data_service.PostMsgToClient(msg)
        return IPAxis(-1, name, self)

    def RemoveAxis(self, index_or_name):
        if(isinstance(index_or_name, str)):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveAxisByName)
            msg.string_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveAxis)
            msg.int_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)

    def GetPlotCount(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetPlotsCount)
        return rs.data_service.GetInt(msg)

    def Plots(self, index_or_name):
        if(isinstance(index_or_name, str)):
            return IPPlot(-1, index_or_name, self)
        else:
            return IPPlot(index_or_name, None, self)

    def NewPlot(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddPlot)
        msg.string_data.append(name)
        msg.int_data.append(0)
        rs.data_service.PostMsgToClient(msg)
        return IPPlot(-1, name, self)

    def RemovePlot(self, index_or_name):
        if(isinstance(index_or_name, str)):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemovePlotByName)
            msg.string_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemovePlot)
            msg.int_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)

    def Set3DBarOffset(self, offset):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_BarOffset)
        msg.int_data.append(offset)
        rs.data_service.PostMsgToClient(msg)

    def GetLegend(self):
        return IPLegend(self)

    def GetCursorCount(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetCursorCount)
        return rs.data_service.GetInt(msg)

    def Cursors(self, index_or_name):
        if(isinstance(index_or_name, str)):
            return IPCursor(-1, index_or_name, self)
        else:
            return IPCursor(index_or_name, None, self)

    def NewCursor(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddCursor)
        msg.string_data.append(name)
        msg.int_data.append(0)
        rs.data_service.PostMsgToClient(msg)
        return IPCursor(-1, name, self)

    def RemoveCursor(self, index_or_name):
        if(isinstance(index_or_name, str)):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveCursorByName)
            msg.string_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveCursorByIndex)
            msg.int_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)

    def GetAnnotationCount(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetAnnotationCount)
        return rs.data_service.GetInt(msg)

    def NewAnnotation(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddAnnotation)
        msg.string_data.append(name)
        msg.int_data.append(0)
        rs.data_service.PostMsgToClient(msg)
        return IPAnnotation(-1, name, self)

    def Annotations(self, index_or_name):
        if(isinstance(index_or_name, str)):
            return IPAnnotation(-1, index_or_name, self)
        else:
            return IPAnnotation(index_or_name, None, self)

    def RemoveAnnotation(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveAnnotationByName)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def ShowAnnotationEditBar(self, dockSide, bVisible, x=-1, y=-1, cx=-1, cy=-1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ShowAnnotationEditBar)
        msg.int_data.append(dockSide)
        msg.bool_data.append(bVisible)
        msg.int_data.append(x)
        msg.int_data.append(y)
        msg.int_data.append(cx)
        msg.int_data.append(cy)
        rs.data_service.PostMsgToClient(msg)

    def GetPalette(self):
        return IPPalette(self)

    def SetPalette(self, minScale=0, maxScale=1, bVisible=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetPalette)
        msg.double_data.append(minScale)
        msg.double_data.append(maxScale)
        msg.bool_data.append(bVisible)
        rs.data_service.PostMsgToClient(msg)

    def SetSkyBackground(self, right, left, top, bottom, back, front):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GraphSetSkyBackground)
        msg.string_data.append(right)
        msg.string_data.append(left)
        msg.string_data.append(top)
        msg.string_data.append(bottom)
        msg.string_data.append(back)
        msg.string_data.append(front)
        rs.data_service.PostMsgToClient(msg)

    def SetProjectionType(self, projection3DType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ProjectionType)
        msg.int_data.append(projection3DType)
        rs.data_service.PostMsgToClient(msg)

    def SetOrientation(self, ax, ay, az):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetOrientation)
        msg.double_data.append(ax)
        msg.double_data.append(ay)
        msg.double_data.append(az)
        rs.data_service.PostMsgToClient(msg)

    def SetViewCenter(self, x, y, z):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetViewCenter)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        rs.data_service.PostMsgToClient(msg)

    def SetScale(self, sx, sy, sz):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetViewScale)
        msg.double_data.append(sx)
        msg.double_data.append(sy)
        msg.double_data.append(sz)
        rs.data_service.PostMsgToClient(msg)

    def SetPlotAreaScale(self, scale):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetPlotAreaScale)
        msg.double_data.append(scale)
        rs.data_service.PostMsgToClient(msg)

    def SetClip(self, bClip):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetClip)
        msg.bool_data.append(bClip)
        rs.data_service.PostMsgToClient(msg)

    def GetLightCount(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetLightCount)
        return rs.data_service.GetInt(msg)

    def NewLight(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddLight)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPLight3D(-1, name, self)

    def Lights(self,  index_or_name):
        if(isinstance(index_or_name, str)):
            return IPLight3D(-1, index_or_name, self)
        else:
            return IPLight3D(index_or_name, None, self)

    def RemoveLight(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveLightByName)
        msg.string_data.append(index_or_name)
        rs.data_service.PostMsgToClient(msg)

class IPDraw():
    def __init__(self, name):
        self.draw_id = name
 
    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.draw_id
        return msg

    def SetBackgroundColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawBackgroundColor)
        msg.uint_data.append(color)
        rs.data_service.PostMsgToClient(msg)

    def SetPageSize(self, pageX, pageY, pageWidth, pageHeight, systemLengthUnit):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawPageSize)
        msg.double_data.append(pageX)
        msg.double_data.append(pageY)
        msg.double_data.append(pageWidth)
        msg.double_data.append(pageHeight)
        msg.int_data.append(systemLengthUnit)
        rs.data_service.PostMsgToClient(msg)

    def SetZoomMode(self, drawZoom_Mode):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawZoomMode)
        msg.int_data.append(drawZoom_Mode)
        rs.data_service.PostMsgToClient(msg)

    def ShowDrawTools(self, locationSide, bFloating, bVisible):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DrawDrawTools)
        msg.int_data.append(locationSide)
        msg.bool_data.append(bFloating)
        msg.bool_data.append(bVisible)
        rs.data_service.PostMsgToClient(msg)

    def GetDrawModel(self):
        return IPDrawGroup(0, self)

    def AddDrawGroup(self, bSetActive, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddDrawGroup)
        msg.bool_data.append(bSetActive)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPDrawGroup(name, draw_id)

    def FindDrawGroup(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_FindDrawGroup)
        msg.string_data.append(name)
        return rs.data_service.GetInt(msg), IPDrawGroup(name, draw_id)

    def SetActiveDrawGroup(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ActiveDrawGroup)
        msg.string_data.append(name)
        return IPDrawGroup(name, draw_id)

    def AddDrawItem(self, drawItemType, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddDrawItem)
        msg.string_data.append(name)
        msg.int_data.append(drawItemType)
        return IPDrawGroup(name, draw_id)

    def FindDrawItem(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_FindDrawItem)
        msg.string_data.append(name)
        return rs.data_service.GetInt(msg), IPDrawItem(name, draw_id)

    def DeleteDrawItem(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_DeleteDrawItem)
        msg.string_data.append(name)
        return rs.data_service.PostMsgToClient(msg)

    def RemoveCursor(self, index_or_name):
        if(isinstance(index_or_name, str)):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveDrawCursorByName)
            msg.string_data.append(name)
            return rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveDrawCursorByIndex)
            msg.int_data.append(index_or_name)
            return rs.data_service.PostMsgToClient(msg)

    def NewCursor(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddDrawCursor)
        msg.string_data.append(name)
        return IPCursor(name, draw_id)

    def SetSkyBackground(self, right, left, top, bottom, back, front):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetSkyBackground)
        msg.string_data.append(right)
        msg.string_data.append(left)
        msg.string_data.append(top)
        msg.string_data.append(bottom)
        msg.string_data.append(back)
        msg.string_data.append(front)
        rs.data_service.PostMsgToClient(msg)

    def SetProjectionType(self, projection3DType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ProjectionType)
        msg.int_data.append(projection3DType)
        rs.data_service.PostMsgToClient(msg)

    def SetOrientation(self, ax, ay, az):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetDrawOrientation)
        msg.double_data.append(ax)
        msg.double_data.append(ay)
        msg.double_data.append(az)
        rs.data_service.PostMsgToClient(msg)

    def SetViewCenter(self, x, y, z):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetDrawViewCenter)
        msg.double_data.append(x)
        msg.double_data.append(y)
        msg.double_data.append(z)
        rs.data_service.PostMsgToClient(msg)

    def SetScale(self, sx, sy, sz):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_SetViewScale)
        msg.double_data.append(sx)
        msg.double_data.append(sy)
        msg.double_data.append(sz)
        rs.data_service.PostMsgToClient(msg)

    def GetLightCount(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetDrawLightCount)
        return rs.data_service.GetInt(msg)

    def NewLight(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddDrawLight)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)
        return IPLight3D(-1, name, self)

    def Lights(self, index_or_name):
        if(isinstance(index_or_name, str)):
            return IPLight3D(-1, index_or_name, self)
        else:
            return IPLight3D(index_or_name, None, self)

    def RemoveLight(self, index_or_name):
        if(isinstance(index_or_name, str)):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveDrawLightByName)
            msg.string_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_RemoveDrawLightByIndex)
            msg.int_data.append(index_or_name)
            rs.data_service.PostMsgToClient(msg)

    def GetDrawImage(self, pData, width, height, type, bBottomUp):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GetDrawImage)
        msg.int_data.append(width)
        msg.int_data.append(height)
        msg.int_data.append(type)
        msg.int_data.append(bBottomUp)
        return np.frombuffer(rs.data_service.GetByteBuff(msg), dtype=np.uint8)

class IPDataTable():
    def __init__(self, name):
        self.grid_id = name
    
    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.grid_id
        return msg

    def SetTableType(self, tableType, bInitial=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridType)
        msg.int_data.append(tableType)
        msg.bool_data.append(bInitial)
        rs.data_service.PostMsgToClient(msg)

    def ModifyOption(self, tableOptions, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridOption)
        msg.uint_data.append(tableOptions)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def ModifyPopupMenu(self, tableMenuStyle, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridMemuStyle)
        msg.uint_data.append(tableMenuStyle)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def GetColNumber(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetColNumber)
        return rs.data_service.GetInt(msg)

    def GetRowNumber(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetRowNumber)
        return rs.data_service.GetInt(msg)

    def SetColNumber(self, column_number):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridColNumber)
        msg.int_data.append(column_number)
        rs.data_service.PostMsgToClient(msg)

    def SetRowNumber(self, row_number):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRowNumber)
        msg.int_data.append(row_number)
        rs.data_service.PostMsgToClient(msg)

    def AppendRow(self, numRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridAppendRow)
        msg.int_data.append(numRow)
        rs.data_service.PostMsgToClient(msg)

    def AppendCol(self, numCol):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridAppendCol)
        msg.int_data.append(numCol)
        rs.data_service.PostMsgToClient(msg)

    def InsertRow(self, insertAfter, numRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridInsertRow)
        msg.int_data.append(insertAfter)
        msg.int_data.append(numRow)
        rs.data_service.PostMsgToClient(msg)

    def InsertCol(self, insertAfter, numCol):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridInsertCol)
        msg.int_data.append(insertAfter)
        msg.int_data.append(numCol)
        rs.data_service.PostMsgToClient(msg)

    def InsertCells(self, cellInsertOption, numcell, numrow, numcol):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridInsertCell)
        msg.int_data.append(cellInsertOption)
        msg.int_data.append(numcell)
        msg.int_data.append(numrow)
        msg.int_data.append(numcol)
        rs.data_service.PostMsgToClient(msg)

    def RemoveCells(self, cellDeleteOption, numcell, numrow, numcol):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRemoveCell)
        msg.int_data.append(cellDeleteOption)
        msg.int_data.append(numcell)
        msg.int_data.append(numrow)
        msg.int_data.append(numcol)
        rs.data_service.PostMsgToClient(msg)

    def RemoveRow(self, firstRow, lastRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRemoveRow)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastRow)
        rs.data_service.PostMsgToClient(msg)

    def RemoveCol(self, firstCol, lastCol):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRemoveRow)
        msg.int_data.append(firstCol)
        msg.int_data.append(lastCol)
        rs.data_service.PostMsgToClient(msg)

    def RemoveAll(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRemoveAll)
        rs.data_service.PostMsgToClient(msg)

    def GetSelCells(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetSelCell)
        res = rs.data_service.GetResponse(msg, 4000)
        if (res != None):
            if(len(res.int_data) == 4):
                return res.int_data

    def SetSelCells(self, firstCol, firstRow, lastCol, lastRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridSelCell)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        rs.data_service.PostMsgToClient(msg)

    def JointCells(self, firstCol, firstRow, lastCol, lastRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridJointCell)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        rs.data_service.PostMsgToClient(msg)

    def UnJointCells(self, firstCol, firstRow, lastCol, lastRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridUnJointCell)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        rs.data_service.PostMsgToClient(msg)

    def SetCellData(self, col, row, data):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellData)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.double_data.append(data)
        rs.data_service.PostMsgToClient(msg)

    def SetCellText(self, col, row, pText, bText=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellText)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.string_data.append(pText)
        msg.bool_data.append(bText)
        rs.data_service.PostMsgToClient(msg)

    def SetCellChar(self, col, row, pText, len, bText=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellChar)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.string_data.append(pText[:len])
        msg.bool_data.append(bText)
        rs.data_service.PostMsgToClient(msg)

    def SetRowData(self, row, firstCol, numData, data0, dataInc, bAdd=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRowData)
        msg.int_data.append(row)
        msg.int_data.append(firstCol)
        msg.int_data.append(numData)
        msg.double_data.append(data0)
        msg.double_data.append(dataInc)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetColData(self, col, firstRow, numData, data0, dataInc, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridColData)
        msg.int_data.append(col)
        msg.int_data.append(firstRow)
        msg.int_data.append(numData)
        msg.double_data.append(data0)
        msg.double_data.append(dataInc)
        msg.bool_data.append(bAdd)
        rs.data_service.PostMsgToClient(msg)

    def SetColData(self, col, firstRow, array, bAdd):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridColDataArray)
        msg.int_data.append(col)
        msg.int_data.append(firstRow)
        msg.bool_data.append(bAdd)
        msg.int_data.append(len(array))
        msg.double_data.extend(array)
        rs.data_service.PostMsgToClient(msg)

    def SetData(self, firstCol, firstRow, lastCol, lastRow, array, bTranspose, bAdd=True):
        if(len(array) * 8 > rs.config.max_msg_size):
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridData| RPCMessageID.IPCMsg_Has_Stream)
            step = int(rs.config.max_msg_size / 4)
            n = int(len(array) / step)
            def SteamMsg():
                for i in range(n):
                    del msg.double_data[:]
                    msg.double_data.extend(array[i * step:(i + 1) * step])
                    yield msg
                del msg.double_data[:]
                if n * step < len(array):
                    msg.double_data.extend(array[n * step:])
                yield msg
            rs.data_service.PostMsgStreamToClient(msg, SteamMsg)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridData | RPCMessageID.IPCMsg_Has_Stream | RPCMessageID.IPCMsg_Has_EndStream)
            msg.int_data.append(firstCol)
            msg.int_data.append(firstRow)
            msg.int_data.append(lastCol)
            msg.int_data.append(lastRow)
            msg.bool_data.append(bTranspose)
            msg.bool_data.append(bAdd)
            msg.int_data.append(len(array))
            rs.data_service.PostMsgToClient(msg)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridData)
            msg.int_data.append(firstCol)
            msg.int_data.append(firstRow)
            msg.int_data.append(lastCol)
            msg.int_data.append(lastRow)
            msg.bool_data.append(bTranspose)
            msg.bool_data.append(bAdd)
            msg.int_data.append(len(array))
            msg.double_data.extend(array)
            rs.data_service.PostMsgToClient(msg)

    def SetText(self, firstCol, firstRow, lastCol, lastRow, labels, bTranspose, bAdd = True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridText)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.bool_data.append(bTranspose)
        msg.bool_data.append(bAdd)
        msg.int_data.append(len(labels))
        msg.string_data.extend(labels)
        rs.data_service.PostMsgToClient(msg)

    def SetReadOnly(self, firstCol, firstRow, lastCol, lastRow, bReadOnly=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridReadOnly)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.bool_data.append(bReadOnly)
        rs.data_service.PostMsgToClient(msg)

    def SetColReadOnly(self, col, bReadOnly=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridColReadOnly)
        msg.int_data.append(col)
        msg.bool_data.append(bReadOnly)
        rs.data_service.PostMsgToClient(msg)

    def SetRowReadOnly(self, row, bReadOnly=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRowReadOnly)
        msg.int_data.append(row)
        msg.bool_data.append(bReadOnly)
        rs.data_service.PostMsgToClient(msg)

    def GetCellData(self, col, row):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetCellData)
        msg.int_data.append(col)
        msg.int_data.append(row)
        return rs.data_service.GetDouble(msg)

    def GetCellText(self, col, row):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetCellText)
        msg.int_data.append(col)
        msg.int_data.append(row)
        return rs.data_service.GetString(msg)

    def GetData(self, col0, col1, colInc, row0, row1, rowInc, data):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetData)
        msg.int_data.append(col0)
        msg.int_data.append(col1)
        msg.int_data.append(colInc)
        msg.int_data.append(row0)
        msg.int_data.append(row1)
        msg.int_data.append(rowInc)
        msg.int_data.append(data.size)
        res = rs.data_service.GetResponse(msg)
        if (res != None):
            if(len(res.double_data) > 0):
                data[:] = res.double_data
                return len(res.double_data)

    def GetColData(self, col, firstRow, lastRow, rowInc, data, bValidOnly=False):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetColData)
        msg.int_data.append(col)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastRow)
        msg.int_data.append(rowInc)
        msg.int_data.append(bValidOnly)
        msg.int_data.append(data.size)
        res = rs.data_service.GetResponse(msg)
        if (res != None):
            if(len(res.double_data) > 0):
                data[:] = res.double_data
                return len(res.double_data)

    def GetText(self, col0, col1, colInc, row0, row1, rowInc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetText)
        msg.int_data.append(col0)
        msg.int_data.append(col1)
        msg.int_data.append(colInc)
        msg.int_data.append(row0)
        msg.int_data.append(row1)
        msg.int_data.append(rowInc)
        res = rs.data_service.GetResponse(msg)
        if (res != None):
            if(len(res.string_data) > 0):
                return res.string_data

    def GetColText(self, row, firstCol, lastCol, colInc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetColText)
        msg.int_data.append(row)
        msg.int_data.append(firstCol)
        msg.int_data.append(lastCol)
        msg.int_data.append(colInc)
        res = rs.data_service.GetResponse(msg)
        if (res != None):
            if(len(res.string_data) > 0):
                return res.string_data

    def GetRowText(self, col, firstRow, lastRow, rowInc):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetRowText)
        msg.int_data.append(col)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastRow)
        msg.int_data.append(rowInc)
        res = rs.data_service.GetResponse(msg)
        if (res != None):
            if(len(res.string_data) > 0):
                return res.string_data

    def GetRowData(self, row, firstCol, lastCol, colInc, data, bValidOnly=False):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetRowData)
        msg.int_data.append(row)
        msg.int_data.append(firstCol)
        msg.int_data.append(lastCol)
        msg.int_data.append(colInc)
        msg.int_data.append(bValidOnly)
        msg.int_data.append(data.size)
        res = rs.data_service.GetResponse(msg)
        if (res != None):
            if(len(res.double_data) > 0):
                data[:] = res.double_data
                return len(res.double_data)

    def ClearData(self, firstCol, firstRow, lastCol, lastRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridClearData)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        rs.data_service.PostMsgToClient(msg)

    def DeleteData(self, firstCol, firstRow, lastCol, lastRow):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridDeleteData)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        rs.data_service.PostMsgToClient(msg)

    def SetDefaultColWidth(self, colWidth):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridDefaultColWidth)
        msg.int_data.append(colWidth)
        rs.data_service.PostMsgToClient(msg)

    def SetDefaultRowHeight(self, rowHeight):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridDefaultRowHeight)
        msg.int_data.append(rowHeight)
        rs.data_service.PostMsgToClient(msg)

    def SetColWidth(self, col, width, bFix=False):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridColWidth)
        msg.int_data.append(col)
        msg.int_data.append(width)
        msg.int_data.append(bFix)
        rs.data_service.PostMsgToClient(msg)

    def SetRowHeight(self, row, height, bFix=False):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRowHeight)
        msg.int_data.append(row)
        msg.int_data.append(height)
        msg.int_data.append(bFix)
        rs.data_service.PostMsgToClient(msg)

    def FitColToWindow(self, col0, col1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridFitCol)
        msg.int_data.append(col0)
        msg.int_data.append(col1)
        rs.data_service.PostMsgToClient(msg)

    def FitRowToWindow(self, row0, row1):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridFitRow)
        msg.int_data.append(row0)
        msg.int_data.append(row1)
        rs.data_service.PostMsgToClient(msg)

    def EnableScroll(self, bHScroll, bVScroll, bAutoScroll=True):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridEnableScroll)
        msg.bool_data.append(bHScroll)
        msg.bool_data.append(bVScroll)
        msg.bool_data.append(bAutoScroll)
        rs.data_service.PostMsgToClient(msg)

    def SetTopHeaderNum(self, n):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridTopHeaderNum)
        msg.int_data.append(n)
        rs.data_service.PostMsgToClient(msg)

    def SetLeftHeaderNum(self, n):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridLeftHeaderNum)
        msg.int_data.append(n)
        rs.data_service.PostMsgToClient(msg)

    def GetColName(self, col):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetColName)
        msg.int_data.append(col)
        return rs.data_service.GetString(msg)

    def SetCellFormat(self, firstCol, firstRow, lastCol, lastRow, gridCellType, gridCellStyle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellFormat)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.int_data.append(gridCellType)
        msg.int_data.append(gridCellStyle)
        rs.data_service.PostMsgToClient(msg)

    def SetCellAlignment(self, firstCol, firstRow, lastCol, lastRow, horizontalAlignment, verticalAlignment, gridTextWrap):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellAlignment)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.int_data.append(horizontalAlignment)
        msg.int_data.append(verticalAlignment)
        msg.int_data.append(gridTextWrap)
        rs.data_service.PostMsgToClient(msg)

    def SetCellStyle(self, col, row, gridCellStyle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellAlignment)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(gridCellStyle)
        rs.data_service.PostMsgToClient(msg)

    def SetCellType(self, col, row, gridCellType):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellType)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(gridCellType)
        rs.data_service.PostMsgToClient(msg)

    def SetCellTypeStyle(self, gridCellType, fill, text):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellTypeStyle)
        msg.int_data.append(gridCellType)
        msg.int_data.append(fill)
        msg.int_data.append(text)
        rs.data_service.PostMsgToClient(msg)

    def SetCellhAlignment(self, col, row, horizontalAlignment):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellhAlign)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(horizontalAlignment)
        rs.data_service.PostMsgToClient(msg)

    def SetCellvAlignment(self, col, row, verticalAlignment):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellvAlign)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(verticalAlignment)
        rs.data_service.PostMsgToClient(msg)

    def SetCellTextWrap(self, col, row, gridTextWrap):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridTextWrap)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(gridTextWrap)
        rs.data_service.PostMsgToClient(msg)

    def SetTextRotation(self, col, row, textAngle):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridTextRotation)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.double_data.append(textAngle)
        rs.data_service.PostMsgToClient(msg)

    def SetDataDecimalNum(self, col, row, decNum):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridDecimal)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(decNum)
        rs.data_service.PostMsgToClient(msg)

    def SetDataCategory(self, col, row, gridCellDataCategory):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridDataCategory)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(gridCellDataCategory)
        rs.data_service.PostMsgToClient(msg)

    def SetDataFormat(self, col, row, gridCellDataFormat):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridCellDataFormat)
        msg.int_data.append(col)
        msg.int_data.append(row)
        msg.int_data.append(gridCellDataFormat)
        rs.data_service.PostMsgToClient(msg)

    def AddFont(self, name, size, orientation=0, style=0):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridAddFont)
        msg.string_data.append(name)
        msg.int_data.append(size)
        msg.float_data.append(orientation)
        msg.uint_data.append(style)
        return rs.data_service.GetInt(msg)

    def GetFont(self, index):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetFont)
        msg.int_data.append(index)
        return rs.data_service.GetString(msg)

    def SetCellFont(self, firstCol, firstRow, lastCol, lastRow, fontIndex):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridSetFont)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.int_data.append(fontIndex)
        rs.data_service.PostMsgToClient(msg)

    def AddColor(self, color):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridAddColor)
        msg.uint_data.append(color)
        return rs.data_service.GetInt(msg)

    def SetCellTextColor(self, firstCol, firstRow, lastCol, lastRow, crIndex):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridTextColor)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.int_data.append(crIndex)
        rs.data_service.PostMsgToClient(msg)

    def SetCellFillColor(self, firstCol, firstRow, lastCol, lastRow, crIndex):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridFillColor)
        msg.int_data.append(firstCol)
        msg.int_data.append(firstRow)
        msg.int_data.append(lastCol)
        msg.int_data.append(lastRow)
        msg.int_data.append(crIndex)
        rs.data_service.PostMsgToClient(msg)

    def TabAppearance(self, bTabNavigate, bTabDropDown):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridTab)
        msg.bool_data.append(bTabNavigate)
        msg.bool_data.append(bTabDropDown)
        rs.data_service.PostMsgToClient(msg)

    def SetSheetName(self, iSheet, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridSheetName)
        msg.int_data.append(iSheet)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def AddSheet(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridAddSheet)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def InsertSheet(self, iSheet, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridInsertSheet)
        msg.int_data.append(iSheet)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def RemoveSheet(self, iSheet):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridRemoveSheet)
        msg.int_data.append(iSheet)
        rs.data_service.PostMsgToClient(msg)

    def SelectSheet(self, iSheet):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridSelectSheet)
        msg.int_data.append(iSheet)
        rs.data_service.PostMsgToClient(msg)

    def GetSheetNumber(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_GridGetSheetNumber)
        return rs.data_service.GetInt(msg)

    def GetDataFrame(self, colStart, colEnd, rowStart, rowEnd, needColumnLabel, needIndexLabel, isText):
        import pandas
        ncol = colEnd - colStart + 1
        nrow = rowEnd - rowStart + 1
        n = ncol * nrow
        if(isText):
            data = np.array(self.GetText(colStart, colEnd, 1, rowStart, rowEnd, 1))
        else:
            data = np.zeros(n)
            self.GetData(colStart, colEnd, 1, rowStart, rowEnd, 1, data)
        data = data.reshape([nrow, ncol])
        if(needColumnLabel):
            cols = self.GetRowText(0, colStart, colEnd, 1)
        else:
            cols = np.array(range(0, ncol))
        if(needIndexLabel):
            rows = self.GetColText(0, rowStart, rowEnd, 1)
        else:
            rows = np.array(range(0, nrow))
        return pandas.DataFrame(data, index = rows, columns = cols)

    def GetSeries(self, col, rowStart, rowEnd, needIndexLabel, isText):
        import pandas
        nrow = rowEnd - rowStart + 1
        if(isText):
            data = self.GetColText(col, rowStart, rowEnd, 1)
        else:
            data = np.zeros(nrow)
            self.GetColData(col, rowStart, rowEnd, 1, data)
        if(needIndexLabel):
            rows = self.GetColText(0, rowStart, rowEnd, 1)
        else:
            rows = np.array(range(0, nrow))
        return pandas.Series(data, index = rows)

    def SetDataFrame(self, dataFrame, colStart, rowStart):
        import pandas
        import numbers
        data = dataFrame.values;
        ncol = data.shape[1]
        nrow = data.shape[0]
        for col in range(ncol):
            a = data[:, col]
            if isinstance(a[0], numbers.Number): 
                if a.dtype == object:
                    a = a.astype(np.float64)
                    self.SetColData(col + colStart, rowStart, a, True)
                else:
                    self.SetColData(col + colStart, rowStart, a, True)
            else:
                if a.dtype == str:
                    self.SetText(col + colStart, rowStart, col + colStart, nrow + rowStart - 1, a, False, True)
                else:
                    a = a.astype('str')
                    self.SetText(col + colStart, rowStart, col + colStart, nrow + rowStart - 1, a, False, True)

class IPCamera(IPGraph):
    def __init__(self, name):
        self.name_ = name

    def GetImage(self, width, height, channel, batch):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Device_GetCameraImage)
        msg.int_data.append(batch)
        msg.int_data.append(height)
        msg.int_data.append(width)
        msg.int_data.append(channel)
        res = rs.data_service.GetResponse(msg, 4000)
        if (res != None):
            if(len(res.byte_data) == 1):
                image = np.frombuffer(res.byte_data, dtype=np.uint8)
                image.astype(np.float32)
                return image / 127.5 - 1 

    def GetImage_uint8(self, width, height, channel, batch):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Device_GetCameraImage)
        msg.int_data.append(batch)
        msg.int_data.append(height)
        msg.int_data.append(width)
        msg.int_data.append(channel)
        res = rs.data_service.GetResponse(msg, 4000)
        if (res != None):
            if(len(res.byte_data) == 1):
                image = np.frombuffer(res.byte_data, dtype=np.uint8)
                return np.reshape(image, (batch, height, width, channel))

    def ClearBoundingBox(self):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_ClearBoundingBox)
        rs.data_service.PostMsgToClient(msg)

    def DrawBoundingBox(self, *args):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddBoundingBox)
        msg.double_data.append(x0)
        msg.double_data.append(y0)
        msg.double_data.append(x1)
        msg.double_data.append(y1)
        msg.int_data.append(bNormalized)
        msg.uint_data.append(border_color)
        msg.int_data.append(border_width)
        msg.int_data.append(font_size)
        msg.uint_data.append(text_color)
        rs.data_service.PostMsgToClient(msg)

    def DrawMaskImage(self, image, threshold, color, x0, y0, x1, y1, bNormalized):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Widget_AddMaskImage)
        DIM2 = image.shape[1]
        DIM1 = image.shape[0]
        msg.int_data.append(DIM1)
        msg.int_data.append(DIM2)
        msg.float_data.append(threshold)
        msg.uint_data.append(color)
        msg.double_data.append(x0)
        msg.double_data.append(y0)
        msg.double_data.append(x1)
        msg.double_data.append(y1)
        msg.int_data.append(bNormalized)
        msg.float_data.extend(image)
        rs.data_service.PostMsgToClient(msg)
         
class IPAudio(IPGraph):
    def __init__(self, name):
        self.name_ = name

    def GetWaveform(self, wave):
        return

class IPStudio():

    def __init__(self):
        self.recv_name_ = "AIAcq"
        self.scalarDataList = {}
        type = 10;
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_GetFolder)
        msg.int_data.append(type)
        self.DataFolder = rs.data_service.GetString(msg)
        type = 11
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_GetFolder)
        msg.int_data.append(type)
        self.ProjectFolder = rs.data_service.GetString(msg)
        type = 12
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_GetFolder)
        msg.int_data.append(type)
        self.SystemFolder = rs.data_service.GetString(msg)
        type = 13
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_GetFolder)
        msg.int_data.append(type)
        IPStudio.LogFileName = rs.data_service.GetString(msg)
        if(IPStudio.LogFileName != None):
            with open(IPStudio.LogFileName, 'wb') as fp:
                id = bytes([0x0A,0,0,0x31, 0, 0, 0, 0])
                fp.write(id)

    def _byte(b):
        return bytes((b, ))
        
    def __varintEncode(number):
        buf = b''
        while True:
            towrite = number & 0x7f
            number >>= 7
            if number:
                buf += IPStudio._byte(towrite | 0x80)
            else:
                buf += IPStudio._byte(towrite)
                break
        return buf

    def __varintDecode(stream):
        shift = 0
        result = 0
        numRead = 0
        while True:
            v = stream[numRead]
            result |= (v & 0x7f) << shift
            shift += 7
            numRead += 1
            if(numRead > 5):
                raise ValueError("VarInt is too big")
            if not (v & 0x80):
                break
        return result, numRead

    TableKey_AcqData = 0x30000000
    TableKey_AcqDataCtrl = TableKey_AcqData + 0x01000000 + 0
    TableKey_AcqDataCtrlPyScalar = TableKey_AcqDataCtrl + 5
    TableKey_AcqDataCtrlPyTensor = TableKey_AcqDataCtrl + 4
    TableKey_AcqDataCtrlPyText = TableKey_AcqDataCtrl + 8

    def CloseSaver(self):
        if(IPStudio.LogFileName != None):
            for key, value in self.scalarDataList.items():
                smsg = rs.IVModel_pb2.PModelMessage()
                smsg.msgID = IPStudio.TableKey_AcqDataCtrlPyScalar
                smsg.string_data.append(key)
                smsg.double_data.extend(value)
                self.__SaveMsg(smsg)

    def __GetMsg(self, id):
        msg = rs.IVGrpc_pb2.RPCMessage()
        msg.msgID = id
        msg.recever_name = self.recv_name_
        return msg

    def __SaveMsg(self, msg):
        if(IPStudio.LogFileName != None):
            with open(IPStudio.LogFileName, 'ab') as fp:
                size = msg.ByteSize()
                fp.write(IPStudio.__varintEncode(size))
                fp.write(msg.SerializeToString())

    def __SaveTensor(self, name, type, dtype, data, dim, n1 = 0, n2 = 0, n3 = 0, n4 = 0, meta_data = None):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_SaveTensor)
        msg.string_data.append(name)
        msg.int_data.append(type)
        msg.int_data.append(dtype)
        msg.int64_data.append(0)
        msg.int_data.append(dim)
        msg.int_data.append(n1)
        msg.int_data.append(n2)
        msg.int_data.append(n3)
        msg.int_data.append(n4)
        rs.data_service.PostMsgToClient(msg)
        if(IPStudio.LogFileName != None):
            smsg = rs.IVModel_pb2.PModelMessage()
            smsg.msgID = IPStudio.TableKey_AcqDataCtrlPyTensor
            smsg.string_data.append(name)
            smsg.int_data.append(type)
            smsg.int_data.append(dtype)
            if meta_data != None:
                smsg.int_data.append(len(meta_data))
                smsg.double_data.extend(meta_data)
            else:
                smsg.int_data.append(0)    
            smsg.int_data.append(dim)
            smsg.int_data.append(n1)
            if dim >= 2:
                smsg.int_data.append(n2)
            if dim >= 3:
                smsg.int_data.append(n3)
            if dim >= 4:
                smsg.int_data.append(n4)
            data = data.flatten()
            if dtype == IVDataType.IVData_Double:
                smsg.double_data.extend(data)
            elif dtype == IVDataType.IVData_Float:
                smsg.float_data.extend(data)
            elif dtype == IVDataType.IVData_Int32:
                smsg.int32_data.extend(data)
            elif dtype == IVDataType.IVData_Int16:
                smsg.int32_data.extend(data)
            elif dtype == IVDataType.IVData_Int8:
                smsg.byte_data.append(data)
            self.__SaveMsg(smsg)

    def SaveTensor4(self, name, type, data4):
        self.__SaveTensor(name, type, IVDataType.IVData_Double, data4, 4, data4.shape[0], data4.shape[1], data4.shape[2], data4.shape[3])

    def SaveTensor4_F(self, name, type, data4):
        self.__SaveTensor(name, type, IVDataType.IVData_Float, data4, 4, data4.shape[0], data4.shape[1], data4.shape[2], data4.shape[3])

    def SaveTensor4_I(self, name, type, data4):
        self.__SaveTensor(name, type, IVDataType.IVData_Int32, data4, 4, data4.shape[0], data4.shape[1], data4.shape[2], data4.shape[3])

    def SaveTensor4_S(self, name, type, data4):
        self.__SaveTensor(name, type, IVDataType.IVData_Int16, data4, 4, data4.shape[0], data4.shape[1], data4.shape[2], data4.shape[3])

    def SaveTensor4_C(self, name, type, data4):
        self.__SaveTensor(name, type, IVDataType.IVData_Int8, data4, 4, data4.shape[0], data4.shape[1], data4.shape[2], data4.shape[3])

    def SaveTensor3(self, name, type, data3):
        self.__SaveTensor(name, type, IVDataType.IVData_Double, data3, 3, data3.shape[0], data3.shape[1], data3.shape[2])

    def SaveTensor3_F(self, name, type, data3):
        self.__SaveTensor(name, type, IVDataType.IVData_Float, data3, 3, data3.shape[0], data3.shape[1], data3.shape[2])

    def SaveTensor3_I(self, name, type, data3):
        self.__SaveTensor(name, type, IVDataType.IVData_Int32, data3, 3, data3.shape[0], data3.shape[1], data3.shape[2])

    def SaveTensor3_S(self, name, type, data3):
        self.__SaveTensor(name, type, IVDataType.IVData_Int16, data3, 3, data3.shape[0], data4.shape[1], data3.shape[2])

    def SaveTensor3_C(self, name, type, data3):
        self.__SaveTensor(name, type, IVDataType.IVData_Int8, data3, 3, data3.shape[0], data3.shape[1], data3.shape[2])

    def SaveTensor2(self, name, type, data2):
        self.__SaveTensor(name, type, IVDataType.IVData_Double, data2, 2, data2.shape[0], data2.shape[1])

    def SaveTensor2_F(self, name, type, data2):
        self.__SaveTensor(name, type, IVDataType.IVData_Float, data2, 2, data2.shape[0], data2.shape[1])

    def SaveTensor2_I(self, name, type, data2):
        self.__SaveTensor(name, type, IVDataType.IVData_Int32, data2, 2, data2.shape[0], data2.shape[1])

    def SaveTensor2_S(self, name, type, data2):
        self.__SaveTensor(name, type, IVDataType.IVData_Int16, data2, 2, data2.shape[0], data2.shape[1])

    def SaveTensor2_C(self, name, type, data2):
        self.__SaveTensor(name, type, IVDataType.IVData_Int8, data2, 2, data2.shape[0], data2.shape[1])

    def SaveTensor1(self, name, type, data1):
        self.__SaveTensor(name, type, IVDataType.IVData_Double, data1, 1, data1.shape[0])

    def SaveTensor1_F(self, name, type, data1):
        self.__SaveTensor(name, type, IVDataType.IVData_Float, data1, 1, data1.shape[0])

    def SaveTensor1_I(self, name, type, data1):
        self.__SaveTensor(name, type, IVDataType.IVData_Int32, data1, 1, data1.shape[0])

    def SaveTensor1_S(self, name, type, data1):
        self.__SaveTensor(name, type, IVDataType.IVData_Int16, data1, 1, data1.shape[0])

    def SaveTensor1_C(self, name, type, data1):
        self.__SaveTensor(name, type, IVDataType.IVData_Int8, data1, 1, data1.shape[0])

    def SaveScalar(self, name, value):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_SaveScalar)
        msg.string_data.append(name)
        msg.double_data.append(value)
        rs.data_service.PostMsgToClient(msg)
        if name in self.scalarDataList:
            self.scalarDataList[name].append(value)
        else:
            self.scalarDataList[name] = [value]

    def SaveText(self, name, text):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_SaveText)
        msg.string_data.append(name)
        msg.string_data.append(text)
        rs.data_service.PostMsgToClient(msg)
        if(IPStudio.LogFileName != None):
            smsg = rs.IVModel_pb2.PModelMessage()
            smsg.msgID = IPStudio.TableKey_AcqDataCtrlPyText
            smsg.string_data.append(name)
            smsg.string_data.append(text)
            __SaveMsg(smsg)

    def __SaveWaveform(self, name, dtype, data, dim, n1, n2, samplerate):
        self.__SaveTensor(name, TensorType.Waveform, dtype, data, dim, n1, n2, 0, 0, [samplerate])

    def SaveWaveform2(self, name, data, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Double, data, 2, data.shape[0], data.shape[1], samplerate)

    def SaveWaveform2_F(self, name, data, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Float, data, 2, data.shape[0], data.shape[1], samplerate)

    def SaveWaveform2_I(self, name, data, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Int32, data, 2, data.shape[0], data.shape[1], samplerate)

    def SaveWaveform2_S(self, name, data, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Int16, data, 2, data.shape[0], data.shape[1], samplerate)

    def SaveWaveform2_C(self, name, data, DIM1, DIM2, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Int8, data, 2, data.shape[0], data.shape[1], samplerate)

    def SaveWaveform1(self, name, data, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Double, data, 1, data.shape[0], 0, samplerate)

    def SaveWaveform1_F(self, name, data, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Float, data, 1, data.shape[0], 0, samplerate)

    def SaveWaveform1_I(self, name, IN_ARRAY1, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Int32, data, 1, data.shape[0], 0, samplerate)

    def SaveWaveform1_S(self, name, IN_ARRAY1, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Int16, data, 1, data.shape[0], 0, samplerate)

    def SaveWaveform1_C(self, name, IN_ARRAY1, DIM1, samplerate):
        return __SaveWaveform(self, name, IVDataType.IVData_Int8, data, 1, data.shape[0], 0, samplerate)

    def StartSaveGraphDef(self, graphname):
        self.NewGraphDef = rs.PGraphDef()
        self.graphdef_name = graphname

    def CloseSaveGraphDef(self):
        if(self.NewGraphDef != None and self.graphdef_name != None):
            serialized = self.NewGraphDef.SerializeToString()
            filename, file_extension = os.path.splitext(IPStudio.LogFileName)
            filename = filename + "(" + self.graphdef_name + ").dvf"
            with open(filename, 'wb') as outfile:
                outfile.write(serialized)
            msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_SaveGraphDef)
            msg.byte_data.append(serialized)
            rs.data_service.PostMsgToClient(msg)

    def AddNodeGraphDef(self, nodename, opname):
        self.NewNode = self.NewGraphDef.node.add()
        self.NewNode.name = nodename
        self.NewNode.opname = opname

    def CloseNodeGraphDef(self):
        if(self.NewNode != None):
            self.NewNode = None

    def AddNodeInputGraphDef(self, inputname):
        if(self.NewNode != None):
            self.NewNode.input.append(inputname)

    def AddNodeAttrIntGraphDef(self, attrname, v):
        if(self.NewNode != None):
            self.NewNode.attr[attrname].i = v

    def AddNodeAttrStringGraphDef(self, attrname, v):
        if(self.NewNode != None):
            self.NewNode.attr[attrname].s = bytes(v, 'utf-8')

    def AddNodeAttrFloatGraphDef(self, attrname, v):
        if(self.NewNode != None):
            self.NewNode.attr[attrname].f = v

    def AddNodeAttrBoolGraphDef(self, attrname, v):
        if(self.NewNode != None):
             self.NewNode.attr[attrname].b = v

    def AddNodeAttrShapeGraphDef(self, attrname, shape):
        if(self.NewNode != None):
            ar = rs.PAttrValueDef()
            self.NewNode.attr[attrname].shape.dim = shape

    def LogOutput(self, type, name):
        if type == 0:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Log_Info)
        else:
            msg = self.__GetMsg(RPCMessageID.IPCMsg_Log_Error)
        msg.int_data.append(code)
        msg.string_data.append(name)
        rs.data_service.PostMsgToClient(msg)

    def GetKeyState(self, key):
        return 0

    def WriteVideo(self, filename, dataFormat, frame_rate, channel, width, height, data):
        import cv2
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        vd  = cv2.VideoWriter(filename, fourcc, frame_rate, (width, height))
        vd.write(data)

    def LoadVideo(self, filename, dataFormat, data):
        import cv2
        cap = cv2.VideoCapture(filename)
        ret, frame = cap.read()
        if(ret):
            return frame

    def WriteAudio(self, filename, data, rate):
        import pysndfile
        return pysndfile.sndio.write(filename, data, rate)

    def LoadAudio(self, filename, dtype):
        import pysndfile
        return pysndfile.sndio.read(filename, dtype)

    def GetAudioStream(self, duration):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_Acq_GetAudio)
        msg.double_data.append(duration)
        res = rs.data_service.GetResponse(msg, 4000)
        if (res != None):
            if(len(res.double_data) == 1 and len(res.int_data) >= 1):
                sample_rate = res.double_data[0]
                channel_count = res.int_data[0]
                return res.int_data[1:], sample_rate, channel_count

    def GetInputText(self, name):
        msg = self.__GetMsg(RPCMessageID.IPCMsg_PY_GetInputText)
        msg.string_data.append(name)
        return rs.data_service.GetString(msg)