import pygwidgets
import pyghelpers
import pygame
from Constants import *
import sys

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.background = pygwidgets.Image(window, (0, 0), 'images/101814.jpg')
        self.newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game',
                                                   width=100, height=45)
        self.stayButton = pygwidgets.TextButton(window, (540, 520), 'Stay',
                                                width=120, height=55)
        self.hitButton = pygwidgets.TextButton(window, (340, 520), 'Hit',
                                               width=120, height=55)
        self.quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit',
                                                width=100, height=45)

        self.TIMER_LENGTH = 2
        self.oTimer = pyghelpers.Timer(self.TIMER_LENGTH)

    def getSceneKey(self):
        return SCENE_PLAY

    def handleInputs(self, events, keyPressedList):
        for event in events:

            if self.quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()

            if self.newGameButton.handleEvent(event):
                self.oGame.reset()
                self.stayButton.enable()
                self.hitButton.enable()
                self.oTimer.stop()

            if self.hitButton.handleEvent(event):
                self.oGame.hit(0)
                print(self.oGame.getPlayerScore(0))
                if self.oGame.getPlayerScore(0) > 21:
                    self.stayButton.disable()
                    self.hitButton.disable()
                    # starting timer, when it ends then the computer will
                    # take action each frame in update()
                    self.oTimer.start()

            if self.stayButton.handleEvent(event):
                print(self.oGame.getPlayerScore(0))
                self.stayButton.disable()
                self.hitButton.disable()
                self.oTimer.start()

    def update(self):
        if self.oTimer.update():
            if self.oGame.getPlayerScore(1) <= 16:
                self.oTimer.start()
                self.oGame.hit(1)
                print(self.oGame.getPlayerScore(1))
            else:
                print(self.oGame.getPlayerScore(1))
                self.goToScene(SCENE_RESULTS, self.oGame)

    def enter(self, data):
        self.oGame = data
        self.stayButton.enable()
        self.hitButton.enable()

    def draw(self):
        self.background.draw()
        # Tell the game to draw itself
        self.oGame.draw()

        self.newGameButton.draw()
        self.hitButton.draw()
        self.stayButton.draw()
        self.quitButton.draw()
