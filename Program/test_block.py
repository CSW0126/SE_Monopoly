# Cheung Sui Wing (21027547D)
# Lau Man Chun (21027257D)
# Kwong Chun Him (21028468D)
# Cheng Chi Kit (21028079D)

import sys
from unittest import TestCase
import unittest
from Block import *
from data import *
from Player import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_block.py -v
#OR
#python -m unittest discover  -p 'test_*.py' -v

class TestBlock(TestCase):
    
    def test_start_activate_block_effect(self):
        #Start

        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        start_block = blocks[0] 
        start_block.is_test = True

        #select save game
        start_block.selection_data.append('Save Game !')
        result = start_block.activate_block_effect(players, game_board)
        self.assertEqual(result, 'game_board.save_game() called')

        #select pass
        start_block.selection_data[0] = 'Pass'
        result = start_block.activate_block_effect(players, game_board)
        self.assertEqual(result, 'pass')

        #attr check
        self.assertEqual(start_block.name, 'Go')
        self.assertEqual(start_block.subText, '<---------')
        self.assertEqual(start_block.position, 0)
        self.assertEqual(start_block.__class__.__name__, 'Start')

    
    def test_property_activate_block_effect(self):
        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,1500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        property_block = blocks[1] 
        property_block.is_test = True

        #select save game(no owner)
        property_block.selection_data.append('Save Game !')
        result = property_block.activate_block_effect(get_player_by_number(players, 1), game_board)
        self.assertEqual(result, 'game_board.save_game() called')

        #select pass(no owner)
        property_block.selection_data[0] = 'Pass'
        result = property_block.activate_block_effect(get_player_by_number(players, 1), game_board)
        self.assertEqual(result, 'pass')

        # select buy
        property_block.selection_data[0] = 'Buy !'
        result = property_block.activate_block_effect(get_player_by_number(players, 1), game_board)
        self.assertEqual(result, 'Buy !')
        self.assertEqual(property_block.owner, get_player_by_number(players, 1))

        # when onwer go to his/her property
        property_block.selection_data[0] = ('Save Game !')
        result = property_block.activate_block_effect(get_player_by_number(players, 1), game_board)
        self.assertEqual(property_block.owner, get_player_by_number(players, 1))
        self.assertEqual(result, 'game_board.save_game() called')

        # test pay rent to the owner(has enough money)
        expected_player = get_player_by_number(players, 2)
        expected_owner = get_player_by_number(players, 1)
        expected_owner_money_result = expected_owner.money + property_block.rent
        expected_player_money_result = expected_player.money - property_block.rent
        result = property_block.activate_block_effect(get_player_by_number(players, 2), game_board)
        self.assertEqual(result, 'Pay the rent $'+ str(property_block.rent) + ' to P' + str(expected_owner.player_number))
        self.assertEqual(expected_owner_money_result, property_block.owner.money)
        self.assertEqual(expected_player_money_result, get_player_by_number(players, 2).money)

        # test pay rent to the owner(has enough money)
        expected_player = get_player_by_number(players, 2)
        expected_player.money = 5
        expected_owner = get_player_by_number(players, 1)
        expected_owner_money_result = expected_owner.money + expected_player.money
        expected_player_money_result = expected_player.money - property_block.rent
        result = property_block.activate_block_effect(get_player_by_number(players, 2), game_board)
        self.assertEqual(result, 'Not enough money to pay the rent ! All remaining money add to the owner P' + str(expected_owner.player_number))
        self.assertEqual(expected_owner_money_result, property_block.owner.money)
        self.assertEqual(expected_player_money_result, get_player_by_number(players, 2).money)

        #attr check
        self.assertEqual(property_block.name, 'Central')
        self.assertEqual(property_block.position, 1)
        self.assertEqual(property_block.__class__.__name__, 'Property')

    def test_income_tax_activate_block_effect(self):
        # income tax

        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        income_block = blocks[3] 
        income_block.is_test = True

        # check income tax output
        taxNeedToPay =  round((get_player_by_number(players, 1).money*income_block.tax/100)/10)*10 
        result = income_block.activate_block_effect(get_player_by_number(players, 1), game_board)
        self.assertEqual(result, 'Player ' + str(get_player_by_number(players, 1).player_number) + ' need to pay the tax: '+ str(taxNeedToPay))

        #attr check
        self.assertEqual(income_block.name, 'Income Tax')
        self.assertEqual(income_block.position, 3)
        self.assertEqual(income_block.__class__.__name__, 'IncomeTax')

    def test_jail_activate_block_effect(self):
        #Jail

        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        jail_block = blocks[5] 
        jail_block.is_test = True

        #select save game
        jail_block.selection_data.append('Save Game !')
        result = jail_block.activate_block_effect(players, game_board)
        self.assertEqual(result, 'game_board.save_game() called')

        #select pass
        jail_block.selection_data[0] = 'Pass'
        result = jail_block.activate_block_effect(players, game_board)
        self.assertEqual(result, 'pass')

        #attr check
        self.assertEqual(jail_block.name, 'In Jail')
        self.assertEqual(jail_block.subText, 'Just Visiting')
        self.assertEqual(jail_block.position, 5)
        self.assertEqual(jail_block.__class__.__name__, 'Jail')

    def test_chance_activate_block_effect(self):
        # chance

        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        chance_block = blocks[8] 
        chance_block.is_test = True

        # chance to gain money 
        chance_block.selection_data.append(0)
        expected_player = get_player_by_number(players, 1)
        result = chance_block.activate_block_effect(expected_player, game_board)
        self.assertIn('Player '+ str(expected_player.player_number) + ' gain $', result)

        # chance to lose money
        chance_block.selection_data[0] = 1
        expected_player = get_player_by_number(players, 1)
        result = chance_block.activate_block_effect(expected_player, game_board)
        self.assertIn('Player '+ str(expected_player.player_number) + ' Lose $', result)

        #attr check
        self.assertEqual(chance_block.name, 'Chance')
        self.assertEqual(chance_block.subText, '?')
        self.assertEqual(chance_block.position, 8)
        self.assertEqual(chance_block.__class__.__name__, 'Chance')


    def test_free_parking_activate_block_effect(self):
        # free parking

        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        free_parking_block = blocks[10] 
        free_parking_block.is_test = True

        #select save game
        free_parking_block.selection_data.append('Save Game !')
        result = free_parking_block.activate_block_effect(players, game_board)
        self.assertEqual(result, 'game_board.save_game() called')

        #select pass
        free_parking_block.selection_data[0] = 'Pass'
        result = free_parking_block.activate_block_effect(players, game_board)
        self.assertEqual(result, 'pass')

        #attr check
        self.assertEqual(free_parking_block.name, 'Free')
        self.assertEqual(free_parking_block.subText, 'Parking')
        self.assertEqual(free_parking_block.position, 10)
        self.assertEqual(free_parking_block.__class__.__name__, 'FreeParking')

    def test_go_to_jail_block_effect(self):
        # go to jail 

        #create players
        players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            players.append(player)

        #create blocks
        blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            blocks.append(class_(item))

        #create gameboard
        game_board : GameBoard = GameBoard(players,blocks)

        #set to test mode
        go_to_jail_block = blocks[15] 
        go_to_jail_block.is_test = True

        # check send to jail output
        # go_to_jail_block.selection_data.append('Save Game !')
        result = go_to_jail_block.activate_block_effect(get_player_by_number(players, 1), game_board)
        self.assertEqual(result, 'Send to Jail !')

        # #select pass
        # go_to_jail_block.selection_data[0] = 'Pass'
        # result = go_to_jail_block.activate_block_effect(get_player_by_number(players, 0), game_board)
        # self.assertEqual(result, 'pass')

        #attr check
        self.assertEqual(go_to_jail_block.name, 'Go To Jail')
        self.assertEqual(go_to_jail_block.position, 15)
        self.assertEqual(go_to_jail_block.__class__.__name__, 'GoToJail')
        # check the player position change to jail or not
        self.assertEqual(get_player_by_number(players, 1).position, go_to_jail_block.jail_position)
        # check the player jail left turn is equal to initial jail turn or not
        self.assertEqual(get_player_by_number(players, 1).jail_left, go_to_jail_block.turn)
        # check the player is add to jail list or not
        # self.assertEqual(get_player_by_number(players, 1), game_board.jailList[0])
        self.assertIn(get_player_by_number(players, 1), game_board.jailList)


if __name__ == '__main__':
    unittest.main()