import glob
import os
from math import ceil

rawFolder = os.getcwd() + os.path.sep

picturesFolder = rawFolder + 'stimulis' + os.path.sep

windowMode = True  # if False use FullScreen
windowSize = (1024, 768)  # if windowMode is True then use windowSize

restBGColor = (0, 0, 0)  # expyriment.misc.constants.C_BLACK
restCrossColor = (255, 0, 0)  # expyriment.misc.constants.C_WHITE
regularCrossColor = (0, 255, 0)  # expyriment.misc.constants.C_WHITE
restCrossSize = (100, 100)
restCrossThickness = 20
bgColor = (150, 150, 150)
textSize = 50

nbBlocksMax = 2

shortRest = 2500
restPeriod = 25000
clicPeriod = 200
halfBlockDuration = 45 # Seconds


debug = False

