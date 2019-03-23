from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random
from threading import Timer
import time

def DictionaryToList(dict):
    keys = list( dict.keys() )
    values = list( dict.values() )
    datavalues = []
    colorvalues = []
    for i in values:
        if type( i ) is tuple:
            datavalues.append( i[0] )
            colorvalues.append( i[1] )
        else:
            datavalues.append(i)
    return keys, datavalues, colorvalues


graph = vi.IPGraph( "Pie3D-1" )
graph.SetGraphCategory( vi.GraphCategory.Pie, vi.PlotStyle.PiePie )
graph.SetOrientation(-422.2, 0, -347.7)
graph.SetPlotAreaScale(0.7)
zaxis = graph.Axes(2)
zaxis.SetMaximum(5)
xaxis = graph.Axes(0)
xaxis.SetTickColor(0xFFFF0000)

#legend
legend = graph.GetLegend()
legend.SetVisible( True )

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
doughnut = graph.NewPlot( "Pie1" )
doughnut.SetPlotStyle( vi.PlotStyle.PieDoughnut )
dict = {"Jan." : 2 , "Feb." : 4, "Mar." : 5, "Apr." : 10, "May" : 15, "Jun." : 20, "Jul." : 25, "Aug." : 22, "Sept." : 15, "Oct." : 5, "Nov." : 6, "Dec." : 8}
label, data, color = DictionaryToList(dict)
doughnut.PieLabel( label )
doughnut.PieData( data )
doughnut.PieColor( color )
doughnut.ModifyOption(vi.PlotOptions.PercentLabel, True);
doughnut.SetPieOffset(6, 30);

graph2 = vi.IPGraph( "Pie3D-2" )
graph2.SetGraphCategory( vi.GraphCategory.Pie3D, vi.PlotStyle.PiePie3D )
graph2.SetCaption("Monthly Sale")
graph2.SetCaptionAlign(vi.LocationSide.Location_BottomCenter)
graph2.SetOrientation(-417, 0, -357)
graph2.SetPlotAreaScale(0.7)
zaxis = graph2.Axes(2)
zaxis.SetMaximum(5)
xaxis = graph2.Axes(0)
xaxis.SetTickColor(0xFF00FF00)
xaxis.SetTickPadding(40)

#legend
legend = graph2.GetLegend()
legend.SetVisible( True )

plotnum = graph2.GetPlotCount()
for i in range( plotnum ):
    graph2.RemovePlot( 0 )
pie3D = graph2.NewPlot( "Pie3d" )
pie3D.SetPlotStyle( vi.PlotStyle.PiePie3D )
pie3D.SetPie3DPara( 30, 10 )
dict = {"Jan." : 2 , "Feb." : 4, "Mar." : 5, "Apr." : 10, "May" : 15, "Jun." : 20, "Jul." : 25, "Aug." : 22, "Sept." : 15, "Oct." : 5, "Nov." : 6, "Dec." : 8}
label, data, color = DictionaryToList(dict)
pie3D.PieLabel( label )
pie3D.PieData( data )
pie3D.PieColor( color )






    