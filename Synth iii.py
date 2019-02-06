from scipy import signal as sg
import numpy as np
import sounddevice as sd
import keyboard
# from pynput import keyboard
# import time

sampleRate = 44100  # lowest indistinguishable sample rate
sawWidth = .75  # between 0 and 1, 1 is upwards saw, 0 is downwards saw, .5 is triangle wave
pulseWidth = .25  # between 0 and 1, higher width equals more positive time
noteLength = 350000
REST = 0


def sine(frequency, key):
    x = np.linspace(0, 2, sampleRate, endpoint=False)  # places individual samples of waveform
    y = np.sin(np.pi * frequency * x)  # creates fun part of wave
    sd.play(y, sampleRate)
    i = 0
    while i < length:
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

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):
            sine(C3, 'q')
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
        elif keyboard.is_pressed('^'):
            sine(REST)
        elif keyboard.is_pressed('@'):
            sine(REST)
        elif keyboard.is_pressed('esc'):
            break
        else:
            pass
    except:
        break

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed
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
#         elif keyboard.is_pressed('esc'):
#             break
#         else:
#             pass
#     except:
#         break

# (tab)1q2we4r5t6yu8i9op-[=](delete)\ two octaves
# shift octaves with arrow key

# sine(A4)
# square(A4, pulseWidth)
# tri(A4, sawWidth)
