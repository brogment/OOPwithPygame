
class Player:
    CARD_OFFSET = 70
    CARDS_LEFT = 300

    def __init__(self, yPos):

        self.playerScore = 0
        self.playerCardList = []
        self.yPos = yPos

        # calculate the position of the starting two cards
        self.cardXPositionsList = []
        self.currentXPos = Player.CARDS_LEFT
        for cardNum in range(2):
            self.cardXPositionsList.append(self.currentXPos)
            self.currentXPos += Player.CARD_OFFSET