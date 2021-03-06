## TODO: fix next key press glitch
## TODO: fix suppresion

from scipy import signal as sg
import numpy as np
import sounddevice as sd
import keyboard as kb
import sys


sampleRate = 44100  # lowest indistinguishable sample rate
sawWidth = .75  # between 0 and 1, 1 is upwards saw, 0 is downwards saw, .5 is triangle wave
pulseWidth = .25  # between 0 and 1, higher width equals more positive time
octaveIndex = 4     # between 0 and 9, higher number corresponds to lower octave
octaveDisplay = 6   # reverse of coded octave
waveformIndex = 0   # between 0 and 2, 0 is sine, 1 is tri, 2 is pulse
noteIndex = 48
notesList = [16.35,    # C0
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
    7902.13,    # B8
    0.00]       # Rest
currentNote = 0
go = True

def Sine(frequency):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = np.sin(np.pi * frequency * x)  # creates fun part of wave
    sd.play(y, sampleRate, loop=True)  # sends wave to speakers


def Tri(frequency, width):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = sg.sawtooth(np.pi * frequency * x, width)  # creates fun part of wave
    sd.play(y, sampleRate)  # sends wave to speakers


def Square(frequency, width):
    x = np.linspace(0, 2, sampleRate)  # places individual samples of waveform
    y = sg.square(np.pi * frequency * x, width)  # creates fun part of wave
    sd.play(y, sampleRate)  # sends wave to speakers


def WaveformSelect(key):
    global waveformIndex
    if key == 'last':
        waveformIndex = waveformIndex - 1
        if waveformIndex == - 1:
            waveformIndex = 2
    if key == 'next':
        waveformIndex = waveformIndex + 1
        if waveformIndex == 3:
            waveformIndex = 0
    print('')
    if waveformIndex == 0:
        print("Current waveform:\tSinusoidal")
    elif waveformIndex == 1:
        print("Current waveform:\tTriangle")
    elif waveformIndex == 2:
        print("Current waveform:\tSquare")


def OctaveSelect(key):
    global octaveIndex
    global noteIndex
    if key == 'up':
        octaveIndex = octaveIndex - 1
        if octaveIndex == 0:
            octaveIndex = 1
    if key == 'down':
        octaveIndex = octaveIndex + 1
        if octaveIndex == 10:
            octaveIndex = 9
    noteIndex = (octaveIndex * 12)
    print('')
    DisplayOctave()


def DisplayOctave():
    global octaveDisplay
    if octaveIndex == 5:
        octaveDisplay = 5
    if octaveIndex < 5:
        difference = 5 - octaveIndex
        octaveDisplay = octaveIndex + (difference * 2)
    if octaveIndex > 5:
        difference = octaveIndex - 5
        octaveDisplay = octaveIndex - (difference * 2)
    print("Current octave:\t\t" + str(octaveDisplay))


def PulseMod(key):
    global pulseWidth
    if key == 'down':
        pulseWidth = pulseWidth - .025
        if pulseWidth < 0:
            pulseWidth = 0
    if key == 'up':
        pulseWidth = pulseWidth + .025
        if pulseWidth > 1:
            pulseWidth = 1
    print('')
    print("Current pulse width:\t" + str(pulseWidth))


def SawMod(key):
    global sawWidth
    if key == 'down':
        sawWidth = sawWidth - .025
        if sawWidth < 0:
            sawWidth = 0
    if key == 'up':
        sawWidth = sawWidth + .025
        if sawWidth > 1:
            sawWidth = 1
    print('')
    print("Current saw width:\t" + str(sawWidth))


def SendSound(note):
    index = note - noteIndex
    if waveformIndex == 0:
        Sine(notesList[index])
    elif waveformIndex == 1:
        Tri(notesList[index], sawWidth)
    elif waveformIndex == 2:
        Square(notesList[index], pulseWidth)


def KeyPress(nothing):
    global go
    if go:
        SendSound(currentNote)
        go = False


def KeyRelease(nothing):
    global noteIndex, go
    noteIndex = 12
    SendSound(120)
    noteIndex = (octaveIndex * 12)
    go = True


def StartPress(note):
    global currentNote
    currentNote = note
    kb.on_press(KeyPress)


def DisplayCurrent():
    print('')
    print('')
    print('')
    print('')
    if waveformIndex == 0:
        print("Current waveform:\tSinusoidal")
        DisplayOctave()
    if waveformIndex == 1:
        print("Current waveform:\tTriangle")
        print("Current saw width:\t" + str(sawWidth))
        DisplayOctave()
    if waveformIndex == 2:
        print("Current waveform:\tSquare")
        print("Current pulse width:\t" + str(pulseWidth))
        DisplayOctave()


def DieProgramDie():
    sd.stop()
    print('')
    print('')
    print('')
    print('Thanks for making some dumb music, Panga!')


kb.add_hotkey('s', OctaveSelect, args=['up'])
kb.add_hotkey('x', OctaveSelect, args=['down'])
kb.add_hotkey('z', WaveformSelect, args=['last'])
kb.add_hotkey('c', WaveformSelect, args=['next'])
kb.add_hotkey('v', SawMod, args=['down'])
kb.add_hotkey('b', SawMod, args=['up'])
kb.add_hotkey('n', PulseMod, args=['down'])
kb.add_hotkey('m', PulseMod, args=['up'])
kb.add_hotkey('`', DisplayCurrent)
kb.add_hotkey('q', StartPress, args=[108])  # corresponds with C
kb.on_release_key('q', KeyRelease)
kb.add_hotkey('2', StartPress, args=[109])  # corresponds with CsDb
kb.on_release_key('2', KeyRelease)
kb.add_hotkey('w', StartPress, args=[110])  # corresponds with D
kb.on_release_key('w', KeyRelease)
kb.add_hotkey('3', StartPress, args=[111])  # corresponds with DsEb
kb.on_release_key('3', KeyRelease)
kb.add_hotkey('e', StartPress, args=[112])  # corresponds with E
kb.on_release_key('e', KeyRelease)
kb.add_hotkey('r', StartPress, args=[113])  # corresponds with F
kb.on_release_key('r', KeyRelease)
kb.add_hotkey('5', StartPress, args=[114])  # corresponds with FsGb
kb.on_release_key('5', KeyRelease)
kb.add_hotkey('t', StartPress, args=[115])  # corresponds with G
kb.on_release_key('t', KeyRelease)
kb.add_hotkey('6', StartPress, args=[116])  # corresponds with GsAb
kb.on_release_key('6', KeyRelease)
kb.add_hotkey('y', StartPress, args=[117])  # corresponds with A
kb.on_release_key('y', KeyRelease)
kb.add_hotkey('7', StartPress, args=[118])  # corresponds with AsBb
kb.on_release_key('7', KeyRelease)
kb.add_hotkey('u', StartPress, args=[119])  # corresponds with B
kb.on_release_key('u', KeyRelease)
kb.add_hotkey('i', StartPress, args=[120])  # corresponds with C
kb.on_release_key('i', KeyRelease)
kb.add_hotkey('esc', DieProgramDie)

kb.wait('esc')
