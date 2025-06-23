#  Game class

import pygwidgets
from Constants import *
from Deck import *
from Card import *
from Player import *

class Game():
    CARD_OFFSET = 70
    CARDS_LEFT = 300
    NCARDS = 2

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window,rankValueDict=Deck.blackjackDict)

        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")

        self.reset()

    def reset(self):  # this method is called when a new round starts

        self.oDeck.shuffle()
        self.cardShuffleSound.play()

        self.playerList=[]

        self.oPlayer1 = Player(300)
        self.oPlayer2 = Player(100)
        self.playerList.append(self.oPlayer1)
        self.playerList.append(self.oPlayer2)


        # problem is I should do using addCardToHand method for dealing out initial cards
        for oPlayer in self.playerList:
            for cardIndex in range(0, Game.NCARDS):  # deal out cards to player and dealer
                oCard = self.oDeck.getCard()
                oPlayer.playerCardList.append(oCard)
                oPlayer.playerScore += oCard.getValue()

                oCard.setLoc((oPlayer.cardXPositionsList[cardIndex], oPlayer.yPos))

        self.showCard(0, self.oPlayer1.playerCardList)
        self.showCard(1, self.oPlayer1.playerCardList)
        self.showCard(0, self.oPlayer2.playerCardList)
        #self.showCard(1, self.oPlayer2.playerCardList)

    def getCardNameAndValue(self, index, oPlayer):
        oCard = oPlayer.playerCardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index, cardList):
        oCard = cardList[index]
        oCard.reveal()

    def hit(self, playerID):
        oCard = self.oDeck.getCard()
        oCard.reveal()
        self.playerList[playerID].addCardtoHand(oCard)

    def draw(self):
        # Tell for each card to draw itself
        for oPlayer in self.playerList:
            for oCard in oPlayer.playerCardList:
                oCard.draw()

    def getPlayerScore(self, playerID):
        return self.playerList[playerID].getPlayerScore()
