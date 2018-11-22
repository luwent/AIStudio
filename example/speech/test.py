#deep speed for pytorch
#revised based on https://github.com/SeanNaren/deepspeech.pytorch
#from https://github.com/SeanNaren/deepspeech.pytorch/releases to download pretrained model ibrispeech_pretrained.pth 

import numpy as np
from torch.autograd import Variable
import torch
from decoder import GreedyDecoder
from model import DeepSpeech
import IStudio as iv
import json

studio = iv.AIStudio("pytorch")

filename = inspect.getframeinfo(inspect.currentframe()).filename
model_path     = os.path.dirname(os.path.abspath(filename))
model_file = model_path + "\\librispeech_pretrained.pth"
cuda = "store_true"
batch_size = 20
num_workers = 4
decoder = "greedy"
verbose = "store_true"
top_paths = 1
beam_width = 10
lm_path = None
alpha = 0.8
beta = 1
cutoff_top_n = 40
cutoff_prob = 1
lm_workers = 1

model = DeepSpeech.load_model(model_file)
model.eval()

labels = DeepSpeech.get_labels(model)
audio_conf = DeepSpeech.get_audio_conf(model)

if decoder == "beam":
    from decoder import BeamCTCDecoder

    decoder = BeamCTCDecoder(labels, lm_path=lm_path, alpha=alpha, beta=beta,
                             cutoff_top_n=cutoff_top_n, cutoff_prob=cutoff_prob,
                             beam_width=beam_width, num_processes=lm_workers)
elif decoder == "greedy":
    decoder = GreedyDecoder(labels, blank_index=labels.index('_'))
else:
    decoder = None
target_decoder = GreedyDecoder(labels, blank_index=labels.index('_'))

tranform = iv.IPFFTTransform(1024, 0, 0)
tranform.SetupSTFFT(1024, 128)

def LoadAudioData():
    ass = iv.ShortVector(1)
    n, sr, cc = studio.LoadAudio(model_path + "\\yes.wav",  ass)
    spectrum = iv.ComplexVector(10)
    r = tranform.STFFT(ass, 128, 161, True, spectrum)
    aspectrum = studio.ToNumpy(spectrum)
    spect = np.absolute(aspectrum)
    spect = np.log1p(spect)
    spect = spect.reshape(161, -1)
    spect = torch.FloatTensor(spect)
    mean = spect.mean()
    std = spect.std()
    spect.add_(-mean)
    spect.div_(std)
    return spect

def GetAudioData():
    ass = iv.ShortVector(1)
    studio.GetAudioStream("Record", ass, 5.0, 16000.0, 1)
    #studio.WriteAudio("c:\\data\\test.wav", ass, 16000.0, 1)
    spectrum = iv.ComplexVector(10)
    r = tranform.STFFT(ass, 128, 161, True, spectrum)
    aspectrum = studio.ToNumpy(spectrum)
    spect = np.absolute(aspectrum)
    spect = np.log1p(spect)
    spect = spect.reshape(161, -1)
    spect = torch.FloatTensor(spect)
    mean = spect.mean()
    std = spect.std()
    spect.add_(-mean)
    spect.div_(std)
    return spect
    
spect = LoadAudioData().contiguous()
spect = spect.view(1, 1, spect.size(0), spect.size(1))
out = model(Variable(spect, volatile=True))
decoded_output, decoded_offsets = decoder.decode(out.data)
print(decoded_output)

while(1):
    if(studio.GetKeyState(0x1B) < 0):
        break      
    print("Please speak:")
    spect = GetAudioData().contiguous()
    spect = spect.view(1, 1, spect.size(0), spect.size(1))
    out = model(Variable(spect, volatile=True))
    decoded_output, decoded_offsets = decoder.decode(out.data)
    print(decoded_output)
