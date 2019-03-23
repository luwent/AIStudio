from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
from threading import Timer
import time

graph = vi.IPGraph( "ClinderVolumn3D-1" )
graph.SetGraphCategory(vi.GraphCategory.Cylindrical, vi.PlotStyle.Cylindrical4DVolumn)
graph.SetMouseTrackingMode(vi.GraphMouseTrackingMode.TrackingMode_Rotation, True);

palette = graph.GetPalette()
palette.SetTitle("AMP(Vol)", True)
palette.SetMaximumScale(1)
palette.SetMinimumScale(0)

xaxis = graph.Axes(0)
xaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True)
xaxis.SetMajorGridColor(0xFF0000FF)
xaxis.SetMajorTickNumber(8)
xaxis.SetMinorTickNumber(5)

yaxis = graph.Axes(1)
yaxis.SetMajorGridColor(0xFF0000FF)
yaxis.ModifyOption(vi.AxisOptions.MajorTick | vi.AxisOptions.MinorTick | vi.AxisOptions.MinorGrid, True);
yaxis.SetMajorTickNumber(8)
yaxis.SetMinorTickNumber(5)

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
volumn = graph.NewPlot( "cylinder" )
volumn.SetPlotStyle( vi.PlotStyle.Cylindrical4DVolumn )

nq = 200
nr = 10
nz = 20
rVData = np.empty([nr, nq, nz], dtype=np.float32)

for ir in range(nr):
    print(ir)
    for iq in range(nq):
        for iz in range(nz):
            if ir < nr / 3:
                rVData[ir, iq, iz] = ir / nr
            elif ir < nr * 2 / 3:
                rVData[ir, iq, iz] = ir / nr
            else:
                rVData[ir, iq, iz] = ir / nr

filename = inspect.getframeinfo(inspect.currentframe()).filename
file_path  = os.path.dirname(os.path.abspath(filename))
volumn.VolumnData(rVData, file_path + "\\global.jpg")
volumn.VolumnRange(0, np.pi * 2 / (nq - 1), 0, 1.0 / nr, 0., 1.0 / nz)
volumn.SetVolumeCutPosition(0.5, 0.5, 50)

if graph.GetCursorCount() < 1:
    cursor = graph.NewCursor("C1")
else:
    cursor = graph.Cursors(0)
cursor.ModifyOption(vi.CursorOptions.CursorShowLabel, True)
cursor.SetColor(0xFF00FF00)

timerDivider = 0
 		
def VolumnAnimation():
    r = (timerDivider % 340) / 340.0
    volumn.SetVolumeCutPosition(np.pi * 2 * r, 1 * r, 1 * r)
    
while True:
    VolumnAnimation()
    time.sleep(0.2)
    timerDivider += 10