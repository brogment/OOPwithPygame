# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import pyghelpers
import sys
from Game import *

# 2 - Define constants
WINDOW_WIDTH = 470
WINDOW_HEIGHT = 560
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
restartButton = pygwidgets.CustomButton(window, (320,455),
                                        up='images/restartButtonUp.jpg',
                                        down='images/restartButtonDown.jpg',
                                        over='images/restartButtonOver.jpg')
soundBuzz = pygame.mixer.Sound('sounds/buzz.wav')

# 5 - Initialize variables
timerDisplay = pygwidgets.DisplayText(window,(50,465), '',
                                      fontSize=36, textColor=WHITE)

messageDisplay = pygwidgets.DisplayText(window,(50,510), 'Click on a tile to move it',
                                      fontSize=36, textColor=WHITE)

oGame = Game(window)

oCountDownTimer = pyghelpers.CountDownTimer(180)
oCountDownTimer.start()

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            messageDisplay.setText('')
            oGame.gotClick(event.pos)
            over = oGame.checkForWin()
            if over:
                messageDisplay.setText('Great job!!!')
                oCountDownTimer.stop()

        if restartButton.handleEvent(event):
            oGame.startNewGame()
            oCountDownTimer.start()

    # 8 - Do any "per frame" actions
    timeToShow = oCountDownTimer.getTimeInHHMMSS(2) # ask clock object for elapsed time
    timerDisplay.setValue('Time: ' + timeToShow) # put that into text field
    if oGame.getGamePlaying():
        if oCountDownTimer.ended():
            soundBuzz.play()
            messageDisplay.setText('Doh! You ran out of time.')
            oGame.stopPlaying()

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    oGame.draw()
    restartButton.draw()
    timerDisplay.draw()
    messageDisplay.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait