from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
from threading import Timer
import time

graph = vi.IPGraph( "Polar3D-1" )
graph.SetGraphCategory(vi.GraphCategory.Polar, vi.PlotStyle.Polar3DImage)
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_Rotation, True);

palette = graph.GetPalette()
palette.SetTitle("AMP(Vol)", True)
 
xaxis = graph.Axes(0)
xaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True)
xaxis.SetMajorTickNumber(8)
xaxis.SetMinorTickNumber(5)
xaxis.SetMajorGridColor(0xFF0000FF)

yaxis = graph.Axes(1)
yaxis.SetMajorTickNumber(8)
yaxis.SetMinorTickNumber(5)
yaxis.SetMajorGridColor(0xFF0000FF)
yaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True);

zaxis = graph.Axes(2)
zaxis.SetMaximum(1)
zaxis.SetMinimum(0)

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
polar = graph.NewPlot( "polar" )
polar.SetPlotStyle( vi.PlotStyle.Polar3DImage )
filename = inspect.getframeinfo(inspect.currentframe()).filename
file_path  = os.path.dirname(os.path.abspath(filename))
polar.SurfaceImage(file_path + "\\global.jpg", 0, -np.pi / 2, 1, np.pi * 2, np.pi, 0, vi.PlotCubicPlane.Plane_Z0)
 
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

polatIndex = 0
 		
def PolarAnimation():
    z = 1.1
    alfa = polatIndex *  np.pi / 180 * 3
    theta = np.sin(polatIndex * 0.03 * 3) *  np.pi / 4
    chart.ChartXYZ([alfa], [theta], [z])
    light.SetDirectionLight(-np.cos(theta) * np.cos(alfa), -np.cos(theta) * np.sin(alfa), -np.sin(theta))
    
while True:
    PolarAnimation()
    time.sleep(0.)
    polatIndex += 1







    