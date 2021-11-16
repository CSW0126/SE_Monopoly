from __future__ import print_function, unicode_literals
import sys
from whaaaaat import prompt
from typing import List
from Block import *
from GameBoard import GameBoard
from Menu import Menu
from Player import *
from data import *
import json
import os

os.system("color")
block_list  : List[Block]= []
player_list : List[Player] = []


def main():
    #Main program
    #import Menu.py
    #Call the method print_menu()
    choice = Menu().print_menu()
    #if choice == 0:
        #new Game
    if choice == 0:
        player_list, block_list = start_new_game()
        GameBoard(player_list,block_list).run()

    #if choice == 1:
    elif choice == 1:
        print("read Save")
        try:
            #read save
            f = open('save.txt')
            data = json.load(f)
            f.close()
            game_board = load_game(data)
            game_board.run()
        except:
            #no Save file, start new game
            input('No save, press Any Key to Start New Game')
            player_list, block_list =  start_new_game()
            GameBoard(player_list,block_list).run()
            

    
def start_new_game():
    players : List[Player] = []
    #ask how many player (2-6):
    ans = prompt(ask_how_many_player, style=style)
    #generate players according of the input
    for i in range(int(ans['ans'])):
        temp = Player(i+1, START_MONEY, 0)
        players.append(temp)
    #add all to player_list
    player_list = players

    #generate all Block object according to the property json on data.py
    blocks :List[Block] = []
    for item in property_data:
        class_ = getattr(sys.modules[__name__],item['Type'])
        blocks.append(class_(item))
    #add all to block_list
    block_list = blocks

    return player_list, block_list

def load_game(data : dict):
    players : List[Player] = []
    blocks :List[Block] = []
    #generate all player object according to the saved data
    player_dict = data['Players']
    owner_data = data['Owner_data']
    game_stat = data['Game_stat']

    #generate all player object according to the saved data
    for item in player_dict:
        player = Player(item['player_number'],item['money'],item['position'])
        player.jail_left = item['jail_left']
        players.append(player)

    #generate all block object according to the property json on data.py
    for item in property_data:
        class_ = getattr(sys.modules[__name__],item['Type'])
        blocks.append(class_(item))

    for item in owner_data:
        owner_number = item['owner']
        block_position = item['position']
        owner : Player = get_player_by_number(players,owner_number)


        for block in blocks:
            if block.position == block_position:
                if owner != None:
                    block.set_owner(owner)
                    break

    #set all game stats of game_board according to the saved data
    game_board = GameBoard(players,blocks)
    game_board.set_current_player(get_player_by_number(players,game_stat['current_player']))
    game_board.turn = game_stat['turn']
    game_board.fine = game_stat['fine']

    player_number_list_in_jail = []
    for item in game_stat['jail_list']:
        player_number_list_in_jail.append(item['player_number'])

    for num in player_number_list_in_jail:
        player_in_jail = get_player_by_number(players, num)
        game_board.add_to_jail_list(player_in_jail,game_stat['fine'])

    return game_board
    
if __name__ == "__main__":
   main()