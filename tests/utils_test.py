import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.utils import *


class UtilsTest(unittest.TestCase):

    def test_remove_all(self):
        l=[1,2,3,2,1]
        self.assertEqual(remove_all(l,1), [2,3,2] )

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([0,1,0,2,858,0], 0), 3)

    def test_random_int_list(self):
        print(random_int_list(5,10))

    def test_random_int_matrix(self): #est ce que il faut mettre les self?
        print(random_int_matrix(5,10,False))
        print(random_int_matrix(5,10,True))

    def test_random_symetric_int_matrix(self):
        print(random_symetric_int_matrix(4,10,False))
        print(random_symetric_int_matrix(4,10,True))

    def test_random_oriented_int_matrix(self): #ne fonctionne pas
        print("oriented")
        print(random_oriented_int_matrix(3,10,False))
        print(random_oriented_int_matrix(3,10,True))

    def test_random_triangular_int_matrix(self):
        print(random_triangular_int_matrix(3,10,False))
        print(random_triangular_int_matrix(3,10,True))

    def test_list_cleaner(self):
        self.assertEqual(list_cleaner([1, 1, 3, 4, 1, 2, 4]), [1, 3, 4, 2])

    def test_perm_calc(self):
        self.assertEqual(perm_calc(["a", "d", "c", "b"], ["a", "d", "c", "b"]), [0, 1, 2, 3])
        self.assertEqual(perm_calc(["a", "d", "c", "b"], ["a", "b", "c", "d"]), [0, 3, 2, 1])

    def test_inv_perm(self):
        self.assertEqual(inv_perm([3, 0, 2, 1]), [1, 3, 2, 0])

    def test_appl_perm(self):
        self.assertEqual(appl_perm(["a", "d", "c", "b"], [0, 1, 2, 3]), ["a", "d", "c", "b"])
        self.assertEqual(appl_perm(["a", "d", "c", "b"], [0, 3, 2, 1]), ["a", "b", "c", "d"])

if __name__ == '__main__': # the following code is called only when
    unittest.main()        # precisely this file is run
