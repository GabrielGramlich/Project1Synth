from scipy import signal as sg
import numpy as np
import sounddevice as sd
import keyboard

sampleRate = 44100  # lowest indistinguishable sample rate
sawWidth = .75  # between 0 and 1, 1 is upwards saw, 0 is downwards saw, .5 is triangle wave
pulseWidth = .25  # between 0 and 1, higher width equals more positive time
noteLength = 350000     # MAX 25,000,000
octaveIndex = 0
waveformIndex = 0
REST = 0
notesArray = [16.35,    # C0
    17.32,  # Cs0Db0
    18.35,  # D0
    19.45,  # Ds0Eb0
    20.60,  # E0
    21.83,  # F0
    23.12,  # Fs0Gb0
    24.50,  # G0
    25.96,  # Gs0Ab0
    27.50,  # A0
    29.14,  # As0Bb0
    30.87,  # B0
    32.70,  # C1
    34.65,  # Cs1Db1
    36.71,  # D1
    38.89,  # Ds1Eb1
    41.20,  # E1
    43.65,  # F1
    46.25,  # Fs1Gb1
    49.00,  # G1
    51.91,  # Gs1Ab1
    55.00,  # A1
    58.27,  # As1Bb1
    61.74,  # B1
    65.41,  # C2
    69.30,  # Cs2Db2
    73.42,  # D2
    77.78,  # Ds2Eb2
    82.41,  # E2
    87.31,  # F2
    92.50,  # Fs2Gb2
    98.00,  # G2
    103.83,     # Gs2Ab2
    110.00,     # A2
    116.54,     # As2Bb2
    123.47,     # B2
    130.81,     # C3
    138.59,     # Cs3Db3
    146.83,     # D3
    155.56,     # Ds3Eb3
    164.81,     # E3
    174.61,     # F3
    185.00,     # Fs3Gb3
    196.00,     # G3
    207.65,     # Gs3Ab3
    220.00,     # A3
    233.08,     # As3Bb3
    246.94,     # B3
    261.63,     # C4
    277.18,     # Cs4Db4
    293.66,     # D4
    311.13,     # Ds4Eb4
    329.63,     # E4
    349.23,     # F4
    369.99,     # Fs4Gb4
    392.00,     # G4
    415.30,     # Gs4Ab4
    440.00,     # A4
    466.16,     # As4Bb4
    493.88,     # B4
    523.25,     # C5
    554.37,     # Cs5Db5
    587.33,     # D5
    622.25,     # Ds5Eb5
    659.25,     # E5
    698.46,     # F5
    739.99,     # Fs5Gb5
    783.99,     # G5
    830.61,     # Gs5Ab5
    880.00,     # A5
    932.33,     # As5Bb5
    987.77,     # B5
    1046.50,    # C6
    1108.73,    # Cs6Db6
    1174.66,    # D6
    1244.51,    # Ds6Eb6
    1318.51,    # E6
    1396.91,    # F6
    1479.98,    # Fs6Gb6
    1567.98,    # G6
    1661.22,    # Gs6Ab6
    1760.00,    # A6
    1864.66,    # As6Bb6
    1975.53,    # B6
    2093.00,    # C7
    2217.46,    # Cs7Db7
    2349.32,    # D7
    2489.02,    # Ds7Eb7
    2637.02,    # E7
    2793.83,    # F7
    2959.96,    # Fs7Gb7
    3135.96,    # G7
    3322.44,    # Gs7Ab7
    3520.00,    # A7
    3729.31,    # As7Bb7
    3951.07,    # B7
    4186.01,    # C8
    4434.92,    # Cs8Db8
    4698.63,    # D8
    4978.03,    # Ds8Eb8
    5274.04,    # E8
    5587.65,    # F8
    5919.91,    # Fs8Gb8
    6271.93,    # G8
    6644.88,    # Gs8Ab8
    7040.00,    # A8
    7458.62,    # As8Bb8
    7902.13]    # B8

def Sine(frequency):
    x = np.linspace(0, 2, sampleRate, endpoint=False)  # places individual samples of waveform
    y = np.sin(np.pi * frequency * x)  # creates fun part of wave
    sd.play(y, sampleRate)
    i = 0
    while i < noteLength:
        i = i + 1


def Tri(frequency, width):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = sg.sawtooth(np.pi * frequency * x, width)  # creates fun part of wave
    sd.play(y, sampleRate)  # Sends wave to speakers
    i = 0
    while i < noteLength:
        i = i + 1


def Square(frequency, width):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = sg.square(np.pi * frequency * x, width)  # creates fun part of wave
    sd.play(y, sampleRate)  # Sends wave to speakers
    i = 0
    while i < noteLength:
        i = i + 1


def WaveformSelect():
    if keyboard.is_pressed('z'):    # left
        waveformIndex = waveformIndex - 1
        if waveformIndex == - 1:
            waveformIndex = 2
    if keyboard.is_pressed('c'):    # right 0
        waveformIndex = waveformIndex + 1
        if waveformIndex == 3:
            waveformIndex = 0


def OctaveSelect():
    if keyboard.is_pressed('s'):    # up
        octaveIndex = octaveIndex - 1
        if octaveIndex == 0:
            octaveIndex = 1
    if keyboard.is_pressed('x'):    # down
        octaveIndex = octaveIndex + 1
        if octaveIndex == 10:
            octaveIndex = 9


def PusleMod():
    global pulseWidth
    if keyboard.is_pressed('v'):
        pulseWidth = pulseWidth - .05
        if pulseWidth < 0:
            pulseWidth = 0
    if keyboard.is_pressed('b'):
        pulseWidth = pulseWidth + .05
        if pulseWidth > 1:
            pulseWidth = 1


def SawMod():
    global sawWidth
    if keyboard.is_pressed('n'):
        sawWidth = sawWidth - .05
        if sawWidth < 0:
            sawWidth = 0
    if keyboard.is_pressed('m'):
        sawWidth = sawWidth + .05
        if sawWidth > 1:
            sawWidth = 1


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):    # C
            if waveformIndex == 0:
                Sine(noteLength[octaveIndex])
            elif waveformIndex == 1:
                Tri(noteLength[octaveIndex])
            elif waveformIndex == 2:
                Square(noteLength[octaveIndex])
        elif keyboard.is_pressed('2'):  # CsDb
        elif keyboard.is_pressed('w'):  # D
        elif keyboard.is_pressed('3'):  # DsEb
        elif keyboard.is_pressed('e'):  # E
        elif keyboard.is_pressed('r'):  # F
        elif keyboard.is_pressed('5'):  # FsGb
        elif keyboard.is_pressed('t'):  # G
        elif keyboard.is_pressed('6'):  # GsAb
        elif keyboard.is_pressed('y'):  # A
        elif keyboard.is_pressed('7'):  # AsBb
        elif keyboard.is_pressed('u'):  # B
        elif keyboard.is_pressed('i'):  # C
        elif keyboard.is_pressed('esc'):
            break
        else:
            pass
    except:
        break
