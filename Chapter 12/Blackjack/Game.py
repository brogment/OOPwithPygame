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

        self.roundsWon = 0
        self.roundsLost = 0
        self.roundsTied = 0

        self.reset()

    def reset(self):  # this method is called when a new round starts

        self.oDeck.shuffle()
        self.cardShuffleSound.play()

        self.playerList=[]

        self.oPlayer1 = Player(300)
        self.oPlayer2 = Player(100)
        self.playerList.append(self.oPlayer1)
        self.playerList.append(self.oPlayer2)

        for oPlayer in self.playerList:
            for cardNum in range(0, Game.NCARDS):  # deal out cards to player and dealer
                oCard = self.oDeck.getCard()
                oPlayer.addCardtoHand(oCard)

        self.reveal(0, 0)
        self.reveal(0, 1)
        self.reveal(1, 0)

    def getCardNameAndValue(self, index, oPlayer):
        oCard = oPlayer.playerCardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def hit(self, playerID):
        oCard = self.oDeck.getCard()
        oCard.reveal()
        self.playerList[playerID].addCardtoHand(oCard)

    def draw(self):
        # Tell for each card to draw itself
        for oPlayer in self.playerList:
            for oCard in oPlayer.playerCardList:
                oCard.draw()

        # draw the rest of the deck off to side to later add animation
        # of it moving to player or dealer side of table?
        # would need to set loc for every card in deck, making it offset just
        # 1 or 2 pixels each time to give illusion of a deck
        x=200
        y=200

        for oCard in self.oDeck.playingDeckList:
            oCard.setLoc((x,y))
            x+=.7
            y+=.7
            oCard.draw()

    def getPlayerScore(self, playerID):
        return self.playerList[playerID].getPlayerScore()

    def calcResults(self):
        pScore = self.getPlayerScore(0)
        dScore = self.getPlayerScore(1)

        if pScore > 21 and dScore <= 21:
            self.roundsLost += 1
        elif pScore <= 21 and dScore > 21:
            self.roundsWon += 1
        elif pScore > 21 and dScore > 21:
            self.roundsTied += 1
        elif pScore == dScore:
            self.roundsTied += 1
        elif pScore > dScore:
            self.roundsWon += 1
        elif pScore < dScore:
            self.roundsLost += 1
        else:
            print("Something strange happened")

    def reveal(self, playerID, cardIndex):
        oCard = self.playerList[playerID].playerCardList[cardIndex]
        oCard.reveal()

    def getStats(self):
        return self.roundsWon, self.roundsLost, self.roundsTied