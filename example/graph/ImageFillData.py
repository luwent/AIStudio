from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

#topgraph
graph = vi.IPGraph("Image-1")
graph.SetFrameColor(vi.PFillType.FillType_Solid, [vi.MakeColor(200,200,200)])
graph.SetPlotAreaColor(vi.PFillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph.SetCaption("Image Graph")
palette = graph.SetPalette(0,1,True)

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(60)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)
#yaxis
yaxis = graph.Axes(1)
yaxis.SetTitle("Amplitude")
yaxis.SetMaximum(10)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)
graph.SetMouseTrackingMode(vi.PGraphMouseTrackingMode.TrackingMode_ZoomX |vi.PGraphMouseTrackingMode.TrackingMode_PanX, True )
    

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(0)
plotA = graph.NewPlot("sin")
plotA.SetPlotStyle(vi.PPlotStyle.XYImage)
plotA.PlotXRange(0, 0.05*np.pi)
y = [1*np.sin(i*0.05*np.pi) for i in range(1000)]
plotA.SetDataOffset(0,1)
plotA.PlotY(y)

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(1)
plotB = graph.NewPlot("cos")
plotB.SetPlotStyle(vi.PPlotStyle.XYImage)
plotB.PlotXRange(0, 0.05*np.pi)
by = [1*np.cos(i*0.05*np.pi) for i in range(1000)]
plotB.SetDataOffset(0,3)
plotB.PlotY(by)

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(2)
plotC = graph.NewPlot("sawtooth")
plotC.SetPlotStyle(vi.PPlotStyle.XYImage)
plotC.PlotXRange(0, 1)
f = 100
fs = 10
x = np.arange(f)
xs = np.arange(fs)
j = 0
y = [4 for i in range(100)]
for i in xs:
    if i %2 == 0:
        while j < 10:
            y[i*10+j] =0.1*j
            j = j+1
        j=0
    else:
        while j < 10:
            y[i*10+j] =  -1+0.1*j
            j = j+1
    j = 0
plotC.SetDataOffset(0,5)
plotC.PlotY(y)

def SawtoothWave(df):
    dfs = 10
    dx = np.arange(df)
    dxs = np.arange(dfs)
    dj = 0
    dy = [6 for i in range(100)]
    for i in dxs:
        if i %2 == 0:
            while dj < 10:
                dy[i*10+dj] =(-0.1*dj)
                dj = dj+1
            dj=0
        else:
             while dj < 10:
                dy[i*10+dj] =  1+(-0.1*dj)
                dj = dj+1
        dj = 0
    return dy

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(3)
plotD = graph.NewPlot("back-sawtooth")
plotD.SetPlotStyle(vi.PPlotStyle.XYImage)
plotD.PlotXRange(0, 1)
df = 100
dfs = 10
dx = np.arange(df)
dxs = np.arange(dfs)
dj = 0
dy = [6 for i in range(100)]
for i in dxs:
    if i %2 == 0:
        while dj < 10:
            dy[i*10+dj] =(-0.1*dj)
            dj = dj+1
        dj=0
    else:
        while dj < 10:
            dy[i*10+dj] =  1+(-0.1*dj)
            dj = dj+1
    dj = 0
plotD.SetDataOffset(0,7)
plotD.PlotY(SawtoothWave(100))

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(4)
plotE = graph.NewPlot("sqaure")
plotE.PlotXRange(0, 1)
plotE.SetPlotStyle(vi.PPlotStyle.XYImage)
fs = 100 # sample rate 
fss = 10
xx = np.arange(fss)
x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
j =0
ey = [-1 for i in x]
for i in xx:
    if i % 2 == 0:
        while j < 10:
            ey[i*10+j] = 1
            j = j+1
    j = 0
plotE.SetDataOffset(0,9)
plotE.PlotY(ey)


graph2 = vi.IPGraph("Image-2")
graph2.SetFrameColor(vi.PFillType.FillType_Solid, [vi.MakeColor(200,200,200)])
graph2.SetPlotAreaColor(vi.PFillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph2.SetCaption("Image2 chart")
palette = graph2.SetPalette(-5,5,True)

#xaxis
xaxis = graph2.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(60)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)
#yaxis
yaxis = graph2.Axes(1)
yaxis.SetTitle("Amplitude")
yaxis.SetMaximum(10)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)
graph2.SetMouseTrackingMode(vi.PGraphMouseTrackingMode.TrackingMode_ZoomX |vi.PGraphMouseTrackingMode.TrackingMode_PanX, True )


plotnum = graph2.GetPlotCount()
for i in range(plotnum):
    graph2.RemovePlot(0)
chart = graph2.NewPlot("sin")
chart.SetPlotStyle(vi.PPlotStyle.XYImage)
chart.ChartXRange(0, 0.1*np.pi,1000)
chart.SetDataOffset(0,5)
while(j < 10000):
    y = [ 4*np.sin(0.1*j*0.1*np.pi)] 
    chart.ChartY(y)
    j = j +1