from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

def PlotGraphDemo():
    #top graph
    graph = vi.IPGraph("Graph3D-2")
    graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(223, 218, 241)])
    graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
    graph.SetCaption("Chart Graph Example")
    graph.SetMouseTrackingMode( vi.GraphMouseTrackingMode.TrackingMode_Rotation, True)
    graph.SetOrientation(-422.2, 0, -347.7)
    
    #xaxis
    xaxis = graph.Axes(0)
    xaxis.SetMinimum(0)
    xaxis.SetMaximum(200)
    xaxis.SetTitle("Time")
    xaxis.ModifyOption( vi.AxisOptions.Reversed, True )
    
    #yaxis
    yaxis = graph.Axes(1)
    yaxis.SetMinimum(-1)
    yaxis.SetMaximum(1)
    yaxis.SetTitle("Distance")
    yaxis.ModifyOption( vi.AxisOptions.Reversed | vi.AxisOptions.AutoScroll, True )
    
    #zaxis
    axiscount = graph.GetAxisCount()
    zaxis = graph.Axes(2)
    zaxis.SetMaximum(1)
    zaxis.SetMinimum(-1)
    zaxis.SetTitle("Z-Axis")
    
    plotnum = graph.GetPlotCount()
    if plotnum < 1:
        plot = graph.NewPlot( "E" )
    else:
        plot = graph.Plots(0)
    plot.SetPlotStyle( vi.PlotStyle.XYZCurve )
    plot.SetLineWidth(2)
    plot.SetLineColor( vi.MakeColor(255, 0, 0) )
    plot.SetName("E")

    if plotnum < 2:
        plot2 = graph.NewPlot( "H" )
    else:
        plot2 = graph.Plots(1)
    plot2.SetPlotStyle( vi.PlotStyle.XYZCurve )
    plot2.SetLineWidth(2)
    plot2.SetLineColor( vi.MakeColor(0, 255, 0) )
    plot2.SetName("H")

    if plotnum < 3:
        plot3 = graph.NewPlot( "A" )
    else:
        plot3 = graph.Plots(2)
    plot3.SetPlotStyle( vi.PlotStyle.XYZCurve )
    plot3.SetLineWidth(1)
    plot3.SetLineColor( vi.MakeColor(0, 0, 255, 155) )
    plot3.SetName("A")

    cursor = graph.NewCursor("1");
    cursor.SetCursorPos3D(0, 50, 0);
    
    legend = graph.GetLegend()
    legend.SetVisible( True )

def ChartGraph2Demo():
    #~ #bottom graph
    graph = vi.IPGraph("Graph3D-3")
    graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(223, 218, 241)])
    graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
    graph.SetCaption("Chart Graph 2 Example")
    graph.SetMouseTrackingMode( vi.GraphMouseTrackingMode.TrackingMode_Rotation, True)
    graph.SetOrientation(-422.2, 0, -347.7)
    
    legend = graph.GetLegend()
    legend.SetVisible( True )
    
    #xaxis
    xaxis = graph.Axes(0)
    xaxis.SetMinimum(0)
    xaxis.SetMaximum(100)
    xaxis.SetTitle("Time")
    
    #yaxis
    yaxis = graph.Axes(1)
    yaxis.SetMinimum(-1)
    yaxis.SetMaximum(1)
    yaxis.SetTitle("Distance")
    yaxis.ModifyOption( vi.AxisOptions.AutoScroll, True )
    
    #zaxis
    axiscount = graph.GetAxisCount()
    zaxis = graph.Axes(2)
    zaxis.SetMinimum(-1)
    zaxis.SetMaximum(1)
    zaxis.SetTitle("Z-Axis")
    
    plotnum = graph.GetPlotCount()
    if plotnum < 1:
        plot = graph.NewPlot( "E" )
    else:
        plot = graph.Plots(0)
    plot.SetPlotStyle( vi.PlotStyle.XYZCurve )
    plot.SetLineWidth(2)
    plot.SetLineColor( vi.MakeColor(255, 0, 0) )
    plot.ChartXRange( 0, 1, 200, True, 50 )
    plot.SetName("E")

    if plotnum < 2:
        plot2 = graph.NewPlot( "H" )
    else:
        plot2 = graph.Plots(1)
    plot2.SetPlotStyle( vi.PlotStyle.XYZCurve )
    plot2.SetLineWidth(2)
    plot2.SetLineColor( vi.MakeColor(0, 255, 0) )
    plot2.ChartXRange( 0, 1, 200, True, 50 )
    plot2.SetName("H")

    if plotnum < 3:
        plot3 = graph.NewPlot( "A" )
    else:
        plot3 = graph.Plots(2)
    plot3.SetPlotStyle( vi.PlotStyle.XYZCurve )
    plot3.SetLineWidth(1)
    plot3.SetLineColor( vi.MakeColor(0, 0, 255, 155) )
    plot3.SetLineStyle( vi.LineType.LineType_Dot )
    plot3.ChartXYZRange( 2000, True, False, False, 50 )
    plot3.SetName("A")

    cursor = graph.NewCursor("1")
    cursor.SetCursorPos3D(0, 50, 0)
    

