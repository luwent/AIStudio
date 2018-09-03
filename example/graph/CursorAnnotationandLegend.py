from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

def MakeCursor(name, xpos=50, ypos=5, color = vi.MakeColor(255,0,0), style = vi.PCursorLineShape.CursorMajorXMajorY, snap = vi.PGraphObjSnapModes.SnapFloating):
    cursor = graph.AddCursor(name)
    cursor.SetColor(color)
    cursor.SetCursorStyle(style)
    cursor.SetSnapMode(snap)
    cursor.SetCursorPos(xpos, ypos)
    cursor.ModifyOption(vi.PCursorOptions.CursorShowLabel, True)
    return cursor
    
#topgraph
graph = vi.IPGraph("Plot-5")
graph.SetFrameColor(vi.PFillType.FillType_Solid, [vi.MakeColor(255, 213, 235)])
graph.SetPlotAreaColor(vi.PFillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph.SetCaption("Cursor Graphs")

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)
#yaxis
yaxis = graph.Axes(1)
yaxis.SetTitle("Amplitude")
yaxis.SetMaximum(10)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)

legend = graph.GetLegend()
legend.SetVisible(True)
    
#Cursor 1 
cursorcount = graph.GetCursorCount()
if cursorcount < 1:
    ycursor = MakeCursor("ypoint")
else:
    graph.RemoveCursor("ypoint")
    ycursor = MakeCursor("ypoint")

#Cursor 2
cursorcount = graph.GetCursorCount()
if cursorcount < 2:
    smallcursor = MakeCursor("smallpoint", 20, 8, vi.MakeColor(0,255,255),vi.PCursorLineShape.CursorMinorXMinorY)
else:
    graph.RemoveCursor("smallpoint")
    smallcursor = MakeCursor("smallpoint", 20, 8, vi.MakeColor(0,255,255),vi.PCursorLineShape.CursorMinorXMinorY)

#Cursor3
cursorcount = graph.GetCursorCount()
if cursorcount < 3:
    followcursor = MakeCursor("followpoint", 80, 3, vi.MakeColor(255, 0, 255), vi.PCursorLineShape.CursorMajorXMajorY,vi.PGraphObjSnapModes.SnapPointsOnPlot)
    followcursor.SetSnapPlot(0)
else:
    graph.RemoveCursor("followpoint")
    followcursor = MakeCursor("followpoint", 80, 3, vi.MakeColor(255, 0, 255), vi.PCursorLineShape.CursorMajorXMajorY,vi.PGraphObjSnapModes.SnapPointsOnPlot)
    followcursor.SetSnapPlot(0)
    
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
y = [np.sin(2 * np.pi * f  * (i/fs)) for i in x] 
plotA.SetLineWidth(2)
plotA.SetLineColor(vi.MakeColor(0, 0, 255))
plotA.SetDataOffset(0, 1)
plotA.PlotY(y)

plotnum = graph.GetPlotCount()
if plotnum < 2:
    plotB = graph.NewPlot("Cos")
else:
    plotB = graph.Plots(1)
plotB.PlotXRange(0, 1)
by = [np.cos(2 * np.pi * f * (i/fs)) for i in x] 
plotB.SetDataOffset(0, 3)
plotB.SetLineWidth(2)
plotB.SetLineColor(vi.MakeColor(0, 0, 255))
plotB.PlotY(by)

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

#bottomgraph
graph2 = vi.IPGraph("Plot-6")
graph2.SetFrameColor(vi.PFillType.FillType_Solid, [vi.MakeColor(255, 213, 235)])
graph2.SetPlotAreaColor(vi.PFillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph2.SetCaption("Annotated Graphs")
graph2.SetMouseTrackingMode(vi.PGraphMouseTrackingMode.TrackingMode_ZoomX |vi.PGraphMouseTrackingMode.TrackingMode_PanX, True )

#xaxis
xaxis = graph2.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(100)
xaxis.SetTitle("Time")
xaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)
#yaxis
yaxis = graph2.Axes(1)
yaxis.SetTitle("Amplitude")
yaxis.SetMaximum(10)
yaxis.SetMinimum(0)
yaxis.ModifyOption(vi.PAxisOptions.AutoScale, False)

anncount = graph2.GetAnnotationCount()

for i in range(anncount):
    graph2.RemoveAnnotation("a1")
annotation1 = graph2.AddAnnotation("a1")
annotation1.SetCaption("Multiple Line Rotated Text", 1,1)
annotation1.SetCaptionLocation(15, 2.5)
annotation1.SetCaptionColor(vi.MakeColor(0, 0, 0))
annotation1.SetCaptionBorder(vi.PLineType.LineType_Solid, vi.MakeColor(255, 0, 255),2, 10)

for i in range(anncount):
    graph2.RemoveAnnotation("a2")
annotation2 = graph2.AddAnnotation("a2")
circle = annotation2.SetDrawType( vi.PDrawItemType.DrawItem_Circle )
circle.SetFillColor(vi.MakeColor(255, 0, 0))
circle.SetCoordinates(45, 0, 0)

plotnum = graph2.GetPlotCount()
if plotnum < 1:
    plot = graph.NewPlot("sin")
else:
    plot = graph2.Plots(0)
plot.PlotXRange(0, 1)
fs = 100 # sample rate 
f = 10 # the frequency of the signal
x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [ 5+1*np.sin(2*np.pi*f * (i/fs)) for i in x] 
plot.PlotY(y)
plot.SetLineWidth(2)
plot.SetLineColor(vi.MakeColor(0,0,255))

for i in range(anncount):
    graph2.RemoveAnnotation("a3")
arrowannotation = graph2.AddAnnotation("a3")
arrowannotation.SetCaption("Data Comment",1,1)
arrowannotation.SetCaptionLocation(50,7)
arrowannotation.SetCaptionColor(vi.MakeColor(0, 0, 0))
arrowannotation.SetCaptionBorder(vi.PLineType.LineType_Solid, vi.MakeColor(255, 0, 0),2, 10)
arrowannotation.SetArrowLineColor(vi.MakeColor(255, 0, 0))