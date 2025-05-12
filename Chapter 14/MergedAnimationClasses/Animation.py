from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
import sys
import pygwidgets
import time

class Animation(ABC):
    @abstractmethod
    def __init__(self, window, loc, durationPerImage, imagesList):
        self.window = window
        self.loc = loc
        self.durationPerImage = durationPerImage
        self.imagesList = imagesList

        self.playing = False
        self.index = 0
        self.imagesList = imagesList
        self.nImages = len(self.imagesList)

    def play(self):
        if self.playing:
            return
        self.playing = True
        self.imageStartTime = time.time()
        self.index = 0

    def update(self):
        if not self.playing:
            return
        # How much time has elapsed since we started showing this image
        self.elapsed  = time.time() - self.imageStartTime

        # if enough time has elapsed, move onto the next image
        if self.elapsed > self.durationPerImage:
            self.index += 1

            if self.index < self.nImages: # move onto next image
                self.imageStartTime = time.time()
            else: # animation has finished
                self.playing = False
                self.index = 0

    def draw(self):
        # assumes self.index has been set earlier in the update() method
        theImage = self.imagesList[self.index]
        self.window.blit(theImage, self.loc)

class SimpleAnimation(Animation):

    def __init__(self, window, loc, durationPerImage, picPaths):
        imagesList = []

        for picPath in picPaths:
            image = pygame.image.load(picPath)  # load an image
            image = pygame.Surface.convert_alpha(image)  # optimize blitting
            imagesList.append(image)

        super().__init__(window, loc, durationPerImage, imagesList)

class SheetAnimation(Animation):

    def __init__(self, window, loc, durationPerImage, imagePath, nImages, width, height):
        imagesList = []

        # load the sprite sheet
        spriteSheetImage = pygame.image.load(imagePath)
        # optimize blitting
        spriteSheetImage = pygame.Surface.convert_alpha(spriteSheetImage)

        # calculate number of columns in sheet
        nCols = spriteSheetImage.get_width() // width

        # break up starting image into individual images
        row = 0
        col = 0
        for image in range(nImages):
            x = col * height
            y = row * width

            # create a subsurface from the bigger sprite sheet
            subsurfaceRect = pygame.Rect(x, y, width, height)
            image = spriteSheetImage.subsurface(subsurfaceRect)
            imagesList.append(image)

            col += 1
            if col == nCols:
                col = 0
                row += 1

        super().__init__(window, loc, durationPerImage, imagesList)
