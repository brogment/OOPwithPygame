import pygwidgets
import pyghelpers
import pygame
from Constants import *

class SceneResults(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

    def getSceneKey(self):
        return SCENE_RESULTS

    def handleInputs(self, events, keyPressedList):
        pass

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)