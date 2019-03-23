from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

#topgraph
graph = vi.IPGraph("Plot-3")
graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 235, 164)])
graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph.SetCaption("Multiple-Plot Graphs")

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(0)
yaxis.SetMaximum(10)
yaxis.SetTitle("Amplitude")
yaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
#y axis on the other side
axisnum = graph.GetAxisCount()
if axisnum < 3:
    y2axis = graph.NewAxis("Type",1)
else:
    y2axis = graph.Axes(2)
y2axis.SetMinimum(0)
y2axis.SetMaximum(10)
y2axis.SetTitle("Type")
y2axis.ModifyOption(0x1 << 24, True)
y2axis.ModifyOption(0x1 << 6 | 0x1 << 7, False)

#add a value pair for sin graph
y2axis.AddValuePair("Sin", 1, vi.MakeColor(0,0,0))
y2axis.ModifyValuePairOption(vi.ValuePairOption.VPGridLine, True)
plotnum = graph.GetPlotCount()
if plotnum < 1:
    plotA = graph.NewPlot("Sin")
else:
    plotA = graph.Plots(0)
plotA.PlotXRange(0, 1)
fs = 100 # sample rate 
f = 10 # the frequency of the signal
x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [1 * np.sin(2 * np.pi * f  * (i/fs)) for i in x] 
plotA.SetLineWidth(2)
plotA.SetLineColor(vi.MakeColor(0, 0, 255))
plotA.SetDataOffset(0, 1)
plotA.PlotY(y)

#add a value pair for Cos graph
y2axis.AddValuePair("cos", 3, vi.MakeColor(0, 0, 0))
y2axis.ModifyValuePairOption(vi.ValuePairOption.VPGridLine, True)
plotnum = graph.GetPlotCount()
if plotnum < 2:
    plotB = graph.NewPlot("Cos")
else:
    plotB = graph.Plots(1)
plotB.PlotXRange(0, 1)
by = [1 * np.cos(2 * np.pi * f * (i/fs)) for i in x] 
plotB.SetDataOffset(0, 3)
plotB.SetLineWidth(2)
plotB.SetLineColor(vi.MakeColor(0, 0, 255))
plotB.PlotY(by)

#add a value pair for tan graph
y2axis.AddValuePair("tan", 5, vi.MakeColor(0, 0, 0))
y2axis.ModifyValuePairOption(vi.ValuePairOption.VPGridLine, True)
plotnum = graph.GetPlotCount()
if plotnum < 3:
    plotC = graph.NewPlot("Tan")
else:
    plotC = graph.Plots(2)
plotC.PlotXRange(0, 1)
cy = [0.25 * np.tan(2 * np.pi * f * (i/fs)) for i in x] 
plotC.SetDataOffset(0, 5) 
plotC.SetLineWidth(2)
plotC.SetLineColor(vi.MakeColor(0, 0, 255))
plotC.PlotY(cy)

#~ #add a value pair for sq graph
y2axis.AddValuePair("square", 7, vi.MakeColor(0, 0, 0))
y2axis.ModifyValuePairOption(vi.ValuePairOption.VPGridLine, True)
plotnum = graph.GetPlotCount()
if plotnum < 4:
    plotD = graph.NewPlot("Square")
else:
    plotD = graph.Plots(3)
plotD.PlotXRange(0, 1)
fss = 10
xx = np.arange(fss)
j =0
dy = [8 for i in x]
for i in xx:
    if i % 2 == 0:
        while j < 10:
            dy[i * 10 + j] = 6
            j = j + 1
    j = 0
plotD.SetLineWidth(2)
plotD.SetLineColor(vi.MakeColor(0, 0, 255))
plotD.PlotY(dy)

#add a value pair for cos tan graph
y2axis.AddValuePair("cos tan", 9, vi.MakeColor(0, 0, 0))
y2axis.ModifyValuePairOption(vi.ValuePairOption.VPGridLine, True)
plotnum = graph.GetPlotCount()
if plotnum < 5:
    plotE = graph.NewPlot("Cos-Tan")
else:
    plotE = graph.Plots(4)
plotE.PlotXRange(0, 1)
ey = [np.cos(np.tan(2 * np.pi * f * (i/fs))) for i in x] 
plotE.SetDataOffset(0, 9)
plotE.SetLineWidth(2)
plotE.SetLineColor(vi.MakeColor(0, 0, 255))
plotE.PlotY(ey)

#bottom graph
graph2 = vi.IPGraph("Plot-4")
graph2.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 235, 164)])
graph2.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph2.SetCaption("Multiple-Axis Graph")

#xaxis
xaxis = graph2.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.AxisOptions.AutoScale, False)
#yaxis
yaxis = graph2.Axes(1)
yaxis.SetTitle("Amplitude")
yaxis.SetMaximum(10)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.AxisOptions.AutoScale, False)

#x2 axis
axisnum2 = graph2.GetAxisCount()
if axisnum2 < 3:
    x2axis = graph2.NewAxis("Distance",vi.AxisType.AxisX)
else:
    x2axis = graph2.Axes(2)
x2axis.SetMinimum(0)
x2axis.SetMaximum(100)
x2axis.SetTitle("Distance")
x2axis.ModifyOption(vi.AxisOptions.AutoScale, False)
#y2axis
if axisnum2 < 4:
    y2axis = graph2.NewAxis("Log",vi.AxisType.AxisY)
else:
    y2axis = graph2.Axes(3)
y2axis.SetMinimum(0)
y2axis.SetMaximum(100)
y2axis.SetTitle("Log")
y2axis.ModifyOption(vi.AxisOptions.AutoScale, False)
y2axis.ModifyOption(vi.AxisOptions.LogScale,True)

plotnum = graph2.GetPlotCount()
if plotnum < 1:
    plot = graph2.NewPlot("RandPlot")
else:
    plot = graph2.Plots(0)
plot.PlotXRange(0, 0.1*np.pi)
plot.SetLineColor(vi.MakeColor(0,0,255))
j = 0
while(j < 10000):
    y = [5 + 2 * np.sin(i * 0.1 * np.pi) + random.uniform(0, 1) for i in range(1000)] 
    plot.PlotY(y)  
    j = j +0.5
