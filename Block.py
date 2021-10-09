from __future__ import print_function, unicode_literals
from whaaaaat import prompt
from random import randrange
from abc import ABC, abstractclassmethod
from Config import *
from GameBoard import GameBoard
from data import *
from Player import *

class Block(ABC):
    def __init__(self, block_data):
        self.block_data = block_data
    
    @abstractclassmethod
    def activateBlockEffect(self, player: Player , gameBoard : GameBoard):
        pass

# Start Block
class Start(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        n = player.playerNumber
        enter_RollDice[0]['message'] = 'Player ' + str(n) +  ' Roll Dice! (Enter)'
        ans = prompt(enter_RollDice)

        if ans['ans'] == 'Roll !':
            rollDice(player)
        else:
            #Save GAME
            #TODO
            saveGame()

        
        

# Property Block
class Property(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.price = block_data['Price']
        self.rent = block_data['Rent']
        self.owner = 'None'
    
    def resetOwner(self):
        self.owner == 'None'

    def setOwner(self, player: Player):
        self.owner = player

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        n = player.playerNumber
        enter_RollDice[0]['message'] = 'Player ' + str(n) +  ' Roll Dice! (Enter)'
        ans = prompt(enter_RollDice)

        if ans['ans'] == 'Roll !':
            rollDice(player)
        else:
            #Save GAME
            #TODO
            saveGame()

# Income Tax Block
class IncomeTax(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']
        self.tax = block_data['Tax']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        taxNeedToPay =  round((player.money*self.tax/100)/10)*10 
        player.money -= taxNeedToPay

# Jail , just visiting
class Jail(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']
        self.fine = block_data['Fine']
        self.turn = block_data['Turn']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        return super().activateBlockEffect(player)

# Chance
class Chance(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']
        self.min = block_data['min']
        self.max = block_data['max']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        # random 0/1
        # 0 = gain
        # 1 = lose

        gainOrLose = randrange(2)
        result = 0

        if gainOrLose == 0:
            # gain
            index = self.max // 10
            result = randrange(index+1)*10

        else:
            # Lose
            index = abs(self.min) // 10
            result = randrange(index+1)*-10

        player.money += result

# free parking
class FreeParking(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        return super().activateBlockEffect(player)

#Go to Jail
class GoToJail(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.jailPosition = block_data['JailPosition']
        self.fine = block_data['Fine']
        self.turn = block_data['Turn']


    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        player.position = self.jailPosition
        player.jailLeft = self.turn

def saveGame():
    #TODO
    exit()

def rollDice(player:Player):
    diceResult = dice()
    input('Dice Result: ' + str(diceResult) + ' (Press Any Key to Continue)')
    newPos = player.position + diceResult
    if newPos > 19:
        newPos -= 20
        player.addMoney(SALARY) 
        player.position = newPos
    else:
        player.position = newPos


def dice():
    return 1

    





        





