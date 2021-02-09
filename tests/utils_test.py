import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.utils import *


class UtilsTest(unittest.TestCase):

    def test_remove_all(self):
        l=[1,2,3,2,1]
        self.assertEqual(remove_all(l,1), [2,3,2] )

    def test_random_int_list(self):
        print(random_int_list(5,10))

    def test_random_int_matrix(self): #est ce que il faut mettre les self?
        print(random_int_matrix(5,10,False))
        print(random_int_matrix(5,10,True))

if __name__ == '__main__': # the following code is called only when
    unittest.main()        # precisely this file is run
