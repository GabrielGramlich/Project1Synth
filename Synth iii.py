from scipy import signal as sg
import numpy as np
import sounddevice as sd
import keyboard
# from pynput import keyboard
# import time

sampleRate = 44100  # lowest indistinguishable sample rate
sawWidth = .75  # between 0 and 1, 1 is upwards saw, 0 is downwards saw, .5 is triangle wave
pulseWidth = .25  # between 0 and 1, higher width equals more positive time
noteLength = 10000000
REST = 0
C0 = 16.35
Cs0Db0 = 17.32
D0 = 18.35
Ds0Eb0 = 19.45
E0 = 20.60
F0 = 21.83
Fs0Gb0 = 23.12
G0 = 24.50
Gs0Ab0 = 25.96
A0 = 27.50
As0Bb0 = 29.14
B0 = 30.87
C1 = 32.70
Cs1Db1 = 34.65
D1 = 36.71
Ds1Eb1 = 38.89
E1 = 41.20
F1 = 43.65
Fs1Gb1 = 46.25
G1 = 49.00
Gs1Ab1 = 51.91
A1 = 55.00
As1Bb1 = 58.27
B1 = 61.74
C2 = 65.41
Cs2Db2 = 69.30
D2 = 73.42
Ds2Eb2 = 77.78
E2 = 82.41
F2 = 87.31
Fs2Gb2 = 92.50
G2 = 98.00
Gs2Ab2 = 103.83
A2 = 110.00
As2Bb2 = 116.54
B2 = 123.47
C3 = 130.81
Cs3Db3 = 138.59
D3 = 146.83
Ds3Eb3 = 155.56
E3 = 164.81
F3 = 174.61
Fs3Gb3 = 185.00
G3 = 196.00
Gs3Ab3 = 207.65
A3 = 220.00
As3Bb3 = 233.08
B3 = 246.94
C4 = 261.63
Cs4Db4 = 277.18
D4 = 293.66
Ds4Eb4 = 311.13
E4 = 329.63
F4 = 349.23
Fs4Gb4 = 369.99
G4 = 392.00
Gs4Ab4 = 415.30
A4 = 440.00
As4Bb4 = 466.16
B4 = 493.88
C5 = 523.25
Cs5Db5 = 554.37
D5 = 587.33
Ds5Eb5 = 622.25
E5 = 659.25
F5 = 698.46
Fs5Gb5 = 739.99
G5 = 783.99
Gs5Ab5 = 830.61
A5 = 880.00
As5Bb5 = 932.33
B5 = 987.77
C6 = 1046.50
Cs6Db6 = 1108.73
D6 = 1174.66
Ds6Eb6 = 1244.51
E6 = 1318.51
F6 = 1396.91
Fs6Gb6 = 1479.98
G6 = 1567.98
Gs6Ab6 = 1661.22
A6 = 1760.00
As6Bb6 = 1864.66
B6 = 1975.53
C7 = 2093.00
Cs7Db7 = 2217.46
D7 = 2349.32
Ds7Eb7 = 2489.02
E7 = 2637.02
F7 = 2793.83
Fs7Gb7 = 2959.96
G7 = 3135.96
Gs7Ab7 = 3322.44
A7 = 3520.00
As7Bb7 = 3729.31
B7 = 3951.07
C8 = 4186.01
Cs8Db8 = 4434.92
D8 = 4698.63
Ds8Eb8 = 4978.03
E8 = 5274.04
F8 = 5587.65
Fs8Gb8 = 5919.91
G8 = 6271.93
Gs8Ab8 = 6644.88
A8 = 7040.00
As8Bb8 = 7458.62
B8 = 7902.13


def sine(frequency):
    x = np.linspace(0, 2, sampleRate, endpoint=False)  # places individual samples of waveform
    y = np.sin(np.pi * frequency * x)  # creates fun part of wave
    sd.play(y, sampleRate)
    i = 0
    while i < noteLength:
        i = i + 1


def tri(frequency, width):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = sg.sawtooth(np.pi * frequency * x, width)  # creates fun part of wave
    sd.play(y, sampleRate)  # Sends wave to speakers
    i = 0
    while i < noteLength:
        i = i + 1


def square(frequency, width):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = sg.square(np.pi * frequency * x, width)  # creates fun part of wave
    sd.play(y, sampleRate)  # Sends wave to speakers
    i = 0
    while i < noteLength:
        i = i + 1


# def callb(key):     # what to do on key-release
#     ti1 = str(time.time() - t)[0:5]     # converting float to str, slicing the float
#     print("The key", key, " is pressed for", ti1, 'seconds')
#     return False    # stop detecting more key-releases
#
#
# def callb1(key):    # what to do on key-press
#     return False    # stop detecting more key-presses
#
#
# with keyboard.Listener(on_press=callb1) as listener1:     # setting code for listening key-press
#     listener1.join()
#
# t = time.time()     # reading time in sec
#
# with keyboard.Listener(on_release=callb) as listener:     # setting code for listening key-release
#     listener.join()

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):
#             sine(C3)
#         elif keyboard.is_pressed('2'):
#             sine(Cs3Db3)
#         elif keyboard.is_pressed('w'):
#             sine(D3)
#         elif keyboard.is_pressed('3'):
#             sine(Ds3Eb3)
#         elif keyboard.is_pressed('e'):
#             sine(E3)
#         elif keyboard.is_pressed('r'):
#             sine(F3)
#         elif keyboard.is_pressed('5'):
#             sine(Fs3Gb3)
#         elif keyboard.is_pressed('t'):
#             sine(G3)
#         elif keyboard.is_pressed('6'):
#             sine(Gs3Ab3)
#         elif keyboard.is_pressed('y'):
#             sine(A3)
#         elif keyboard.is_pressed('7'):
#             sine(As3Bb3)
#         elif keyboard.is_pressed('u'):
#             sine(B3)
#         elif keyboard.is_pressed('i'):
#             sine(C4)
#         elif keyboard.is_pressed('^'):
#             sine(REST)
#         elif keyboard.is_pressed('@'):
#             sine(REST)
#         elif keyboard.is_pressed('esc'):
#             break
#         else:
#             pass
#     except:
#         break

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            sine(C3)
        elif keyboard.is_pressed('2'):
            sine(Cs3Db3)
        elif keyboard.is_pressed('w'):
            sine(D3)
        elif keyboard.is_pressed('3'):
            sine(Ds3Eb3)
        elif keyboard.is_pressed('e'):
            sine(E3)
        elif keyboard.is_pressed('r'):
            sine(F3)
        elif keyboard.is_pressed('5'):
            sine(Fs3Gb3)
        elif keyboard.is_pressed('t'):
            sine(G3)
        elif keyboard.is_pressed('6'):
            sine(Gs3Ab3)
        elif keyboard.is_pressed('y'):
            sine(A3)
        elif keyboard.is_pressed('7'):
            sine(As3Bb3)
        elif keyboard.is_pressed('u'):
            sine(B3)
        elif keyboard.is_pressed('i'):
            sine(C4)
        elif keyboard.is_pressed('esc'):
            break
        else:
            pass
    except:
        break

# (tab)1q2we4r5t6yu8i9op-[=](delete)\ two octaves
# shift octaves with arrow key

# sine(A4)
# square(A4, pulseWidth)
# tri(A4, sawWidth)
