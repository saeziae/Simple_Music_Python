#!/usr/bin/env python3
import pyaudio as пиаудио
import struct as структ
from time import sleep as спать
from random import random
from math import sin
import threading
###################################################
#####        ###            #######################
##### Author ### Promontana #######################
#####        ###            #######################
###################################################
#####        ###            #######################
##### Github ### saeziae    #######################
#####        ###            #######################
###################################################
#####         ###                                 #
##### License ### GNU General Public License v3.0 #
#####         ###                                 #
###################################################


ФОРМАТ = пиаудио.paInt16
КАНАЛЫ = 2
ЧАСТОТА = 24000

п = пиаудио.PyAudio()

рамка0 = []


def thr(Частота, бремя):
    спать(0.1)
    pass
    if Частота == 1:
        # спать(0.1)
        рамка = шум(440, бремя)
        рамка0.append(рамка)
    elif Частота != 0:
        рамка = частота(Частота, бремя)
        рамка0.append(рамка)
    else:
        # спать(0.1)
        данные = [0 for _ in range(int(ЧАСТОТА*бремя))]
        баитов = str(len(данные))
        данные = структ.pack(баитов + 'h', *данные)
        рамка0.append(данные)


def sqr(x):
    return (-1 if (x * 2) % 2 >= 1 else 1)


def tri(x):
    return abs((x * 2) % 2 - 1)


def шум(Частота: float = 440, бремя: float = 1):
    """生成噪音"""
    подсчет = int(ЧАСТОТА * бремя)
    данные = []
    for и in range(подсчет):
        а = ЧАСТОТА / Частота
        в = и / а
        г = в * 3.14159 * 2
        д = (sin(г) * 10000 + 2 * (random() - 0.5) * 20000) * (1-и/подсчет)
        #д = (random() - 0.5) * 30000 * (1-и/подсчет)
        е = int(д)
        данные.append(е)

    #данные+=[0 for _ in range(ЧАСТОТА//10)]
    баитов = str(len(данные))
    данные = структ.pack(баитов + 'h', *данные)

    return данные


