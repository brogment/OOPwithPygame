import sys
import pygwidgets
import pyghelpers
import pygame
from Game import *

class SceneStart(pyghelpers.Scene):

    def __init__(self, window):
        self.window = window
        self.background = pygwidgets.Image(window, (0,0), 'images/101814.jpg')
        self.newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game',
                                              width=100, height=45)
        self.quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit',
                                              width=100, height=45)

        self.oGame = Game(window)

    def getSceneKey(self):
        return SCENE_START

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()
            if self.newGameButton.handleEvent(event):
                self.goToScene(SCENE_PLAY, self.oGame)

    def draw(self):
      self.background.draw()
      self.newGameButton.draw()
      self.quitButton.draw()