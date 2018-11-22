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


graph = vi.IPGraph( "Pie-1" )
graph.SetGraphCategory( vi.PGraphCategory.Pie, vi.PPlotStyle.PiePie )

#legend
legend = graph.GetLegend()
legend.SetVisible( True )

plotnum = graph.GetPlotCount()
for i in range( plotnum ):
    graph.RemovePlot( 0 )
pie2D = graph.NewPlot( "Pie1" )
pie2D.SetPlotStyle( vi.PPlotStyle.PiePie )
dict = {"Jan." : 2 , "Feb." : 4, "Mar." : 5, "Apr." : 10, "May" : 15, "Jun." : 20, "Jul." : 25, "Aug." : 22, "Sept." : 15, "Oct." : 5, "Nov." : 6, "Dec." : 8}
label, data, color = DictionaryToList(dict)
pie2D.PieLabel( label )
pie2D.PieData( data )
pie2D.PieColor( color )


graph2 = vi.IPGraph( "Pie-2" )
graph2.SetGraphCategory( vi.PGraphCategory.Pie3D, vi.PPlotStyle.PiePie3D )

#legend
legend = graph2.GetLegend()
legend.SetVisible( True )

plotnum = graph2.GetPlotCount()
for i in range( plotnum ):
    graph2.RemovePlot( 0 )
pie3D = graph2.NewPlot( "Pie3d" )
pie3D.SetPlotStyle( vi.PPlotStyle.PiePie3D )
pie3D.SetPie3DPara( 30, 10 )
dict = {"Jan." : 2 , "Feb." : 4, "Mar." : 5, "Apr." : 10, "May" : 15, "Jun." : 20, "Jul." : 25, "Aug." : 22, "Sept." : 15, "Oct." : 5, "Nov." : 6, "Dec." : 8}
label, data, color = DictionaryToList(dict)
pie3D.PieLabel( label )
pie3D.PieData( data )
pie3D.PieColor( color )

timercount = 0
def PieAnimation():
    if( timercount % 2 == 0):
        pie2D.SetPlotStyle( vi.PPlotStyle.PiePie )
        pie3D.SetPlotStyle(  vi.PPlotStyle.PiePie3D )
    else:
        pie2D.SetPlotStyle( vi.PPlotStyle.PieDoughnut )
        pie3D.SetPlotStyle( vi.PPlotStyle.PieDoughnut3D )
       
while (timercount < 20):
    PieAnimation()
    time.sleep( 0.5 )
    timercount = timercount + 1





    