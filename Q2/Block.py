from abc import ABC, abstractclassmethod
from random import randrange

from Player import Player
from GameBoard import GameBoard

class Block(ABC):
    def __init__(self, block_data: dict):
        self.block_data = block_data
        self.position = block_data['Position']
        self.name = block_data['Name']
    
    @abstractclassmethod
    def activate_block_effect(self, player: Player , game_board : GameBoard):
        #print save game option
        #call gameboard.save_game()
        pass

# Start Block
class Start(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText = block_data['SubText']

    def activate_block_effect(self, player: Player, game_board: GameBoard): 
        #call super() no effect
        return super().activate_block_effect(player,game_board)

# Property Block
class Property(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.price = block_data['Price']
        self.rent = block_data['Rent']
        self.owner = 'None'

    def reset_owner(self):
        self.owner == 'None'

    def set_owner(self, player: Player):
        self.owner = player

    def activate_block_effect(self, player: Player, game_board : GameBoard):

        #if owner is None:
            #if player.money < price:
                #print not enough money,
                #print option Pass, Save Game
                #if ans is Pass, pass,
                #if ans is Save Game, call game_board.save_game()
            #if player.money >= price:
                #Ask player to buy the property
                #print the option Buy, Pass, Save Game
                #if buy, player.money -= price, set_owner(player), printGameboard()
                #if pass, pass
                #if save Game, save Game

        #if owner is the player:
            #print no effect
            #print option pass , save game
            #if pass, pass
            #if save game, call game_board.save_game()

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
        self.subText = block_data['SubText']
        self.tax = block_data['Tax']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        #calculate the tax: round((player.money*self.tax/100)/10)*10 
        #player.money -= tax
        #print game board
        pass

# Jail , just visiting
class Jail(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText = block_data['SubText']
        self.fine = block_data['Fine']
        self.turn = block_data['Turn']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        #call super() no effect
        return super().activate_block_effect(player,game_board)

# Chance
class Chance(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText = block_data['SubText']
        self.min = block_data['min']
        self.max = block_data['max']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
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
        self.subText = block_data['SubText']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        #call super() no effect
        return super().activate_block_effect(player,game_board)


#Go to Jail
class GoToJail(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.jail_position = block_data['JailPosition']
        self.fine = block_data['Fine']
        self.turn = block_data['Turn']


    def activate_block_effect(self, player: Player, game_board : GameBoard):
        # print message 'Send to Jail !'
        # set player.position = self.jail_position
        # set player.jail_left = self.turn
        # call game_board.add_to_jail_list(player,self.fine)
        # print game board
        pass