PlotGraphDemo()
ChartGraph2Demo()

timercount = 0
datay1 = np.empty(200)
datay = np.empty(4000)
dataz = np.empty(4000)
datay2 = np.empty(20)
dataz2 = np.empty(20)
datax2 = np.empty(20)
phase = 0
phase2 = 0
freq = 0.02
chartNum = 0

def PlotChartAnimation( bool1, chartname1, bool2, chartname2, chartDir ):
    global phase
    global phase2    
    global chartNum
    
    if( bool1 == True ):
        graph = vi.IPGraph( chartname1 )
        #make sine graph
        i = 0
        x = phase * np.pi / 180
        dx = 2 * np.pi * freq
        while i < 200:
            datay1[i] = np.sin(x)
            x = x + dx
            i = i + 1
        x = phase + freq * 360 * i
        phase = x - (x / 360) * 360
        plot = graph.Plots(0)
        plot.PlotXRange( 0, 1 )
        plot.PlotZRange( 0.0, 0.0 )
        plot.PlotY( datay1 )
        plot1 = graph.Plots(1)
        plot1.PlotXRange( 0, 1 )
        plot1.PlotYRange( 0.0, 0.0 )
        plot1.PlotZ( datay1 )
        plot2 = graph.Plots(2)
        for j in range(4000):
            datay[j] = np.fabs(datay1[( int(j / 20) )]) * np.sin( j * np.pi / 10 )
            dataz[j] = np.fabs(datay1[( int(j / 20) )]) * np.cos( j * np.pi / 10 )
        plot2.PlotXRange( 0, 1 / 20.0 )
        plot2.PlotY( datay )
        plot2.PlotZ( dataz )
      
    if( bool2 == True ):
        graph = vi.IPGraph( chartname2 )
        #make sine graph
        phase1 = phase2 + 2 * np.pi * freq
        phase2 = phase2 + 2 * np.pi * freq * 2
        y = [np.sin(phase1), np.sin(phase2)]
        plot = graph.Plots(0)
        plot1 = graph.Plots(1)
        plot2 = graph.Plots(2)
        plot.PlotZRange( 0.0, 0.0 )
        plot1.PlotYRange( 0.0, 0.0 )
        if( chartDir == 0 ):
            plot.ChartY(y)
            plot1.ChartZ( y )
        for j in range(20):
            datay2[j] = np.fabs(y[( int(j / 10) )]) * np.sin( j * np.pi / 10 )
            dataz2[j] = np.fabs(y[( int(j / 10) )]) * np.cos( j * np.pi / 10 )    
            datax2[j] = chartNum + 1 / 20.0
        plot2.ChartXYZ( datax2, datay2, dataz2 )
        
while True:
    PlotChartAnimation( True, "Graph3D-2", True, "Graph3D-3", 0 )
    timercount = timercount + 1
    phase = phase + np.pi / 2
    chartNum = chartNum + 2
        
        
        
    