
from typing import List
from Block import Block
from Player import Player


class GameBoard:
    def __init__(self, players : List[Player], blocks:List[Block]):
        #game turn
        self.turn = 1
        #player object List
        self.players = players
        #block object list
        self.blocks = blocks
        #current player
        self.set_current_player(players[0])
        #jail list (player object list) 
        self.jailList = []
        #fine
        self.fine = 0

    def print_board(self):
        #sort the player by money
        #print the game board according to the game stats
        pass

    def roll_dice(self, player : Player): 
        #print the text and ask player to press enter to roll dice
        #get the result of the dice
        #player move to new position
            #if player's new position > 19
                #new position -= 20
                #player add salary
                #player move to new position
            #else
                #player move to new position

        #call printBoard() to refresh the game board

        #call activate_block_effect(player) to activate the block effect
        pass

    def add_to_jail_list(self,player,fine):
        #send to jail block's activate_block_effect(player) method would call this method
        #self.fine = fine
        #self.jailList.append(player)
        pass

    def save_game(self):
        #save the game to a file
        exit()

    def roll_dice_face(self):
        #[1,2,3], [1,2,4], [1,3,4], [2,3,4]
        #return the dice face index (0-3)
        pass

    def dice(self):
        #call roll_dice_face()
        #[1,2,3], [1,2,4], [1,3,4], [2,3,4]
        #roll the num inside of the face (0-2)
        #return the number
        pass

    def run(self):
        #main logic of the game
        #print game board

        #while self.turn < Max_Turn:
            #if self.currentPlayer.is_in_jail():

                #ask for roll dice twice OR Pay the fine OR save game
                #if roll dice twice:
                    #call roll_dice_face twice
                    #if two face are the same, pass = true, else False
                    #if pass, jail_left of player = 0, current player remove from the jailList
                    #if not pass, current player's jail_left -= 1
                        #if jail_left == 0, remove current from the jailList, current player's money -= fine
                    #call printBoard()
            
                #if pay fine:
                    #if player.money -= fine < 0, 
                        #print the text not enough money
                        #go to roll dice twice option
                    #else
                        #current player.money -= fine
                        #current player.jail_left = 0
                        #remove current player from jailList
                        #call printBoard() to refresh the game board
                        #call roll_dice to move

                #else (save_game)
                    #call save_game()
            #if current player not in jail:
                #roll dice

            #change current player to next player
            #if next player is dead, next again
            #if out of bound exception, reset to first player
            #if one player left, END game

        #end while loop, it means turn == Max_turn
            #end game
            #print winner list
        pass

