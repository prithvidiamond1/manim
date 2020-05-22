
from manimlib.imports import *

import soundfile as sf
import sounddevice as sd
import math

import numpy as np
import random

freqrange = 255
chunkrange = 50
framerate = 60

songname = "deadmau5 - Ghosts N Stuff"

data, samplerate = sf.read('deadmau5 - Ghosts N Stuff.wav', dtype='int16')

frequencies = np.abs(np.fft.fft(data))

frequencies = np.max(frequencies, axis=1)

frequencies /= np.max(frequencies)
frequencies *= freqrange

# frequencies = np.concatenate((frequencies, np.zeros((((math.floor(len(frequencies)/samplerate)+1)*samplerate)-len(frequencies)))))

samples = len(frequencies)

chunks = np.array_split(frequencies, int((samples/samplerate)*framerate))

tempchunks = []
for chunk in chunks:
    chunksplit = np.array_split(chunk, chunkrange)
    tempchunk = []
    for array in chunksplit:
        tempchunk.append(np.sqrt(np.mean(np.square(array))))
    tempchunks.append(np.array(tempchunk))
chunks = np.array(tempchunks)


class bars(Scene):
    def construct(self):
        w = 0.185
        color = BLUE_D

        title = Text(songname, font="DM Sans Bold")
        title.move_to((((FRAME_HEIGHT/4)+1)*DOWN)+((FRAME_WIDTH/4)*LEFT))
        self.play(Write(title))

        line = Line(start=((FRAME_WIDTH/2)*LEFT), end=((FRAME_WIDTH/2)*RIGHT), buff=0.4)
        line.move_to(((FRAME_HEIGHT/4)*DOWN))

        # for idx in range(1, 51):
        #     rect = Rectangle(height=1, width=w, fill_color=color, color=color, fill_opacity=1)
        #     rect.move_to((((FRAME_WIDTH-0.2)/2)*LEFT)+(((w+0.08)*(idx+1))*RIGHT)+(((FRAME_HEIGHT/4)*DOWN)+(0.5*UP)))
        #     rect.stretch_about_point(((random.randint(0,255)+1)/46.54), 1, rect.get_bottom())
        #     self.add(rect)
        # self.add(line)
        # self.add(title)
        # self.wait(5)

        # for chunk in chunks:
        #     for idx, bar in enumerate(chunk, 1):
        #         rect = Rectangle(height=1, width=w, fill_color=color, color=color, fill_opacity=1)
        #         rect.move_to((((FRAME_WIDTH-0.2)/2)*LEFT)+(((w+0.08)*(idx+1))*RIGHT)+(((FRAME_HEIGHT/4)*DOWN)+(0.5*UP)))
        #         rect.stretch_about_point(((bar+1)/46.54), 1, rect.get_bottom())
        #         self.add(rect)
        #     self.add(line)
        #     self.add(title)
        #     self.wait(1/59)
        #     self.clear()
        




