import numpy as np
import IStudio as iv
import IMath as im

#get graphs
graph1 = iv.IPGraph("Plot-4")
legend = graph1.GetLegend()
legend.SetVisible(True)
graph2 = iv.IPGraph("Plot-5")
legend = graph2.GetLegend()
legend.SetVisible(True)

functionlib = im.IPFunctions()

#original waveform
n = 8000
dt = 0.005
data = np.zeros(n)
data1 = np.zeros(n)
functionlib.ChirpWave(data, 1, 0, 10, 1/dt)

#IIR Filter
IIRfilterlib = im.IPIIRFilter()

graph1.RemovePlot(-1)
plot1 = graph1.NewPlot("Chirp")
plot1.SetLineStyle(iv.LineType.LineType_Solid)
plot1.SetLineColor(iv.MakeColor(255, 0, 0))
plot1.PlotXRange(0, dt)
plot1.PlotY(data)

lowCutOffFreq = 1
highCutOffFreq = 2
order = 2
ripple = 0.1
cascade = 5
IIRfilterlib.UpdateIIRFilter(iv.FilterBandType.FilterBand_LowPass, 1/dt, lowCutOffFreq, lowCutOffFreq, order, cascade,  iv.IIRFilterType.IIR_Bessel, ripple)
IIRfilterlib.Filter(data, data1)

plot2 = graph1.NewPlot("LP Filter")
plot2.SetLineStyle(iv.LineType.LineType_Solid)
plot2.SetLineColor(iv.MakeColor(0, 255, 0))
plot2.PlotXRange(0, dt)
plot2.PlotY(data1)

IIRfilterlib.UpdateIIRFilter(iv.FilterBandType.FilterBand_HighPass, 1/dt, highCutOffFreq, highCutOffFreq, order, cascade,  iv.IIRFilterType.IIR_Bessel, ripple)
IIRfilterlib.Filter(data, data1)

plot3 = graph1.NewPlot("HP Filter")
plot3.SetLineStyle(iv.LineType.LineType_Solid)
plot3.SetLineColor(iv.MakeColor(0, 0, 255))
plot3.PlotXRange(0, dt)
plot3.PlotY(data1)

IIRfilterlib.UpdateIIRFilter(iv.FilterBandType.FilterBand_BandPass, 1/dt, lowCutOffFreq, highCutOffFreq, order, cascade,  iv.IIRFilterType.IIR_Bessel, ripple)
IIRfilterlib.Filter(data, data1)

plot4 = graph1.NewPlot("BP Filter")
plot4.SetLineStyle(iv.LineType.LineType_Solid)
plot4.SetLineColor(iv.MakeColor(0, 255, 255))
plot4.PlotXRange(0, dt)
plot4.PlotY(data1)

IIRfilterlib.UpdateIIRFilter(iv.FilterBandType.FilterBand_BandStop, 1/dt, lowCutOffFreq, highCutOffFreq, order, cascade,  iv.IIRFilterType.IIR_Bessel, ripple)
IIRfilterlib.Filter(data, data1)

plot5 = graph1.NewPlot("BS Filter")
plot5.SetLineStyle(iv.LineType.LineType_Solid)
plot5.SetLineColor(iv.MakeColor(0, 0, 0))
plot5.PlotXRange(0, dt)
plot5.PlotY(data1)

#FIR Filter
FIRfilterlib = im.IPFIRFilter()

graph2.RemovePlot(-1)
plot1 = graph2.NewPlot("Chirp")
plot1.SetLineStyle(iv.LineType.LineType_Solid)
plot1.SetLineColor(iv.MakeColor(255, 0, 0))
plot1.PlotXRange(0, dt)
plot1.PlotY(data)

lowCutOffFreq = 1
highCutOffFreq = 2
numTap = 64
WindowType = iv.WindowType.WindowIdeal

FIRfilterlib.UpdateFIRFilter(iv.FilterBandType.FilterBand_LowPass, 1/dt, lowCutOffFreq, lowCutOffFreq, numTap, WindowType)
FIRfilterlib.Filter(data, data1)

plot2 = graph2.NewPlot("LP Filter")
plot2.SetLineStyle(iv.LineType.LineType_Solid)
plot2.SetLineColor(iv.MakeColor(0, 255, 0))
plot2.PlotXRange(0, dt)
plot2.PlotY(data1)

FIRfilterlib.UpdateFIRFilter(iv.FilterBandType.FilterBand_HighPass, 1/dt, highCutOffFreq, highCutOffFreq, numTap, WindowType)
FIRfilterlib.Filter(data, data1)

plot3 = graph2.NewPlot("HP Filter")
plot3.SetLineStyle(iv.LineType.LineType_Solid)
plot3.SetLineColor(iv.MakeColor(0, 0, 255))
plot3.PlotXRange(0, dt)
plot3.PlotY(data1)

FIRfilterlib.UpdateFIRFilter(iv.FilterBandType.FilterBand_BandPass, 1/dt, lowCutOffFreq, highCutOffFreq, numTap, WindowType)
FIRfilterlib.Filter(data, data1)

plot4 = graph2.NewPlot("BP Filter")
plot4.SetLineStyle(iv.LineType.LineType_Solid)
plot4.SetLineColor(iv.MakeColor(0, 255, 255))
plot4.PlotXRange(0, dt)
plot4.PlotY(data1)

FIRfilterlib.UpdateFIRFilter(iv.FilterBandType.FilterBand_BandStop, 1/dt, lowCutOffFreq, highCutOffFreq, numTap, WindowType)
FIRfilterlib.Filter(data, data1)

plot5 = graph2.NewPlot("BS Filter")
plot5.SetLineStyle(iv.LineType.LineType_Solid)
plot5.SetLineColor(iv.MakeColor(0, 0, 0))
plot5.PlotXRange(0, dt)
plot5.PlotY(data1)