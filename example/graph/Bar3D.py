from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import random

#topgraph
filename = inspect.getframeinfo(inspect.currentframe()).filename
file_path     = os.path.dirname(os.path.abspath(filename))
graph = vi.IPGraph("Graph3D-6")
graph.SetCaption("Temperature vs. Month")
graph.SetMouseTrackingMode( vi.GraphMouseTrackingMode.TrackingMode_Rotation, True)
graph.SetOrientation(-422.2, 0, -347.7)
graph.SetGraphCategory( vi.GraphCategory.Bar3D, vi.PlotStyle.BarVBar )
graph.SetSkyBackground(file_path + "\\right.jpg", file_path + "\\left.jpg", file_path + "\\top.jpg", file_path + "\\bottom.jpg", file_path + "\\back.jpg", file_path + "\\front.jpg")

#legend
legend = graph.GetLegend()
legend.SetVisible(True)

#xaxis
xaxis = graph.Axes(0)
xaxis.SetMinimum(0.5)
xaxis.SetMaximum(12.5)
xaxis.SetTitle("Month")
xaxis.ModifyOption(vi.AxisOptions.MajorGrid, False)

#yaxis
yaxis = graph.Axes(1)
yaxis.SetMinimum(-0.5)
yaxis.SetMaximum(0.5)
yaxis.SetTitle( "Location" )
yaxis.ModifyOption( vi.AxisOptions.ShowTitle, False)

#zaxis
axiscount = graph.GetAxisCount()
zaxis = graph.Axes(2)
zaxis.SetMinimum(-10)
zaxis.SetMaximum(100)
zaxis.SetTitle( "Temperature (Degrees)" )

lightcount = graph.GetLightCount()
if lightcount < 1:
    light = graph.NewLight("Light")
else:
    light = graph.Lights(0)
light.ModifyOption( vi.LightOptions.LightEnable, True )
light.SetColor( vi.MakeColor(255, 255, 255), vi.MakeColor(100, 100, 100), vi.MakeColor(0, 0, 0) )
light.SetDirectionLight(1, 0.5, -1)

plotnum = graph.GetPlotCount()
if plotnum < 1:
    bar1 = graph.NewPlot( "New York" )
else:
    bar1 = graph.Plots(0)
bar1.SetPlotStyle( vi.PlotStyle.BarVBar )
label1 = [ "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec." ]
data1 = [ -2, 0, 5, 10, 15, 20, 25, 22, 15, 5, 0, -1 ]
bar1.Bar( label1, data1 )
bar1.BarColor( vi.FillType.FillType_Solid, vi.MakeColor(255,0,0) , 1, vi.MakeColor(255,0,0) )
bar1.SetBarPara( 90, -1, 6 )

if plotnum < 2:
    bar2 = graph.NewPlot( "Los Angeles" )
else:
    bar2 = graph.Plots(1)
bar2.SetPlotStyle( vi.PlotStyle.BarVBar )
data2 = [ 14, 15, 15.5, 16.5, 18.4, 21, 25, 22, 21, 20, 17, 15 ]
bar2.Bar( label1, data2 )
bar2.BarColor( vi.FillType.FillType_Solid, vi.MakeColor(0,255,0) , 1, vi.MakeColor(0,255,0) )
bar2.SetBarPara( 90, -1, 6 )

if plotnum < 3:
    bar3 = graph.NewPlot( "Columbus" )
else:
    bar3 = graph.Plots(2)
bar3.SetPlotStyle( vi.PlotStyle.BarVBar )
data3 = [ -4, -2, 5.5, 11.5, 16.4, 22, 23, 20, 12, 4, 2, -2 ]
bar3.Bar( label1, data3 )
bar3.BarColor( vi.FillType.FillType_Solid, vi.MakeColor(0,0,255) , 1, vi.MakeColor(0,0,255) )
bar3.SetBarPara( 90, -1, 6 )

#Bottom Graph
graph2 = vi.IPGraph("Graph3D-7")
graph2.SetCaption("Temperature vs. Month")
graph2.SetMouseTrackingMode( vi.GraphMouseTrackingMode.TrackingMode_Rotation, True)
graph2.SetOrientation(-422.2, 0, -347.7)
graph2.SetGraphCategory( vi.GraphCategory.Bar3D, vi.PlotStyle.BarVBar )

#xaxis
xaxis = graph2.Axes(0)
xaxis.SetMinimum(0.5)
xaxis.SetMaximum(12.5)
xaxis.SetTitle("Month")
xaxis.ModifyOption(vi.AxisOptions.MajorGrid, False)

#yaxis
yaxis = graph2.Axes(1)
yaxis.SetMinimum(0)
yaxis.SetMaximum(4)
yaxis.SetTitle("")
yaxis.ModifyOption( vi.AxisOptions.ShowTitle | vi.AxisOptions.TickLabel, False)

#zaxis
axiscount = graph2.GetAxisCount()
if axiscount < 3:
    zaxis = graph2.NewAxis( "zaxis", 2 )
else:
    zaxis = graph2.Axes(2)
zaxis.SetMinimum(-10)
zaxis.SetMaximum(30)
zaxis.SetTitle( "Temperature (Degrees)" )
zaxis.ModifyOption(vi.AxisOptions.AutoScale, False)

lightcount = graph2.GetLightCount()
if lightcount < 1:
    light = graph2.NewLight("Light")
else:
    light = graph2.Lights("Light")
light.ModifyOption( vi.LightOptions.LightEnable, True )
light.SetColor( vi.MakeColor(255, 255, 255), vi.MakeColor(0, 255, 0), vi.MakeColor(0, 0, 0) )
light.SetDirectionLight(1, 0.5, -1)

label2 = [ "New York", "Los Angeles", "Columbus" ]
data4 = [ -2, 0, 5, 10, 15, 20, 25, 22, 15, 5, 0, -1, 14, 15, 15.5, 16.5, 18.4, 21, 25, 22, 21, 20, 17, 15, -4, -2, 5.5, 11.5, 16.4, 22, 23, 20, 12, 4, 2, -2 ]
colors = np.empty(36, np.uint32)
for i in range(12):
    colors[i] = vi.MakeColor(255, 0, 0)
    colors[i + 12] = vi.MakeColor(0, 255, 0)
    colors[i + 24] = vi.MakeColor(0, 0, 255)
    
plotnum = graph2.GetPlotCount()
if plotnum < 1:
    bar = graph2.NewPlot( "bar" )
else:
    bar = graph2.Plots(0)
bar.SetPlotStyle( vi.PlotStyle.BarVBar )
bar.Bar3D( label1, label2, data4, colors )
bar.BarColor( vi.FillType.FillType_Solid, vi.MakeColor(255,0,255) , 1, vi.MakeColor(255,0,0) )
bar.SetBarPara( 70 )