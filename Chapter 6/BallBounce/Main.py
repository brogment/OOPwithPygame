# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *
# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
pygame.mixer.music.load('sound/background.mp3')
pygame.mixer.music.play(-1, 0.0)

# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    oBall = Ball(window,WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    for oBall in ballList:
        oBall.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
