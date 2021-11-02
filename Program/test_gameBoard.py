import sys
from textwrap import indent
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

        #add first player to jail, set fine = 150
        self.game_board.add_to_jail_list(self.players[0], 150)
        #check the len of the jailList
        self.assertEqual(len(self.game_board.jailList), 1)
        #check the jail player object ref
        self.assertEqual(self.game_board.jailList[0], self.players[0])
        #check the fine
        self.assertEqual(self.game_board.fine, 150)

        #add next player
        self.game_board.add_to_jail_list(self.players[1],150)
        #check len
        self.assertEqual(len(self.game_board.jailList),2)
        #check player number
        self.assertEqual(self.game_board.jailList[1], self.players[1])

        self.game_board.jailList.clear
    

    def test_save_game(self):
        #fake data
        self.game_board.turn = 2
        self.game_board.add_to_jail_list(self.game_board.players[0],150)
        self.game_board.add_to_jail_list(self.game_board.players[1],150)
        self.game_board.blocks[1].owner = self.game_board.players[0]

        players_dict = []
        property_owner_data = []
        game_stat = {}

        for player in self.game_board.players:
            players_dict.append(player.__dict__)

        for block in self.game_board.blocks:
            if block.__class__.__name__ == 'Property':
                if block.owner != None:
                    property_owner_data.append({'position':block.position, 'owner' : block.owner.player_number})

        game_stat['turn'] = self.game_board.turn
        game_stat['current_player'] = self.game_board.current_player.player_number
        game_stat['fine'] = self.game_board.fine
        game_stat['jail_list'] = []

        for player in self.game_board.jailList:
            game_stat['jail_list'].append(player.__dict__)

        game_data = {
            'Players' : players_dict,
            'Owner_data' : property_owner_data,
            'Game_stat': game_stat
        }

        #call save game
        self.game_board.save_game()

        #read save
        f = open('save.txt')
        actual_data = json.load(f)
        f.close()

        #campare game data with read data
        game_data = json.dumps(game_data, sort_keys=True)
        read_data = json.dumps(actual_data, sort_keys=True)
        self.maxDiff = None
        
        self.assertEqual(read_data,game_data)


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
        #set current player, and match the player number
        for player in self.players:
            self.game_board.set_current_player(player=player)
            self.assertEqual(self.game_board.current_player.player_number, player.player_number)

    def test_run(self):
        #TODO
        pass

if __name__ == '__main__':
    unittest.main()