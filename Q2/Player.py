from data import SALARY


class Player:
    def __init__(self, playerNumber, money , position):
        self.playerNumber = playerNumber
        self.money = money
        self.position = position
        self.jailLeft = 0

    def payMoney(self, money):
        self.money -= money

    def addMoney(self, money):
        self.money += money


    def isAlice(self):
        if self.money > 0:
            return True
        else:
            return False

    def isInJail(self):
        if self.jailLeft > 0 :
            return True
        else:
            return False