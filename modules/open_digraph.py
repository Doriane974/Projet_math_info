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

    '''méthode appliqué au node qui renvoie une copie de ce node
    argument : nonde
    return : node '''
    def copy(self):                     # renvoie une copie du node (node)
        return node(self.id, self.label, self.parents.copy(),self.children.copy())

    '''méthode appliquée au node qui renvoie l'id de ce node
    argument : none
    return : int '''
    def get_id(self):                   # renvoie l'id du node (int)
        return self.id

    '''méthode appliquée au node qui renvoie le label de ce node
    argument : none
    retunr : label '''
    def get_label(self):                # renvoie le label du node
        return self.label

    '''méthode appliquée au node qui renvoie la liste des parents de ce node
    argument : none
    return : id list '''
    def get_parent_ids(self):           # renvoie la liste des parents du node (int list)
        return self.parents

    '''méthode appliquée au node qui renvoie la liste des enfants du node
    argument : nonde
    return : id list  '''
    def get_children_ids(self):         # renvoie la liste des enfants du node (int list)
        return self.children

    '''méthode appliquée au node qui affecte une valeur a l'id du node
    argument : id : id que l'on veut affecter
    return : none '''
    def set_id (self, id) :             # affecte une valeur a l'id du node (char)
        self.id = id

    '''méthode appliquée au node qui affecte un label au node
    argument : label : label que l'on veut affecter
    return : none '''
    def set_label (self, label) :       # affecte un string au label du node (string)
        self.label = label

    '''méthode appliquée au node qui affecte une valeur au parents de ce node
    argument : id list
    return : none  '''
    def set_parent_ids (self, parent_ids) :         # affecte une valeur aux ids des parents du node (int list)
        self.parents = parent_ids

    '''méthode appliquée au node qui affecte une valeur au enfants de ce node
    argument : id list
    return : none  '''
    def set_children_ids (self, children_ids) :     # affecte une valeur aux ids des enfants du node (int list)
        self.children = children_ids

    '''méthode appliquée au node qui ajoute une valeur a la liste des ids des enfants de ce node
    argument : child_id : id à ajouter
    return : none  '''
    def add_child_id (self, child_id) :             # ajoute une valeur a la liste des id des enfants du node (int)
        self.children.append(child_id)

    '''méthode appliquée au node qui ajoute une valeur a la liste des ids des parents de ce node
    arguments : parent id : id à ajouter
    return : none '''
    def add_parent_id (self, parent_id) :           # ajoute une valeur a la liste des id des parents du node (int)
        self.parents.append(parent_id)

    '''méthode appliquée au node qui retire la valeur spécifiée a la liste des ids des parents du node
    argument : parent id : id
    return : none '''
    def remove_parent_id(self, parent_id):          # retire la valeur specifiee a la liste des ids des parents du node (int)
        if parent_id in self.get_parent_ids():
            self.parents.remove(parent_id)

    '''méthode appliquée au node qui retire la valeur spécifiée a la liste des ids des parents du node
    argument ; child_id : id
    return : none '''
    def remove_child_id(self, child_id):            # retire la valeur specifiee a la liste des ids des enfants du node (int)
        if child_id in self.get_children_ids():
            self.children.remove(child_id)

    '''méthode appliquée au node qui retire tous les ids donnés des parents du node
    argument : parent_id : id list
    return : none  '''
    def remove_parent_id_all(self, parent_id):      # retire tous les ids des parents du node (int list)
        remove_all(self.parents, parent_id)

    '''méthode appliquée au node qui retire tous les ids donnés des enfants du node
    argument : child_id : id list
    return : none  '''
    def remove_child_id_all(self, child_id):        # retire tous les ids des enfants du node (int list)
        remove_all(self.children, child_id)



    '''méthode qui s'applique a un node qui donne le degre sortant du node
    argument : none
    return : int '''
    def outdegree(self):                            # donne le degre sortant du node
        return len(self.get_children_ids())
    '''méthode qui s'applique a un node qui donne le degre entrant du node
    argument : none
    return : int '''
    def indegree(self):                             # donne le degre entrant du node
        return len(self.get_parent_ids())
    '''méthode qui s'applique a un node qui donne le degré du node (degre entrant + degre sortant)
    argument : none
    return : int '''
    def degree(self):                               # donne le degre du node
        return self.indegree() + self.outdegree()

    def change_id_node(self, n):
        self.id = self.get_id() + n


