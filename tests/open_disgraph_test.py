import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.open_disgraph import *

class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', [], [1])
        n1 = node(0,'i',[],[1])
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, [])
        self.assertEqual(n0.children, [1])
        self.assertIsInstance(n0, node)
        self.assertEqual(n0.id,n1.id)
        self.assertEqual(n0.label, n1.label)
        self.assertEqual(n0.parents, n1.parents)
        self.assertEqual(n0.children, n1.children)

    def test_init_open_digraph(self):
        n0 = node(0, 'i', [], [1])
        n1 = node(1,'b',[],[2])
        g=([1,2],[3,4],[n0,n1])
        #self.assertEqual(g.inputs, [1,2])
        #self.assertEqual(g.outputs, [3, 4])
        #self.assertEqual(g.nodes, [n0,n1])

'''class NodeTest(unittest.testcase):
    def setUp(self):
        self.n0 = node(0, 'a', [], [1])
    def test_get_id(self):
        self.assertEqual(self.n0.get_id(), 0)
    def test_get_label(self):
        self.assertEqual(self.n0.get_label(), 'a')
'''


if __name__ == '__main__': # the following code is called only when
    unittest.main()        # precisely this file is run
