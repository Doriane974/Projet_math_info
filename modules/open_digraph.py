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

    def copy(self):                     # renvoie une copie du node (node)
        return node(self.id, self.label, self.parents.copy(),self.children.copy())

    def get_id(self):                   # renvoie l'id du node (int)
        return self.id

    def get_label(self):                # renvoie le label du node (int)
        return self.label

    def get_parent_ids(self):           # renvoie la liste des parents du node (int list)
        return self.parents

    def get_children_ids(self):         # renvoie la liste des enfants du node (int list)
        return self.children

    def set_id (self, id) :             # affecte une valeur a l'id du node (char)
        self.id = id

    def set_label (self, label) :       # affecte un string au label du node (string)
        self.label = label

    def set_parent_ids (self, parent_ids) :         # affecte une valeur aux ids des parents du node (int list)
        self.parents = parent_ids

    def set_children_ids (self, children_ids) :     # affecte une valeur aux ids des enfants du node (int list)
        self.children = children_ids

    def add_child_id (self, child_id) :             # ajoute une valeur a la liste des id des enfants du node (int)
        self.children.append(child_id)

    def add_parent_id (self, parent_id) :           # ajoute une valeur a la liste des id des parents du node (int)
        self.parents.append(parent_id)

    def remove_parent_id(self, parent_id):          # retire la valeur specifiee a la liste des ids des parents du node (int)
        self.parents.remove(parent_id)

    def remove_child_id(self, child_id):            # retire la valeur specifiee a la liste des ids des enfants du node (int)
        self.children.remove(child_id)

    def remove_parent_id_all(self, parent_id):      # retire tous les ids des parents du node (int list)
        remove_all(self.parents, parent_id)

    def remove_child_id_all(self, child_id):        # retire tous les ids des enfants du node (int list)
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

    def copy(self):                         # renvoie une copie du graphe (digraph)
        return open_digraph(self.inputs.copy(), self.outputs.copy(), [node.copy() for node in self.nodes.values()])

    def empty():                            # renvoie un graphe vide (digraph)
        return open_digraph([],[],[])

    def get_inputs_ids(self):               # extrait la liste des ids des inputs du graphe (int list)
        return self.inputs

    def get_outputs_ids(self):              # extrait la liste des ids des outputs du graphe (int list)
        return self.outputs

    def get_id_node_map(self): #renvoie un dictionnaire id:nodes
        return self.nodes

    def get_nodes(self):                    # renvoie une liste de tous les noeuds
        L = []
        for i in self.nodes.values():
            L.append(i)
        return L

    def get_node_ids(self):                 # renvoie une liste des ids des nodes (int list)
        return [i for i in self.nodes.keys()]

    def get_node_by_id(self, id):            # renvoie le node dont l'id correspond a id
        return self.nodes.get(id)    # faire le cas ou le i n'existe pas

    def get_node_by_ids(self, node_ids):              # renvoie une liste de noeuds a partir d’une liste d’ids
        return [self.nodes.get(i) for i in node_ids]

    def set_input_ids (self, input_ids) :              # affecte les inputs du graphe a input_ids
        self.inputs = input_ids

    def set_output_ids (self, output_ids) :             # affecte les outputs du graphe a output_ids
        self.outputs= output_ids

    def add_input_id (self, input_id) :                 # ajoute une valeur a la liste des inputs du graphe
        self.inputs.append(input_id)

    def add_output_id (self, output_id) :               # ajoute une valeur a la liste des outputs du graphe
        self.outputs.append(output_id)

    def new_id(self):                                   # renvoie un id non utilise par le graphe
        dict = self.get_id_node_map()
        return (max(dict)+1)

    def add_edge(self, src, tgt):                       # ajoute une arete entre les nodes
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)

    def add_edges(self, src, tgt):          # ajoute des aretes entre les nodes
        for i in tgt:
            self.add_edge(src,i)

    def add_node(self, label='', parents=[], children=[]):             # ajoute un node au graphe                               # pas sur du tout, et à tester
        id=self.new_id()
        n0 = node(id, label, [],[])
        for i in parents:
            self.add_edge(i,n0)
        self.add_edge(n0,children)
        return id

    def remove_edge(self,src,tgt):                                      # retire une arete du graphe
        self.get_node_by_id(src).remove_parent_id_all(tgt)
        self.get_node_by_id(src).remove_child_id_all(tgt)
        self.get_node_by_id(tgt).remove_parent_id_all(src)
        self.get_node_by_id(tgt).remove_child_id_all(src)

    def remove_node_by_id(self, id):                                    # retire un node (selon l'id) au graphe
        #print("aaaaaaaaaaa")
        #print(id)
        node_removed = self.nodes.pop(id)
        remove_all(self.inputs, id)
        remove_all(self.outputs,id)

    def remove_edges(self,src,tgt):#src et tgt sont des listes de nodes    # a tester  # retire plusieurs aretes au graphe
        for i in src :
            for  j in tgt :
                self.remove_edge(i.id ,j.id)

    def remove_nodes_by_id(self,ids):   #ids une liste de ids        # a tester     # retire plusieurs nodes au graphe
        for i in ids:
            self.remove_node_by_id(i)


    def is_well_formed(self):                       # verifie si le graphe est correctement forme
        # partie 1
        for input_id in self.inputs :                           # on parcourt les inputs
            if not (input_id in self.get_node_ids()):           # on verifie que chaque input est dans les ids des nodes
                return False
        for output_id in self.outputs :                         # idem pour les outputs
            if not (output_id in self.get_node_ids()):
                return False

        # partie 2
        for key in self.nodes.keys() :                          # on parcourt les clefs du dict nodes
            if not (key in self.get_node_ids()):                # on verifie que la clef correspond a l'id d'un node
                return False

        # partie 3
        for node in self.nodes.values() :                       # on parcourt les nodes
            for child_id in node.get_children_ids() :           # pour chaque node, on parcourt les enfants
                if not (count_occurrences(node.get_children_ids(), child_id) == count_occurrences(self.get_node_by_id(child_id).get_parent_ids(), node.get_id())):      # pour chaque enfant, on compte le nombre d'occurrence(s) de son id dans les enfants du node
                    return False                                                                                                                                        # et on verifie que ce nombre est egal a celui des occurrences du node parmi les parents de l'enfant

        return True                                             # si aucune erreur n'a ete detectee, alors le graphe est bien forme
