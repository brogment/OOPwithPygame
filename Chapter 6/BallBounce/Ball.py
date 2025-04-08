import pygame
from pygame.locals import *
import random

class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth

        self.image = pygame.image.load('images/ball.png')
        self.bounceSound = pygame.mixer.Sound('sound/boing.wav')

        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # pick random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # pick random speed in both directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall. If so, change that direction.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
            self.bounceSound.play()

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
            self.bounceSound.play()

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

