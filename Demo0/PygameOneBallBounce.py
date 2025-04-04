# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_SIDE = 100
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
MAX_WIDTH = WINDOW_WIDTH - BALL_SIDE
MAX_HEIGHT = WINDOW_HEIGHT - BALL_SIDE
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions

    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed

    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed

    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(ballImage, (ballX, ballY))  # draw the ball

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
