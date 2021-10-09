from __future__ import print_function, unicode_literals
from whaaaaat import prompt
from data import *


def printMenu():


    print("  __  __                               _")        
    print(" |  \/  | ___  _ __   ___  _ __   ___ | |_   _  ")
    print(" | |\/| |/ _ \| '_ \ / _ \| '_ \ / _ \| | | | | ")
    print(" | |  | | (_) | | | | (_) | |_) | (_) | | |_| | ")
    print(" |_|  |_|\___/|_| |_|\___/| .__/ \___/|_|\__, | ")
    print("                          |_|            |___/  ")


    answers = prompt(questions, style=style)
    if answers['select'] == 'New Game':
        # New Game, 0
        return 0
    elif answers['select'] == 'Continue':
        # Continue, 1
        return 1
    elif answers['select'] == 'Check Game Rule':
        # Check Game Rule
        #TODO
        print()
        print("------------------------------------")
        print("Rule1: ")
        print("Rule2: ")
        print("------------------------------------")
        print()

        back = prompt(gameRuleBack, style=style)
        print(back)
        if back['choice'] == 'Back':
            printMenu()
    else:
        exit()
    
