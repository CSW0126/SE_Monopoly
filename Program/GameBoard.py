from __future__ import annotations,print_function, unicode_literals
from logging import log
from typing import List
from Block import *
from Player import Player
from random import randrange
from data import *
from whaaaaat import prompt
from data import SALARY
import json
import os

class GameBoard:
    def __init__(self, players : List[Player], blocks:List[Block]):
        #game turn
        self.turn    : int = 1
        #player object List
        self.players : List[Player] = players
        #block object list
        self.blocks  : List[Block]= blocks
        #current player
        self.set_current_player(players[0])
        #jail list (player object list) 
        self.jailList: List[Player] = []
        #fine
        self.fine    : int= 0
        self.is_test = False
        self.select_data = []

    def print_board(self):
        self.__reset_owner_of_dead_player()
        ranked_player : List[Player] = self.__sort_ranking()
        #sort the player by money
        #print the game board according to the game stats
        print(f"╔════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╗")
        print(f"║                    ║                    ║                    ║                    ║                    ║                    ║")
        print(f"║ {self.__print_chess(10,1)}                {self.__print_chess(10,4)} ║ {self.__print_chess(11,1)}    {self.blocks[11].name}      {self.__print_chess(11,4)} ║ {self.__print_chess(12,1)}                {self.__print_chess(12,4)} ║ {self.__print_chess(13,1)}    {self.blocks[13].name}    {self.__print_chess(13,4)} ║ {self.__print_chess(14,1)}    {self.blocks[14].name}      {self.__print_chess(14,4)} ║ {self.__print_chess(15,1)}                {self.__print_chess(15,4)} ║")
        print(f"║                    ║                    ║       {self.blocks[12].name}       ║                    ║                    ║                    ║")
        print(f"║ {self.__print_chess(10,2)}     {self.blocks[10].name}       {self.__print_chess(10,5)} ║ {self.__print_chess(11,2)}    HKD:{self.blocks[11].price}     {self.__print_chess(11,5)} ║ {self.__print_chess(12,2)}                {self.__print_chess(12,5)} ║ {self.__print_chess(13,2)}    HKD:{self.blocks[13].price}     {self.__print_chess(13,5)} ║ {self.__print_chess(14,2)}    HKD:{self.blocks[14].price}     {self.__print_chess(14,5)} ║ {self.__print_chess(15,2)}   {self.blocks[15].name}   {self.__print_chess(15,5)} ║")
        print(f"║      {self.blocks[10].subText}       ║      Rent:{self.blocks[11].rent}       ║         {self.blocks[12].subText}          ║      Rent:{self.blocks[13].rent}       ║      Rent:{self.blocks[14].rent}       ║                    ║")
        print(f"║ {self.__print_chess(10,3)}                {self.__print_chess(10,6)} ║ {self.__print_chess(11,3)}                {self.__print_chess(11,6)} ║ {self.__print_chess(12,3)}                {self.__print_chess(12,6)} ║ {self.__print_chess(13,3)}                {self.__print_chess(13,6)} ║ {self.__print_chess(14,3)}                {self.__print_chess(14,6)} ║ {self.__print_chess(15,3)}                {self.__print_chess(15,6)} ║")
        print(f"║                    ║    Owner: {self.__print_owner(self.blocks[11])}     ║                    ║    Owner: {self.__print_owner(self.blocks[13])}     ║    Owner: {self.__print_owner(self.blocks[14])}     ║                    ║")
        print(f"╠════════════════════╬════════════════════╩════════════════════╩════════════════════╩════════════════════╬════════════════════╣")
        print(f"║                    ║                                                                                   ║                    ║")
        print(f"║ {self.__print_chess(9,1)}   {self.blocks[9].name}     {self.__print_chess(9,4)} ║                                                                                   ║ {self.__print_chess(16,1)}    {self.blocks[16].name}    {self.__print_chess(16,4)} ║")
        print(f"║                    ║                                                                                   ║                    ║")
        print(f"║ {self.__print_chess(9,2)}    HKD:{self.blocks[9].price}     {self.__print_chess(9,5)} ║                                                                                   ║ {self.__print_chess(16,2)}    HKD:{self.blocks[16].price}     {self.__print_chess(16,5)} ║")
        print(f"║      Rent:{self.blocks[9].rent}       ║                         ┌──────────────────────────┐                              ║      Rent:{self.blocks[16].rent}       ║")
        print(f"║ {self.__print_chess(9,3)}                {self.__print_chess(9,6)} ║                         │ This Round : Player {self.current_player.player_number}  {self.__print_chess_Text()} │                              ║ {self.__print_chess(16,3)}                {self.__print_chess(16,6)} ║")
        print(f"║    Owner: {self.__print_owner(self.blocks[9])}     ║                         │                          │                              ║    Owner: {self.__print_owner(self.blocks[16])}     ║")
        print(f"╠════════════════════╣                         │     Turn: {self.__print_turn_text()}/100        │                              ╠════════════════════╣")
        print(f"║                    ║                         └──────────────────────────┘                              ║                    ║")
        print(f"║ {self.__print_chess(8,1)}                {self.__print_chess(8,4)} ║                                                                                   ║ {self.__print_chess(17,1)}   {self.blocks[17].name}    {self.__print_chess(17,4)} ║")
        print(f"║       {self.blocks[8].name}       ║      ┌────────────────────────────┐               ┌───────────────────────┐       ║                    ║")
        print(f"║ {self.__print_chess(8,2)}                {self.__print_chess(8,5)} ║      │         Ranking:           │               │        In Jail        │       ║ {self.__print_chess(17,2)}    HKD:{self.blocks[17].price}     {self.__print_chess(17,5)} ║")
        print(f"║         {self.blocks[8].subText}          ║      ├───────┬──────┬─────────────┤               ├──────┬────────────────┤       ║      Rent:{self.blocks[17].rent}       ║")
        print(f"║ {self.__print_chess(8,3)}                {self.__print_chess(8,6)} ║      │  No.{self.__check_rank(ranked_player,0)}│               │ {self.__print_jail_list(0)}│       ║ {self.__print_chess(17,3)}                {self.__print_chess(17,6)} ║")
        print(f"║                    ║      │  No.{self.__check_rank(ranked_player,1)}│               │ {self.__print_jail_list(1)}│       ║    Owner: {self.__print_owner(self.blocks[17])}     ║")
        print(f"╠════════════════════╣      │  No.{self.__check_rank(ranked_player,2)}│               │ {self.__print_jail_list(2)}│       ╠════════════════════╣")
        print(f"║                    ║      │  No.{self.__check_rank(ranked_player,3)}│               │ {self.__print_jail_list(3)}│       ║                    ║")
        print(f"║ {self.__print_chess(7,1)}   {self.blocks[7].name}     {self.__print_chess(7,4)} ║      │  No.{self.__check_rank(ranked_player,4)}│               │ {self.__print_jail_list(4)}│       ║ {self.__print_chess(18,1)}                {self.__print_chess(18,4)} ║")
        print(f"║                    ║      │  No.{self.__check_rank(ranked_player,5)}│               │ {self.__print_jail_list(5)}│       ║       {self.blocks[18].name}       ║")
        print(f"║ {self.__print_chess(7,2)}    HKD:{self.blocks[7].price}     {self.__print_chess(7,5)} ║      └───────┴──────┴─────────────┘               └──────┴────────────────┘       ║ {self.__print_chess(18,2)}                {self.__print_chess(18,5)} ║")
        print(f"║      Rent:{self.blocks[7].rent}       ║                                                                                   ║         {self.blocks[18].subText}          ║")
        print(f"║ {self.__print_chess(7,3)}                {self.__print_chess(7,6)} ║                                                                                   ║ {self.__print_chess(18,3)}                {self.__print_chess(18,6)} ║")
        print(f"║    Owner: {self.__print_owner(self.blocks[7])}     ║                                                                                   ║                    ║")
        print(f"╠════════════════════╣                                                                                   ╠════════════════════╣")
        print(f"║                    ║                                                                                   ║                    ║")
        print(f"║ {self.__print_chess(6,1)}    {self.blocks[6].name}      {self.__print_chess(6,4)} ║                                                                                   ║ {self.__print_chess(19,1)}     {self.blocks[19].name}      {self.__print_chess(19,4)} ║")
        print(f"║                    ║                      {self.__print_text()}                   ║                    ║")
        print(f"║ {self.__print_chess(6,2)}    HKD:{self.blocks[6].price}     {self.__print_chess(6,5)} ║                                                                                   ║ {self.__print_chess(19,2)}    HKD:{self.blocks[19].price}     {self.__print_chess(19,5)} ║")
        print(f"║      Rent:{self.blocks[6].rent}       ║                                                                                   ║      Rent:{self.blocks[19].rent}       ║")
        print(f"║ {self.__print_chess(6,3)}                {self.__print_chess(6,6)} ║                                                                                   ║ {self.__print_chess(19,3)}                {self.__print_chess(19,6)} ║")
        print(f"║    Owner: {self.__print_owner(self.blocks[6])}     ║                                                                                   ║    Owner: {self.__print_owner(self.blocks[19])}     ║")
        print(f"╠════════════════════╬════════════════════╦════════════════════╦════════════════════╦════════════════════╬════════════════════╣")
        print(f"║                    ║                    ║                    ║                    ║                    ║                    ║")
        print(f"║ {self.__print_chess(5,1)}   ┌───────┐    {self.__print_chess(5,4)} ║ {self.__print_chess(4,1)}    {self.blocks[4].name}     {self.__print_chess(4,4)} ║ {self.__print_chess(3,1)}   {self.blocks[3].name}   {self.__print_chess(3,4)} ║ {self.__print_chess(2,1)}   {self.blocks[2].name}     {self.__print_chess(2,4)} ║ {self.__print_chess(1,1)}    {self.blocks[1].name}     {self.__print_chess(1,4)} ║ {self.__print_chess(0,1)} (Salary:${SALARY}) {self.__print_chess(0,4)} ║")
        print(f"║     │{self.blocks[5].name}│      ║                    ║                    ║                    ║                    ║                    ║")
        print(f"║ {self.__print_chess(5,2)}   └───────┘    {self.__print_chess(5,5)} ║ {self.__print_chess(4,2)}    HKD:{self.blocks[4].price}     {self.__print_chess(4,5)} ║ {self.__print_chess(3,2)}    {self.blocks[3].subText}     {self.__print_chess(3,5)} ║ {self.__print_chess(2,2)}   HKD:{self.blocks[2].price}      {self.__print_chess(2,5)} ║ {self.__print_chess(1,2)}    HKD:{self.blocks[1].price}     {self.__print_chess(1,5)} ║ {self.__print_chess(0,2)}       {self.blocks[0].name}       {self.__print_chess(0,5)} ║")
        print(f"║   {self.blocks[5].subText}    ║      Rent:{self.blocks[4].rent}       ║                    ║     Rent:{self.blocks[2].rent}        ║      Rent:{self.blocks[1].rent}       ║                    ║")
        print(f"║ {self.__print_chess(5,3)}                {self.__print_chess(5,6)} ║ {self.__print_chess(4,3)}                {self.__print_chess(4,6)} ║ {self.__print_chess(3,3)}                {self.__print_chess(3,6)} ║ {self.__print_chess(2,3)}                {self.__print_chess(2,6)} ║ {self.__print_chess(1,3)}                {self.__print_chess(1,6)} ║ {self.__print_chess(0,3)}   {self.blocks[0].subText}   {self.__print_chess(0,6)} ║")
        print(f"║                    ║    Owner: {self.__print_owner(self.blocks[4])}     ║                    ║    Owner: {self.__print_owner(self.blocks[2])}     ║    Owner: {self.__print_owner(self.blocks[1])}     ║                    ║")
        print(f"╚════════════════════╩════════════════════╩════════════════════╩════════════════════╩════════════════════╩════════════════════╝")

    def roll_dice(self, player : Player): 
        test_str = []
        if not self.is_test:
            #print the text and ask player to press enter to roll dice
            input('Player ' + str(self.current_player.player_number) + ': Roll Dice! (Press Any Key to Continue)')

        if not self.is_test:
            #get the result of the dice
            dice_result = self.dice()
            input('Dice Result: ' + str(dice_result) + ' (Press Any Key to Continue)')
        else:
            dice_result = self.select_data[0]
        
        #player move to new position
        new_pos = player.position + dice_result
        #if player's new position > 19
        if new_pos > 19:
            #new position -= 20
            new_pos -= 20
            #player add salary
            player.money += SALARY
            if not self.is_test:
                input("Pass the Go Block, add $1500")
        #player move to new position
        player.position = new_pos

        if not self.is_test:
            #call printBoard() to refresh the game board
            self.print_board()
        else:
            test_str.append('print_board.called')

        if not self.is_test:
            #call activate_block_effect(player) to activate the block effect
            self.blocks[self.current_player.position].activate_block_effect(self.current_player, self)
        else:
            test_str.append('activate_block_effect.called')
            return test_str


    def add_to_jail_list(self,player,fine):
        #send to jail block's activate_block_effect(player) method would call this method
        #self.fine = fine
        self.fine = fine
        #self.jailList.append(player)
        self.jailList.append(player)

    def save_game(self):
        #save the game to a file
        players_dict = []
        property_owner_data = []
        game_stat = {}

        for player in self.players:
            players_dict.append(player.__dict__)

        for block in self.blocks:
            if block.__class__.__name__ == 'Property':
                if block.owner != None:
                    property_owner_data.append({'position':block.position, 'owner' : block.owner.player_number})
        
        game_stat['current_player'] = self.__find_next_save_player(self.current_player.player_number)
        game_stat['turn'] = self.turn
        game_stat['fine'] = self.fine
        game_stat['jail_list'] = []
        for player in self.jailList:
            game_stat['jail_list'].append(player.__dict__)
        
        data = {
            'Players' : players_dict,
            'Owner_data' : property_owner_data,
            'Game_stat': game_stat
        }
            
        
        with open('save.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)

        if not self.is_test:
            os._exit(1) 

    def roll_dice_face(self):
        #[1,2,3], [1,2,4], [1,3,4], [2,3,4]
        #return the dice face index (0-3)
        result = randrange(4)
        #print(result)
        return result

    def dice(self):
        #call roll_dice_face()
        face_index : int = self.roll_dice_face()
        #[1,2,3], [1,2,4], [1,3,4], [2,3,4]
        dice_face = DICE[face_index]
        #roll the num inside of the face (0-2)
        num_index = randrange(3)
        dice_result = dice_face[num_index]
        #return the number
        pos3_num = dice_result
        if num_index == 0:
            pos1_num = dice_face[1]
            pos2_num = dice_face[2]
        elif num_index == 1:
            pos1_num = dice_face[2]
            pos2_num = dice_face[0]
        elif num_index == 2:
            pos1_num = dice_face[0]
            pos2_num = dice_face[1]

        #DRAW THE DICE
        #print(dice_face)
        #print(dice_result)
        if not self.is_test:
            print("     ╱ ╲  ")
            print("    ╱   ╲ ")
            print("   ╱     ╲ ")
            print(f"  ╱ {str(pos1_num)}   {str(pos2_num)} ╲ ")
            print(" ╱         ╲ ")
            print(f"╱     {str(pos3_num)}     ╲")
            print("───────────── ")

        #test
        #return 1
        return dice_result

    def set_current_player(self, player:Player):
        #set the current player
        self.current_player : Player = player

    def run(self):
        log_str = []
        #main logic of the game
        #print game board
        if not self.is_test:
            self.print_board()

        while self.turn < MAX_TURN:
            if self.current_player.is_in_jail():
                if not self.is_test:
                    #print in jail option
                    self.__in_jail_option()
                else:
                    log_str.append("__in_jail_option().call")
            else:
            #if current player not in jail:
                if not self.is_test:
                    #roll dice
                    self.print_board()
                    self.roll_dice(self.current_player)
                else:
                    log_str.append('roll_dice().call')

            #change current player to next player
            current_player_no : int = self.current_player.player_number
            count = 0
            new_no = current_player_no
            while True:
                #if 1 player left
                remaining_player = 0
                for player in self.players:
                    if player.is_alive():
                        remaining_player += 1
                if remaining_player == 1:
                    if not self.is_test:
                        self.__print_winner_list()
                    else:
                        log_str.append('self.__print_winner_list().called when all player dead')
                        return log_str


                new_no += 1
                count += 1

                try:
                    found = False
                    #found next player
                    for player in self.players:
                        if player.player_number == new_no:
                            next_player = player
                            found = True
                            break

                    if not found:
                        #if no next player, set to first player
                        new_no = 1
                        self.turn += 1
                        next_player = self.players[0]
                except:
                    self.turn += 1
                    new_no = 1
                    #if out of bound exception, reset to first player
                    next_player = self.players[0]

                if next_player.is_alive():
                    self.current_player = next_player
                    break

            #if test, only test 1 loop
            if self.is_test:
                break
                
        #end while loop, it means turn == Max_turn
        #end game
        #print winner list
        if not self.is_test:
            self.__print_winner_list()
        else:
            log_str.append('__print_winner_list().called out of the while loop')
            return log_str

    def __roll_dice_twice(self):
        #call roll_dice_face twice
        #if two face are the same, pass = true, else False
        result1 = self.roll_dice_face()
        result2 = self.roll_dice_face()
        print("     ╱ ╲                      ╱ ╲")
        print("    ╱   ╲                    ╱   ╲")
        print("   ╱     ╲                  ╱     ╲")
        print(f"  ╱ {DICE[result1][0]}   {DICE[result1][1]} ╲       VS       ╱ {DICE[result2][0]}   {DICE[result2][1]} ╲ ")
        print(" ╱         ╲              ╱         ╲")
        print(f"╱     {DICE[result1][2]}     ╲            ╱     {DICE[result2][2]}     ╲")
        print("─────────────            ───────────── ")
        if result1 == result2:
            #if pass, jail_left of player = 0, current player remove from the jailList
            self.current_player.jail_left = 0
            self.jailList = [i for i in self.jailList if i.player_number != self.current_player.player_number]
            input("Two face are the same! (Enter to continue)")
            #call printBoard()
            self.print_board()
        else:
            input("Two face are Not the same! ")
            #if not pass, current player's jail_left -= 1
            self.current_player.jail_left -= 1
            #if jail_left == 0, remove current from the jailList, current player's money -= fine
            self.print_board()
            input('Jail Turn - 1 !')
            if self.current_player.jail_left == 0:
                self.jailList = [i for i in self.jailList if i.player_number != self.current_player.player_number]
                self.current_player.money -= self.fine 

                self.print_board()
                input("Jail Turn become 0, pay $150 as fine!")

    
    def __in_jail_option(self):
        #ask for roll dice twice OR Pay the fine OR save game
        self.print_board()
        enter_jail[0]['message'] = f'Player {self.current_player.player_number}  You are in Jail, You can pay $150 / roll the dice twice with same face to leave. (After 3 turns, you still need to pay $150)'
        ans = prompt(enter_jail)
        #if roll dice twice:
        if ans['ans'] == 'Roll dice twice !':
            self.__roll_dice_twice()

        #if pay fine:
        elif ans['ans'] == 'Pay the fine !':
            #if player.money -= fine < 0, 
            if self.current_player.money - self.fine < 0:
                #print the text not enough money
                input(f"Player {self.current_player.player_number} You do not have enough money! (Replace the action to Roll dice twice)")
                #go to roll dice twice option
                self.__roll_dice_twice()
            else:
                #current player.money -= fine
                self.current_player.money -= self.fine
                #current player.jail_left = 0
                self.current_player.jail_left = 0
                #remove current player from jailList
                self.jailList = [i for i in self.jailList if i.player_number != self.current_player.player_number]
                #call printBoard() to refresh the game board
                self.print_board()
            #else (save_game)
        else:
            #call save_game()
            self.save_game()

    def __find_next_save_player(self, current_save_player_number):
        new_save_no = current_save_player_number
        next_save_player = None
        while True:
            remain_save_player = 0
            for player in self.players:
                if player.is_alive():
                    remain_save_player += 1
                
            new_save_no += 1

            found = False
            #found next player
            for save_player in self.players:
                if save_player.player_number == new_save_no:
                    next_save_player = save_player
                    found = True
                    break
                
            if not found:
                new_save_no = 1
                self.turn += 1
                next_save_player = self.players[0]

            if next_save_player.is_alive():
                return next_save_player.player_number
        return 0

    #----------------------Print Text Related method-------------------------
    def __print_winner_list(self):
        winner_list  : List[Player] = []
        winner_money : int = 0

        sorted_player = self.__sort_ranking()
        for index, player in enumerate(sorted_player):
            if index == 0:
                winner_money = player.money
                winner_list.append(player)
            else:
                if player.money == winner_money:
                    winner_list.append(player)
                else:
                    break
        print('Winner Are:')    
        for player in winner_list:
            print('            Player ' + str(player.player_number) +" "+ BoardColor[f'P{str(player.player_number)}'].value + '♣' +BoardColor.END.value + ' with money : $' + str(player.money))

        
        print('\n\n\n\n\n\n')
        exit()

    def __sort_ranking(self):
        return sorted(self.players, key=lambda x: x.money, reverse=True)

    def __print_chess(self, position:int , player_number: int):
        try:
            for player in self.players:
                if player.player_number == player_number and player.position == position:
                    return BoardColor[f'P{str(player_number)}'].value + '♣' + BoardColor.END.value
            return ' '
        except:
            return ' '

    def __print_owner(self, block:Block):
        if block.owner is None:
            return 'None'
        else:
            return 'P' + str(block.owner.player_number) + '  '

    def __print_jail_list(self, position):
        if self.jailList:
            try:
                n = self.jailList[position].player_number
                return 'P' + str(n) + ' ' + BoardColor[f'P{str(n)}'].value + '♣' +BoardColor.END.value + ' │ ' + str(self.jailList[position].jail_left)+ ' Turn(s) Left '
            except:
                return '     │                '
        else:
            return '     │                '

    def __check_rank(self, ranked_player : List[Player], position: int):
        rank = []
        lastRank = 1
        for index, player in enumerate(ranked_player):
            if index == 0:
                rank.append(lastRank)
                continue
            else:
                if player.money == ranked_player[index-1].money:
                    rank.append(lastRank)
                else:
                    lastRank += 1
                    rank.append(lastRank)

        try:
            moneyStr = str(ranked_player[position].money)

            while len(moneyStr) < 11:
                moneyStr += ' '
            n = str(ranked_player[position].player_number)

            return str(rank[position]) + ' │ P' + n + " " + BoardColor[f'P{str(n)}'].value + '♣' +BoardColor.END.value + ' │ $'+ moneyStr
        except:
            return '- │      │             '

    def __print_chess_Text(self):
        currentNo = self.current_player.player_number
        string = BoardColor[f'P{currentNo}'].value + '♣' + BoardColor.END.value
        return string

    def __print_turn_text(self):
        string = ''
        if self.turn < 10:
            string =  '  ' + str(self.turn)
        elif self.turn < 100:
            string = ' ' + str(self.turn)
        else:
            string = str(self.turn)

        return string

    def __print_text(self):
        string = ''
        MAX = 6
        for i in range(len(self.players)):
            if i == max:
                break
            string += ('P' + str(i+1)+ " "+BoardColor[f'P{i+1}'].value + '♣' + BoardColor.END.value +"   ")

        for i in range(MAX-len(self.players)):
            string += "       "
        return string
    #END ----------------------Print Text Related method-------------------------

    def __reset_owner_of_dead_player(self):
        #for each block
        for block in self.blocks:
            #only consider the Property Block
            if block.__class__.__name__ == 'Property':
                #if have owner
                if block.owner != None:
                    #check if it is alive
                    if not block.owner.is_alive():
                        #if not, reset the block owner:
                        block.reset_owner()