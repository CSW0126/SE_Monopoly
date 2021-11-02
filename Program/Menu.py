from __future__ import print_function, unicode_literals, annotations
from whaaaaat import prompt
from data import *

class Menu:
    def __init__(self):
        self.is_test = False
        self.select_data = []

    def print_menu(self):
        #print header
        if not self.is_test:
            for line in game_logo:
                print(line)

        #print select options
        answers = {}
        if not self.is_test:
            answers = prompt(questions, style=style)
        else:
            answers['select'] = self.select_data[0]

        #if answer is 'New Game', return 0
        if answers['select'] == 'New Game': return 0

        #if answer is 'Continue', return 1
        elif answers['select'] == 'Continue': return 1

        #if answer is 'Check Game Rule', print the game rule
        elif answers['select'] == 'Check Game Rule':
            if not self.is_test:
                #print the game rule
                print("\n------------------------------------")
                for line in rule:
                    print(line)
                print("------------------------------------\n")

            back = {}
            if not self.is_test:
                #show option back
                back = prompt(game_rule_back, style=style)
            else:
                back['choice'] = self.select_data[1]
            #print(back)
            #if back is selected, call print_menu() again
            if back['choice'] == 'Back':
                if not self.is_test:
                    self.print_menu()
                else:
                    return 2
        
        #if answer is 'Exit', call exit()
        else: 
            if not self.is_test:
                exit()
            else:
                return 3