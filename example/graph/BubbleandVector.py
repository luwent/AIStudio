from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
import time

def MakeCursor( graphname, name, xpos=50, ypos=5, color = vi.MakeColor(255,0,0), style = vi.CursorLineShape.CursorMajorXMajorY, snap = vi.GraphObjSnapModes.SnapFloating):
    graph = vi.IPGraph( graphname )
    cursor = graph.NewCursor(name)
    cursor.SetColor(color)
    cursor.SetCursorStyle(style)
    cursor.SetSnapMode(snap)
    cursor.SetCursorPos(xpos,ypos)
    cursor.ModifyOption(vi.CursorOptions.CursorShowLabel, True)
    return cursor

def CreateBubbleDemo():
    graph = vi.IPGraph("Image-5")
    graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(200,200,200)])
    graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])

    #palette
    palette = graph.SetPalette(0,1,True)
    
    #xaxis
    xaxis = graph.Axes(0)
    xaxis.SetMinimum(0)
    xaxis.SetMaximum(1)
    xaxis.SetTitle("X")
    xaxis.ModifyOption(vi.AxisOptions.MajorGrid, False)
    #yaxis
    yaxis = graph.Axes(1)
    yaxis.SetMinimum(0)
    yaxis.SetMaximum(1)
    yaxis.SetTitle("Y")
    graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_ZoomX |vi.GraphMouseTrackingMode.TrackingMode_PanX, True )
    
    #bubble plot
    plotnum = graph.GetPlotCount()
    for i in range(plotnum):
        graph.RemovePlot(0)
    bubble1 = graph.NewPlot("bubble1")
    bubble1.SetPlotStyle(vi.PlotStyle.XYBubble)
    bubble1.SetBubblePara(20)

    #cursor
    cursorcount = graph.GetCursorCount()
    if cursorcount < 1:
        cursor = MakeCursor("Image-5", "cursor", 0.5, 0.5)
    else:
        graph.RemoveCursor("cursor")
        cursor = MakeCursor("Image-5", "cursor", 0.5, 0.5)

def CreateVectorDemo():
    graph = vi.IPGraph("Image-6")
    graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(200,200,200)])
    graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])
    
    #xaxis
    xaxis = graph.Axes(0)
    xaxis.SetMinimum(-10)
    xaxis.SetMaximum(10)
    xaxis.SetTitle("X")
    xaxis.ModifyOption(vi.AxisOptions.MajorGrid, False)
    #yaxis
    yaxis = graph.Axes(1)
    yaxis.SetMinimum(-10)
    yaxis.SetMaximum(10)
    yaxis.SetTitle("Y")
    graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_ZoomX |vi.GraphMouseTrackingMode.TrackingMode_PanX, True )
    
    #vector plot
    plotnum = graph.GetPlotCount()
    for i in range(plotnum):
        graph.RemovePlot(0)
    vector1 = graph.NewPlot("vect1")
    vector1.SetPlotStyle(vi.PlotStyle.XYVector)
    

CreateBubbleDemo()
CreateVectorDemo()

def BubbleVectorAnimation( bool1, bool2, bubblename, vectorname ) :
    if ( bool1 and timercount % 5 == 0 ):
        bgraph = vi.IPGraph( bubblename )
        bubble = bgraph.Plots(0)
        data1 = [random.uniform(0,1) for i in range(100)] 
        data2 = [random.uniform(0,1) for i in range(100)]
        data3 = [random.uniform(0,1) for i in range(100)]
        bubble.BubbleXY(data1, data2, data3)
    if( bool2 and timercount % 15 == 0 ):
        vgraph = vi.IPGraph( vectorname )
        vector = vgraph.Plots(0)
        vector.SetVectorPara(4, 40)
        data1 = [random.uniform(0,1) for i in range(200)] 
        data2 = [random.uniform(0,1) for i in range(200)]
        data3 = np.empty(200)
        data4 = np.empty(200)
        for i in range(200):
            data1[i] = data1[i] - 0.5
            data2[i] = data2[i] - 0.5
            data3[i] = np.arctan2( data2[i], data1[i] ) * 180 / np.pi
            data4[i] = np.sqrt( data1[i] * data1[i] + data2[i] * data2[i] ) * 2
            data1[i] = data1[i] * 20
            data2[i] = data2[i] * 20
        vector.VectorAL( data1, data2, data3, data4 )
    
timercount = 0
while True:
    BubbleVectorAnimation(True, True, "Image-5", "Image-6")
    timercount = timercount + 1


