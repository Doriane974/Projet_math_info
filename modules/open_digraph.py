import operator
import sys
sys.path.append('../')
from modules.utils import *
from modules.open_digraph_composition_mx import *
from modules.open_digraph_getters_mx import *
#from modules.open_digraph_add_mx import *
from modules.open_digraph_calc_degrees_mx import *
from modules.node_getters_mx import *



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
        '''
        output : str ; the string given by str(node)
        '''
        return "(" + str(self.id) +"," + self.label +","+ str(self.parents) + "," + str(self.children) + ")"

    def __repr__(self):
        return "node"+str(self)


    def copy(self):                     # renvoie une copie du node (node)
        '''méthode appliqué au node qui renvoie une copie de ce node
        argument : nonde
        return : node '''
        return node(self.id, self.label, self.parents.copy(),self.children.copy())


    def get_id(self):                   # renvoie l'id du node (int)
        '''méthode appliquée au node qui renvoie l'id de ce node
        argument : none
        return : int '''
        return self.id


    def get_label(self):                # renvoie le label du node
        '''méthode appliquée au node qui renvoie le label de ce node
        argument : none
        retunr : label '''
        return self.label


    def get_parent_ids(self):           # renvoie la liste des parents du node (int list)
        '''méthode appliquée au node qui renvoie la liste des parents de ce node
        argument : none
        return : id list '''
        return self.parents


    def get_children_ids(self):         # renvoie la liste des enfants du node (int list)
        '''méthode appliquée au node qui renvoie la liste des enfants du node
        argument : nonde
        return : id list  '''
        return self.children



    def set_id (self, id) :             # affecte une valeur a l'id du node (char)
        '''méthode appliquée au node qui affecte une valeur a l'id du node
        argument : id : id que l'on veut affecter
        return : none '''
        self.id = id


    def set_label (self, label) :       # affecte un string au label du node (string)
        '''méthode appliquée au node qui affecte un label au node
        argument : label : label que l'on veut affecter
        return : none '''
        self.label = label


    def set_parent_ids (self, parent_ids) :         # affecte une valeur aux ids des parents du node (int list)
        '''méthode appliquée au node qui affecte une valeur au parents de ce node
        argument : id list
        return : none  '''
        self.parents = parent_ids


    def set_children_ids (self, children_ids) :     # affecte une valeur aux ids des enfants du node (int list)
        '''méthode appliquée au node qui affecte une valeur au enfants de ce node
        argument : id list
        return : none  '''
        self.children = children_ids


    def add_child_id (self, child_id) :             # ajoute une valeur a la liste des id des enfants du node (int)
        '''méthode appliquée au node qui ajoute une valeur a la liste des ids des enfants de ce node
        argument : child_id : id à ajouter
        return : none  '''
        self.children.append(child_id)


    def add_parent_id (self, parent_id) :           # ajoute une valeur a la liste des id des parents du node (int)
        '''méthode appliquée au node qui ajoute une valeur a la liste des ids des parents de ce node
        arguments : parent id : id à ajouter
        return : none '''
        self.parents.append(parent_id)


    def add_parents_ids (self, parents_ids):
        '''méthode appliquée au node qui ajoute une liste de valeur a la liste des ids des parents de ce node
        arguments : parents_ids : liste d'id à ajouter
        return : none '''
        for id in parents_ids :
            self.add_parent_id(id)


    def remove_parent_id(self, parent_id):          # retire la valeur specifiee a la liste des ids des parents du node (int)
        '''méthode appliquée au node qui retire la valeur spécifiée a la liste des ids des parents du node
        argument : parent id : id
        return : none '''
        if parent_id in self.get_parent_ids():
            self.parents.remove(parent_id)


    def remove_child_id(self, child_id):            # retire la valeur specifiee a la liste des ids des enfants du node (int)
        '''méthode appliquée au node qui retire la valeur spécifiée a la liste des ids des parents du node
        argument ; child_id : id
        return : none '''
        if child_id in self.get_children_ids():
            self.children.remove(child_id)


    def remove_parent_id_all(self, parent_id):      # retire tous les ids des parents du node (int list)
        '''méthode appliquée au node qui retire tous les ids donnés des parents du node
        argument : parent_id : id list
        return : none  '''
        remove_all(self.parents, parent_id)


    def remove_child_id_all(self, child_id):        # retire tous les ids des enfants du node (int list)
        '''méthode appliquée au node qui retire tous les ids donnés des enfants du node
        argument : child_id : id list
        return : none  '''
        remove_all(self.children, child_id)




    def outdegree(self):                            # donne le degre sortant du node
        '''méthode qui s'applique a un node qui donne le degre sortant du node
        argument : none
        return : int '''
        return len(self.get_children_ids())


    '''méthode qui s'applique a un node qui donne le degre entrant du node
    argument : none
    return : int '''
    def indegree(self):                             # donne le degre entrant du node
        '''méthode qui s'applique a un node qui donne le degre entrant du node
        argument : none
        return : int '''
        return len(self.get_parent_ids())

    def degree(self):                               # donne le degre du node
        '''méthode qui s'applique a un node qui donne le degré du node (degre entrant + degre sortant)
        argument : none
        return : int '''
        return self.indegree() + self.outdegree()

    def change_id_node(self, n):
        '''méthode appliquée a un node qui change l'id de ce node, en additionnant n
        à l'id actuel
        argumetns : n : nombre a ajouté
        return : none '''
        self.id = self.get_id() + n


class open_digraph(open_digraph_composition_mx, open_digraph_getters_mx,  open_digraph_calc_degrees_mx): #for open directed graph

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


    def copy(self):                         # renvoie une copie du graphe (digraph)
        '''méthode appliquée au graphe qui retourne une copie du graphe
        argument : none
        return : un nouveau graph '''
        return open_digraph(self.inputs.copy(), self.outputs.copy(), [node.copy() for node in self.nodes.values()])


    def empty():                            # renvoie un graphe vide (digraph)
        '''fonction qui renvoie un graphe vide
        arguments : none
        return : un graphe '''
        return open_digraph([],[],[])

    def id_exists_in_graph(self,id):
        '''méthode appliquée au graphe qui vérifie si une id existe deja dans le graphe
        argument : id : l'id dont on veut savoir si elle existe ou non
        return : bool : True si l'id existe, False sinon '''
        if id in self.get_node_ids():
            return True
        else:
            return False


    def set_input_ids (self, input_ids) :              # affecte les inputs du graphe a input_ids
        '''méthode appliquée au graphe qui affecte input_ids aux inputs du graph
        argument : inputs_ids : id list
        return : none '''
        self.inputs = input_ids


    def set_output_ids (self, output_ids) :             # affecte les outputs du graphe a output_ids
        '''méthode appliquée au graphe qui affecte output_ids aus outputs du graph
        argument : outputs_ids : id list
        return : none '''
        self.outputs= output_ids

    def add_input_id (self, input_id) :                 # ajoute une valeur a la liste des inputs du graphe
        '''méthode appliquée au graphe qui ajoute une valeur a la liste des inputs du graphe
        argument : input_id : id à ajouter  '''
        self.inputs.append(input_id)

    def add_output_id (self, output_id) :               # ajoute une valeur a la liste des outputs du graphe
        '''méthode appliquée au graphe qui ajoute une valeur a la liste des outputs du graphe
        argument : output_id : id à ajouter  '''
        self.outputs.append(output_id)


    def add_edge(self, src, tgt):                       # ajoute une arete entre les nodes
        '''méthode appliquée au graphe qui ajoute une arrete entre 2 nodes
        argument : src : Id du node qui deviendra le parent
                   tgt : Id du node qui deviendra l'enfant '''
        #print("nodes =", self.get_node_ids())
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)


    def add_edges(self, src, tgt):          # ajoute des aretes entre les nodes
        '''méthode appliquée au graph qui ajoute des arrete entre un node et une liste de node
        arguments : src : Id du node qui deviendra le parent
                    tgt ; liste d'Id des nodes qui deviendront les enfants de src '''
        #print("tgt =", tgt)
        for i in tgt:
            self.add_edge(src,i)


    def add_node(self, id=None, label='', parents=[], children=[]):             # ajoute un node au graphe                               # pas sur du tout, et à tester
        '''méthode appliquée au graphe qui ajoute un node au graphe
        argument : label : label, par défaut ''
                   parents : id list, par défaut []
                   children : id list, par défaut []
        return : id : l'id du node qui a été ajouté '''
        if id is None:
            id = self.new_id()
        n0 = node(id, label, [],[])
        self.nodes[id]=n0
        #print('add_node1', n0, children)
        for i in parents:
            self.add_edge(i, id)
        #print('add_node2', n0, children)
        self.add_edges(id, children)
        return id


    def new_id(self):                                   # renvoie un id non utilise par le graphe
        '''méthode appliquée au graphe qui  retourne un Id qui n'est pas utilisé dans le graphe
        argument : none
        return : un id '''
        dict = self.get_id_node_map()
        if (dict =={}):
            return 0
        else:
            if dict :
                return (max(dict)+1) #quand je rajoute default=-1 ca bug
            else :
                return 0


    def remove_edge(self,src,tgt):                                      # retire une arete du graphe
        '''méthode appliquée au graphe qui retire une arete du graph
        argument : src : id
                   tgt : id
        return : none '''

        self.get_node_by_id(src).remove_parent_id(tgt)
        self.get_node_by_id(src).remove_child_id(tgt)
        self.get_node_by_id(tgt).remove_parent_id(src)
        self.get_node_by_id(tgt).remove_child_id(src)


    def remove_node_by_id(self, id):
        '''méthode appliquée au graphe qui enleve un noeud ayant l'Id voulue du graphe
        argument : id : id du noeud que l'on veut retirer
        return : none '''
        for parent in self.get_node_by_id(id).get_parent_ids() :
            self.get_node_by_id(parent).remove_child_id_all(id)
        for child in self.get_node_by_id(id).get_children_ids() :
            self.get_node_by_id(child).remove_parent_id_all(id)
        remove_all(self.inputs, id)
        remove_all(self.outputs, id)
        self.nodes.pop(id)


    def remove_edges(self,src,tgt):#src et tgt sont des listes de nodes    # a tester  # retire plusieurs aretes au graphe
        '''méthode appliquée au graphe qui retire plusieurs arretes du graphe, entre les nodes compris dans 2 listes. modifie le graphe
        arguments : src : node list
                    tgt : node list
        return : none '''
        for i in src :
            for  j in tgt :
                self.remove_edge(i.id ,j.id)


    def remove_nodes_by_id(self,ids):   #ids une liste de ids        # a tester     # retire plusieurs nodes au graphe
        '''méthode appliquée au graphe. Retire plusieurs nodes au graphe
        argument : ids : liste d'ids (les éléments de la liste correspondants aux ids des noeuds que l'on veut enlever.)
        return : none '''
        for i in ids:
            self.remove_node_by_id(i)


    ############################################################################
    ###                   Ne passe pas le test je crois                        #
    def is_well_formed(self):                       # verifie si le graphe est correctement forme
        '''Méthode appliquée au graphe qui vérifie si il est bien formé
        arguments : none
        return : bool : True si bien formé, False sinon'''
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


    def change_id(self, node_id, new_id):
        '''méthode qui change la valeur d'une id d'un noeud du graph, méthode appliquée au graph
        argument : node_id : id que l'on veut modifier
                   new_id : l'id par laquelle on veut remplacer node_id
        return : none
        '''
        if(not self.id_exists_in_graph(new_id)):
            #print("node_id =", node_id," new_id = ", new_id)
            for i in self.get_node_by_id(node_id).get_parent_ids():                 #i parcours une liste des parents du node d'id node_id
                #print("i=",i)
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
        else:
            #print(new_id)
            raise ValueError('new id already exists')


    def change_ids(self, change):
        '''méthode qui change plusieurs ids du graphe. Méthode appliquée au graphe.
        argument: change : liste de couple. Premier élément des couple : id a remplacer. Deuxieme élément ; id par lequel remplacer
        return : none '''
        sorted(change, key = lambda t: t[1])
        for couple in change :
            self.change_id(couple[0], couple[1])


    def random_graph(self, n, bound, inputs=0, outputs=0, form="free"):     # renvoie un graphe correspondant a la matrice d adjacence de type form, de taille n * n et avec des valeurs entre 0 et bound
        '''méthode appliquée a un graph qui renvoie un graph correspondant a la matrice d'adjacence de type form , de taille n*n et avec des valeurs entre 0 et bound
        argument : n : int : taille de la matrice
                   bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
                   intputs : int, par défaut 0
                   outputs : int, par défaut 0
                   form : string, par défaut 'free', peut prendre les valeurs : DAG, oriented, undirected, free'''

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
        #print(matrix)
        #print(graph)
        return graph


    def is_cyclic(self):
        '''methode qui teste la cyclicité d'un graphe
        arguments : none
        return : True si le graph est cyclic
                 False sinon
        '''
        def is_cyclic_aux(g, listnodes):
            if (listnodes==[]):
                return False
            for i in range(len(listnodes)):
                #print(listnodes)
                if (g.get_node_by_id(listnodes[i]).get_children_ids() == []):
                    g.remove_node_by_id(listnodes[i])
                    listnodes.remove(listnodes[i])
                    return is_cyclic_aux(g, listnodes)
                if (i==len(listnodes)-1) :
                   return True
        g = self.copy()
        return is_cyclic_aux(g, g.get_node_ids())

    #TD7

    def shift_indices(self, n):
        '''méthode qui ajoute n a tous les indices du graphe
        arguments : n : int
        return : none '''
        #trier dans l'ordre décroissant a chaque fois. edit : en fait ca résout pas le problème
        list_inputs = self.get_inputs_ids()
        list_inputs.sort(reverse=True)
        list_outputs = self.get_outputs_ids()
        list_outputs.sort(reverse=True)
        for id in list_inputs :
            self.get_node_by_id(id).change_id_node(n)
        for id in list_outputs :
            self.get_node_by_id(id).change_id_node(n)
        L = []
        for id in self.get_node_ids():
            L.append((id, id + n))
        self.change_ids(L)


    def connected_components(self): # done
        ''' Methode permettant d extraire d un graphe le nombre de composantes connexes et quel node est dans quelle cc
        arguments : None
        return : nb_cc, int, nombre de cc dans le graphe
                 dict, un dictionnaire id de node : id de cc correspondante'''
        # On va se servir d'une fonction auxilliaire recursive pour explorer les enfants (seulement, car on parcourt tous les nodes donc on aura les parents a un moment) de chaque node.
        nb_cc = 0                   # nombre de composantes connexes
        dict = {}                    # dictionnaire int id de node : int num de composante connexe
        for node in self.get_nodes():           # on parcourt tous les nodes, car on veut rechercher les cc sur tout le graph
            list_nodes_ids_cc = []              # la liste des id des nodes de la cc du node node
            node_id = node.get_id()     # id du node considere
            #print("cc1", nb_cc, dict, list_nodes_ids_cc, node_id)
            if not node_id in dict:         # on teste si le node est deja dans le dictionnaire, si c est le cas, ce n est pas la peine de le tester donc on passe au suivant
                cc_id = nb_cc           # id de la composante connexe consideree, on l initialise a nb_cc soit le premier id non utilise
                children = list_cleaner(self.rec_exploration(node))         # on utilise la fonction recursive pour optenir tous les descendants du node considere, et on retire les doublons
                list_nodes_ids_cc = [node_id] + [i.get_id() for i in children]    # la liste partielle de la cc est composée du node node et de ses descendants
                new_cc = True                           # boolen pour noter si le node node est dans un cc non repertoriee
                #print("cc2", nb_cc, dict, list_nodes_ids_cc, node_id, cc_id)
                for id in list_nodes_ids_cc:            # on parcourt la liste d id des nodes de la cc qu on vient de creer
                    if id in dict:                      # si un id est deja dans le dict, il faudra ajouter les nodes a une cc deja existante
                        cc_id = dict[id]                # sinon, il faudra en creer une nouvelle
                        new_cc = False
                        break
                #print("cc3", nb_cc, dict, list_nodes_ids_cc, node_id, cc_id)
                for id in list_nodes_ids_cc:            # on parcourt de nouveau la liste, cette fois pour la remplir
                    dict[id] = cc_id                    # si le node est deja dans le dict, cela ne pose pas de probleme (pas de doublons dans un dict)
                if new_cc:                              # si on  a cree une nouvelle cc, il y en a une de plus au total
                    nb_cc += 1
                #print("cc4", nb_cc, dict, list_nodes_ids_cc, node_id, cc_id)
        return (nb_cc, dict)


    def rec_exploration(self, node):
        '''Fonction recursive permettant l exploration des enfants d un node (node), et qui stocke ceux-ci dans une liste node_list
        arguments : node, le node a partir duquel on part
        return : children_list, liste des nodes descendants du node node
        Note : cela peut produire des doublons, mais ceux-ci seront geres lors des appels a la fonction'''
        #print("pouet", node)
        children_list = []          # on cree la liste des descendants du node self, initialisee vide.
        children = self.get_node_by_ids(node.get_children_ids())         # on recupere les enfants du node
        for child in children:                      # on parcourt les enfants du node
            if not child in children_list :         # si ces enfants ne sont pas deja dans la liste
                children_list.append(child)         # on les y ajoute
                children_list += self.rec_exploration(child)    # et on appelle recursivement cette fonction pour ajouter les petits enfants
        return children_list                        # on renvoie la liste vers les appels recursifs precedents


    def decompose(self):
        '''Methode qui decompose un graphe en ses composantes connexes et permutations
        arguments : None
        return : list_cc, une liste d open digraphs des composantes connexes du graphe
                 perm_inputs, une permutation representant les entrees du graphe
                 perm_outputs, une permutation representant les sorties du graphe'''
        # On va se servir de connected_components() pour retrouver quelle node va dans quelle cc,
        # ensuite "reconstruire" les cc, et pour finir calculer les permutations d'input/output pour pouvoir reconstruire le graphe
        inputs = self.get_inputs_ids()                  # on recupere les inputs du graphe
        outputs = self.get_outputs_ids()                # on recupere les outputs du graphe
        nodes = self.get_nodes()                        # on recupere les nodes du graphe
        nb_cc, dict_cc = self.connected_components()    # on recuper les cc du graphe
        list_cc = []                                    # on initialise la liste des cc a vide
        inputs2 = []                                    # (pour la permutation)
        outputs2 = []
        # print("decompose")
        for cc_id in range(nb_cc):                      # on connait le nombre de cc du graphe, donc pour chaque cc, on peut la construire sous forme d open drigraph
            dict_node_cc = {}                           # on cree a vide le dictionnaire des nodes de la cc en cours
            inputs_cc = []                              # on cree a vide la liste des inputs de la cc en cours
            outputs_cc = []                             # on cree a vide la liste des outputs de la cc en cours
            for node in nodes:                          # on doit commencer par creer le graphe de la cc pour pouvoir operer avec
                node_id = node.get_id()                 # on recupere l id du node considere
                if cc_id == dict_cc[node_id]:           # on teste si le node considere est dans la cc en cours
                     dict_node_cc[node_id] = node       # si c est le cas, on l ajoute au dict des nodes de la cc en cours
            # print("dict_node_cc =", dict_node_cc)
            for node_id in inputs:                      # on parcourt les id dans les inputs du graphe
                if node_id in dict_node_cc:             # si le node en input est dans la cc, alors il est en input du graphe de la cc
                    inputs_cc.append(node_id)           # donc on l y ajoute
            for node_id in outputs:                     # on parcourt les id dans les outputs du graphe
                if node_id in dict_node_cc:             # si le node en output est dans la cc, alors il est en output du graphe de la cc
                    outputs_cc.append(node_id)          # donc on l y ajoute
            # print("list_node_cc =", list(dict_node_cc.values()))
            list_cc.append(open_digraph(inputs_cc, outputs_cc, list(dict_node_cc.values())))   # on peut enfin construire le graphe de la cc
            inputs2.append(inputs_cc)
            outputs2.append(outputs_cc)
            #print("list_cc =", list_cc[0])
            # print("inputs2 =", inputs2)
            # print("outputs2 =", outputs2)
        perm_inputs = perm_calc(inputs, inputs2)                    # on calcule les permutations
        perm_outputs = perm_calc(outputs, outputs2)
        return list_cc, perm_inputs, perm_outputs


    def dijkstra(self, src, tgt = None, direction = None) :
        '''algorithme de dijkstra
        ############################################################################
        ###########                   A DEBUGUER                         ###########
        arguments : src : id du node initial
                    tgt : optionnel : id du node dont on veut donnaitre le plus court chemin entre lui et src
                    direction : optionnel : peut prendre la valeur 1, -1 ou None, décrit la drirection dans laquelle
                                            on va chercher le plus court chemin '''
        Q = [src]
        dist = {}
        dist[src] = 0
        prev = {}
        while(Q != []):
            u = min(Q, key = lambda x:dist[x] ) #une fonction qui a x associe dist x
            remove_all(Q, u)
            neighbour=[]
            if (direction == -1):
                neighbour = self.get_node_by_id(u).get_parent_ids()
            if(direction == 1 ):
                neighbour = self.get_node_by_id(u).get_children_ids()
            if (direction == None):
                neighbour = self.get_node_by_id(u).get_parent_ids()
                for id in self.get_node_by_id(u).get_children_ids():
                    neighbour.append(id)
            for v in neighbour:
                if(not (v in dist)):
                    Q.append(v)
                if ( (not(v in dist)) or (dist[v]>dist[u]+1)):
                    dist[v] = dist[u]+1
                    prev[v] = u
        '''Faire la 1ere partie de exo 2 '''
        return dist, prev


    def shortest_path(self, src, tgt):
        '''Méthode qui s'applique a un graphe, qui calcule le chemin le plus court entre 2 node, de src vers tgt
        arguments : src : node
                    tgt : node
        return : int : shortest distance entre src et tgt '''
        dist, prev = self.dijkstra(src, tgt)
        return dist[tgt]


    def dist_common_ancestors(self, src1, src2):
        '''méthode qui s'applique a un graphe, qui, étant donné 2 noeuds, renvoie un dictionnaire
        qui associe a chaque ancetres commun des deux noeuds sa distance a chacun des 2 noeuds
        arguments : src1 : noeud
                    src2 : noeud
        return : dictionnaire
        '''
        dist_1, prev_1 = self.dijkstra(src1, tgt = None, direction = -1)
        dist_2, prev_2 = self.dijkstra(src2)
        dist_common_ancestors = {}
        for id_node_ancetre_de_1 in dist_1:
            for id_node_ancetre_de_2 in dist_2:
                if (id_node_ancetre_de_1 == id_node_ancetre_de_2):
                    dist_common_ancestors[id_node_ancetre_de_2] = (dist_1[id_node_ancetre_de_1], dist_2[id_node_ancetre_de_2])
        return dist_common_ancestors

    def tri_topologique(self):
        '''méthode qui implemente le tri topologique compressé vers le haut.
        @param : none
        @return : id list list'''

        g = self.copy()
        listNodeSelf = self.get_node_ids()
        listDejaTrie = []
        listRestant = listNodeSelf
        listTriTopo = []

        while len(listRestant)>0 :
            #la liste du niveau actuel
            nodeNiveau = []
            #on regarde les nodes qui n'ont pas de parents dans le graph
            for id in listRestant:
                if g.get_node_by_id(id).get_parent_ids() == []:
                    #on les ajoute a la liste du niveau actuel
                    nodeNiveau.append(id)

            for id in nodeNiveau:
                #on supprime les ids qu'on vient de mettre dans la liste de nouveau de la liste des nodes restant a trier
                listRestant.remove(id)
                #on les ajoute a la liste des nodes deja trié
                listDejaTrie.append(id)


            #print("in Tri topologique, listDejaTrie = ", listDejaTrie)
            #print("in Tri topologique, listRestant = ", listRestant)
            #print("in Tri topologique, listTriTopo = ", listTriTopo)

            #On supprime les noeuds deja trié du graphe, afin d'avoir de nouveaux noeuds sans parents
            for id in nodeNiveau:
                g.remove_node_by_id(id)

            #on ajoute la liste du niveau a la liste totale du tri topo
            listTriTopo.append(nodeNiveau)

        #on retourne la liste du tri topologique
        return listTriTopo

    def profondeur_node_by_id(self, id):
        listTriTopo = self.tri_topologique()
        i = 0
        for list in listTriTopo:
            if id in list:
                return i
            else :
                i=i+1


    def fusion_nodes(self, id1, id2, label = None):
        '''méthode appliquée a un graphe qui fuisionne 2 nodes en un seul.
        arguments : id1 : id du premier noeud à fusionner
                    id 2 : id du deuxieme noeud a fusionner
                    label : par défaut : none, le label a donner au noeud créé par la fusion.
                            Si rien n'est préciser, le label de la fusion sera le label du noeud d'id id1
        return : None
        '''
        #on ajoute aux enfant de id1 les enfants de id2
        #print("fusion node,id1, id2 =", id1, "   ", id2)
        #print("fusion node,self.get_node_by_id(id1) = ", self.get_node_by_id(id1))
        for child2 in self.get_node_by_id(id2).get_children_ids():
            self.get_node_by_id(id1).add_child_id(child2)
        #print("fusion1")
        #on ajoute aux parents de id1 les parents de id2
        for parent2 in self.get_node_by_id(id2).get_parent_ids():
            self.get_node_by_id(id1).add_parent_id(parent2);
        #print("fusion2")
        #on ajoute remplace id1 par id2 dans la liste des inputs
        for i in range(len(self.get_inputs_ids())):
            if ( self.get_inputs_ids()[i] == id2):
                self.inputs[i] = id1
        #print("fusion3")
        #on ajoute remplace id1 par id2 dans la liste des outputs
        for i in range(len(self.get_outputs_ids())):
            if ( self.get_outputs_ids()[i] == id2):
                self.outputs[i] = id1
        #print("fusion4")
        #on ajoute le bon label
        if(label != None ):
            self.get_node_by_id(id1).set_label(label)
        self.remove_node_by_id(id2)


    def compte_generation(self, id_base, comptGlobal, comptLocal):
        '''methode qui s'applique a un graphe qui compte le nombre maximal d'enfant d'un node.
        arguments : id : l'id du noeud dont on veut connaitre le nombre de génération d'héritier il a
                    comptGlobal : un compteur, initialisé a 0 par défaut
        return : le nombre de génération en dessous du node d'id id .
        '''
        for id in self.get_node_by_id(id_base).get_children_ids(): #on parcourts les enfants de id_base
            #print("compte_generation, dans la boucle for, id = ", id)
            comptLocal = comptLocal + 1#si il a un enfant, on incrémente
            if(self.get_node_by_id(id).get_children_ids() == []):#si cet enfant n'a pas d'enfant, on compare avec le cpt global
                #print("dans Compte_generation, dans la boucle for, dans le if, i= ", comptLocal, "et cptGloabl = ", comptGlobal)
                if ( comptLocal > comptGlobal):
                    comptGlobal = comptLocal
                    comptLocal = 0
            else:
                return self.compte_generation(id, comptGlobal,comptLocal)#si l'enfant a un enfant, on réappelle la fonction mais avec l'enfant de l'id de base ,
        return comptGlobal



def graph_from_adjacency_matrix(matrix) :           # renvoie un graphe correspondant a la matrice d adjacence matrix
    '''Fonction qui renvoie un graphe correspondant a une matrice d'adjacence
    argument : matrix : int list list : matrice d'adjacence
    return : graph '''
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
                #print('matrix =', matrix)
                #print('i =', i)
                #print('j =', j)
                graph.add_edge(j, i)                # on a decide arbitrairement que la valeur de matrix[i][j] correspondrait a une arete de j vers i

    return graph



#bug parse_parenthese
#rajouter s2 au label de current node ?? dans parse parenthese, seudo code
#exo 2 : fusionner, quand est il des inputs, outputs?
