import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.utils import *


class UtilsTest(unittest.TestCase):

    def test_remove_all(self):
        l=[1,2,3,2,1]
        self.assertEqual(self.remove_all(l,2),[1,3,1])



if __name__ == '__main__': # the following code is called only when
    unittest.main()        # precisely this file is run
