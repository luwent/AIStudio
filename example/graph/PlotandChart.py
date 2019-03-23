from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

#top graph
graph = vi.IPGraph("Chart-1")
graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(223, 218, 241)])
graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph.SetCaption("Chart Graph Example")

#bottom graph
graph2 = vi.IPGraph("Plot-2")
graph2.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(223, 218, 241)])
graph2.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph2.SetCaption("Random Plot Graph Example")

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(-10)
yaxis.SetMaximum(10)
yaxis.SetTitle("Distance")

plotnum = graph.GetPlotCount()
if plotnum < 1:
   chart = graph.NewPlot("Chart1")
else:
   chart = graph.Plots(0)
chart.ChartXRange(0, 0.1*np.pi, 400, True, 50)
chart.SetLineWidth(2)
chart.SetLineColor(vi.MakeColor(0, 0, 255))
chart.SetLineStyle(vi.LineType.LineType_Dot)

plotnum = graph2.GetPlotCount()
if plotnum < 1:
    plot = graph2.NewPlot("RandPlot")
else:
    plot = graph2.Plots(0)
plot.PlotXRange(0, 0.1*np.pi)
plot.SetLineColor(vi.MakeColor(0, 0, 255))
j = 0

while(j < 10000):
    ychart = [4 * np.sin(j * 0.1 * np.pi)] 
    chart.ChartY(ychart)
    yplot = [4 * np.sin(i * 0.1 *np.pi) + random.uniform(0, 1) for i in range(1000)] 
    plot.PlotY(yplot)  
    j = j +0.5
    