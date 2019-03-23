from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
import time

graph = vi.IPGraph("Graph3D-8")
graph.SetCaption("Annotation Example")
graph.SetMouseTrackingMode( vi.GraphMouseTrackingMode.TrackingMode_Rotation, True)
graph.SetOrientation(-422.2, 0, -347.7)

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(200)
xaxis.SetTitle( "Time" )
xaxis.ModifyOption( vi.AxisOptions.Reversed, True )
xaxis.SetTickLabelOrientation( vi.TextOrientationStyle.FaceCamera )

#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(-1)
yaxis.SetMaximum(1)
yaxis.SetTitle( "Amplitude" )
yaxis.ModifyOption( vi.AxisOptions.Reversed | vi.AxisOptions.AutoScroll, True )
yaxis.SetTickLabelOrientation( vi.TextOrientationStyle.FaceCamera )

#zaxis
axiscount = graph.GetAxisCount()
zaxis = graph.Axes(2)
zaxis.SetMinimum(-1)
zaxis.SetMaximum(1)
zaxis.SetTitle("Z-Axis")
zaxis.SetTickLabelOrientation( vi.TextOrientationStyle.FaceCamera )

plotnum = graph.GetPlotCount()
if plotnum < 1:
    plot = graph.NewPlot( "plot" )
else:
    plot = graph.Plots(0)
plot.SetPlotStyle( vi.PlotStyle.XYZCurve )
plot.SetLineStyle( vi.LineType.LineType_None ) 
plot.SetLineWidth(4)
plot.SetLineColor( vi.MakeColor(220, 55, 0) )
plot.SetPointStyle( vi.IconType.Icon_StarSolid )
plot.SetPointSize(8)
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
    a1 = graph.NewAnnotation("a1")
else:
    a1 = graph.Annotations("a1")
a1.SetCaption( "Face Camera Text", vi.HorizontalAlignment.HorizontalAlign_Center, vi.VerticalAlignment.VerticalAlign_Center)
a1.SetCaptionLocation3D( 50, 0, 0.5 )
a1.SetCaptionColor( vi.MakeColor(0, 0, 255), vi.MakeColor(0, 0, 0, 0x2E) )
a1.SetCaptionBorder(vi.LineType.LineType_Solid, vi.MakeColor(255, 0, 0), 2, 10)
a1.SetCaptionOrientation( vi.TextOrientationStyle.FaceCamera )
a1.SetArrowLineColor(0xFFFF0000);
a1.SetArrowHeadPos3D(100, 0, 0);
a1.SetArrowTailStyle(vi.LineCapType.LineCapType_3DTetrahedron);
a1.SetArrowHeadStyle(vi.LineCapType.LineCapType_3DSphere, 10, 10);

annotationcount = graph.GetAnnotationCount()
if annotationcount < 2:
    a2 = graph.NewAnnotation("a2")
else:
    a2 = graph.Annotations("a2")
a2.SetCaption( "3D Text", 1, 1)
a2.SetCaptionLocation3D( 150, 0, 0 )
a2.SetCaptionColor( vi.MakeColor(0, 0, 255), vi.MakeColor(223, 218, 241) )
a2.SetCaptionBorder(1)
a2.SetCaptionOrientation( vi.TextOrientationStyle.Rotation3D )

if annotationcount < 3:
    torus = graph.NewAnnotation("a3")
else:
    torus = graph.Annotations("a3")
torus = torus.SetDrawType( vi.DrawItemType.DrawItem_Torus )
torus.SetCoordinates3D(170, 0.0, 0.0, 0)
torus.SetCoordinates3D(50, 0.5, 0.2, 1)
torus.SetFillColor(vi.MakeColor(0, 255, 0))

lightcount = graph.GetLightCount()
if lightcount < 1:
    light = graph.NewLight("Light")
else:
    light = graph.Lights(0)
light.ModifyOption( vi.LightOptions.LightEnable, True )
light.SetColor( vi.MakeColor(255, 255, 255), vi.MakeColor(255, 255, 0), vi.MakeColor(0, 0, 255) ) #0xFFFFFFFF, 0xFF3F3F3F, 0x000000000
#light.SetDirectionLight(1, 0.5, -1)
light.SetSpotLight( 210, 0, 0, -1, 0, 0, 45 )
light.SetAttenuation( 1, .00, 0.0000 )

if graph.GetCursorCount() < 1:
    cursor = graph.NewCursor("C1");
else:
    cursor = graph.Cursors(0);
cursor.SetCursorPos3D(20, 0, 0);

rotateZ = 0;
rotateL = 0;
while(1):
    graph = vi.IPGraph("Graph3D-8")
    annotation = graph.Annotations(0)
    annotation.SetCaptionOrientation(vi.TextOrientationStyle.FaceCamera, rotateZ % 360, 0, 0)
    annotation = graph.Annotations(1)
    annotation.SetCaptionOrientation(vi.TextOrientationStyle.Rotation3D, 0, 0, rotateZ % 360)

    light = graph.Lights(0)
    light.SetColor(0xFFFFFFFF, 0, 0)
    light.SetSpotLight(310, 0, 0, -np.cos((rotateL - 45) * 3.14 / 180), 0, np.sin((rotateL - 45) * 3.14 / 180), 30)

    rotateZ += 1
    rotateL += 10
    rotateL = rotateL % 90
    time.sleep( 0.5 )
