from abc import ABC, abstractclassmethod
from random import randrange

from Player import Player
from GameBoard import GameBoard

class Block(ABC):
    def __init__(self, block_data):
        self.block_data = block_data
    
    @abstractclassmethod
    def activateBlockEffect(self, player: Player , gameBoard : GameBoard):
        #print save game option
        #call gameboard.saveGame()
        pass

# Start Block
class Start(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']

    def activateBlockEffect(self, player: Player, gameBoard: GameBoard): 
        #call super() no effect
        return super().activateBlockEffect(player,gameBoard)

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

        #if owner is None:
            #if player.money < price:
                #print not enough money,
                #print option Pass, Save Game
                #if ans is Pass, pass,
                #if ans is Save Game, call gameBoard.saveGame()
            #if player.money >= price:
                #Ask player to buy the property
                #print the option Buy, Pass, Save Game
                #if buy, player.money -= price, setOwner(player), printGameboard()
                #if pass, pass
                #if save Game, save Game

        #if owner is the player:
            #print no effect
            #print option pass , save game
            #if pass, pass
            #if save game, call gameBoard.saveGame()

        #if owner is not None and owner is not the player
            #pay rent
            #if player.money - rent < 0
                #player do not have enough money to play the rent, only add the remaining money to the owner
                #owner += player.money
                #player.money -= rent
                #printGameboard()
                #print message 'do not have enough money to pay ....'

            #if player have enough money to pay
                #owner.money += rent
                #player.money -= rent
                #printGameBoard
                #print message
        pass

# Income Tax Block
class IncomeTax(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']
        self.tax = block_data['Tax']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        #calculate the tax: round((player.money*self.tax/100)/10)*10 
        #player.money -= tax
        #print game board
        pass

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
        #call super() no effect
        return super().activateBlockEffect(player,gameBoard)

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

        #if gain : 
            #index = self.max // 10
            #result = randrange(index+1)*10
            #print message
        #if lose: 
            #abs(self.min) // 10
            #result = randrange(index+1)*10
            #print message


        #player.money += result
        #print game board
        pass

# free parking
class FreeParking(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
        #call super() no effect
        return super().activateBlockEffect(player,gameBoard)


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
        # print message 'Send to Jail !'
        # set player.position = self.jailPosition
        # set player.jailLeft = self.turn
        # call gameBoard.addToJailList(player,self.fine)
        # print game board
        pass