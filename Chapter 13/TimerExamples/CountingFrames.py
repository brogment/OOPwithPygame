# pygame demo 0 - window only

# 1 - Import packages
import pygame
import pygwidgets
from pygame.locals import *
import sys

# 2 - Define constants
WHITE = (255,255,255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
TIMER_LENGTH = 2.5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
headerMessage = pygwidgets.DisplayText(window, (0,50), f'Click \"Start\" to start a '
                                                       f'{str(TIMER_LENGTH)} second timer',
                                       fontSize=36,justified='center',width=WINDOW_WIDTH)
startButton = pygwidgets.TextButton(window, (200,100), 'Start')
clickMeButton = pygwidgets.TextButton(window, (320,100), 'Click Me')
timerMessage = pygwidgets.DisplayText(window, (0,160), 'Message showing during timer',
                                      fontSize=36, justified='center',width=WINDOW_WIDTH)
timerMessage.hide()
timerRunning = False


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            nFramesElapsed = 0  # initialize a counter
            nFramesToWait = int(FRAMES_PER_SECOND * TIMER_LENGTH)
            startButton.disable()
            timerMessage.show()
            print('Starting timer')
            timerRunning = True

        if clickMeButton.handleEvent(event):
            print('Other button was clicked')


    # 8 - Do any "per frame" actions
    if timerRunning:
        nFramesElapsed += 1
        if nFramesElapsed >= nFramesToWait:
            startButton.enable()
            timerMessage.hide()
            print('Timer Has ended by counting frames')
            timerRunning = False

    # 9 - Clear the window
    window.fill(WHITE)

    # 10 - Draw all window elements
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait