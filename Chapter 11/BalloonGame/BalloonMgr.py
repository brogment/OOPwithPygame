import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from Balloon import *

class BalloonMgr():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        print(self.__dict__)

    def start(self, speedModifier, nBalloons):
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0
        self.speedModifier = speedModifier
        self.nBalloons = nBalloons

        for balloonNum in range(0, self.nBalloons):
            randomBalloonClassList = random.choices((BalloonSmall,
                                                    BalloonMedium,
                                                    BalloonLarge,
                                                    BalloonMega),
                                                    weights=[5,5,5,3])
            randomBalloonClass = randomBalloonClassList[0]
            oBalloon = randomBalloonClass(self.window, self.maxWidth,
                                          self.maxHeight, balloonNum, self.speedModifier)
            self.balloonList.append(oBalloon)

    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for oBalloon in reversed(self.balloonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)
                if wasHit:
                    health = oBalloon.getHealth() - 1
                    if health <= 0:
                        self.balloonList.remove(oBalloon)
                        self.nPopped += 1
                        self.score += nPoints
                    else:
                        oBalloon.setHealth(health)
                    return

    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == BALLOON_MISSED:
                self.balloonList.remove(oBalloon)
                self.nMissed += 1

    def getScore(self):
        return self.score

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()
