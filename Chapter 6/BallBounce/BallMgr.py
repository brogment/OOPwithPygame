import pygame
from pygame.locals import *
import random
from Ball import *

class BallMgr:
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def start(self, nBalls, speed):
        self.ballList = []
        self.nBalls = nBalls
        self.speed = speed

        for ballNum in range(0, self.nBalls):
            oBall = Ball(self.window, self.maxWidth, self.maxHeight, ballNum)
            self.ballList.append(oBall)

    def update(self):
        for oBall in self.ballList:
            oBall.update(self.ballList)

    def draw(self):
        for oBall in self.ballList:
            oBall.draw()


