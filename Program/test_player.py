# Cheung Sui Wing (21027547D)
# Lau Man Chun (21027257D)
# Kwong Chun Him (21028468D)
# Cheng Chi Kit (21028079D)


import unittest
from Player import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_player.py -v
#OR
#python -m unittest discover  -p 'test_*.py' -v

class TestPlayer(unittest.TestCase):
    
    def test_is_alive(self):
        #check player's money, 
        #if money < 0 : False
        #if money >= 0: True

        #money is negative , dead
        player = Player(1,-20, 0)
        self.assertFalse(player.is_alive())

        #money is 0, alive
        player.money = 0
        self.assertTrue(player.is_alive())

        #money > 0, alive
        player.money = 1
        self.assertTrue(player.is_alive())

    def test_is_in_jail(self):
        #check if player in jail
        #if jail_left > 0, True
        #if jail_lef == 0, False

        player = Player(1, 1000, 0)

        #jail_left > 0, true
        player.jail_left = 1
        self.assertTrue(player.is_in_jail())

        #jail_left == 0, false
        player.jail_left = 0
        self.assertFalse(player.is_in_jail())


    def test_pay_money(self):
        #subtraction
        
        player = Player(1, 1000, 0)

        #1000-10=990
        player.pay_money(10)
        self.assertEqual(player.money,990)

        #1000-0=1000
        player.money = 1000
        player.pay_money(0)
        self.assertEqual(player.money,1000)

        #1000-1000 = 0
        player.money = 1000
        player.pay_money(1000)
        self.assertEqual(player.money, 0)
        
        #1000 - 1100 = -100
        player.money = 1000
        player.pay_money(1100)
        self.assertEqual(player.money, -100)

        #-100 - 100 = -200
        player.money = -100
        player.pay_money(100)
        self.assertEqual(player.money, -200)

        #-100 - -100 = 0
        player.money = -100
        player.pay_money(-100)
        self.assertEqual(player.money, 0)


    def test_add_money(self):
        #add $
        player = Player(1, 1000, 0)

        #1000 + 100 = 1200
        player.add_money(200)
        self.assertEqual(player.money, 1200)

        #-200 + 100 = -100
        player.money = -200
        player.add_money(100)
        self.assertEqual(player.money, -100)

        #200 + 0 = 200
        player.money = 200
        player.add_money(0)
        self.assertEqual(player.money, 200)

        #200 + -200 = 0
        player.money = 200
        player.add_money(-200)
        self.assertEqual(player.money, 0)


if __name__ == '__main__':
    unittest.main()
