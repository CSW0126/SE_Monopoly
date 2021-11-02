# Cheung Sui Wing (21027547D)
# Lau Man Chun (21027257D)
# Kwong Chun Him (21028468D)
# Cheng Chi Kit (21028079D)

import sys
from unittest import TestCase
import unittest
from data import *
from Block import *
from Player import *
from GameBoard import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_gameBoard.py -v
#OR
#python -m unittest discover  -p 'test_*.py' -v

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
        #assume roll 1
        self.game_board.select_data.append(1)


        #case 1:
        #set player position in 19
        self.game_board.players[0].position = 19
        #original money of the player
        org_money = self.game_board.players[0].money
        #function call str
        logStr = self.game_board.roll_dice(self.game_board.players[0])
        
        #if roll 1 , player go to Start block, salary += 1500
        #player position should be in 0
        self.assertEqual(self.game_board.players[0].position, 0)
        #player money should be + 1500 (org+2000)
        self.assertEqual(self.game_board.players[0].money, (org_money + 1500))
        #2 function call
        self.assertTrue('print_board.called' in logStr)
        self.assertTrue('activate_block_effect.called' in logStr)

        #case 2, 
        #not > 19, player position += 1
        self.game_board.players[0].position = 18
        #original money of the player
        org_money = self.game_board.players[0].money
        #function call str
        logStr = self.game_board.roll_dice(self.game_board.players[0])
        #position is 19
        self.assertEqual(self.game_board.players[0].position, 19)
        #money no change
        self.assertEqual(self.game_board.players[0].money, org_money)
        #2 function call
        self.assertTrue('print_board.called' in logStr)
        self.assertTrue('activate_block_effect.called' in logStr)

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

        #generate save data
        game_data = {
            'Players' : players_dict,
            'Owner_data' : property_owner_data,
            'Game_stat': game_stat
        }

        #call save game, it would generate the save.txt
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
        #case 1 , current player in jail, call __in_jail_option
        test_player : Player = self.game_board.players[5]  #player 5 should be the last player, end when this player's round end
        self.game_board.add_to_jail_list(test_player, 150)
        self.game_board.set_current_player(test_player)
        test_player.jail_left = 3
        self.game_board.turn = 99 #1 round left

        log_str = self.game_board.run()

        #should call jail option then call print winner list out of the while loop,
        self.assertTrue("__in_jail_option().call" in log_str)
        #current turn >= MAX_TURN, call __print_winner_list
        self.assertTrue("__print_winner_list().called out of the while loop" in log_str)
        self.assertEqual(len(log_str), 2)  #should only contain 2 element
        #turn should be 100 current turn >= MAX_TURN, call __print_winner_list
        self.assertEqual(self.game_board.turn, 100)


        #case 2 , current player not in jail call roll_dice
        test_player : Player = self.game_board.players[0]
        self.game_board.turn = 1
        self.game_board.set_current_player(test_player)
        test_player.jail_left = 0
        test_player.position = 0

        log_str = self.game_board.run()
        #current player is players[1]
        self.assertEqual(self.game_board.current_player, self.game_board.players[1])
        self.assertTrue('roll_dice().call' in log_str)
        self.assertEqual(self.game_board.turn, 1) #turn should not change


        #all other situation of changing current player:

        #set player[1] dead, current player would skip this player
        test_player : Player = self.game_board.players[0]
        self.game_board.turn = 1
        self.game_board.set_current_player(test_player)
        self.game_board.players[1].money = -1000

        log_str = self.game_board.run()
        #should go to player[2]
        self.assertEqual(self.game_board.current_player, self.game_board.players[2])
        self.assertEqual(self.game_board.turn, 1)

        #player[2] also dead, should go from [0] to [3]
        self.game_board.players[2].money = -1000
        test_player : Player = self.game_board.players[0]  # current [0]
        self.game_board.turn = 1
        self.game_board.set_current_player(test_player)
        self.game_board.run()
        self.assertEqual(self.game_board.current_player, self.game_board.players[3]) # [0] to [3]
        self.assertEqual(self.game_board.turn, 1) #still 1


        #reset player data
        for player in self.game_board.players:
            player.money = 1000
            player.jail_left = 0
            player.position = 1

        #if player [5] dead, current player is [4], change to [0]
        #turn + 1
        test_player : Player = self.game_board.players[4]  # current [4]
        self.game_board.players[5].money = -1000           # [5] dead
        self.game_board.set_current_player(test_player)    # set current to [4]
        self.game_board.turn = 1
        self.game_board.run()

        self.assertEqual(self.game_board.current_player, self.game_board.players[0]) #current become [0]
        self.assertEqual(self.game_board.turn, 2)                                    # turn become 2


        #reset player data
        for player in self.game_board.players:
            player.money = 1000
            player.jail_left = 0
            player.position = 1
        #if player [5][0] dead, current player is [4] change to [1]
        #turn + 1
        test_player : Player = self.game_board.players[4]  # current [4]
        self.game_board.players[5].money = -1000           # [5] dead
        self.game_board.players[0].money = -1000           # [0] dead
        self.game_board.set_current_player(test_player)    # set current to [4]
        self.game_board.turn = 2                           # turn 2
        self.game_board.run()

        self.assertEqual(self.game_board.current_player, self.game_board.players[1]) #current become [1]
        self.assertEqual(self.game_board.turn, 3)                                    # turn become 3


        #set all player dead, call print winner list
        for player in self.game_board.players:
            player.money = -1000
            player.jail_left = 0
            player.position = 1

        #only player[2] left
        test_player : Player = self.game_board.players[2]  # current [2]
        test_player.money = 1000
        self.game_board.set_current_player(test_player)    # set current to [2]
        self.game_board.turn = 2
        log_str = self.game_board.run()

        self.assertTrue('self.__print_winner_list().called when all player dead' in log_str)

if __name__ == '__main__':
    unittest.main()