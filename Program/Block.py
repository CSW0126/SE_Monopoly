from __future__ import annotations,print_function, unicode_literals
from abc import ABC, abstractclassmethod
from typing import Dict
from whaaaaat import prompt
from random import randrange
from Player import Player
from GameBoard import GameBoard
from data import *

class Block(ABC):
    def __init__(self, block_data: dict):
        self.block_data : Dict = block_data
        self.position   : int = block_data['Position']
        self.name       : str = block_data['Name']
        self.is_test     : bool = False
        self.selection_data : dict = []
    
    @abstractclassmethod
    def activate_block_effect(self, player: Player , game_board : GameBoard):
        #print save game option
        ans = []
        if not self.is_test:
            ans = prompt(no_effect_block)
        else:
            ans['ans'] = self.selection_data[0]
        #call gameboard.save_game()
        if ans['ans'] == 'Save Game !': game_board.save_game()

# Start Block
class Start(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText : str = block_data['SubText']

    def activate_block_effect(self, player: Player, game_board: GameBoard): 
        #call super() no effect
        return super().activate_block_effect(player,game_board)

# Property Block
class Property(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.price : int = block_data['Price']
        self.rent  : int = block_data['Rent']
        self.owner : Player = None

    def reset_owner(self):
        self.owner = None

    def set_owner(self, player: Player):
        self.owner = player

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        enter_property[0]['choices'] = []
        choice = enter_property[0]['choices']
        #if owner is None:
        if self.owner is None:
            #if player.money < price:
            if player.money < self.price:
                #print not enough money,
                enter_property[0]['message'] ='Player ' + str(player.player_number) + ': Not enough money to buy the property !'
                #print option Pass, Save Game
                choice.append('Pass !')
                choice.append('Save Game !')
                ans = prompt(enter_property)
                #if ans is Pass, pass,
                #if ans is Save Game, call game_board.save_game()
                if ans['ans'] == 'Save Game !': game_board.save_game()
            else:
            #if player.money >= price:
                enter_property[0]['message'] ='Player ' + str(player.player_number) + ': Buy the property ?'
                #Ask player to buy the property
                #print the option Buy, Pass, Save Game
                choice.append('Buy !')
                choice.append('Pass !')
                choice.append('Save Game !')
                ans = prompt(enter_property)

                #if buy, player.money -= price, set_owner(player), printGameboard()
                if ans['ans'] ==  'Buy !':
                    self.owner = player
                    self.owner.money -= self.price
                    game_board.print_board()
                #if pass, pass
                #if save Game, save Game
                elif ans['ans'] == 'Save Game !':
                    game_board.save_game()

        #if owner is the player:
        elif self.owner.player_number == player.player_number:
            #print no effect
            enter_property[0]['message'] = 'You are the owner, no effect !'
            #print option pass , save game
            choice.append('Pass !')
            choice.append('Save Game !')
            ans = prompt(enter_property)
            #if pass, pass
            #if save game, call game_board.save_game()
            if ans['ans'] == 'Save Game !': game_board.save_game()

        #if owner is not None and owner is not the player
        else:
            #pay rent
            #if player.money - rent < 0
            if player.money - self.rent < 0:
                #player do not have enough money to play the rent, only add the remaining money to the owner
                #owner += player.money
                self.owner.money += player.money
                
                #player.money -= rent
                player.money -= self.rent
                #printGameboard()
                game_board.print_board()
                #print message 'do not have enough money to pay ....'
                input('Not enough money to pay the rent ! All remaining money add to the owner P' + str(self.owner.player_number))
            
            else:
            #if player have enough money to pay
                #owner.money += rent
                self.owner.money += self.rent
                #player.money -= rent
                player.money -= self.rent
                #printGameBoard
                game_board.print_board()
                #print message
                input('Pay the rent $'+ str(self.rent) + ' to P' + str(self.owner.player_number))

# Income Tax Block
class IncomeTax(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText : str = block_data['SubText']
        self.tax     : int = block_data['Tax']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        #calculate the tax: round((player.money*self.tax/100)/10)*10 
        taxNeedToPay =  round((player.money*self.tax/100)/10)*10 
        input('Player ' + str(player.player_number) + ' need to pay the tax: '+ str(taxNeedToPay))
        #player.money -= tax
        player.money -= taxNeedToPay
        #print game board
        game_board.print_board()

# Jail , just visiting
class Jail(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText : str = block_data['SubText']
        self.fine    : int = block_data['Fine']
        self.turn    : int = block_data['Turn']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        #call super() no effect
        return super().activate_block_effect(player,game_board)

# Chance
class Chance(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText : str = block_data['SubText']
        self.min     : int = block_data['min']
        self.max     : int = block_data['max']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        # random 0/1
        # 0 = gain
        # 1 = lose
        gainOrLose = randrange(2)
        result = 0
        #if gain :
        if gainOrLose == 0:
            index = self.max // 10
            result = randrange(index+1)*10
            #print message
            input('Player '+ str(player.player_number) + ' gain $' + str(result))

        #if lose:
        else:
            index = abs(self.min) // 10
            result = randrange(index+1)*-10
            #print message
            input('Player '+ str(player.player_number) + ' Lose $' + str(result))
        player.money += result
        game_board.print_board()

        #player.money += result
        #print game board

# free parking
class FreeParking(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.subText : str = block_data['SubText']

    def activate_block_effect(self, player: Player, game_board : GameBoard):
        #call super() no effect
        return super().activate_block_effect(player,game_board)


#Go to Jail
class GoToJail(Block):
    def __init__(self, block_data):
        super().__init__(block_data)
        self.jail_position : int = block_data['JailPosition']
        self.fine          : int = block_data['Fine']
        self.turn          : int = block_data['Turn']


    def activate_block_effect(self, player: Player, game_board : GameBoard):
        # print message 'Send to Jail !'
        input('Send to Jail !')
        # set player.position = self.jail_position
        player.position = self.jail_position
        # set player.jail_left = self.turn
        player.jail_left = self.turn
        # call game_board.add_to_jail_list(player,self.fine)
        game_board.add_to_jail_list(player, self.fine)
        # print game board
        game_board.print_board()