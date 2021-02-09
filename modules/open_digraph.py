import operator
import sys
sys.path.append('../')
from modules.utils import *


class node:
    def __init__(self, identity, label, parents, children):

        #identity: int; its unique id in the graph
        #label: string;
        #parents: int list; a sorted list containing the ids of its parents
        #children: int list; a sorted list containing the ids of its children

        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    def __str__(self):
        return "(" + str(self.id) +"," + self.label +","+ str(self.parents) + "," + str(self.children) + ")"
        '''
        output : str ; the string given by str(node)
        '''
    def __repr__(self):
        return "node"+str(self)

    def copy(self):
        return node(self.id, self.label, self.parents.copy(),self.children.copy())

    def get_id(self):
        return self.id

    def get_label(self):
        return self.label

    def get_parent_ids(self):
        return self.parents

    def get_children_ids(self):
        return self.children

    def set_id (self, id) :
        self.id = id

    def set_label (self, label) :
        self.label = label

    def set_parent_ids (self, parent_ids) :
        self.parents = parent_ids

    def set_children_ids (self, children_ids) :
        self.children = children_ids

    def add_child_id (self, child_id) :
        self.children.append(child_id)

    def add_parent_id (self, parent_id) :
        self.parents.append(parent_id)

    def remove_parent_id(self, parent_id):
        self.parents.remove(parent_id)

    def remove_child_id(self, child_id):
        self.children.remove(child_id)

    def remove_parent_id_all(self, parent_id):
        remove_all(self.parents, parent_id)

    def remove_child_id_all(self, child_id):
        remove_all(self.children, child_id)



class open_digraph: #for open directed graph

    def __init__(self, inputs, outputs, nodes):
        #inputs: int list; the ids of the input nodes
        #outputs: int list; the ids of the output nodes
        #nodes: node list;
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

    def __str__(self):
        return "(" + str(self.inputs) +"," + str(self.outputs) +","+ str(print(self.nodes)) + ")" #il faut utiliser __repr__

    def __repr__(self):
        return "open_digraph" + str(self)

    def copy(self):
        return open_digraph(self.inputs.copy(), self.outputs.copy(), [node.copy() for node in self.nodes.values()])

    def empty():
        return open_digraph([],[],[])

    def get_inputs_ids(self):
        return self.inputs

    def get_outputs_ids(self):
        return self.outputs

    def get_id_node_map(self): #renvoie un dictionnaire id:nodes
        return self.nodes

    def get_nodes(self):
        L = []
        for i in self.nodes.values():
            L.append(i)
        return L

    def get_node_ids(self):
        return [i for i in self.nodes]

    def get_node_by_id(self, i):
        return self.nodes.get(i)    # faire le cas ou le i n'existe pas

    def get_node_by_ids(self):
        return [self.nodes.get(i) for i in self.nodes]

    def set_input_ids (self, input_ids) :
        self.inputs = input_ids

    def set_output_ids (self, output_ids) :
        self.outputs= output_ids

    def add_input_id (self, input_id) :
        self.inputs.append(input_id)

    def add_output_id (self, output_id) :
        self.outputs.append(output_id)

    def new_id(self):
        dict = self.get_id_node_map()
        return (max(dict)+1)

    def add_edge(self, src, tgt):           #Le test ne fonctionne pas
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)

    def add_edges(self, src, tgt):          #le test ne fonctionne pas
        for i in tgt:
            self.add_edge(src,i)

    def add_node(self, label='', parents=[], children=[]):  #pas sur du tout, et à tester
        id=self.new_id()
        n0 = node(id, label, [],[])
        for i in parents:
            self.add_edge(i,n0)
        self.add_edge(n0,children)
        return id

    def remove_edge(self,src,tgt):
        self.get_node_by_id(src).remove_parent_id_all(tgt)
        self.get_node_by_id(src).remove_child_id_all(tgt)
        self.get_node_by_id(tgt).remove_parent_id_all(src)
        self.get_node_by_id(tgt).remove_child_id_all(src)

    def remove_node_by_id(self, id):
        print("aaaaaaaaaaa")
        print(id)
        node_removed = self.nodes.pop(id)
        remove_all(self.inputs, id)
        remove_all(self.outputs,id)

    def remove_edges(self,src,tgt):#src et tgt sont des listes de nodes    # a tester
        for i in src :
            for  j in tgt :
                self.remove_edge(i.id ,j.id)

    def remove_nodes_by_id(self,ids):   #ids une liste de ids        # a tester
        for i in ids:
            self.remove_node_by_id(i)


    def is_well_formed(self):
        # partie 1
        for input_id in self.inputs :
            if not (input_id in self.get_node_ids()):
                return False
        for output_id in self.outputs :
            if not (output_id in self.get_node_ids()):
                return False

        # partie 2
        for key in self.nodes.keys() :
            if not (key in self.get_node_ids()):
                return False

        # partie 3
        for node in self.nodes.values() :
            for child_id in node.get_children_ids() :
                if not (count_occurrences(node.get_children_ids(), child_id) == count_occurrences(self.get_node_by_id(child_id).get_parent_ids(), node.get_id())):
                    return False

        return True
