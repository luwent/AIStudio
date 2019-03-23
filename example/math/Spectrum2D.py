import numpy as np
import IStudio as iv
import IMath as im

#get graphs
graph1 = iv.IPGraph("Plot-8")
graph1.SetCaption("Original Image")
graph2 = iv.IPGraph("Plot-9")
graph2.SetCaption("Spectrum")

#original waveform
nx = 200
ny = 200
m = 0
data = np.zeros((nx, ny))
for iy in range(ny):
    for  ix in range(nx):
        if(np.abs(ix - 100) < 5 and np.abs(iy - 100) < 5):
            data[iy][ix] = 0.8
        else:
            data[iy][ix] = 0

graph1.RemovePlot(-1)
plot1 = graph1.NewPlot("image")
plot1.SetPlotStyle(iv.PlotStyle.XYImage);
plot1.ImageRange(0, 1, 0, 1);
plot1.ImageColor(data);

nn = 1024
fftlib = im.IPFFTTransform(nn, iv.WindowType.WindowIdeal, iv.PaddingType.PaddingZero)
fftlib.SetupFFT2D(nn, nn,  iv.WindowType.WindowIdeal, iv.PaddingType.PaddingZero)
amp = np.zeros(nn)
phase = np.zeros(nn)
spectrum = np.zeros((nn, nn), dtype=np.complex128)
fftlib.FFT2D(data, spectrum);
fftlib.SwapQuadrant2D(spectrum);

plot2 = graph2.NewPlot("AMP")
plot2.SetPlotStyle(iv.PlotStyle.XYImage);
plot2.ImageRange(-0.50, 1.0 / nn , -0.5, 1.0 / nn);
plot2.ImageColor(np.abs(spectrum));
	
 