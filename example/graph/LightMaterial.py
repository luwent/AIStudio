from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
import time

graph = vi.IPGraph("Graph3D-5")
graph.SetCaption("Light Material Graph Example")
graph.SetMouseTrackingMode( vi.PGraphMouseTrackingMode.TrackingMode_Rotation, True)
graph.SetOrientation(-422.2, 0, -347.7)

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(200)
xaxis.SetTitle( "Time" )
xaxis.ModifyOption( vi.PAxisOptions.Reversed, True )
xaxis.SetTickLabelOrientation( vi.PTextOrientationStyle.FaceCamera )

#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(-1)
yaxis.SetMaximum(1)
yaxis.SetTitle( "Amplitude" )
yaxis.ModifyOption( vi.PAxisOptions.Reversed | vi.PAxisOptions.AutoScroll, True )
yaxis.SetTickLabelOrientation( vi.PTextOrientationStyle.FaceCamera )

#zaxis
axiscount = graph.GetAxisCount()
if axiscount < 3:
    zaxis = graph.NewAxis( "zaxis", 2 )
else:
    zaxis = graph.Axes(2)
zaxis.SetMinimum(-1)
zaxis.SetMaximum(1)
zaxis.SetTitle("Z-Axis")
zaxis.SetTickLabelOrientation( vi.PTextOrientationStyle.FaceCamera )

plotnum = graph.GetPlotCount()
if plotnum < 1:
    plot = graph.NewPlot( "plot" )
else:
    plot = graph.Plots(0)
plot.SetPlotStyle( vi.PPlotStyle.XYZCurve )
plot.SetLineStyle( vi.PLineType.LineType_3DCylinder ) 
plot.SetLineWidth(4)
plot.SetLineColor( vi.MakeColor(220, 55, 0) )
plot.SetPointStyle( 1001 )
plot.SetPointSize(3)
plot.SetPointColor( vi.MakeColor(255, 0, 0) )
plot.SetPointFillColor( vi.MakeColor(0, 255, 0) )
datax= np.empty(100)
datay = np.empty(100)
dataz = np.empty(100)
for i in range(100):
    datax[i] = i * 2
    datay[i] = i * np.sin( i * np.pi / 5 ) / 100
    dataz[i] = i * np.cos( i * np.pi / 5) / 100
plot.PlotXYZCurve( datax, datay, dataz, dataz )

annotationcount = graph.GetAnnotationCount()
if annotationcount < 1:
    a1 = graph.AddAnnotation("a1")
else:
    a1 = graph.GetAnnotation("a1")
a1.SetCaption( "Face Camera Text", 1, 1)
a1.SetCaptionLocation3D( 50, 0, 0.5 )
a1.SetCaptionColor( vi.MakeColor(0, 0, 255), vi.MakeColor(223, 218, 241) )
a1.SetCaptionBorder(1)
a1.SetCaptionOrientation( vi.PTextOrientationStyle.FaceCamera )

annotationcount = graph.GetAnnotationCount()
if annotationcount < 2:
    a2 = graph.AddAnnotation("a2")
else:
    a2 = graph.GetAnnotation("a2")
a2.SetCaption( "3D Text", 1, 1)
a2.SetCaptionLocation3D( 150, 0, 0 )
a2.SetCaptionColor( vi.MakeColor(0, 0, 255), vi.MakeColor(223, 218, 241) )
a2.SetCaptionBorder(1)
a2.SetCaptionOrientation( vi.PTextOrientationStyle.Rotation3D )

if annotationcount < 3:
    a3 = graph.AddAnnotation("a3")
else:
    a3 = graph.GetAnnotation("a3")
torus = a3.SetDrawType( vi.PDrawItemType.DrawItem_Torus )
torus.SetCoordinates(170, 0.0, 0.0, 0)
torus.SetCoordinates(50, 0.5, 0.2, 1)
torus.SetFillColor(vi.MakeColor(0, 255, 0))

lightcount = graph.GetLightCount()
if lightcount < 1:
    light = graph.AddLight("Light")
else:
    light = graph.GetLight("Light")
light.ModifyOption( vi.PLightOptions.LightEnable, True )
light.SetColor( vi.MakeColor(255, 255, 255), vi.MakeColor(255, 255, 0), vi.MakeColor(0, 0, 255) ) #0xFFFFFFFF, 0xFF3F3F3F, 0x000000000
#light.SetDirectionLight(1, 0.5, -1)
light.SetSpotLight( 210, 0, 0, -1, 0, 0, 45 )
light.SetAttenuation( 1, .00, 0.0000 )
