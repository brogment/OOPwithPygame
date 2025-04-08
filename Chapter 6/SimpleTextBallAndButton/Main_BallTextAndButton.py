# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from Ball import *
from SimpleText import *
from SimpleButton import *

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255,255,255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

frameCounter = 0

# This makes it so whenever the restart button is clicked, the frame counter resets to 0, alternative
# to checking if the event returns true and setting framecounter = 0 there
def myCallBackFunction():
    print('working')
    global frameCounter
    frameCounter = 0

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window,
                              (60,20),
                              'Program has run through this many loops: ',
                              WHITE)
oFrameCountDisplay = SimpleText(window,
                                (500, 20),
                                '',
                                WHITE)
oRestartButton = SimpleButton(window,
                              (280,60),
                              'images/restartUp.png',
                              'images/restartDown.png',
                              callBack=myCallBackFunction)



# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        oRestartButton.handleEvent(event)


    # 8 - Do any "per frame" actions
    oBall.update()
    frameCounter += 1
    oFrameCountDisplay.setValue(str(frameCounter))

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait