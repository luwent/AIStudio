from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

#topgraph
graph = vi.IPGraph("Bar-1")
graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(200,200,200)])
graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph.SetCaption("Temperature vs. Month")

#legend
legend = graph.GetLegend()
legend.SetVisible(True)

legend.SetLocationSide( vi.LocationSide.Location_Bottom)

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0.5)
xaxis.SetMaximum(12.5)
xaxis.SetTitle("Month")
xaxis.ModifyOption(vi.AxisOptions.MajorGrid, False)
#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(-10)
yaxis.SetMaximum(30)
yaxis.SetTitle("Temperature (Degrees)")
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_ZoomX |vi.GraphMouseTrackingMode.TrackingMode_PanX, True )

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(0)
bar1 = graph.NewPlot("New York")
bar1.SetPlotStyle(vi.PlotStyle.BarVBar)
label1 = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
data1 = [ -2, 0, 5, 10, 15, 20, 25, 22, 15, 5, 0, -1]
bar1.Bar(label1, data1)
bar1.BarColor(vi.FillType.FillType_Solid, vi.MakeColor(255,0,0) , 1, vi.MakeColor(255,0,0))
bar1.SetBarPara(70, -1, 6)

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(1)
bar2 = graph.NewPlot("Los Angeles")
bar2.SetPlotStyle(vi.PlotStyle.BarVBar)
data2 = [ 14, 15, 15.5, 16.5, 18.4, 21, 25, 22, 21, 20, 17, 15 ]
bar2.Bar(label1, data2)
bar2.BarColor(vi.FillType.FillType_Solid, vi.MakeColor(0,255,0) , 1, vi.MakeColor(0,255,0))
bar2.SetBarPara(70, -1, 6)

plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(2)
bar3 = graph.NewPlot("Columbus")
bar3.SetPlotStyle(vi.PlotStyle.BarVBar)
data3 = [ -4, -2, 5.5, 11.5, 16.4, 22, 23, 20, 12, 4, 2, -2 ]
bar3.Bar(label1, data3)
bar3.BarColor(vi.FillType.FillType_Solid, vi.MakeColor(0,0,255) , 1, vi.MakeColor(0,0,255))
bar3.SetBarPara(70, -1, 6)

#Bottom Graph
graph2 = vi.IPGraph("Bar-2")
graph2.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(200,200,200)])
graph2.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph2.SetGraphCategory(vi.GraphCategory.Bar3D, vi.PlotStyle.BarVBar)
graph2.SetCaption("Temperature vs. Month")

#legend
legend = graph2.GetLegend()
legend.SetVisible(True)


#xaxis
xaxis = graph2.Axes(0)
xaxis.SetMinimum(0.5)
xaxis.SetMaximum(12.5)
xaxis.SetTitle("Month")
xaxis.ModifyOption(vi.AxisOptions.MajorGrid, False)
#yaxis
yaxis = graph2.Axes(1)
yaxis.SetMinimum(-10)
yaxis.SetMaximum(30)
yaxis.SetTitle("Temperature (Degrees)")
graph2.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_ZoomX |vi.GraphMouseTrackingMode.TrackingMode_PanX, True )

plotnum = graph2.GetPlotCount()
for i in range(plotnum):
    graph2.RemovePlot(0)
bar1 = graph2.NewPlot("New York")
bar1.SetPlotStyle(vi.PlotStyle.BarVBar)
label1 = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
data1 = [ -2, 0, 5, 10, 15, 20, 25, 22, 15, 5, 0, -1]
bar1.Bar(label1, data1)
bar1.BarColor(vi.FillType.FillType_Solid, vi.MakeColor(255,0,0) , 1, vi.MakeColor(255,0,0))
bar1.SetBarPara(70, -1, 6)

plotnum = graph2.GetPlotCount()
for i in range(plotnum):
    graph2.RemovePlot(1)
bar2 = graph2.NewPlot("Los Angeles")
bar2.SetPlotStyle(vi.PlotStyle.BarVBar)
data2 = [ 14, 15, 15.5, 16.5, 18.4, 21, 25, 22, 21, 20, 17, 15 ]
bar2.Bar(label1, data2)
bar2.BarColor(vi.FillType.FillType_Solid, vi.MakeColor(0,255,0) , 1, vi.MakeColor(0,255,0))
bar2.SetBarPara(70, -1, 6)

plotnum = graph2.GetPlotCount()
for i in range(plotnum):
    graph2.RemovePlot(2)
bar3 = graph2.NewPlot("Columbus")
bar3.SetPlotStyle(vi.PlotStyle.BarVBar)
data3 = [ -4, -2, 5.5, 11.5, 16.4, 22, 23, 20, 12, 4, 2, -2 ]
bar3.Bar(label1, data3)
bar3.BarColor(vi.FillType.FillType_Solid, vi.MakeColor(0,0,255) , 1, vi.MakeColor(0,0,255))
bar3.SetBarPara(70, -1, 6)
