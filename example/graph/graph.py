from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np

graph1 = vi.IPGraph("Plot-1")
graph1.SetFrameColor(vi.PFillType.FillType_Solid, [0xFFFF0000])
graph1.SetPlotAreaColor(vi.PFillType.FillType_Solid, [0xFFFFFF00])
graph1.SetCaption("Example Graph")
xaxis = graph1.Axes(0)
xaxis.SetTitle("time")
yaxis = graph1.Axes(1)
yaxis.SetTitle("distance")
plot1 = graph1.NewPlot("firstplot")
plot1.PlotXRange(0, 0.1)
plot1.PlotY([1, 2, 3, 5, 10])
xaxis.SetMaximum(0.5)
