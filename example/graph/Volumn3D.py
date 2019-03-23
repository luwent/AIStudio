from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
from threading import Timer
import time

graph = vi.IPGraph( "Volumn3D-1" )
graph.SetGraphCategory(vi.GraphCategory.XY, vi.PlotStyle.XYZ4DVolumn)
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_Rotation, True);

palette = graph.GetPalette()
palette.SetTitle("AMP(Vol)", True)
palette.SetMaximumScale(1)
palette.SetMinimumScale(-1)

xaxis = graph.Axes(0)
xaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True)
xaxis.SetMajorGridColor(0xFF0000FF)

yaxis = graph.Axes(1)
yaxis.SetMajorGridColor(0xFF0000FF)
yaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True);

zaxis = graph.Axes(2)
zaxis.SetMaximum(100)
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
volumn = graph.NewPlot( "polar" )
volumn.SetPlotStyle( vi.PlotStyle.XYZ4DVolumn )

nx = 40
ny = 50
nz = 100
rVData = np.empty([nz, ny, nx], dtype=np.float32)

for iz in range(nz):
    print(iz)
    a = np.sin(iz * 20.0 / nz)
    for iy in range(ny):
        b = np.cos(iy * 30.0 / ny)
        for ix in range(nx):
            c = np.sin(ix * 40.0 / nx)
            rVData[iz, iy, ix] = a * b * c
volumn.VolumnData(rVData);
volumn.VolumnRange(0, 0.1, 0, 0.1, 0., 1);
volumn.SetVolumeCutPosition(0.5, 0.5, 50);
volumn.SetLineWidth(2);

if graph.GetCursorCount() < 1:
    cursor = graph.NewCursor("C1")
else:
    cursor = graph.Cursors(0)
cursor.ModifyOption(vi.CursorOptions.CursorShowLabel, True)
cursor.SetColor(0xFF00FF00)

timerDivider = 0
 		
def VolumnAnimation():
    r = (timerDivider % 30) / 30.0
    volumn.SetVolumeCutPosition(1 * r, 1 * r, 100 * r)
    
while True:
    VolumnAnimation()
    time.sleep(0.5)
    timerDivider += 1







    