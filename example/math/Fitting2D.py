import numpy as np
import IStudio as iv
import IMath as im

#get graph and data table
graph = iv.IPGraph("Graph3D-1")
xaxis = graph.Axes(0)
xaxis.ModifyOption( (iv.AxisOptions.AutoScale), True )
yaxis = graph.Axes(1)
yaxis.ModifyOption( (iv.AxisOptions.AutoScale), True )
zaxis = graph.Axes(2)
zaxis.ModifyOption( (iv.AxisOptions.AutoScale), True )

table = iv.IPDataTable("Data-2")
fittingmath = im.IPFitting()

#get data from data table, type some data in col1, col2 and clo3
x = np.zeros(7)
n= table.GetColData(1, 1, 7, 1, x)
y = np.zeros(7)
n= table.GetColData(2, 1, 7, 1, y)
z = np.zeros(7)
n= table.GetColData(3, 1, 7, 1, z)

#clear all plots
graph.RemovePlot(-1)
#plot raw data
plot1 = graph.NewPlot("xyz")
plot1.SetLineStyle(iv.LineType.LineType_None)
plot1.SetPointStyle(iv.IconType.Icon_CircleEmpty)
plot1.SetPointColor(iv.MakeColor(255, 0, 0))
plot1.PlotXYZCurve(x, y, z)

statistics = np.zeros(20)
ox = np.zeros(50)
oy = np.zeros(40)
oz = np.zeros([40,  50])
for i in range(50):
    ox[i] = i * 0.1
for i in range(40):
    oy[i] = i * 0.1
    
output = fittingmath.LeastSquareLinear(x, y, z, statistics, ox, oy, oz)
print(output)
plot2 = graph.NewPlot("fit1")
plot2.SetPlotStyle(iv.PlotStyle.XYZSurface)
plot2.SurfaceXYZ2(ox, oy, oz, oz)

poly = np.zeros(20)
output = fittingmath.LeastSquarePoly(x, y, z, 4, poly, statistics, ox, oy, oz)
print(output)
plot3 = graph.NewPlot("fit2")
plot3.SetPlotStyle(iv.PlotStyle.XYZSurface)
plot3.SurfaceXYZ2(ox, oy, oz, oz)

r, a0, x0, dx, y0, dy, residual = fittingmath.GaussianFit2D(x, y, z)
print(r, a0, x0, dx, y0, dy, residual)
plot4 = graph.NewPlot("fit3")
plot4.SetPlotStyle(iv.PlotStyle.XYZSurface)
for iy in range(40):
    for ix in range(50):
        oz[iy, ix] = fittingmath.GaussianFun2D(ox[ix], oy[iy], a0, x0, dx, y0, dy, 0)
plot4.SurfaceXYZ2(ox, oy, oz, oz)

x = np.zeros(5)
n= table.GetColData(1, 1, 5, 1, x)
y = np.zeros(4)
n= table.GetColData(2, 1, 5, 1, y)
z = np.zeros([4, 5])
n= table.GetData2(5, 9, 1, 2, 5, 1, z)

plot6 = graph.NewPlot("xyz2d")
plot6.SetLineStyle(iv.LineType.LineType_None)
plot6.SetPointStyle(iv.IconType.Icon_3DBox)
plot6.SetPointFillColor(iv.MakeColor(255, 0, 0))
plot6.SurfaceXYZ2(x, y, z)

knotx= np.zeros(3 + 2)
knoty= np.zeros(3 + 2)
coef= np.zeros(3 * 3)
r = fittingmath.LeastSquareSpline(x, y, z, 2, 2, knotx, knoty, coef, ox, oy, oz)
print(r)
plot5 = graph.NewPlot("fit4")
plot5.SetPlotStyle(iv.PlotStyle.XYZSurface)
plot5.SurfaceXYZ2(ox, oy, oz, oz)

