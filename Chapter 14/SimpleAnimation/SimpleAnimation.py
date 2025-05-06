import pygame
import time

class SimpleAnimation():
    def __init__(self, window, loc, picPaths, durationPerImage):
        self.window = window
        self.loc = loc
        self.imagesList = []
        for picPath in picPaths:
            image = pygame.image.load(picPath) # load an image
            image = pygame.Surface.convert_alpha(image) # optimize blitting
            self.imagesList.append(image)

        self.playing = False
        self.durationPerImage = durationPerImage
        self.nImages = len(self.imagesList)
        self.index = 0

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