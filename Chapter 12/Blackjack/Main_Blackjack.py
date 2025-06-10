# 1 - Import packages
import pygame
import pyghelpers
import pygwidgets
from Constants import *
from ScenePlay import *
from SceneResults import *
from SceneStart import *

# 2 - Define constants

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# # 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables

scenesList = [SceneStart(window),
              ScenePlay(window)]#,
    #           SceneResults(window)]

# pass in sceneList and FPS to frame manager
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

oSceneMgr.run()
