#########################################################################
### This program is a digital synthesizer with super fun things in it ###
#########################################################################

from scipy import signal as sg
import matplotlib.pyplot as plt
import numpy as np
import struct
import soundfile as sf
import sounddevice as sd
import pyglet

### The following are variables for all waveforms

sampleRate = 44100  # lowest indistinguishable sample rate
bitDepth = 16
bitRate = sampleRate * bitDepth
frequency = 440  # frequency of A4 in Hz
amplitude = 20  # volume

### The following creates a sinusoidal wave and writes it to a file

x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
y = amplitude * np.sin(np.pi * frequency * x)  # creates fun part of wave
# plt.plot(x, y)  # plots it for visual interpretation
# plt.xlabel('frequency(n)')  # labels the graphic
# plt.ylabel('voltage(V)')    # labels the graphic
# plt.show()  # prints graph
sd.play(y, 44100)

while True:
    print("What?!!?!")

# sineFile = open('sine.wav', 'wb')   # opens a binary wave file
# for i in y:
#     print i # displays each sample placement
#     sineFile.write(struct.pack('b', i))    # writes each sample to binary file
# sineFile.close()   # closes file


# wave = pyglet.media.load('/Users/panga/PycharmProjects/untitled/sine.wav', 'rb')
# wave.play()
# pyglet.app.run()
#
# data = wave.readframes(wave.getnframes())
# sig = np.frombuffer(data, dtype='<i2').reshape(-1, wave.getnchannels())
#
# data, fs = sf.read('sineFile.aiff')
# sd.play(data, fs, blocking=True)
#
# ### The following creates a sawtooth wave and writes it to a file
#
# sawWidth = 1   # between 0 and 1, 1 is up, 0 is down, .5 is triangle wave
# x = np.linspace(0, time, sampleRate)   # places individual samples of waveform
# y = amplitude * sg.sawtooth(np.pi * frequency * x, sawWidth)  # creates fun part of wave
# plt.plot(x, y)  # plots it for visual interpretation
# plt.xlabel('frequency(n)')  # labels the graphic
# plt.ylabel('voltage(V)')    # labels the graphic
# plt.show()  # prints graph
# sawFile = open('saw.aiff', 'wb')   # opens a binary wave file
# for i in y:
#     print i # displays each sample placement
#     sawFile.write(struct.pack('b', i))    # writes each sample to binary file
# sawFile.close()   # closes file
#
# ### The following creates a square wave and writes it to a file
#
# pulseWidth = .5     # between 0 and 1, higher width equals more positive time
# x = np.linspace(0, time, sampleRate)   # places individual samples of waveform
# y = amplitude * sg.square(np.pi * frequency * x, pulseWidth)  # creates fun part of wave
# plt.plot(x, y)  # plots it for visual interpretation
# plt.xlabel('frequency(n)')  # labels the graphic
# plt.ylabel('voltage(V)')    # labels the graphic
# plt.show()  # prints graph
# squareFile = open('square.aiff', 'wb')   # opens a binary wave file
# for i in y:
#     print i # displays each sample placement
#     squareFile.write(struct.pack('b', i))    # writes each sample to binary file
# squareFile.close()   # closes file
#
#
# ### Failed attempt
#
# import math
# import pyaudio
#
# PyAudio = pyaudio.PyAudio     #initialize pyaudio
#
# numberOfFrames = int(sampleRate * time)
# restOfFrames = numberOfFrames % sampleRate
# waveData = ''
#
# for i in y:
#     waveData = waveData+int(i)
# for i in range(restOfFrames):
#     waveData = waveData+chr(128)
#
# p = PyAudio()
# stream = p.open(format = p.get_format_from_width(1),
#                 channels = 1,
#                 rate = sampleRate,
#                 output = True)
#
# stream.write(waveData)
# stream.stop_stream()
# stream.close()
# p.terminate()




