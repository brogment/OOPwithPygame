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

        self.statsButton = pygwidgets.TextButton(window, (750, 530), 'Stats',
                                                width=100, height=45)


        self.roundsWonLabel = pygwidgets.DisplayText(window, (750,300),'Rounds Won:'
                                                ,textColor=pygwidgets.PYGWIDGETS_WHITE)
        self.roundsLostLabel = pygwidgets.DisplayText(window, (750, 320), 'Rounds Lost:'
                                                , textColor=pygwidgets.PYGWIDGETS_WHITE)
        self.roundsTiedLabel = pygwidgets.DisplayText(window, (750, 340), 'Rounds Tied:'
                                                , textColor=pygwidgets.PYGWIDGETS_WHITE)

        self.roundsWonCounter = pygwidgets.DisplayText(window, (850, 300), '0'
                                                , textColor=pygwidgets.PYGWIDGETS_WHITE)
        self.roundsLostCounter = pygwidgets.DisplayText(window, (850, 320), '0'
                                                , textColor=pygwidgets.PYGWIDGETS_WHITE)
        self.roundsTiedCounter = pygwidgets.DisplayText(window, (850, 340), '0'
                                                , textColor=pygwidgets.PYGWIDGETS_WHITE)





        self.TIMER_LENGTH = 2
        self.oTimer = pyghelpers.Timer(self.TIMER_LENGTH)

        # flag for if the second card dealt to dealer had been flipped over
        # and round is ending
        self.flipped = False

    def getSceneKey(self):
        return SCENE_PLAY

    def handleInputs(self, events, keyPressedList):
        for event in events:

            if self.quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()

            if self.statsButton.handleEvent(event):
                self.goToScene(SCENE_RESULTS, self.oGame)

            if self.newGameButton.handleEvent(event):
                self.oGame.reset()
                self.stayButton.enable()
                self.hitButton.enable()
                self.oTimer.stop()

            if self.hitButton.handleEvent(event):
                self.oGame.hit(0)
                print(f"player score: {self.oGame.getPlayerScore(0)}")
                if self.oGame.getPlayerScore(0) > 21:
                    self.stayButton.disable()
                    self.hitButton.disable()
                    # starting timer, when it ends then the computer will
                    # take action each frame in update()
                    self.oTimer.start()

            if self.stayButton.handleEvent(event):
                print(f"player score: {self.oGame.getPlayerScore(0)}")
                self.stayButton.disable()
                self.hitButton.disable()
                self.oTimer.start()

    def update(self):

        if self.oTimer.update():
            if self.oGame.getPlayerScore(1) <= 16:
                self.oTimer.start()
                self.oGame.hit(1)
                print(f"dealer score: {self.oGame.getPlayerScore(1)}")
            elif self.flipped == False:
                self.oGame.reveal(1, 1)
                self.flipped = True
                self.oTimer.start()
                print(f"dealer score: {self.oGame.getPlayerScore(1)}")
            else:
                # round is over
                self.flipped = False

                self.oGame.calcResults()

                wins, loses, ties = self.oGame.getStats()
                self.roundsWonCounter.setValue(wins)
                self.roundsLostCounter.setValue(loses)
                self.roundsTiedCounter.setValue(ties)

                self.oGame.reset()
                self.stayButton.enable()
                self.hitButton.enable()
                self.oTimer.stop()

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
        self.statsButton.draw()

        self.roundsWonLabel.draw()
        self.roundsLostLabel.draw()
        self.roundsTiedLabel.draw()
        self.roundsWonCounter.draw()
        self.roundsLostCounter.draw()
        self.roundsTiedCounter.draw()