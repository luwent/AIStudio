from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
from threading import Timer
import time

graph = vi.IPGraph( "Bubble3D-1" )
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_Rotation, True);

palette = graph.GetPalette()
palette.SetTitle("Temperature(oC)", False)
palette.SetTransparency(120, 0, 100, True)

xaxis = graph.Axes(0)
xaxis.SetTitle("X")
xaxis.SetMaximum(1)
yaxis = graph.Axes(1)
yaxis.SetMaximum(1)
yaxis.SetMinimum(0)
yaxis.SetTitle("Y")
zaxis = graph.Axes(2)
zaxis.SetMaximum(1)
zaxis.SetMinimum(-1)
zaxis.SetTitle("Z")

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
bubble = graph.NewPlot( "bubble" )
bubble.SetPlotStyle( vi.PlotStyle.XYZBubble )
bubble.SetBubblePara(10)
 
if graph.GetCursorCount() < 1:
    cursor = graph.NewCursor("C1");
else:
    cursor = graph.Cursors(0);
cursor.ModifyOption(vi.CursorOptions.CursorShowLabel, True)
cursor.SetColor(0xFF00FF00);

graph2 = vi.IPGraph( "Vector3D-1" )
graph2.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_Rotation, True);

palette = graph2.GetPalette()
palette.SetTitle("Speed", False)
palette.SetTransparency(120, 0, 100, True)

xaxis = graph2.Axes(0)
xaxis.SetTitle("X")
xaxis.SetMinimum(-10)
xaxis.SetMaximum(10)
yaxis = graph2.Axes(1)
yaxis.SetMaximum(10)
yaxis.SetMinimum(-10)
yaxis.SetTitle("Y")
zaxis = graph2.Axes(2)
zaxis.SetMaximum(10)
zaxis.SetMinimum(0)
zaxis.SetTitle("Z")

lightcount = graph2.GetLightCount()
if lightcount < 1:
    light = graph2.NewLight("Light")
else:
    light = graph2.Lights(0)
light.ModifyOption( vi.LightOptions.LightEnable, True )
light.SetColor( 0xFFFFFFFF, 0xFF3F3F3F, 0x000000000)
light.SetDirectionLight(1, 0.5, -1)

plotnum = graph2.GetPlotCount()
for i in range( plotnum ):
    graph2.RemovePlot( 0 )
vector = graph2.NewPlot( "vector" )
vector.SetPlotStyle( vi.PlotStyle.XYZVector )
vector.SetVectorPara(4, 40)

def BubbleVectorAnimation( bool1, bool2):
    datax = [random.uniform(0,1) for i in range(100)] 
    datay = [random.uniform(0,1) for i in range(100)]
    dataz = [random.uniform(0,1) for i in range(100)]
    datar = [random.uniform(0,1) for i in range(100)]
    bubble.BubbleXYZ(datax, datay, dataz, datar)

    datax = [random.uniform(0,1) for i in range(200)] 
    datay = [random.uniform(0,1) for i in range(200)]
    dataz = [random.uniform(0,1) for i in range(200)]
    data_theta = np.empty(200)
    data_azimuthal = np.empty(200)
    data_length = np.empty(200)
    n = 200
    for i in range(200):
        r = datax[i] * 2 + (i + 10.0) * 8.0 / 200
        theta = i * 10.0 + 10
        datax[i] = r * np.cos(theta * 3.14 / 180)
        datay[i] = r * np.sin(theta * 3.14 / 180)
        dataz[i] = i * 10.0 / n
        data_theta[i] = theta
        data_azimuthal[i] = 0
        data_length[i] = (i + 1.0) / n
    vector.VectorABL( datax, datay, dataz, data_theta, data_azimuthal, data_length )
    
while True:
    BubbleVectorAnimation(True, True)
    time.sleep(0.5)






    