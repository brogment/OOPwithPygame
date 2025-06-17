import pygwidgets
import pyghelpers
import pygame
from Constants import *
import sys

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.background = pygwidgets.Image(window, (0, 0), 'images/background.png')
        self.newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game',
                                                   width=100, height=45)
        self.stayButton = pygwidgets.TextButton(window, (540, 520), 'Stay',
                                                width=120, height=55)
        self.hitButton = pygwidgets.TextButton(window, (340, 520), 'Hit',
                                               width=120, height=55)
        self.quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit',
                                                width=100, height=45)

    def getSceneKey(self):
        return SCENE_PLAY

    def handleInputs(self, events, keyPressedList):
        for event in events:

            if self.quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()

            if self.hitButton.handleEvent(event):
                bust = self.oGame.hit(0)
                if bust:
                    self.stayButton.disable()
                    self.hitButton.disable()
                    #self.goToScene(SCENE_RESULTS)

            if self.stayButton.handleEvent(event):
                self.stayButton.disable()
                self.hitButton.disable()
               # self.goToScene(SCENE_RESULTS)

    def enter(self, data):
        self.oGame = data
        self.stayButton.enable()
        self.hitButton.enable()
        # getting the game from the start scene
        # needed so each round will pull from the same deck until it's depleted
        # otherwise a fresh deck will be made for every round

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)

        #     # Tell the game to draw itself
        self.oGame.draw()
        #     # Draw remaining UI elements

        self.newGameButton.draw()
        self.hitButton.draw()
        self.stayButton.draw()
        self.quitButton.draw()
