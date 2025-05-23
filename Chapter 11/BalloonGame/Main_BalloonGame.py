# pygame demo 0 - window only

# 1 - Import packages

from pygame.locals import *
import sys
import pygame
import pygwidgets
from BalloonMgr import *

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
YELLOW = (139, 128, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                       'Score: 0', textColor=BLACK,
                                       backgroundColor=None, width=140, fontSize=24)

oLevelDisplay = pygwidgets.DisplayText(window, (10, 10), '', textColor=YELLOW,
                                       backgroundColor=None, fontSize=30)

oStatusDisplay = pygwidgets.DisplayText(window, (150, USABLE_WINDOW_HEIGHT + 25),
                                       '', textColor=BLACK, backgroundColor=None,
                                        width=300, fontSize=24)
oStartButton = pygwidgets.TextButton(window,
                                     (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10),
                                     'Start')
oStopButton = pygwidgets.TextButton(window,
                                    (WINDOW_WIDTH - 213, USABLE_WINDOW_HEIGHT + 10),
                                    'Stop')
# 5 - Initialize variables

playing = False
speedModifier = 1
nBalloons = 8

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    nPointsEarned = 0
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            oBalloonMgr.handleEvent(event)
            theScore = oBalloonMgr.getScore()
            oScoreDisplay.setValue('Score: ' + str(theScore))

            if oStopButton.handleEvent(event):
                playing = False
                oStartButton.enable()

        elif oStartButton.handleEvent(event):

            oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
            oBalloonMgr.start(speedModifier, nBalloons)
            oBalloonMgr.setScore(0)
            oScoreDisplay.setValue('Score: 0')
            oBalloonMgr.setLevel(1)
            oLevelDisplay.setValue('LEVEL 1')
            playing = True
            oStartButton.disable()

    # 8 - Do any "per frame" actions
    if playing:
        oBalloonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()
        oStatusDisplay.setValue('Popped: ' + str(nPopped) +
                                '   Missed: ' + str(nMissed) +
                                '   Out of: ' + str(nBalloons))
        if (nPopped + nMissed) == nBalloons:
            if nPopped == nBalloons:
                speedModifier *= 1.1
                oBalloonMgr.start(speedModifier, nBalloons)
                theLevel = oBalloonMgr.getLevel() + 1
                oBalloonMgr.setLevel(theLevel)
                oLevelDisplay.setValue('LEVEL ' + str(theLevel))
            else:
                playing = False
                oStartButton.enable()
                speedModifier = 1
    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    if playing:
        oBalloonMgr.draw()
    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT,
                                               WINDOW_WIDTH, PANEL_HEIGHT))
    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()
    oStopButton.draw()
    oLevelDisplay.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait