#  Game class

import pygwidgets
from Constants import *
from Deck import *
from Card import *
from Player import *

class Game():
    CARD_OFFSET = 70
    CARDS_LEFT = 300
    # PLAYER_CARDS_TOP = 300
    # DEALER_CARDS_TOP = 100
    NCARDS = 2

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window,rankValueDict=Deck.blackjackDict)
        self.messageText = pygwidgets.DisplayText(window, (50, 460),
                                    '', width=900, justified='center',
                                    fontSize=36, textColor=WHITE)

        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")

        self.reset()  # start a round of the game

    def reset(self):  # this method is called when a new round starts

        self.oDeck.shuffle()
        self.cardShuffleSound.play()

        self.playerList=[]

        self.oPlayer1 = Player(300)
        self.oPlayer2 = Player(100)
        self.playerList.append(self.oPlayer1)
        self.playerList.append(self.oPlayer2)

        for oPlayer in self.playerList:
            for cardIndex in range(0, Game.NCARDS):  # deal out cards to player and dealer
                oCard = self.oDeck.getCard()
                oPlayer.playerCardList.append(oCard)
                oPlayer.playerScore += oCard.getValue()

                oCard.setLoc((oPlayer.cardXPositionsList[cardIndex], oPlayer.yPos))

        self.showCard(0, self.oPlayer1.playerCardList)
        self.showCard(1, self.oPlayer1.playerCardList)
        self.showCard(0, self.oPlayer2.playerCardList)

        self.messageText.setValue('Hit or stay?')

    def getCardNameAndValue(self, index, oPlayer):
        oCard = oPlayer.playerCardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index, cardList):
        oCard = cardList[index]
        oCard.reveal()

    def hit(self):

        oCard = self.oDeck.getCard()
        oCard.reveal()

        self.oPlayer1.playerCardList.append(oCard)
        self.cardXPositionsList.append(self.thisLeft)
        self.thisLeft = self.thisLeft + Game.CARD_OFFSET

        thisXPosition = self.cardXPositionsList[-1]
        oCard.setLoc((thisXPosition, self.oPlayer1.yPos))
        self.oPlayer1.playerScore += oCard.getValue()
        if self.oPlayer1.playerScore > 21:
            return True
        else:
            return False

    def draw(self):
        # Tell for each card to draw itself
        for oPlayer in self.playerList:
            for oCard in oPlayer.playerCardList:
                oCard.draw()

        self.messageText.draw()
