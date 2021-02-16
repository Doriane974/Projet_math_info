import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.open_digraph import *
from modules.utils import *
from modules.Interface import *

class InitTest(unittest.TestCase):
    def test_init_point(self):
        p1=point(1,2)
        p2=point(2,3)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p2.x, 2)
        self.assertEqual(p1.y, 2)
        self.assertEqual(p2.y, 3)

    def test_n(self):
        p1=point(1,2)
        print(p1.n())
        p2=point(2,3)
        print(p2.n())

    def test_copy(self):
        p1=point(1,2)
        p2 = p1.copy()
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 2)

    def test_add(self):
        p1=point(1,2)
        p2=point(2,3)
        p1 = p1 + p2
        self.assertEqual(p1.x, 3)
        self.assertEqual(p1.y, 5)

    def test_rmul(self):
        p1=point(1,2)
        p1= 2*p1
        self.assertEqual(p1.x, 2)
        self.assertEqual(p1.y, 4)

    def test_sub(self):
        p1=point(1,2)
        p2=point(2,1)
        p1 = p1 - p2
        self.assertEqual(p1.x, -1)
        self.assertEqual(p1.y, 1)






if __name__ == '__main__': # the following code is called only when
    unittest.main()        # precisely this file is run