class open_digraph: #for open directed graph

    def __init__(self, inputs, outputs, nodes):
        #inputs: int list; the ids of the input nodes
        #outputs: int list; the ids of the output nodes
        #nodes: node list;
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.get_id() : node for node in nodes} # self.nodes: <int,node> dict

    def __str__(self):
        return "(" + str(self.inputs) +"," + str(self.outputs) +","+ str(print(self.nodes)) + ")" #il faut utiliser __repr__

    def __repr__(self):
        return "open_digraph" + str(self)

    '''méthode appliquée au graphe qui retourne une copie du graphe
    argument : none
    return : un nouveau graph '''
    def copy(self):                         # renvoie une copie du graphe (digraph)
        return open_digraph(self.inputs.copy(), self.outputs.copy(), [node.copy() for node in self.nodes.values()])

    '''fonction qui renvoie un graphe vide
    arguments : none
    return : un graphe '''
    def empty():                            # renvoie un graphe vide (digraph)
        return open_digraph([],[],[])

    '''méthode appliquée au graphe qui extrait la liste des ids des inputs du graphe
    argument : none
    return : int list '''
    def get_inputs_ids(self):               # extrait la liste des ids des inputs du graphe (int list)
        return self.inputs

    '''méthode appliquée au graphe qui extrait la liste des ids des outputs du graphe
    argument : none
    return : int list '''
    def get_outputs_ids(self):              # extrait la liste des ids des outputs du graphe (int list)
        return self.outputs

    '''méthode appliquée au graphe qui extrait le dictinnaire des nodes du graphe
    argument : none
    return : dictionnaire : keys : ids, values : nodes  '''
    def get_id_node_map(self): #renvoie un dictionnaire id:nodes
        return self.nodes

    '''méthode appliquée au graphe qui renvoie une liste de tous les nodes du graphes
    argument : none
    return : node list '''
    def get_nodes(self):    # renvoie une liste de tous les noeuds
        return list(self.nodes.values())

    '''méthode appliquée au graphe qui renvoie une liste de tous les ids des nodes du graphes
    argument : none
    return : int list '''
    def get_node_ids(self):                 # renvoie une liste des ids des nodes (int list)
        return [i for i in self.nodes.keys()]

    '''méthode appliquée au graphe qui vérifie si une id existe deja dans le graphe
    argument : id : l'id dont on veut savoir si elle existe ou non
    return : bool : True si l'id existe, False sinon '''
    def id_exists_in_graph(self,id):
        if id in self.get_id_node_map():
            return True
        else:
            return False

    '''Méthode appliquée au graphe qui renvoie le node dont l'id correspond a id
    argument : id : id dont ont veut obtenir le node correspondant
    return : node '''
    def get_node_by_id(self, id):            # renvoie le node dont l'id correspond a id
        return self.nodes.get(id)

    '''méthode appliquée au graphe qui renvoie une liste de noeuds a partir d'une liste d'id
    argument : node_ids : id list
    return : node list '''
    def get_node_by_ids(self, node_ids):              # renvoie une liste de noeuds a partir d’une liste d’ids
        return [self.nodes.get(i) for i in node_ids]

    '''méthode appliquée au graphe qui affecte input_ids aux inputs du graph
    argument : inputs_ids : id list
    return : none '''
    def set_input_ids (self, input_ids) :              # affecte les inputs du graphe a input_ids
        self.inputs = input_ids

    '''méthode appliquée au graphe qui affecte output_ids aus outputs du graph
    argument : outputs_ids : id list
    return : none '''
    def set_output_ids (self, output_ids) :             # affecte les outputs du graphe a output_ids
        self.outputs= output_ids

    '''méthode appliquée au graphe qui ajoute une valeur a la liste des inputs du graphe
    argument : input_id : id à ajouter  '''
    def add_input_id (self, input_id) :                 # ajoute une valeur a la liste des inputs du graphe
        self.inputs.append(input_id)

    '''méthode appliquée au graphe qui ajoute une valeur a la liste des outputs du graphe
    argument : output_id : id à ajouter  '''
    def add_output_id (self, output_id) :               # ajoute une valeur a la liste des outputs du graphe
        self.outputs.append(output_id)

    '''méthode appliquée au graphe qui  retourne un Id qui n'est pas utilisé dans le graphe
    argument : none
    return : un id '''
    def new_id(self):                                   # renvoie un id non utilise par le graphe
        dict = self.get_id_node_map()
        if (dict =={}):
            return -1
        else:
            if dict :
                return (max(dict)+1) #quand je rajoute default=-1 ca bug
            else :
                return 0

    '''méthode appliquée au graphe qui ajoute une arrete entre 2 nodes
    argument : src : Id du node qui deviendra le parent
               tgt : Id du node qui deviendra l'enfant '''
    def add_edge(self, src, tgt):                       # ajoute une arete entre les nodes
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)

    '''méthode appliquée au graph qui ajoute des arrete entre un node et une liste de node
    arguments : src : Id du node qui deviendra le parent
                tgt ; liste d'Id des nodes qui deviendront les enfants de src '''
    def add_edges(self, src, tgt):          # ajoute des aretes entre les nodes
        for i in tgt:
            self.add_edge(src,i)

    '''méthode appliquée au graphe qui ajoute un node au graphe
    argument : label : label, par défaut ''
               parents : id list, par défaut []
               children : id list, par défaut []
    return : id : l'id du node qui a été ajouté '''
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

    '''méthode appliquée au graphe qui retire une arete du graph
    argument : src : id
               tgt : id
    return : none '''
    def remove_edge(self,src,tgt):                                      # retire une arete du graphe

        self.get_node_by_id(src).remove_parent_id(tgt)
        self.get_node_by_id(src).remove_child_id(tgt)
        self.get_node_by_id(tgt).remove_parent_id(src)
        self.get_node_by_id(tgt).remove_child_id(src)

    '''méthode appliquée au graphe qui enleve un noeud ayant l'Id voulue du graphe
    argument : id : id du noeud que l'on veut retirer
    return : none '''
    def remove_node_by_id(self, id):
        for parent in self.get_node_by_id(id).get_parent_ids() :
            self.get_node_by_id(parent).remove_child_id_all(id)
        for child in self.get_node_by_id(id).get_children_ids() :
            self.get_node_by_id(child).remove_parent_id_all(id)
        del self.nodes[id]

    ''''''
    '''méthode appliquée au graphe qui retire plusieurs arretes du graphe, entre les nodes compris dans 2 listes. modifie le graphe
    arguments : src : node list
                tgt : node list
    return : none '''
    def remove_edges(self,src,tgt):#src et tgt sont des listes de nodes    # a tester  # retire plusieurs aretes au graphe
        for i in src :
            for  j in tgt :
                self.remove_edge(i.id ,j.id)

    '''méthode appliquée au graphe. Retire plusieurs nodes au graphe
    argument : ids : liste d'ids (les éléments de la liste correspondants aux ids des noeuds que l'on veut enlever.)
    return : none '''
    def remove_nodes_by_id(self,ids):   #ids une liste de ids        # a tester     # retire plusieurs nodes au graphe
        for i in ids:
            self.remove_node_by_id(i)

    '''Méthode appliquée au graphe qui vérifie si il est bien formé
    arguments : none
    return : bool : True si bien formé, False sinon'''
    def is_well_formed(self):                       # verifie si le graphe est correctement forme
        #########################################
        #              A modifier ?              #
        #########################################
        # partie 1
        for input_id in self.get_inputs_ids() :                           # on parcourt les inputs
            if not (input_id in self.get_node_ids()):           # on verifie que chaque input est dans les ids des nodes
                return False
        for output_id in self.get_outputs_ids() :                         # idem pour les outputs
            if not (output_id in self.get_node_ids()):
                return False

        # partie 2
        for node_id in self.get_node_ids() :                          # on parcourt les clefs du dict nodes
            if node_id != self.get_node_by_id(node_id).get_id():         # on verifie que la clef correspond a l'id d'un node
                return False

        # partie 3
        for node in self.get_nodes() :                       # on parcourt les nodes
            for child_id in node.get_children_ids() :           # pour chaque node, on parcourt les enfants
                if not (count_occurrences(node.get_children_ids(), child_id) == count_occurrences(self.get_node_by_id(child_id).get_parent_ids(), node.get_id())):      # pour chaque enfant, on compte le nombre d'occurrence(s) de son id dans les enfants du node
                    return False                                                                                                                                        # et on verifie que ce nombre est egal a celui des occurrences du node parmi les parents de l'enfant
            for parent_id in node.get_parent_ids() :           # pour chaque node, on parcourt les parents
                if not (count_occurrences(node.get_parent_ids(), parent_id) == count_occurrences(self.get_node_by_id(parent_id).get_children_ids(), node.get_id())):       # pour chaque parent, on compte le nombre d'occurrence(s) de son id dans les parents du node
                    return False                                                                                                                                        # et on verifie que ce nombre est egal a celui des occurrences du node parmi les enfants du parent
        return True                                             # si aucune erreur n'a ete detectee, alors le graphe est bien forme'''


    '''méthode qui change la valeur d'une id d'un noeud du graph, méthode appliquée au graph
    argument : node_id : id que l'on veut modifier
               new_id : l'id par laquelle on veut remplacer node_id
    return : none
    '''
    def change_id(self, node_id, new_id):
        #if(self.id_exists_in_graph(new_id) ):
        #self.get_node_by_id(node_id).id = new_id
        for i in self.get_node_by_id(node_id).get_parent_ids():                 #i parcours une liste des parents du node d'id node_id
            children= self.get_node_by_id(i).get_children_ids()                 #children prend la valeur de la liste des ids des children du node d'id i (donc chaque parent du node d'id node_id)
            for j in range(len(children)):                                      #on parcours tous les elemens de children
                if (children[j] == node_id):
                    children[j] = new_id
            self.get_node_by_id(i).children = children
        for i in self.get_node_by_id(node_id).get_children_ids():
            parents =  self.get_node_by_id(i).get_parent_ids()
            for j in range(len(parents)):
                if(parents[j] == node_id):
                    parents[j]=new_id
            self.get_node_by_id(i).parents = parents 
        for i in range(len(self.get_inputs_ids())):
            if (self.get_inputs_ids()[i]==node_id):
                self.inputs[i]=new_id
        for i in range(len(self.get_outputs_ids())):
            if (self.get_outputs_ids()[i]==node_id):
                self.outputs[i]=new_id
        self.nodes[new_id]=self.get_node_by_id(node_id)
        self.nodes.pop(node_id)
        #else:
        #    print(new_id)
        #    raise ValueError('new id already exists')

    '''méthode qui change plusieurs ids du graphe. Méthode appliquée au graphe.
    argument: change : liste de couple. Premier élément des couple : id a remplacer. Deuxieme élément ; id par lequel remplacer
    return : none '''
    def change_ids(self, change):
        sorted(change, key = lambda t: t[1])
        for couple in range(len(change)) :
            self.change_id(change[couple][0], change[couple][1])

    '''méthode appliquée a un graph qui renvoie un graph correspondant a la matrice d'adjacence de type form , de taille n*n et avec des valeurs entre 0 et bound
    argument : n : int : taille de la matrice
               bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
               intputs : int, par défaut 0
               outputs : int, par défaut 0
               form : string, par défaut 'free', peut prendre les valeurs : DAG, oriented, undirected, free'''
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


    '''méthode qui s'applique a un graphe qui calcule le degré entrant maximum du graphe
    argument : none
    return : int '''
    def max_indegree(self):
        max = 0
        for node in self.get_nodes() :
            degree = node.indegree()
            if degree > max :
                max = degree
        return max

    '''méthode qui s'applique a un graphe qui calcule le degré entrant minimum du graphe
    argument : none
    return : int '''
    def min_indegree(self):
        if not self.get_node_ids():
            return -1
        min = self.get_node_by_id(self.get_node_ids()[0]).indegree()              # on prend le degree entrant d'un node quelquonque comme premier minimum
        for node in self.get_nodes() :
            degree = node.indegree()
            if degree < min :
                min = degree
        return min

    '''méthode qui s'applique a un graphe qui calcule le degré sortant maximum du graphe
    argument : none
    return : int '''
    def max_outdegree(self):
        max = 0
        for node in self.get_nodes() :
            degree = node.outdegree()
            if degree > max :
                max = degree
        return max

    '''méthode qui s'applique a un graphe qui calcule le degré sortant minimum du graphe
    argument : none
    return : int '''
    def min_outdegree(self):
        if not self.get_node_ids():
            return -1
        min = self.get_node_by_id(self.get_node_ids()[0]).outdegree()              # on prend le degree sortant d'un node quelquonque comme premier minimum
        for node in self.get_nodes() :
            degree = node.outdegree()
            if degree < min :
                min = degree
        return min

    '''méthode qui s'applique a un graphe qui calcule le degre maximum d'un graphe
    argument : None
    return : int '''
    def max_degree(self):
        max = 0
        for node in self.get_nodes() :
            degree = node.degree()
            if degree > max :
                max = degree
        return max

    '''méthode qui s'applique a un graphe qui calcule le degre minimum d'un graphe
    argument : None
    return : int '''
    def min_degree(self):
        if not self.get_node_ids():
            return -1
        min = self.get_node_by_id(self.get_node_ids()[0]).degree()              # on prend le degree d'un node quelquonque comme premier minimum
        for node in self.get_nodes() :
            degree = node.degree()
            if degree < min :
                min = degree
        return min

    '''methode qui teste la cyclicité d'un graphe
    arguments : none
    return : True si le graph est cyclic
             False sinon
    '''
    def is_cyclic(self):
        def is_cyclic_aux(listnodes):
            if not listnodes:
                return True
            for i in range(len(listnodes)):
                if (self.get_node_by_id(listnodes[i]).get_children_ids() == []):
                    listnodes.remove(listnodes[i])
                    return is_cyclic_aux(listnodes)
                if (i==len(listnodes)-1) :
                   return False
        return is_cyclic_aux(self.get_node_ids())

    '''méthode qui ajoute n a tous les indices du graphe'''
    def shift_indices(self, n):
        for id in self.inputs :
            self.get_node_by_id(id).change_id_node(n)
        for id in self.outputs :
            self.get_node_by_id(id).change_id_node(n)
        L = []
        for id in self.get_node_ids():
            L.append((id, id + n))
            self.change_ids(L)





        #TD7

    '''methode qui compose parallelement deux cycles booleen, en en modifiant un mais pas l'autre
    arguments : g, le graphe a composer dans self
    return : none
    '''
    def iparallel(self,g):
        for input_id in g.get_inputs_ids():
            self.add_input_id(input_id)
        for output_id in g.get_outputs_ids():
            self.add_output_id(output_id)
        for node_id in g.get_node_ids():
            slef.add_node(str(g.get_node_by_id(node_id).get_label()), g.get_parent_ids(), g.get_children_ids())

    '''methode qui compose parallelement deux cycles booleen, sans les modifier
    arguments : g, le graphe a composer avec self
    return : graph, un nouveau graph qui est la composition parallele de g et de self
    '''
    def parallel(self,g):
        graph = self.copy()
        graph.iparallel(g)
        return graph





