from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np

graph = vi.IPGraph("Plot-1")
graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(190, 223, 208)])
graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255,255,255)])
graph.SetCaption("Simple Plot-Graph Example")

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.AxisOptions.AutoScale, False)

#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(-10)
yaxis.SetMaximum(10)
yaxis.SetTitle("Distance")
yaxis.ModifyOption(vi.AxisOptions.AutoScale, False)

#plot1
plotnum = graph.GetPlotCount()
if plotnum < 1:
    plot1 = graph.NewPlot("Plot1")
else:
    plot1 = graph.Plots(0)
plot1.PlotXRange(0, 1)
fs = 100 # sample rate 
f = 10 # the frequency of the signal
x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [8 * np.sin( 2 * np.pi * f * (i/fs) ) for i in x] 
plot1.SetLineStyle(vi.LineType.LineType_Solid)
plot1.SetLineWidth(2)
plot1.SetLineColor(vi.MakeColor(255, 0, 0))
plot1.PlotY(y)

#plot2
if plotnum < 2:
    plot2 = graph.NewPlot("Plot2")
else:
    plot2 = graph.Plots(1)
plot2.PlotXRange(0, 1)
fs = 100 # sample rate 
f =  5# the frequency of the signal
x2 = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y2= [2 * np.sin( 2 * np.pi * f * (i/fs) ) for i in x2] 
plot2.SetLineStyle(vi.LineType.LineType_Dot)
plot2.SetLineWidth(2)
plot2.SetLineColor(vi.MakeColor(0, 255, 0))
plot2.PlotY(y2)

#plot3
if plotnum < 3:
    plot3 = graph.NewPlot("Plot3")
else:
    plot3 = graph.Plots(2)
plot3.PlotXRange(0, 1)
fs = 100 # sample rate 
f =  1# the frequency of the signal
x3 = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y3= [ 4 * np.sin( 2 * np.pi * f * (i/fs) ) for i in x3] 
plot3.SetLineStyle(vi.LineType.LineType_Dash)
plot3.SetLineWidth(2)
plot3.SetLineColor(vi.MakeColor(0, 0, 255))
plot3.PlotY(y3)


