import pygame
from pygame.locals import *
import random

class Ball():

    def __init__(self, window, windowWidth, windowHeight, ID):
        self.window = window
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.ID = ID

        self.image = pygame.image.load('images/ball.png')
        self.bounceSound = pygame.mixer.Sound('sound/boing.wav')

        # A rect is made up of [x, y, width, height]
        self.ballRect = self.image.get_rect()
        self.width = self.ballRect.width
        self.height = self.ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # pick random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # pick random speed in both directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self, ballList):

        # checking to see if this ball is colliding with any other balls
        # for oBall in ballList:
        #    if self.ballRect.colliderect(oBall.ballRect):
        #         print(self.ballRect)
        #         self.xSpeed = -self.xSpeed
        #         self.ySpeed = -self.ySpeed
        #         self.bounceSound.play()

        # Check for hitting a wall. If so, change that direction.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
            self.bounceSound.play()
            print(self.ballRect)

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
            self.bounceSound.play()
            print(self.ballRect)

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

        self.ballRect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

