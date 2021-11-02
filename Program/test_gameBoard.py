import sys
from unittest import mock, TestCase, result
import unittest
from GameBoard import *
from data import *
from Block import *
from Player import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_gameBoard.py -v

class TestGameBoard(TestCase):

    def setUp(self):
        #create players
        self.players :List[Player] = []
        for i in range(6):
            player = Player(i+1,500,0)
            self.players.append(player)

        #create blocks
        self.blocks : List[Block] = []
        for item in property_data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            self.blocks.append(class_(item))

        #create gameboard
        self.game_board : GameBoard = GameBoard(self.players,self.blocks)
        self.game_board.is_test = True

    def test_roll_dice(self):
        #TODO
        pass

    def test_add_to_jail_list(self):
        #TODO
        pass

    def test_save_game(self):
        #TODO
        pass

    def test_roll_dice_face(self):
        results = []
        #random the dice face 1000 times
        for i in range(1000):
            results.append(self.game_board.roll_dice_face())

        #check if the values include, only contain 0-3
        isPass = True
        for item in results:
            if 0 == item or 1 == item or 2 == item or 3 == item:
                continue
            else:
                isPass = False
                break

        #only contain 0-3
        self.assertTrue(isPass)
        #include 0-3       
        self.assertTrue(0 in results)
        self.assertTrue(1 in results)
        self.assertTrue(2 in results)
        self.assertTrue(3 in results)


    def test_dice(self):
        results = []
        #random the dice 1000 times
        for i in range(1000):
            results.append(self.game_board.dice())

        #check if the values include, only contain 1-4
        isPass = True
        for item in results:
            if 1 == item or 2 == item or 3 == item or 4 == item:
                continue
            else:
                isPass = False
                break
        
        #only contain 1-4
        self.assertTrue(isPass)
        #include 1-4       
        self.assertTrue(1 in results)
        self.assertTrue(2 in results)
        self.assertTrue(3 in results)
        self.assertTrue(4 in results)

    
    def test_set_current_player(self):
        #TODO
        pass

    def test_run(self):
        #TODO
        pass

if __name__ == '__main__':
    unittest.main()