from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
from threading import Timer
import time

graph = vi.IPGraph( "Cylinder3D-1" )
graph.SetGraphCategory(vi.GraphCategory.Cylindrical, vi.PlotStyle.XYZ4DVolumn)
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_Rotation, True);

palette = graph.GetPalette()
palette.SetTitle("AMP(Vol)", True)
palette.SetMaximumScale(1)
palette.SetMinimumScale(-1)

xaxis = graph.Axes(0)
xaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True)
xaxis.SetMajorGridColor(0xFF0000FF)
xaxis.SetMajorTickNumber(8)
xaxis.SetMinorTickNumber(5)

yaxis = graph.Axes(1)
yaxis.SetMajorGridColor(0xFF0000FF)
yaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True);
xaxis.SetMajorTickNumber(8)
xaxis.SetMinorTickNumber(5)

zaxis = graph.Axes(2)
zaxis.SetMaximum(10)
zaxis.SetMinimum(0)
zaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True);

lightcount = graph.GetLightCount()
if lightcount < 1:
    light = graph.NewLight("Light")
else:
    light = graph.Lights(0)
light.ModifyOption( vi.LightOptions.LightEnable, True )
light.SetColor( 0xFFFFFFFF, 0xFF3F3F3F, 0x000000000)
light.SetDirectionLight(1, 0.5, -1)

plotnum = graph.GetPlotCount()
for i in range( plotnum ):
    graph.RemovePlot( 0 )
cylinder = graph.NewPlot( "cylinder" )
cylinder.SetPlotStyle( vi.PlotStyle.Cylindrical3DImage )
filename = inspect.getframeinfo(inspect.currentframe()).filename
file_path  = os.path.dirname(os.path.abspath(filename))
cylinder.SurfaceImage(file_path + "\\global.jpg", 0, 1, 0, np.pi * 2, 0, 10, vi.PlotCubicPlane.Plane_Y0)

chart = graph.NewPlot( "chart" )
chart.ChartXYZRange(360, True, True, True)
chart.SetLineColor(0xFF00FF00)
chart.SetLineWidth(2)

if graph.GetCursorCount() < 1:
    cursor = graph.NewCursor("C1")
else:
    cursor = graph.Cursors(0)
cursor.ModifyOption(vi.CursorOptions.CursorShowLabel, True)
cursor.SetColor(0xFF00FF00)

timerDivider = 0
 		
def Animation():
    y = 1.1;
    theta = timerDivider *  np.pi / 180 * 3
    z = (timerDivider % 500) * 10.0 / 500
    chart.ChartXYZ([theta], [y], [z])
    light.SetDirectionLight(-np.cos(theta), -np.sin(theta), 0)

while True:
    Animation()
    time.sleep(0.0)
    timerDivider += 1







    