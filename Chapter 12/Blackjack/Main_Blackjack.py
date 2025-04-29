# 1 - Import packages
import pygame
import pygwidgets
from pygame.locals import *
import sys
from Deck import *
from Constants import *
from Game import *

# 2 - Define constants
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (6,64,43)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
background = pygwidgets.Image(window, (0,0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game',
                                      width=100, height=45)
stayButton = pygwidgets.TextButton(window, (540, 520), 'Stay',
                                      width=120, height=55)
hitButton = pygwidgets.TextButton(window, (340, 520), 'Hit',
                                      width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit',
                                      width=100, height=45)

# 5 - Initialize variables
oGame = Game(window)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if (event.type == pygame.QUIT or
           (event.type == KEYDOWN and event.key == K_ESCAPE) or
            quitButton.handleEvent(event)):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            hitButton.enable()
            stayButton.enable()
        
        if hitButton.handleEvent(event):
            bust = oGame.hit()
            if bust:
                stayButton.disable()
                hitButton.disable()

        if stayButton.handleEvent(event):
            stayButton.disable()
            hitButton.disable()

                
    # 8 - Do any "per frame" actions

    # 9 - Clear the window before drawing it again
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    # Tell the game to draw itself
    oGame.draw()
    # Draw remaining UI elements
    newGameButton.draw()
    hitButton.draw()
    stayButton.draw()
    quitButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait