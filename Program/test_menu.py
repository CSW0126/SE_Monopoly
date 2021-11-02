import unittest
from Menu import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_menu.py -v

class TestMenu(unittest.TestCase):
    
    def test_print_menu(self):
        menu : Menu = Menu()
        menu.is_test = True

        #select new game
        menu.select_data.append('New Game')
        self.assertEqual(menu.print_menu(), 0)

        #select continue
        menu.select_data[0] = 'Continue'
        self.assertEqual(menu.print_menu(), 1)

        #select check game rule
        menu.select_data[0] = 'Check Game Rule'
        menu.select_data.append('Back')
        self.assertEqual(menu.print_menu(), 2)

        #select exit
        menu.select_data[0] = 'Exit'
        self.assertEqual(menu.print_menu(), 3)



if __name__ == '__main__':
    unittest.main()