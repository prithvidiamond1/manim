
from manimlib.imports import *

import soundfile as sf
import sounddevice as sd
import math

import numpy as np
import random

freqrange = 255
chunkrange = 50
framerate = 10

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

# chunks = chunks[:70]
chunk_length = len(chunks)


class bars(Scene):
    def construct(self):
        w = 0.185
        color = WHITE

        init_h = 0.05
        bar_vgap = 0.03
        animationlist, prev_h = [], [init_h for x in range(50)]

        bg_image = ImageMobject('bgskyhighHD')
        bg_image.set_width(self.camera.get_frame_width()).set_height(self.camera.get_frame_height())
        self.add(bg_image)

        # title = Text('')
        title = Text(songname, font='DM Sans')
        title.move_to((((FRAME_HEIGHT/4)+0.5)*DOWN)+((FRAME_WIDTH/4)*LEFT)+(0.4*RIGHT))

        line = Line(start=((FRAME_WIDTH/2)*LEFT), end=((FRAME_WIDTH/2)*RIGHT), buff=0.4)
        line.move_to(((FRAME_HEIGHT/4)*DOWN)+((init_h + bar_vgap)*DOWN))

        startlist, endlist = [], []

        for cn, chunk in enumerate(chunks):
            animationlist = []
            for idx, bar in enumerate(chunk, 1):
                rect = Rectangle(height=1, width=w, fill_color=color, color=color, fill_opacity=1)
                rect.move_to((((FRAME_WIDTH-0.2)/2)*LEFT)+(((w+0.08)*(idx+1))*RIGHT)+(((FRAME_HEIGHT/4)*DOWN)+(0.5*UP)))

                if cn == 0:
                    startlist.append(FadeIn(rect))
                if cn == chunk_length-1:
                    endlist.append(FadeOut(rect))

                rect.stretch_about_point(prev_h[idx-1], 1, rect.get_bottom())
                animationlist.append(ApplyMethod(rect.stretch_about_point, ((bar+1)/46.54)/prev_h[idx-1], 1, rect.get_bottom()))
                prev_h[idx-1] = (bar+1)/46.54

            if cn == 0:
                self.play(AnimationGroup(*([FadeInFromLarge(title, scale_factor=1.5), FadeInFromLarge(line, scale_factor=0.8)]+startlist)), run_time=1)
                self.add_sound('deadmau5 - Ghosts N Stuff.wav', gain=2)

            self.add(bg_image)
            self.add(line)
            self.add(title)
            self.play(AnimationGroup(*animationlist), run_time=(1/(framerate)))
            self.clear()

            if cn == chunk_length-1:
                self.add(bg_image)
                self.play(AnimationGroup(*([FadeOut(title), FadeOut(line)]+endlist)), run_time=1)



