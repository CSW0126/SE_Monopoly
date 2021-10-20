from data import SALARY


class Player:
    def __init__(self, player_number, money , position):
        self.player_number = player_number
        self.money = money
        self.position = position
        self.jail_left = 0

    def pay_money(self, money):
        self.money -= money

    def add_money(self, money):
        self.money += money


    def is_alive(self):
        if self.money > 0:
            return True
        else:
            return False

    def is_in_jail(self):
        if self.jail_left > 0 :
            return True
        else:
            return False