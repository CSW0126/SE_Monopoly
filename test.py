
from typing import Any


class Player:
    def __init__(self, id: dict, money):
        self._id = id
        self.money = money


a = Player({'1':1},100)

print(str(a.money))

a.money = 120

print(str(a.money))