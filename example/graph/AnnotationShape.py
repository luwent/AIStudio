from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
import time

graph = vi.IPGraph("Graph3D-4")
graph.SetFrameColor(vi.FillType.FillType_Solid, [vi.MakeColor(223, 218, 241)])
graph.SetPlotAreaColor(vi.FillType.FillType_Solid, [vi.MakeColor(255, 255, 255)])
graph.SetCaption("Annotation Graph Example")
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
if axiscount < 3:
    zaxis = graph.NewAxis( "zaxis", 2 )
else:
    zaxis = graph.Axes(2)
zaxis.SetMinimum(-1)
zaxis.SetTitle("Z-Axis")
zaxis.SetTickLabelOrientation( vi.TextOrientationStyle.FaceCamera )

plotnum = graph.GetPlotCount()
if plotnum < 1:
    plot = graph.NewPlot( "star" )
else:
    plot = graph.Plots(0)
plot.SetPlotStyle( vi.PlotStyle.XYZCurve )
plot.SetLineStyle( vi.LineType.LineType_None ) #linetype_3DCylinder
plot.SetLineWidth(4)
plot.SetLineColor( vi.MakeColor(220, 55, 0) )
plot.SetPointStyle( 201 )
plot.SetPointSize(8)
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
#~ graph.RemoveAnnotation("a1")
#~ a1 = graph.AddAnnotation("a1")
a1.SetCaption( "Face Camera Text", 1, 1)
a1.SetCaptionLocation3D( 50, 0, 0.5 )
a1.SetCaptionColor( vi.MakeColor(0, 0, 255), vi.MakeColor(223, 218, 241) )
a1.SetCaptionBorder(1)
a1.SetCaptionOrientation( vi.TextOrientationStyle.FaceCamera )
a1.SetArrowLineColor( vi.MakeColor(255, 0, 0) )
a1.SetArrowHeadPos3D( 100, 0, 0 )
a1.SetArrowTailStyle( vi.LineCapType.LineCapType_3DTetrahedron )
a1.SetArrowHeadStyle( vi.LineCapType.LineCapType_3DSphere, 10, 10 )


annotationcount = graph.GetAnnotationCount()
if annotationcount < 2:
    a2 = graph.AddAnnotation("a2")
else:
    a2 = graph.GetAnnotation("a2")
#~ graph.RemoveAnnotation("a2")
#~ a2 = graph.AddAnnotation("a2")
a2.SetCaption( "3D Text", 1, 1)
a2.SetCaptionLocation3D( 150, 0, 0 )
a2.SetCaptionColor( vi.MakeColor(0, 0, 255), vi.MakeColor(223, 218, 241) )
a2.SetCaptionBorder(1)
a2.SetCaptionOrientation( vi.TextOrientationStyle.Rotation3D )

if annotationcount < 3:
    a3 = graph.AddAnnotation("a3")
else:
    a3 = graph.GetAnnotation("a3")
#~ graph.RemoveAnnotation("a3")
#~ a3 = graph.AddAnnotation("a3")
torus = a3.SetDrawType( vi.DrawItemType.DrawItem_Torus )
torus.SetCoordinates(170, 0.0, 0.0, 0)
torus.SetCoordinates(50, 0.5, 0.2, 1)
torus.SetFillColor(vi.MakeColor(0, 255, 0))

lightcount = graph.GetLightCount()
if lightcount < 1:
    light = graph.AddLight("Light")
else:
    light = graph.GetLight("Light")
light.ModifyOption( vi.LightOptions.LightEnable, True )
light.SetColor( 0xFFFFFFFF, 0xFF3F3F3F, 0x000000000 )
light.SetDirectionLight(1, 0.5, -1)
light.SetSpotLight( 210, 0, 0, -1, 0, 0, 45 )
light.SetAttenuation( 1, .00, 0.0000 )

rotateZ = 0
rotateL = 0
timerDivider = 0
while True:
    if( timerDivider % 10 == 0 ):
        Annotation = graph.GetAnnotation("a1")
        Annotation.SetCaptionOrientation( vi.TextOrientationStyle.FaceCamera, rotateZ % 360, 0, 0 )
        Annotation2 = graph.GetAnnotation("a2")
        Annotation2.SetCaptionOrientation( vi.TextOrientationStyle.Rotation3D, 0, 0, rotateZ % 360 )
        
        Light = graph.GetLight("Light")
        Light.SetColor( vi.MakeColor(255, 255, 255), 0, 0 )
        Light.SetSpotLight( 310, 0, 0, -np.cos((rotateL - 45) * 3.14 / 180), 0, np.sin((rotateL - 45) * 3.14 / 180), 30 )
        
        rotateZ = rotateZ + 1
        rotateL = rotateL + 10
        rotateL = rotateL % 90
        graph.RedrawGraph()
        time.sleep(0.2)
    timerDivider = timerDivider + 1