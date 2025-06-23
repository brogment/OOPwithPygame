# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *
from BallMgr import *

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
pygame.mixer.music.load('sound/background.mp3')
pygame.mixer.music.play(-1, 0.0)
targetImage = pygame.image.load('images/target.jpg')

# 5 - Initialize variables
oBallMgr = BallMgr(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oBallMgr.start(3, 1)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    oBallMgr.update()

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements

    oBallMgr.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
