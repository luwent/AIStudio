import numpy as np
import IStudio as iv
import IMath as im

#get graphs
graph1 = iv.IPGraph("Plot-6")
graph1.SetCaption("Spectrum Amplitude")
graph2 = iv.IPGraph("Plot-7")
graph1.SetCaption("Spectrum Phase")

functionlib = im.IPFunctions()

#original waveform
n = 4000
dt = 0.005
data = np.zeros(n)
data1 = np.zeros(n)
functionlib.ChirpWave(data, 1, 0, 5, 1/dt)

fftlib = im.IPFFTTransform(4096, iv.WindowType.WindowIdeal, iv.PaddingType.PaddingZero)
amp = np.zeros(4096)
phase = np.zeros(4096)
r, df = fftlib.AmpPhaseSpectrum(data, amp, phase, True, dt)

graph1.RemovePlot(-1)
plot1 = graph1.NewPlot("AMP")
plot1.SetLineStyle(iv.LineType.LineType_Solid)
plot1.SetLineColor(iv.MakeColor(255, 0, 0))
plot1.PlotXRange(0, df)
plot1.PlotY(amp)

graph2.RemovePlot(-1)
plot1 = graph2.NewPlot("PHA")
plot1.SetLineStyle(iv.LineType.LineType_Solid)
plot1.SetLineColor(iv.MakeColor(255, 0, 0))
plot1.PlotXRange(0, df)
plot1.PlotY(phase)