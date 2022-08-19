import numpy as np
import math
import matplotlib.pyplot as plt
import wave, struct, math, random


def plot_one_period_sine(sample_rate,amplitude):
    time = np.arange(0,2*math.pi,1.0/sample_rate)
    samples = amplitude * 32767.0 * np.sin(time)
    plt.plot(time,samples)
    plt.show()

def make_sine_audio_file(filename="sin.wav", sampleRate=44100.0, duration=1.0, frequency=440.0, amplitude=0.8):
    sampleRate = 44100.0 # hertz
    obj = wave.open(filename,'w')
    obj.setnchannels(1) # mono
    obj.setsampwidth(2)
    obj.setframerate(sampleRate)
    for i in range (0, int(duration * sampleRate)):
       time = i/sampleRate
       value = amplitude * 32767.0 * math.sin(2.0 * math.pi * frequency * time)
       data = struct.pack('<h', int(value))
       obj.writeframesraw( data )
    obj.close()        

