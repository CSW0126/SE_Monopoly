
from __future__ import print_function, unicode_literals
from Block import *
from whaaaaat import prompt
from GameBoard import *
from Player import *
import Menu
import sys
from data import *


blockList = []
playerList = []

def main():
    
    #Menu
    choice = Menu.printMenu()
    if choice == 0:
        #new game
        players = []
        ans = prompt(AskHowManyPlayer, style=style)
        for i in range(int(ans['ans'])):
            #create player
            temp = Player(i+1, Config.START_MONEY, 0)
            players.append(temp)

        playerList = players
        # create block
        blocks = []
        for item in Property_Data:
            class_ = getattr(sys.modules[__name__],item['Type'])
            #print(class_)
            blocks.append(class_(item))
        
        blockList = blocks

    elif choice == 1:
        #continue, read save
        print("read Save")


    GameBoard(playerList,blockList).run()
    

if __name__ == "__main__":
    main()