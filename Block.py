from __future__ import print_function, unicode_literals
from os import O_WRONLY
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
        ans = prompt(no_Effect_Block)

        if ans['ans'] == 'Save Game !':
            #save game
            gameBoard.saveGame()

# Start Block
class Start(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']

    def activateBlockEffect(self, player: Player, gameBoard: GameBoard):
        return super().activateBlockEffect(player, gameBoard)

        
        

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
        enter_Property[0]['choices'] = []
        choice = enter_Property[0]['choices']
        #check owner
        if self.owner == 'None':
            #show buy / pass / save game

            if player.money < self.price:
                # not enough money
                enter_Property[0]['message'] ='Player ' + str(player.playerNumber) + ': Not enough money to buy the property !'
                choice.append('Pass !')
                choice.append('Save Game !')
                ans = prompt(enter_Property)
                if ans['ans'] == 'Save Game !':
                    gameBoard.saveGame()
                
            else:
                enter_Property[0]['message'] ='Player ' + str(player.playerNumber) + ': Buy the property ?'
                choice.append('Buy !')
                choice.append('Pass !')
                choice.append('Save Game !')
                ans = prompt(enter_Property)

                if ans['ans'] ==  'Buy !':
                    # not enough money
                    self.owner = player
                    self.owner.money -= self.price
                    gameBoard.print_board()
                elif ans['ans'] == 'Save Game !':
                    gameBoard.saveGame()
            
        elif self.owner.playerNumber == player.playerNumber:
            #owner show msg only
            enter_Property[0]['message'] = 'You are the owner, no effect !'
            choice.append('Pass !')
            choice.append('Save Game !')
            ans = prompt(enter_Property)

            if ans['ans'] == 'Save Game !':
                gameBoard.saveGame()
        else:
            #pay rent
            if player.money - self.rent < 0:
                #not enough money
                self.owner.money += player.money
                player.money -= self.rent
                gameBoard.print_board()
                input('Not enough money to pay the rent ! All remaining money add to the owner P' + str(self.owner.playerNumber))

            else:
                #normal case
                self.owner.money += self.rent
                player.money -= self.rent
                gameBoard.print_board()
                input('Pay the rent $'+ str(self.rent) + ' to P' + str(self.owner.playerNumber))


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
        input('Player ' + str(player.playerNumber) + ' need to pay the tax: '+ str(taxNeedToPay))
        player.money -= taxNeedToPay
        gameBoard.print_board()

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

        gainOrLose = randrange(2)
        result = 0

        if gainOrLose == 0:
            # gain
            index = self.max // 10
            result = randrange(index+1)*10
            input('Player '+ str(player.playerNumber) + ' gain $' + str(result))

        else:
            # Lose
            index = abs(self.min) // 10
            result = randrange(index+1)*-10
            input('Player '+ str(player.playerNumber) + ' Lose $' + str(result))
        player.money += result
        gameBoard.print_board()

# free parking
class FreeParking(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.position = block_data['Position']
        self.name = block_data['Name']
        self.subText = block_data['SubText']

    def activateBlockEffect(self, player: Player, gameBoard : GameBoard):
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
        input('Send to Jail !')
        player.position = self.jailPosition
        player.jailLeft = self.turn
        gameBoard.addToJailList(player, 150)
        gameBoard.print_board()


    





        





