import sys
from unittest import TestCase
import unittest
from Block import *
from data import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_block.py -v

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
        self.assertEqual(start_block.position, 0)
        self.assertEqual(start_block.__class__.__name__, 'Start')

    
        def test_property_activate_block_effect(self):
            pass

        def test_incomeTest_activate_block_effect(self):
            pass

        def test_jail_activate_block_effect(self):
            pass

        def test_chance_activate_block_effect(self):
            pass

        def test_free_parking_activate_block_effect(self):
            pass

        def test_go_to_jail_activate_block_effect(self):
            pass


if __name__ == '__main__':
    unittest.main()