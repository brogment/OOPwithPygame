import pygame
import time

class SimpleSpriteSheetAnimation():
    def __init__(self, window, loc, imagePath, nImages, width, height, durationPerImage):
        self.window = window
        self.loc = loc
        self.nImages = nImages
        self.imagesList = []
        self.playing = False
        self.durationPerImage = durationPerImage
        self.index = 0

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
            self.imagesList.append(image)

            col += 1
            if col == nCols:
                col = 0
                row += 1

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