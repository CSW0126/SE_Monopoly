from typing import List
from data import SALARY


class Player:
    def __init__(self, player_number, money , position):
        self.player_number = player_number
        self.money = money
        self.position = position
        self.jail_left = 0

    def is_alive(self):
        if self.money >= 0:
            return True
        else:
            return False

    def is_in_jail(self):
        if self.jail_left > 0 :
            return True
        else:
            return False

def get_player_by_number(players : List[Player],number : int):
    for player in players:
        if player.player_number == number:
            return player
    return None