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

    def id_exists_in_graph(self,id):
        if id in self.nodes:
            return True
        else:
            return False

    def get_node_by_id(self, id):            # renvoie le node dont l'id correspond a id
        return self.nodes.get(id)


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
        if dict :
            return (max(dict)+1)
        else :
            return 0

    def add_edge(self, src, tgt):                       # ajoute une arete entre les nodes
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)

    def add_edges(self, src, tgt):          # ajoute des aretes entre les nodes
        for i in tgt:
            self.add_edge(src,i)

    def add_node(self, label='', parents=[], children=[]):             # ajoute un node au graphe                               # pas sur du tout, et à tester
        id=self.new_id()
        n0 = node(id, label, [],[])
        self.nodes[id]=n0
        print('add_node1', n0, children)
        for i in parents:
            self.add_edge(i, id)
        print('add_node2', n0, children)
        self.add_edges(id, children)
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



    def change_id(self, node_id, new_id):
        if(self.id_exists_in_graph(new_id)==False):
            #self.get_node_by_id(node_id).id = new_id
            for i in self.get_node_by_id(node_id).parents:
                for j in self.get_node_by_id(i).children:
                    if (self.get_node_by_id(j).id == node_id):
                        self.get_node_by_id(j).set_id(new_id)
            for i in self.get_node_by_id(node_id).children:
                for j in self.get_node_by_id(i).parents:
                    if (self.get_node_by_id(j).id == node_id):
                        self.get_node_by_id(j).set_id(new_id)
            for i in range(len(self.inputs)):
                if (self.inputs[i]==node_id):
                    self.inputs[i]=new_id
            for i in range(len(self.outputs)):
                if (self.outputs[i]==node_id):
                    self.outputs[i]=new_id
            self.nodes[new_id]=self.nodes[node_id]
            self.nodes.pop(node_id)
        else:
            raise ValueError('new id already exists')

    def change_ids(self, change):
        sorted(change, key = lambda t: t[1])
        for couple in change :
            self.change_id(couple[0], couple[1])


    def random_graph(self, n, bound, inputs=0, outputs=0, form="free"):     # renvoie un graphe correspondant a la matrice d adjacence de type form, de taille n * n et avec des valeurs entre 0 et bound
        '''
        le fonctionnement est assez simple : on cree la matrice en fonction de la forme voulue, puis on fait le graphe correspondant
        utiliser l argument form pour definir le type de matrice et donc de graphe voulu
        free : matrice aleatoire
        DAG : matrice triangulaire donc sans doublon
        oriented : matrice orientee donc graphe oriente, cad que les aretes ne peuvent aller que dans un sens
        undirected : matrice symetric donc graphe non-dirige
        '''
        if form =="free":
            matrix = random_int_matrix(n, bound)
        elif form =="DAG":
            matrix = random_triangular_int_matrix(n, bound)
        elif form =="oriented":
            matrix = random_oriented_int_matrix(n, bound)
        elif form =="undirected":
            matrix = random_symetric_int_matrix(n, bound)
        graph = graph_from_adjacency_matrix(matrix)
        print(matrix)
        print(graph)
        return graph



    def normalise_ids(self) :               # non testee
        size = len(self.nodes)
        unused_ids = []
        unwanted_ids = []
        for i in range(size):
            if not self.node.id_exists_in_graph(i) :
                unused_ids.append(i)
        for node in self.nodes :
            id = node.get_id()
            if id >= size :
                unwanted_ids.append(id)
        lenth = len(unwanted_ids)
        if lenth == len(unused_ids) :
            change = []
            for i  in range(lenth) :
                change.append((unwanted_ids[i], unused_ids[i]))
            self.change_ids(change)
        else :
            raise ValueError('Les vides dans nodes ne correspondent pas aux trop-pleins')




        def adjacency_matrix(self) :                # non testee
            self.normalise_ids()
            size = len(self.nodes)
            matrix = [0] * size * size
            for node in self.nodes :
                node_id = node.get_id()
                for parent_id in node.get_parent_ids() :
                    matrix[node_id][parent_id] += 1                 # convention arbitraire : on ne sert que des parents (puisque les enfants n'apportent pas plus d'information si le graphe est bien formé)
                                                                    # et on considere que matrix[i][j] represente une arete de j vers i
            return matrix





def graph_from_adjacency_matrix(matrix) :           # renvoie un graphe correspondant a la matrice d adjacence matrix
    graph = open_digraph.empty()                    # on cree un graphe vide vide a partir duquel on va construire le graphe voulu

    # on ne sert pas de la methode add_node car on part du graphe vide
    # et donc la methode tente de faire des aretes avec des nodes qui n ont pas encore ete crees
    # modifier la methode pour resoudre le bug serait trop complique donc on fait autrement
    # a la place, on parcourt deux fois la matrice, une premiere fois pour creer tous les nodes sans les aretes

    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if matrix[i][j] != 0 :                  # on considere que les nodes sont uniques cad qu on ne cree pas plus d un node avec un id donne
                n0 = node(j, 'node' + str(j), [],[])         # on cree un nouveau node sans enfant ni parent, d id et de label node + j soit son indice dans la matrice
                graph.nodes[j]=n0                   # on ajoute ce node au dictionnaire graph.nodes avec en clef j
    '''
    et on parcourt une deuxieme fois la matrice pour etablir les aretes avec la methode add_edge
    '''
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            for _ in range(matrix[i][j]) :
                graph.add_edge(j, i)                # on a decide arbitrairement que la valeur de matrix[i][j] correspondrait a une arete de j vers i

    return graph                                    # bug a regler : pb si matrice tro petite : certains sommets n existent pas mais sont des enfants quand meme
                                                    # test a finir

        #
        # def graph_from_adjacency_matrix(matrix) :
        #     return True #justepour pouvoir compiler
        #     #graph = open_digraph.empty()
        #     #for i in range len(matrix) :
        #     #    #for j in range len(matrix[i]) :
        #     #        if matrix[i][j] != 0 :
        #     #            graph.add_node('a', )
        #
