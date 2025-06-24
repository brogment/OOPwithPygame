import pygwidgets
import pyghelpers
import pygame
from Constants import *
import sys
from Game import *

class SceneResults(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.background = pygwidgets.Image(window, (0,0), 'images/101814.jpg')
        self.newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game',
                                                   width=100, height=45)
        self.quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit',
                                                width=100, height=45)

        self.resultsText = pygwidgets.DisplayText(window, (300,300), 'Play Again?',
                                                  fontSize=120, textColor=pygwidgets.PYGWIDGETS_WHITE)
        self.roundsWon = pygwidgets.DisplayText(window, (150,400),
                                                f'Rounds Won:\tRounds Lost:\tRounds Tied:',
                                                fontSize=44,textColor=pygwidgets.PYGWIDGETS_WHITE)

    def getSceneKey(self):
        return SCENE_RESULTS

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()
            if self.newGameButton.handleEvent(event):
                newGame = Game(self.window)
                self.goToScene(SCENE_PLAY, newGame)

    def draw(self):
        self.background.draw()
        self.newGameButton.draw()
        self.quitButton.draw()
        self.resultsText.draw()
        self.roundsWon.draw()

    def enter(self, data):
        self.oGame = data