#  Game class

import pygwidgets
from Constants import *
from Deck import *
from Card import *

class Game():
    CARD_OFFSET = 70
    CARDS_TOP = 300
    CARDS_LEFT = 300
    NCARDS = 2

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window)
        self.messageText = pygwidgets.DisplayText(window, (50, 460),
                                    '', width=900, justified='center',
                                    fontSize=36, textColor=WHITE)

        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")

        self.cardXPositionsList = []
        self.thisLeft = Game.CARDS_LEFT
        # Calculate the x positions of first two cards
        for cardNum in range(Game.NCARDS):
            self.cardXPositionsList.append(self.thisLeft)
            self.thisLeft = self.thisLeft + Game.CARD_OFFSET

        self.reset()  # start a round of the game

    def reset(self):  # this method is called when a new round starts

        self.score = 0
        self.cardShuffleSound.play()
        self.cardList = []
        self.oDeck.shuffle()
        for cardIndex in range(0, Game.NCARDS):  # deal out cards to player
            oCard = self.oDeck.getCard()
            self.cardList.append(oCard)
            self.score += oCard.getValue()

            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))

        self.showCard(0)
        self.showCard(1)
        print(self.score)

        self.messageText.setValue('Hit or stay?')

    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()
    def hit(self):
        oCard = self.oDeck.getCard()
        self.cardList.append(oCard)

        self.cardXPositionsList.append(self.thisLeft)
        self.thisLeft = self.thisLeft + Game.CARD_OFFSET

        thisXPosition = self.cardXPositionsList[-1]
        oCard.setLoc((thisXPosition, Game.CARDS_TOP))

    # def hitHigherOrLower(self, higherOrLower):
    #     self.cardNumber += 1
    #     self.showCard(self.cardNumber)
    #     nextCardName, nextCardValue = self.getCardNameAndValue(self.cardNumber)
    #
    #     if higherOrLower == HIGHER:
    #         if nextCardValue > self.currentCardValue:
    #             self.messageText.setValue('Yes, the ' + nextCardName + ' was higher')
    #             self.winnerSound.play()
    #         else:
    #             self.messageText.setValue('No, the ' + nextCardName + ' was not higher')
    #             self.loserSound.play()
    #     else: # user hit lower button
    #         if nextCardValue < self.currentCardValue:
    #             self.messageText.setValue('Yes, the ' + nextCardName + ' was lower')
    #             self.winnerSound.play()
    #         else:
    #             self.messageText.setValue('No, the ' + nextCardName + ' was not lower')
    #             self.loserSound.play()
    #
    #
    #     self.currentCardValue = nextCardValue # set up for next card
    #     done = (self.cardNumber == (Game.NCARDS - 1)) # did we reach last card
    #     return done

    def draw(self):
        # Tell for each card to draw itself
        for oCard in self.cardList:
            oCard.draw()

        self.messageText.draw()
