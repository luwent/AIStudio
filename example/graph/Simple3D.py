from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np

graph = vi.IPGraph("Graph3D-1")
graph.SetCaption("Simple Example")

palette = graph.SetPalette(-1,1,True)

	#~ IVCursor3D* pCursor =(IVCursor3D*) m_DemoGraph->AddCursor();
	#~ pCursor->SetCursorPos(4, 5, 0.50);

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0)
xaxis.SetMaximum(10)
xaxis.SetTitle("X-Axis")
xaxis.ModifyOption( (vi.AxisOptions.ShowPeerAxisLine | vi.AxisOptions.ShowPeerTick | vi.AxisOptions.ShowPeerLabel | vi.AxisOptions.MinorGrid), True )

#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(0)
yaxis.SetMaximum(10)
yaxis.SetTitle("Y-Axis")
yaxis.ModifyOption( (vi.AxisOptions.ShowPeerAxisLine | vi.AxisOptions.ShowPeerTick | vi.AxisOptions.ShowPeerLabel | vi.AxisOptions.MinorGrid), True )

#zaxis
axiscount = graph.GetAxisCount()
if axiscount < 3:
    zaxis = graph.NewAxis( "zaxis", 2 )
else:
    zaxis = graph.Axes(2)
zaxis.SetMinimum(-1)
zaxis.SetTitle("Z-Axis")
zaxis.ModifyOption( (vi.AxisOptions.ShowPeerAxisLine | vi.AxisOptions.ShowPeerTick | vi.AxisOptions.ShowPeerLabel | vi.AxisOptions.MinorGrid), True )

#Add Annotation
acount = graph.GetAnnotationCount()
for i in range( acount ):
    graph.RemoveAnnotation( "Annotation1" )
Annotation1 = graph.NewAnnotation( "Annotation1" )
Annotation1.SetCaption( "Maximum" )
Annotation1.SetCaptionLocation3D( 5, 5, 0.5 )
Annotation1.SetCaptionColor( vi.MakeColor(0, 0, 255) )
Annotation1.SetArrowHeadPos3D( 3.14 / 2 * 3, 3.14, 1.1 )
Annotation1.SetArrowLineStyle( vi.LineType.LineType_Solid )
Annotation1.SetArrowHeadStyle( vi.LineCapType.LineCapType_3DTetrahedron )

#graph.SetPlotAreaColor(vi.FillType_FillTypeSolid, [vi.MakeColor(255,255, 255)])
plotnum = graph.GetPlotCount()
for i in range(plotnum):
    graph.RemovePlot(0)
plot = graph.NewPlot( "Simple3D" )

datax = np.empty(200)
datay = np.empty(200)
dataz = np.empty(200*200)
datac = np.empty(200*200)

def PlotDualSine():
    for i in range(200):
        datax[i] = i / 20.0
        datay[i] = i / 20.0
    for i in range(200):
        for j in range(200):
            dataz[j + i * 200] = np.sin( datax[j] ) * np.cos( datay[i] )
            datac[j + i * 200] = i*j / (200.0*200.0)
    plot.SetPlotStyle( vi.PlotStyle.XYZSurface )
    plot.SurfaceXYZ( datax, datay, dataz, datac)
    
PlotDualSine()

	#~ pPlot->SurfaceXYZ(datax, datay, dataz, 0, 200, 200, true);

