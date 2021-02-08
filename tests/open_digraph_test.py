import sys
sys.path.append('../') # allows us to fetch files from the project root
import unittest
from modules.open_digraph import *


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

    def test_init_open_digraph(self): #a completer ici - Question 3
        n0 = node(0, 'i', [], [1])
        n1 = node(1,'b',[],[2])
        self.g = open_digraph([1],[3],[n0,n1])
        self.assertEqual(self.g.inputs, [1])
        self.assertEqual(self.g.outputs, [3])
        #self.assertEqual(g.nodes, [n0,n1])

class NodeTest(unittest.TestCase):

    def setUp(self):                    #dans l'enonce
        self.n0 = node(0, 'a', [], [1]) #dans l'enonce
        self.n1 = node(1, 'b', [0], []) #ligne rajoutée

    def test_get_id(self):              #dans l'enonce
        self.assertEqual(self.n0.get_id(), 0)   #dans l'enonce
        self.assertEqual(self.n1.get_id(), 1)

    def test_get_label(self):           #dans l'enonce
        self.assertEqual(self.n0.get_label(), 'a')  #dans l'enonce
        self.assertEqual(self.n1.get_label(), 'b')

    def test_copy(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        n2 = self.n0.copy()
        n2.label = 'c'
        self.assertEqual(n2.id, self.n0.id)
        self.assertNotEqual(n2.label, self.n0.label)
        self.assertIsNot(n2, self.n0)

    def test_get_id(self):
        self.n0 = node(0, 'a', [], [1])
        self.assertEqual(self.n0.get_id(),0)
        self.assertNotEqual(self.n0.get_id(),1)

    def test_get_label(self):
        self.n0 = node(0, 'a', [], [1])
        self.assertEqual(self.n0.get_label(),'a')
        self.assertNotEqual(self.n0.get_label(),'b')

    def test_get_parents_ids(self):
        self.n0 = node(0, 'a', [2], [1])
        self.assertEqual(self.n0.get_parent_ids(),[2])
        self.n2 = node(0, 'a', [0], [1])
        self.assertNotEqual(self.n1.get_parent_ids(),[2])

    def test_get_children_ids(self):
        self.n0 = node(0, 'a', [2], [1])
        self.assertEqual(self.n0.get_children_ids(),[1])
        self.n2 = node(0, 'a', [0], [1])
        self.assertNotEqual(self.n1.get_children_ids(),[2])

    def test_remove_parent_id(self):
        self.n0 = node(0, 'a', [2], [1])
        self.n0.remove_parent_id(2)
        self.assertEqual(self.n0.parents,[])

    def test_remove_child_id(self):
        self.n0 = node(0, 'a', [2], [2])
        self.n0.remove_child_id(2)
        self.assertEqual(self.n0.children,[])

    def test_remove_parent_id_all(self):
        self.n0 = node(0, 'a', [2,3,2], [2])
        self.n0.remove_parent_id_all(2)
        self.assertEqual(self.n0.parents,[3])

    def test_remove_child_id_all(self):
        self.n0 = node(0, 'a', [2], [2,3,2])
        self.n0.remove_child_id_all(2)
        self.assertEqual(self.n0.children,[3])



class DigraphTest(unittest.TestCase):

    def setUp(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])                     # to be completed

    def test_copy(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.d2 = open_digraph([],[],[])
        d2 = self.d0.copy()
        d2.inputs = [1]
        self.assertEqual(d2.outputs, self.d0.outputs)
        self.assertNotEqual(d2.inputs, self.d0.inputs)
        self.assertIsNot(d2,self.d0)

    def test_get_inputs_ids(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.assertEqual(self.d0.get_inputs_ids(),[0])
        self.assertNotEqual(self.d0.get_inputs_ids(),[1])

    def test_get_id_node_map(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.d1 = open_digraph([0],[1],[self.n0, self.n1])
        print(set(self.d1.get_id_node_map()) == set(self.d0.get_id_node_map()))
        print(self.d1.get_id_node_map())

    def test_get_nodes(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.assertEqual(self.d0.get_nodes(),[self.n0,self.n1])

    def test_get_node_ids(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.assertEqual(self.d0.get_node_ids(),[0,1])

    def test_get_node_by_id(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.assertEqual(self.d0.get_node_by_id(0), self.n0)

    def test_get_node_by_ids(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        self.assertEqual(self.d0.get_node_by_ids(),[self.n0,self.n1])

    def test_new_id(self):
        self.n0 = node(0, 'a', [], [1])
        self.n1 = node(1, 'b', [0], [])
        self.d0 = open_digraph([0],[1],[self.n0, self.n1])
        print(self.d0.new_id())

#    def test_add_edge(self):
#        self.n0 = node(0, 'a', [], [2])
#        self.n1 = node(1, 'b', [3], [])
#        self.add_edge(self.n0, self.n1)
#        self.assertEqual(self.n0.children, [2,1])
#        self.assertEqual(self.n1.parents, [3,0])

#    def test_add_edges(self):
#        self.n0 = node(0, 'a', [], [3])
#        self.n1 = node(1, 'b', [4], [])
#        self.n2 = node(2, 'a', [], [5])
#        self.add_edge(self.n0, [self.n1, self.n2])
#        self.assertEqual(self.n0.children, [3,1,2])
#        self.assertEqual(self.n1.parents, [4,0])
#        self.assertEqual(self.n2.parents, [0])




if __name__ == '__main__': # the following code is called only when
    unittest.main()        # precisely this file is run
