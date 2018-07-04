from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np

graph1 = vi.IPGraph("Plot-1")
graph1.SetFrameColor(vi.PFillType.FillType_Solid, [0xFFFF0000])
graph1.SetPlotAreaColor(vi.PFillType.FillType_Solid, [0xFF00FF00])
graph1.SetCaption("Simple Plot-Graph Example")
#xaxis
xaxis = graph1.Axes(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
#yaxis
yaxis = graph1.Axes(1)
yaxis.SetTitle("Distance")
yaxis.SetMaximum(10)
yaxis.SetMinimum(-10)

#plot1
plotnum = graph1.GetPlotCount()
if plotnum < 1:
    plot1 = graph1.NewPlot("firstplot")
else:
    plot1 = graph1.Plots(0)
plot1.PlotXRange(0, 1)
#sinwave
fs = 100 # sample rate 
f = 10 # the frequency of the signal
x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [ 8*np.sin(2*np.pi*f * (i/fs)) for i in x] 
plot1.PlotY(y)
plot1.SetLineWidth(2)
plot1.SetLineColor(0xFFFFFF00)

#plot2
if plotnum < 2:
    plot2 = graph1.NewPlot("secondplot")
else:
    plot2 = graph1.Plots(1)
plot2.PlotXRange(0, 1)
#sinwave
fs = 100 # sample rate 
f =  5# the frequency of the signal
x2 = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y2= [ 2*np.sin(2*np.pi*f * (i/fs)) for i in x2] 
plot2.PlotY(y2)
plot2.SetLineWidth(1)

#plot3
if plotnum < 3:
    plot3 = graph1.NewPlot("thirdplot")
else:
    plot3 = graph1.Plots(2)
plot3.PlotXRange(0, 1)
#sinwave
fs = 100 # sample rate 
f =  1# the frequency of the signal
x3 = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y3= [ 4*np.sin(2*np.pi*f * (i/fs)) for i in x3] 
plot3.PlotY(y3)
plot3.SetLineWidth(1)



