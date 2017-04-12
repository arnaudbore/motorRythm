import sys

import numpy as np
from expyriment import control, stimuli, io, design, misc
from expyriment.misc import constants
from expyriment.misc._timer import get_time

from config import *

if not windowMode:  # Check WindowMode and Resolution
    control.defaults.window_mode = windowMode
    control.defaults.window_size = misc.get_monitor_resolution()
    windowSize = control.defaults.window_size
else:
    control.defaults.window_mode = windowMode
    control.defaults.window_size = windowSize

exp = design.Experiment('test')  # Save experiment name

# Start Keyboard acquisition
trigger = io.Keyboard()
control.initialize(exp)

# Blanck Screen
bs = stimuli.BlankScreen(restBGColor)
bs.present(False, True)

# Crosses
greenFixCross = stimuli.FixCross(colour=regularCrossColor, size=restCrossSize, line_width=restCrossThickness)
greenFixCross.preload()
redFixCross = stimuli.FixCross(colour=restCrossColor, size=restCrossSize, line_width=restCrossThickness)
redFixCross.preload()
blackFixCross = stimuli.FixCross(colour=restBGColor, size=restCrossSize, line_width=restCrossThickness)
blackFixCross.preload()

# Tone used
tone1 = stimuli.Tone(50, 675)
tone1.preload()

# Init var
nBlock = 0

def readKeyboard():
    global exp
    global times
    key = exp.keyboard.check([49,50,51,52])
    if key is not None:
        times.append(exp.clock.time)

control.register_wait_callback_function(readKeyboard)
control.start(exp, auto_create_subject_id=True, skip_ready_screen=True)


nbBlock = 1

redFixCross.present(bs)
exp.clock.wait(shortRest)

times = []

while nbBlock <= nbBlocksMax:
    greenFixCross.present(bs)
    exp.clock.wait(shortRest)
    startBlock = get_time()

    nbip = 0

    while get_time() < startBlock + halfBlockDuration:
        if nbip > 21:
            tone1.play(maxtime=50)
            blackFixCross.present(bs)
            exp.clock.wait(500)
            greenFixCross.present(bs)
            exp.clock.wait(1500)
        else:
            tone1.play(maxtime=50)
            exp.clock.wait(2000)
            nbip +=1

    exp.clock.wait(halfBlockDuration*1000)
    redFixCross.present(bs)
    exp.clock.wait(restPeriod)
    nbBlock += 1

control.end()


