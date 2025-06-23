from Card import *

class Player:
    CARD_OFFSET = 70
    CARDS_LEFT = 300

    def __init__(self, yPos):

        self.playerScore = 0
        self.playerCardList = []
        self.yPos = yPos
        self.acesInHand = []

        # calculate the position of the starting two cards
        self.cardXPositionsList = []
        self.currentXPos = Player.CARDS_LEFT
        for cardNum in range(2):
            self.cardXPositionsList.append(self.currentXPos)
            self.currentXPos += Player.CARD_OFFSET

    def addCardtoHand(self, oCard):
        self.playerCardList.append(oCard)
        self.cardXPositionsList.append(self.currentXPos)
        self.currentXPos += Player.CARD_OFFSET
        thisXPosition = self.cardXPositionsList[-1]
        oCard.setLoc((thisXPosition, self.yPos))
        self.playerScore += oCard.getValue()

        if oCard.getRank() == 'Ace':
            self.acesInHand.append(len(self.playerCardList)-1)


    def getPlayerScore(self):

        while self.playerScore > 21 and len(self.acesInHand) > 0:
            aceIndex = self.acesInHand[-1]
            self.playerCardList[aceIndex].setValue(1)
            self.acesInHand.pop()
            self.playerScore -= 10 # hacky way to avoid having to sum up the deck again
        return self.playerScore




