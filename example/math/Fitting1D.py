import numpy as np
import IStudio as iv
import IMath as im

#get graph and data table
graph = iv.IPGraph("Plot-1")
table = iv.IPDataTable("Data-1")
fittingmath = im.IPFitting()

#get data from data table, type some data in col1 and col2
x = np.zeros(5)
n= table.GetColData(1, 1, 5, 1, x)
y = np.zeros(5)
n= table.GetColData(2, 1, 5, 1, y)
 
#clear all plots
graph.RemovePlot(-1)
#plot raw data
plot1 = graph.NewPlot("xy")
plot1.SetLineStyle(iv.LineType.LineType_None)
plot1.SetPointStyle(iv.IconType.Icon_CircleEmpty)
plot1.SetPointColor(iv.MakeColor(255, 0, 0))
plot1.PlotXY(x, y)

statistics = np.zeros(20)
ox = np.zeros(100)
oy = np.zeros(100)
for i in range(100):
    ox[i] = i * 0.05
output = fittingmath.LeastSquareLinear(x, y, statistics, ox, oy)
print(output)
plot2 = graph.NewPlot("fit1")
plot2.SetLineStyle(iv.LineType.LineType_Solid)
plot2.SetLineWidth(1)
plot2.PlotXY(ox, oy)

poly = np.zeros(20)
output = fittingmath.LeastSquarePoly(x, y, 4, poly, statistics, ox, oy)
print(output)
plot3 = graph.NewPlot("fit2")
plot3.SetLineStyle(iv.LineType.LineType_Solid)
plot3.SetLineColor(iv.MakeColor(0, 255, 0))
plot3.SetLineWidth(1)
plot3.PlotXY(ox, oy)


poly = np.zeros(20)
print(poly.dtype)
r, a0, a1, a2, a3, residual = fittingmath.CubicFit(x, y, poly)
print(r, a0, a1, a2, a3, residual)
plot4 = graph.NewPlot("fit3")
plot4.SetLineStyle(iv.LineType.LineType_Solid)
plot4.SetLineColor(iv.MakeColor(0, 0, 255))
plot4.SetLineWidth(2)
for i in range(100):
    oy[i] = fittingmath.CubicFun(ox[i], a0, a1, a2, a3)
plot4.PlotXY(ox, oy)

