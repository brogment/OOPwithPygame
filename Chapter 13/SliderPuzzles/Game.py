from Square import *
import random

class Game():
    START_LEFT = 35
    START_TOP = 30
    def __init__(self, window):
        self.window = window

        '''
        The game board is made up of 4 rows and 4 columns - 16 squares,
        with 15 labelled images (1 to 15) and a blank square image.
        However, because Python lists and tuples start at zero, the squares
        are internally numbered (indexed) 0 to 15, like this:
             0  1  2  3
             4  5  6  7
             8  9 10 11
            12 13 14 15
        (A Square is an area of the window, each contains a tile, which is movable.)

        The following is a dict of squareNumber:tuple.  Each tuple contains all
        moves (vertical and horizontal neighbors) that can switch with this square.
        For example, for Square 0, only Squares 1 and 4 are legal moves.
        '''

        LEGAL_MOVES_DICT = {
            0:(1, 4),
            1:(0, 2, 5),
            2:(1, 3, 6),
            3:(2, 7),
            4:(0, 5, 8),
            5:(1, 4, 6, 9),
            6:(2, 5, 7, 10),
            7:(3, 6, 11),
            8:(4, 9, 12),
            9:(5, 8, 10, 13),
            10:(6, 9, 11, 14),
            11:(7, 10, 15),
            12:(8, 13),
            13:(9, 12, 14),
            14:(10, 13, 15),
            15:(11, 14)}

        yPos = Game.START_TOP

        self.squaresList = []
        for row in range(0,4):
            xPos = Game.START_LEFT
