from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np

graph2 = vi.IPGraph("Plot-2")
graph2.SetFrameColor(vi.PFillType.FillType_Solid, [0xFFFF0000])
graph2.SetPlotAreaColor(vi.PFillType.FillType_Solid, [0xFF00FF00])
graph2.SetCaption("Chart Graph Example")
#xaxis
#xaxis = graph2.Axes(0)
#xaxis.SetMaximum(100)
#xaxis.SetTitle("Time")
#yaxis
#yaxis = graph2.Axes(1)
#yaxis.SetTitle("Distance")
#yaxis.SetMaximum(10)
#yaxis.SetMinimum(-10)

#plot1
#chart1 = graph2.NewPlot("firstplot")
#chart1.ChartXRange(0, 1)
#sinwave
#fs = 100 # sample rate 
#f = 10 # the frequency of the signal
#x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
#y = [ 8*np.sin(2*np.pi*f * (i/fs)) for i in x] 
#chart1.ChartY(y)