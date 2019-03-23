import numpy as np
import IStudio as iv
import IMath as im

#get graphs
graph1 = iv.IPGraph("Plot-2")
legend = graph1.GetLegend()
legend.SetVisible(True)
graph2 = iv.IPGraph("Plot-3")
legend = graph2.GetLegend()
legend.SetVisible(True)
functionlib = im.IPFunctions()

#get data from data table, type some data in col1 and col2
x = np.zeros(200)
y = np.zeros(200)
 
#clear all plots
graph1.RemovePlot(-1)

for i in range(200):
    x[i] = i * 0.1
    y[i] = functionlib.Bsjn(x[i], 0)
  
#plot raw data
plot1 = graph1.NewPlot("J0(x)")
plot1.SetLineStyle(iv.LineType.LineType_Solid)
plot1.SetLineColor(iv.MakeColor(255, 0, 0))
plot1.PlotXY(x, y)

for i in range(200):
    y[i] = functionlib.Bsjn(x[i], 1)
plot2 = graph1.NewPlot("J1(x)")
plot2.SetLineStyle(iv.LineType.LineType_Dash)
plot2.SetLineColor(iv.MakeColor(0, 255, 0))
plot2.PlotXY(x, y)

for i in range(200):
    y[i] = functionlib.Bsjn(x[i], 2)
plot3 = graph1.NewPlot("J2(x)")
plot3.SetLineStyle(iv.LineType.LineType_DashDot)
plot3.SetLineColor(iv.MakeColor(0, 0, 255))
plot3.PlotXY(x, y)


#clear all plots
graph2.RemovePlot(-1)

for i in range(200):
    x[i] = i * 0.1
    y[i] = functionlib.Bei0(x[i])
  
#plot raw data
plot1 = graph2.NewPlot("Bei0(x)")
plot1.SetLineStyle(iv.LineType.LineType_Solid)
plot1.SetLineColor(iv.MakeColor(255, 0, 0))
plot1.PlotXY(x, y)

for i in range(200):
    y[i] = functionlib.Kei0(x[i])
plot2 = graph2.NewPlot("Kei0(x)")
plot2.SetLineStyle(iv.LineType.LineType_Dash)
plot2.SetLineColor(iv.MakeColor(0, 255, 0))
plot2.PlotXY(x, y)

for i in range(200):
    y[i] = functionlib.Ber0(x[i])
plot3 = graph2.NewPlot("Ber0(x)")
plot3.SetLineStyle(iv.LineType.LineType_DashDot)
plot3.SetLineColor(iv.MakeColor(0, 0, 255))
plot3.PlotXY(x, y)
