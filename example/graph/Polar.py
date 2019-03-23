from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

def CreatePolarDemo():
    graph = vi.IPGraph( "Image-7" )
    graph.SetGraphCategory( vi.GraphCategory.Polar, vi.PlotStyle.PolarImage )
    
    #palette
    palette = graph.SetPalette(0, 1, True)
    
    #axis
    xaxis = graph.Axes(0)
    yaxis = graph.Axes(1)
    yaxis.SetMinimum(0)
    yaxis.SetMaximum(200)
    xaxis.ModifyOption( vi.AxisOptions.MajorGrid, True )
    yaxis.ModifyOption( vi.AxisOptions.MajorGrid, True )
    xaxis.SetMajorGridColor( vi.MakeColor(0, 0, 255) )
    yaxis.SetMajorGridColor( vi.MakeColor(0, 0, 255) )
    
    plotnum = graph.GetPlotCount()
    for i in range( plotnum ):
        graph.RemovePlot(0)
    pImg = graph.NewPlot( "PolarImage" ) 
    pImg.SetPlotStyle( vi.PlotStyle.PolarImage )
    pImg.ImageRange(0, 1, 0, 1)
    dataxy = np.empty(200 * 360)
    for iy in range(200):
        for ix in range(360):
            dataxy[ix + iy * 360] = np.sin(ix * 2* np.pi / 90.0) * np.sin(iy / 10.0) * abs(np.cos(ix * 2* np.pi / 360.0))
    pImg.ImageColor(dataxy, 360, 200)
    for ix in range(360):
        dataxy[ix] = 150 * np.sin(ix * 2 * np.pi / 90.0) * abs(np.cos(ix * 2 * np.pi / 360.0))
    
    plotnum = graph.GetPlotCount()
    for i in range( plotnum ):
        graph.RemovePlot(1)
    plot = graph.NewPlot( "PolarCurve" ) 
    plot.SetPlotStyle( vi.PlotStyle.PolarCurve )    
    plot.PlotY( dataxy )
    plot.PlotXRange(0, 1)    
    plot.SetLineColor( vi.MakeColor(0, 255, 0) )
    plot.SetLineWidth(2)
    dataxy = []

def CreatePolarDemo2():
    graph = vi.IPGraph( "Image-8" )
    graph.SetPlotAreaColor( vi.FillType.FillType_Solid, [vi.MakeColor(197, 251, 196)] )
    graph.SetGraphCategory( vi.GraphCategory.Polar, vi.PlotStyle.PolarImage ) 
    
    palette = graph.SetPalette(0, 1, False)    
    
    #axis
    xaxis = graph.Axes(0)
    yaxis = graph.Axes(1)
    yaxis.SetMinimum(0)
    yaxis.SetMaximum(200)
    xaxis.ModifyOption( vi.AxisOptions.MajorGrid, True )
    xaxis.SetMajorGridColor( vi.MakeColor(0, 0, 255) ) 
    xaxis.ModifyOption( vi.AxisOptions.ShowTitle, False )
    yaxis.SetMajorGridColor( vi.MakeColor(0, 0, 255) ) 
    yaxis.ModifyOption( (vi.AxisOptions.ShowTitle | vi.AxisOptions.ShowTick | vi.AxisOptions.TickLabel | vi.AxisOptions.AxisLine), False )
    
    axisnum = graph.GetAxisCount()
    if axisnum < 3:
        axisrad = graph.NewAxis( "Radius", vi.AxisType.AxisRadius )
    else:
        axisrad = graph.Axes(2)
    axisrad.SetTickPadding( vi.AxisOptions.FixPadding )
    axisrad.AddValuePair( "E", 0, vi.MakeColor(0, 0, 255) )
    axisrad.AddValuePair( "N", 90, vi.MakeColor(0, 0, 255) )
    axisrad.AddValuePair( "W", 180, vi.MakeColor(0, 0, 255) )
    axisrad.AddValuePair( "S", 270, vi.MakeColor(0, 0, 255) )
    axisrad.ModifyOption( vi.AxisOptions.ValuePairOnly, True )
    
    plotnum = graph.GetPlotCount()
    for i in range( plotnum ):
        graph.RemovePlot(0)
    plot = graph.NewPlot( "PolarCurve" ) 
    plot.SetPlotStyle( vi.PlotStyle.PolarCurve )
    plot.ChartXRange(0, 1, 360)

CreatePolarDemo()    
CreatePolarDemo2()

polarindex = 0
def CreatePolar2Demo( name ):
    global polarindex
    graph = vi.IPGraph( name )
    plot = graph.Plots(0)
    d = 150 * np.sin(polarindex * 2 * np.pi / 90.0) * abs(np.cos(polarindex * 2 * np.pi / 360.0))
    polarindex = polarindex + 1
    plot.ChartY([d])
    plot.SetLineColor( vi.MakeColor(255, 0, 0) )
    plot.SetLineWidth(2)
    if(polarindex > 720):
        polarindex = 0
        plot = graph.NewPlot( "PolarCurve" ) 
        plot.ChartXRange(0, 1, 360)

while True:
    CreatePolar2Demo("Image-8")


