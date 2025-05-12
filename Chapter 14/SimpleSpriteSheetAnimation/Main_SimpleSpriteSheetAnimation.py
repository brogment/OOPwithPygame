# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleSpriteSheetAnimation import *


# 2 - Define constants
BG_COLOR = (0, 128, 128)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
oWaterAnimation = SimpleSpriteSheetAnimation(window, (22,140),
                                             'images/water_003.png',
                                             50, 192, 192, .05)
oPlayButton = pygwidgets.TextButton(window,(60,320), 'PLAY')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oWaterAnimation.play()

    # 8 - Do any "per frame" actions
    oWaterAnimation.update()
    # 9 - Clear the window
    window.fill(BG_COLOR)

    # 10 - Draw all window elements
    oWaterAnimation.draw()
    oPlayButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait