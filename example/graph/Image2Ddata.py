from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
import time

#topgraph
graph = vi.IPGraph("Image-3")
graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(200,200,200)])
graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph.SetCaption("Image Graph")
palette = graph.SetPalette(0,1,True)

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("X")
xaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
#yaxis
yaxis = graph.Axes(1)
yaxis.SetTitle("Y")
yaxis.SetMaximum(200)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_ZoomX |vi.GraphMouseTrackingMode.TrackingMode_PanX, True )

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(0)
plot = graph.NewPlot("image")
plot.SetPlotStyle(vi.PlotStyle.XYImage)
plot.ImageRange(0, 1, 0, 1)
dataxy = np.empty(200*100)
for iy in range(200):
    for ix in range(100):
        dataxy[ix + iy * 100] = np.sin(ix / 10.0) * np.sin(iy / 10.0)
plot.ImageColor(dataxy, 100, 200)

#topgraph
graph2 = vi.IPGraph("Image-4")
graph2.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(200,200,200)])
graph2.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph2.SetCaption("Image Graph")
palette = graph2.SetPalette(0,1,True)

#xaxis
xaxis = graph2.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("X")
xaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
#yaxis
yaxis = graph2.Axes(1)
yaxis.SetTitle("Y")
yaxis.SetMaximum(200)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
graph2.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_ZoomX |vi.GraphMouseTrackingMode.TrackingMode_PanX, True )

plotnum = graph2.GetPlotCount()
for i in range(plotnum):
    graph2.RemovePlot(0)
plot = graph2.NewPlot("image")
plot.SetPlotStyle(vi.PlotStyle.XYImage)
plot.ImageRange(0, 1, 0, 1)
dataxy = np.empty(200*100)
i = 0
for iy in range(200):
    i = 0
    for ix in range(100):
        dataxy[ix + iy * 100] = np.sin(ix / 10.0) * np.sin(iy / 10.0)
    plot.ImageColor(dataxy, 100, 200)