def частота(Частота: float, бремя: float = 1):
    """生成頻率"""
    подсчет = int(ЧАСТОТА * бремя)

    данные = []
    for и in range(подсчет):
        а = ЧАСТОТА / Частота
        в = и / а
        г = в  # * 3.14159 * 2
        д = (sqr(г) * 0.5 +
             sqr(г*4/3) * 0.2 +
             tri(г*2/3) * 0.1 +
             tri(г*3/4) * 0.1 +
             sqr(г*3/2) * 0.1
             )*30000# * (1-и/подсчет)**2
        #д = (1 if (в * 2) % 2 >= 1 else -1) * 30000
        е = int(д)
        данные.append(е)

    данные += [0 for _ in range(ЧАСТОТА//10)]
    баитов = str(len(данные))
    данные = структ.pack(баитов + 'h', *данные)

    return данные


def музициробвать(Частота: float, бремя: float):
    if Частота == 1:
        рамка = шум(440, бремя)
        поток.write(рамка)
    elif Частота != 0:
        # if бремя <= 1.5:
        рамка = частота(Частота, бремя)
        поток.write(рамка)
        спать(0.05)
        # else:
        #    for _ in range(int(бремя)*2):
        #        рамка = частота(Частота, 0.5)
        #        поток.write(рамка)
        #    спать(0.1)
    else:
        спать(бремя)


тон = {
    "C0": 16.35,
    "#C0": 17.32,
    "bD0": 17.32,
    "D0": 18.35,
    "#D0": 19.45,
    "bE0": 19.45,
    "E0": 20.60,
    "F0": 21.83,
    "#F0": 23.12,
    "bG0": 23.12,
    "G0": 24.50,
    "#G0": 25.96,
    "bA0": 25.96,
    "A0": 27.50,
    "#A0": 29.14,
    "bB0": 29.14,
    "B0": 30.87,
    "C1": 32.70,
    "#C1": 34.65,
    "bD1": 34.65,
    "D1": 36.71,
    "#D1": 38.89,
    "bE1": 38.89,
    "E1": 41.20,
    "F1": 43.65,
    "#F1": 46.25,
    "bG1": 46.25,
    "G1": 49.00,
    "#G1": 51.91,
    "bA1": 51.91,
    "A1": 55.00,
    "#A1": 58.27,
    "bB1": 58.27,
    "B1": 61.74,
    "C2": 65.41,
    "#C2": 69.30,
    "bD2": 69.30,
    "D2": 73.42,
    "#D2": 77.78,
    "bE2": 77.78,
    "E2": 82.41,
    "F2": 87.31,
    "#F2": 92.50,
    "bG2": 92.50,
    "G2": 98.00,
    "#G2": 103.83,
    "bA2": 103.83,
    "A2": 110.00,
    "#A2": 116.54,
    "bB2": 116.54,
    "B2": 123.47,
    "C3": 130.81,
    "#C3": 138.59,
    "bD3": 138.59,
    "D3": 146.83,
    "#D3": 155.56,
    "bE3": 155.56,
    "E3": 164.81,
    "F3": 174.61,
    "#F3": 185.00,
    "bG3": 185.00,
    "G3": 196.00,
    "#G3": 207.65,
    "bA3": 207.65,
    "A3": 220.00,
    "#A3": 233.08,
    "bB3": 233.08,
    "B3": 246.94,
    "C4": 261.63,
    "#C4": 277.18,
    "bD4": 277.18,
    "D4": 293.66,
    "#D4": 311.13,
    "bE4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "#F4": 369.99,
    "bG4": 369.99,
    "G4": 392.00,
    "#G4": 415.30,
    "bA4": 415.30,
    "A4": 440.00,
    "#A4": 466.16,
    "bB4": 466.16,
    "B4": 493.88,
    "C5": 523.25,
    "#C5": 554.37,
    "bD5": 554.37,
    "D5": 587.33,
    "#D5": 622.25,
    "bE5": 622.25,
    "E5": 659.25,
    "F5": 698.46,
    "#F5": 739.99,
    "bG5": 739.99,
    "G5": 783.99,
    "#G5": 830.61,
    "bA5": 830.61,
    "A5": 880.00,
    "#A5": 932.33,
    "bB5": 932.33,
    "B5": 987.77,
    "C6": 1046.50,
    "#C6": 1108.73,
    "bD6": 1108.73,
    "D6": 1174.66,
    "#D6": 1244.51,
    "bE6": 1244.51,
    "E6": 1318.51,
    "F6": 1396.91,
    "#F6": 1479.98,
    "bG6": 1479.98,
    "G6": 1567.98,
    "#G6": 1661.22,
    "bA6": 1661.22,
    "A6": 1760.00,
    "#A6": 1864.66,
    "bB6": 1864.66,
    "B6": 1975.53,
    "C7": 2093.00,
    "0": 0,
    "X": 1,
}

список = [
    ("X", 1),
    ("X", 1),
    ("X", 1),
    ("X", 1),
]
УВМ = 40

поток = п.open(format=ФОРМАТ, channels=КАНАЛЫ, rate=ЧАСТОТА, output=True)
with open("music.txt", "r") as f:
    список_р = f.readlines()
    for и in список_р:
        и = и.split(" ")
        список.append((и[0], и[1].replace("\n", "")))

# музициробвать(тон[и[0]], float(и[1])/УВМ*60)
###################################################################
threading.Thread(target=thr, args=(
    тон[список[0][0]], 60*float(список[0][1])/УВМ)).start()
спать(1)
Len = 0
for и in range(len(список)-1):
    # спать(0.1)
    threading.Thread(target=thr, args=(
        тон[список[и+1][0]], 60*float(список[и+1][1])/УВМ)).start()
    while len(рамка0) <= Len:
        # wait for generating wave
        pass
    else:
        print(список[и])
        поток.write(рамка0[-1])
        Len += 1
while len(рамка0) <= Len:
    # wait for generating wave
    pass
else:
    поток.write(рамка0[-1])
###################################################################
поток.stop_stream()
поток.close()
п.terminate()
