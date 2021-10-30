from __future__ import print_function, unicode_literals, annotations
from whaaaaat import prompt
from data import *

class Menu:

    def print_menu(self):
        #print header
        for line in game_logo:
            print(line)

        #print select options
        answers = prompt(questions, style=style)

        #if answer is 'New Game', return 0
        if answers['select'] == 'New Game': return 0

        #if answer is 'Continue', return 1
        elif answers['select'] == 'Continue': return 1

        #if answer is 'Check Game Rule', print the game rule
        elif answers['select'] == 'Check Game Rule':
            #print the game rule
            print("\n------------------------------------")
            for line in rule:
                print(line)
            print("------------------------------------\n")

            #show option back
            back = prompt(game_rule_back, style=style)
            print(back)
            #if back is selected, call print_menu() again
            if back['choice'] == 'Back':
                self.print_menu()
        
        #if answer is 'Exit', call exit()
        else: exit()