class bool_circ(open_digraph):
    def __init__(self,g):
        '''
        Méthode __init__ :
        Initialise un circuit booléen à partir du graph
        g: open_digraph
        '''
        self.inputs = g.get_inputs_ids()
        self.outputs = g.get_outputs_ids()
        self.nodes = g.get_id_node_map() # self.nodes: <int,node> dict
        if (g.is_well_formed() == False ):
            raise Exception("Désolé, le circuit booleen est mal formé")

    '''methode qui convertit un circuit en graphe
    arguments : circ, circuit a convertir
    return : g, le graphe correspondant au circuit circ
    '''
    def convert(self, circ):
        #circ :  un circuit booléen bool_circ
        g = open_digraph([],[],[])
        g.inputs = self.get_inputs_ids()
        g.nodes = self.get_nodes()
        g.outputs = self.get_outputs_ids()
        return g



    '''methode qui verifie si un circuit est bien un circuit booleen
    arguments : non
    return : True si le circuit est bien forme i.e. si il est valide et acyclique
            False sinon
    '''

    def is_well_formed(self) :
        acyclique = self.is_cyclic()
        for node in self.get_nodes():
            if not node.get_label() :
                valide = node.indegree() == 1
            elif node.get_label() == '&' or  node.get_label() == '|' :
                valide = node.outdegree() == 1
            elif node.get_label() == "~" :
                valide = node.indegree() == 1 and node.outdegree() == 1
        return acyclique and valide

    '''méthode appliquée a un circuit booleen, qui donne l'indice minimum du circuit
    argument : none
    return : un indice '''
    def min_id(self):
        if(self.get_node_ids() == []):
            return 0
        idmin = self.get_node_ids()[0]
        for id in self.get_node_ids() :
            if (id <idmin) :
                idmin = id
        return idmin

    '''méthode appliquée a un circuit booleen, qui donne l'indice maximum du circuit
    argument : none
    return : un indice '''
    def max_id(self):
        if (self.get_node_ids() == []):
            return 0
        idmax = self.get_node_ids()[0]
        for id in self.get_node_ids() :
            if (id >idmax) :
                idmax = id
        return idmax










'''Fonction qui renvoie un graphe correspondant a une matrice d'adjacence
argument : matrix : int list list : matrice d'adjacence
return : graph '''
def graph_from_adjacency_matrix(matrix) :           # renvoie un graphe correspondant a la matrice d adjacence matrix
    graph = open_digraph.empty()                    # on cree un graphe vide vide a partir duquel on va construire le graphe voulu
    '''
    on ne sert pas de la methode add_node car on part du graphe vide
    et donc la methode tente de faire des aretes avec des nodes qui n ont pas encore ete crees
    modifier la methode pour resoudre le bug serait trop complique donc on fait autrement
    a la place, on parcourt deux fois la matrice, une premiere fois pour creer tous les nodes sans les aretes
    '''
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

    return graph
