import unittest
from Block import *
from data import *

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#py test_block.py -v

class TestBlock(unittest.TestCase):
    
    def test_activate_block_effect(self):
        #Block
        start_block: Start = Start(property_data[0])
        start_block.is_test = True
        start_block.selection_data[0] = 'Save Game !'

        self.assertTrue()






if __name__ == '__main__':
    unittest.main()