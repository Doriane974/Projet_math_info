import operator
import sys
sys.path.append('../')
from modules.utils import *
from modules.open_digraph_composition_mx import *
from modules.open_digraph_getters_mx import *
from modules.open_digraph_add_mx import *
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

    '''méthode appliquée au graphe qui ajoute une valeur a la liste des outputs du graphe
    argument : output_id : id à ajouter  '''
    def add_output_id (self, output_id) :               # ajoute une valeur a la liste des outputs du graphe
        self.outputs.append(output_id)


    def add_edge(self, src, tgt):                       # ajoute une arete entre les nodes
        '''méthode appliquée au graphe qui ajoute une arrete entre 2 nodes
        argument : src : Id du node qui deviendra le parent
                   tgt : Id du node qui deviendra l'enfant '''
        self.get_node_by_id(src).add_child_id(tgt)
        self.get_node_by_id(tgt).add_parent_id(src)


    def add_edges(self, src, tgt):          # ajoute des aretes entre les nodes
        '''méthode appliquée au graph qui ajoute des arrete entre un node et une liste de node
        arguments : src : Id du node qui deviendra le parent
                    tgt ; liste d'Id des nodes qui deviendront les enfants de src '''
        for i in tgt:
            self.add_edge(src,i)


    def add_node(self, label='', parents=[], children=[]):             # ajoute un node au graphe                               # pas sur du tout, et à tester
        '''méthode appliquée au graphe qui ajoute un node au graphe
        argument : label : label, par défaut ''
                   parents : id list, par défaut []
                   children : id list, par défaut []
        return : id : l'id du node qui a été ajouté '''
        id=self.new_id()
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







    ''''''

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


    '''méthode qui renvoie le nombre de composante donnexe d'un graphe, et un
    dictionnaire qui associe a chaque id de noeuds du graph un int qui correspond à une composante connexe
    arguments : none
    return : nb_cc, dict
    '''

    # WIP
    '''
    def connected_components(self): # pas fini
        nb_cc = 0                   # nombre de composantes connexes
        dict = {}                    # dictionnaire int id de node : int num de composante connexe
        list_cc = []                # liste (de listes) des composantes connexes, non rendue. Contient des listes, chacune contenant les nodes de la cc.
        for node in self.get_nodes() :
            node_id = node.get_id()     # id du node considere
            cc_id = nb_cc           # id de la composante connexe consideree, on l initialise a nb_cc soit le premier id non utilise
            for id in range(len(list_cc)):      # on parcourt la liste des cc
                if node_id in list_cc[id] :     # teste si le node appartient deja a une composante connexe
                    cc_id = id                  # si c est le cas, on ajoutera les nodes dans celle ci
                    break                       # sinon, on en creera une nouvelle
            if cc_id == nb_cc :                 # si cc_id == nb_cc, alors cc_id n a pas ete modifie, donc le node n etait dans aucune cc de la list_cc
                nb_cc += 1                      # on a une cc supplementaire donc on augmente nb_cc
                list_cc.append([])              # on ajoute une nouvelle liste correspondant a la nouvelle cc dans list_cc
                list_cc[cc_id].append(node_id)

            else :                              # sinon, le node etait deja dans list_cc, donc on ajoute ses enfants et parents dans la meme cc
                return
            #dict[node_id] = cc_id
        return (nb_cc, dict)
'''


    def connected_components(self): # done
        ''' Fonction permettant d extraire d un graphe le nombre de composantes connexes et quel node est dans quelle cc
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
        '''méthode appliquée a ungraphe qui fuisionne 2 nodes en un seul.
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
        #print("fusion faite")


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


    def convert(self, circ):
        '''methode qui convertit un circuit en graphe
        arguments : circ, circuit a convertir
        return : g, le graphe correspondant au circuit circ
        '''
        #circ :  un circuit booléen bool_circ
        g = open_digraph([],[],[])
        g.inputs = self.get_inputs_ids()
        g.nodes = self.get_nodes()
        g.outputs = self.get_outputs_ids()
        return g





    def is_well_formed(self) :
        '''methode qui verifie si un circuit est bien un circuit booleen
        arguments : non
        return : True si le circuit est bien forme i.e. si il est valide et acyclique
                False sinon
        '''
        if self.is_cyclic():
            return False
        valide = False
        for node in self.get_nodes():
            label = node.get_label()

            #on regarde si c'est un noeud de copie
            if not label :
                valide = node.indegree() == 1
                label = '|'

            elif label == '&' or  label == '|' :
                valide = node.outdegree() == 1
                if(node.get_id() in self.get_outputs_ids()):
                    valide = True
            elif label == "~" :
                inDegre = node.indegree()
                if (node.get_id() in self.get_inputs_ids()):
                    inDegre = 1
                outDegre =  node.outdegree()
                if (node.get_id() in self.get_outputs_ids()):
                    outDegre = 1
                valide = inDegre == 1 and outDegre == 1
            ####################################################################
            #     faire verifier cette ligne à mayeul, puisque j'ai un doute   #
            elif label == "^" or label == "XOR":
                valide = True
            elif label == "1" or label == "0":
                if node.get_parent_ids() == []:
                    valide = True

            labelValide = ['0', '1', 'XOR', '^', '~', '&', '|', '']
            if not label in labelValide :
                return False
            if(valide == False ):
                return valide
        return valide


    ############################################################################
    ##                               A tester                                 ##
    def min_id(self):
        '''méthode appliquée a un circuit booleen, qui donne l'indice minimum du circuit
        argument : none
        return : un indice '''
        if(self.get_node_ids() == []):
            return 0
        idmin = self.get_node_ids()[0]
        for id in self.get_node_ids() :
            if (id <idmin) :
                idmin = id
        return idmin

    ############################################################################
    ##                               A TESTER                                 ##
    def max_id(self):
        '''méthode appliquée a un circuit booleen, qui donne l'indice maximum du circuit
        argument : none
        return : un indice '''
        if (self.get_node_ids() == []):
            return 0
        idmax = self.get_node_ids()[0]
        for id in self.get_node_ids() :
            if (id >idmax) :
                idmax = id
        return idmax



    #############################   A TESTER   #################################
    def parse_parenthese(s):
        '''fonction qui transfore une formule propositionnelle en circuit booleen
        argument : s : string, la formule propociitonnelle a transformer
        return : un circuit booleen '''
        prems = node(0,'',[],[])
        g = open_digraph([],[0],[prems]);
        bc = bool_circ(g);
        current_node = 0
        s2 = ''
        for char in s :
            if(char == '('):
                bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2) # il faut concatener
                new = bc.add_node('',[],[current_node])
                current_node = new
                s2 = ''
            else:
                if( char == ')' ):
                    bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2)
                    id = bc.get_node_by_id(current_node).get_children_ids()
                    current_node = id[0]
                    s2 = ''
                else :
                    s2 = s2 + char
        return bc

    '''version temporaire pour exo3 en cours'''
    def parse_parenthese_2(s):
        prems = node(0,'',[],[])
        g = open_digraph([],[0],[prems])
        bc = bool_circ(g)
        current_node = 0
        s2 = ''
        for char in s :
            if(char == '('):
                bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2) # il faut concatener
                new = bc.add_node('',[],[current_node])
                current_node = new

                s2 = ''
            else:
                if( char == ')' ):
                    bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2)
                    id = bc.get_node_by_id(current_node).get_children_ids()
                    current_node = id[0]
                    s2 = ''
                else :
                    s2 = s2 + char
        #il ajouter aux inputs les nodes qui n'ont pas de parents
        for node1 in bc.get_nodes():
            if (node1.get_parent_ids() == []):
                bc.add_input_id(node1.get_id())
        #Il faut fusionner les nodes qui ont le meme label
        fusionner = True
        #print(bc.get_inputs_ids())
        while (fusionner) :
            fusionner = False
            for i in range(len(bc.get_inputs_ids())):
                #print("i = ", i)
                nodei = bc.get_node_by_id(bc.get_inputs_ids()[i])
                labeli = nodei.get_label()
                #print("labeli = ",labeli)
                #print("fusionner = ", fusionner)
                for j in range(i+1 , len(bc.get_inputs_ids())):
                    #print("j = ", j )
                    nodej = bc.get_node_by_id(bc.get_inputs_ids()[j])
                    labelj = nodej.get_label()
                    #print("labelj = ",labelj)
                    #print("fusionner = ", fusionner)
                    if(labeli == labelj and nodei != nodej) :
                        #print("fusioooooooon !")
                        fusionner = True
                        bc.fusion_nodes(nodei.get_id(), nodej.get_id())
                #print("pouet")
        return bc


    # version exo 4 (incomplete)
    def parse_parenthese_3(s):      # s une sequence de chaine de caractere
    # Utiliser les fonctions de composition paralleles (attention aux entrees a fusionner)
        prems = node(0,'',[],[])
        g = open_digraph([],[0],[prems])
        bc = bool_circ(g)
        current_node = 0
        s2 = ''
        for char in s :
            if(char == '('):
                bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2) # il faut concatener
                new = bc.add_node('',[],[current_node])
                current_node = new

                s2 = ''
            else:
                if( char == ')' ):
                    bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2)
                    id = bc.get_node_by_id(current_node).get_children_ids()
                    current_node = id[0]
                    s2 = ''
                else :
                    s2 = s2 + char
        #il ajouter aux inputs les nodes qui n'ont pas de parents
        for node1 in bc.get_nodes():
            if (node1.get_parent_ids() == []):
                bc.add_input_id(node1.get_id())
        #Il faut fusionner les nodes qui ont le meme label
        fusionner = True
        #print(bc.get_inputs_ids())
        while (fusionner) :
            fusionner = False
            for i in range(len(bc.get_inputs_ids())):
                #print("i = ", i)
                nodei = bc.get_node_by_id(bc.get_inputs_ids()[i])
                labeli = nodei.get_label()
                #print("labeli = ",labeli)
                #print("fusionner = ", fusionner)
                for j in range(i+1 , len(bc.get_inputs_ids())):
                    #print("j = ", j )
                    nodej = bc.get_node_by_id(bc.get_inputs_ids()[j])
                    labelj = nodej.get_label()
                    #print("labelj = ",labelj)
                    #print("fusionner = ", fusionner)
                    if(labeli == labelj and nodei != nodej) :
                        #print("fusioooooooon !")
                        fusionner = True
                        bc.fusion_nodes(nodei.get_id(), nodej.get_id())
                #print("pouet")
        return bc




    ########################################################################
    ################                A tester                ################
    def int_to_bool_circ(self, n, size_register=8):
        debut = 8 - size_register
        j = 2
        binaire = bin(n)
        for c in range(8):
            if(c<debut):
                new_id = self.add_node('0', [], [])
                #self.add_input_id(new_id)
                self.add_output_id(new_id)
            else:
                new_id = self.add_node(str(binaire[j]), [],[])
                #self.add_input_id(new_id)
                self.add_output_id(new_id)
                j = j+1
        self.is_well_formed()

    def apply_copy_rule(self, data_node_id, cp_node_id):
        '''data_node_id, cp_node_id : int; the ids of the nodes on which to apply the rule
        Applies the "data copy" rule of boolean circuits on the given nodes.
        output : int list; the list of nodes that were created
        '''
        print("in apply_copy_rule 1), self = ",self)

        data = self.get_node_by_id(data_node_id).get_label()
        assert data in ['0','1'], "wrong data label"
        assert self.get_node_by_id(data_node_id).get_children_ids()==[cp_node_id], \
            "the two nodes are not connected"

        self.get_node_by_id(cp_node_id).set_label(data)
        # cas ou le noeud de copie est aussi un output
        for ind in range(len(self.get_outputs_ids())):
            if self.outputs[ind] == cp_node_id:
                self.outputs.insert(ind, data_node_id)
        print("in apply_copy_rule, self 2) = ",self)

        #cas ou le noeud de copie est aussi un input
        for ind in range(len(self.get_inputs_ids())):
            if self.inputs[ind] == data_node_id:
                self.inputs.insert(ind+1, cp_node_id)
        # cas general
        children = self.get_node_by_id(cp_node_id).get_children_ids()
        for child in children:
            self.get_node_by_id(data_node_id).add_child_id(child)
        self.remove_edge(data_node_id, cp_node_id)
        print("in apply_copy_rule, self.nodes = ",self.nodes)
        print("in apply_copy_rule, self.inputs = ",self.inputs)
        print("in apply_copy_rule, self.outputs = ",self.outputs)
        assert(self.is_well_formed())


    '''Comment on va faire :
    on va changer le label du noeud de copie pour le noeud a copier.
    On va donner les enfants du noeuds de copie au  oeud a copier
    on va enlever l'arrete entre le noeud de copie et le noeud a copier
    '''


    def apply_no_rule(self, data_node_id, neg_node_id):
        '''méthode qui applique la regle de la negation sur un node
            @param : data_node_id : l'id du node à negativer
                     neg_node_id : l'id du node de negation
            @return : none
        '''
        data = self.get_node_by_id(data_node_id).get_label()
        assert data in ['0','1'], "wrong data label"
        if(data == '0'):
            data = '1'
        else :
            data = '0'
        assert self.get_node_by_id(data_node_id).get_children_ids()==[neg_node_id], \
            "the two nodes are not connected"
        #on change le label du node d'id data_node_id en son opposé.
        self.get_node_by_id(data_node_id).set_label(data)
        #si le noeud de negation est un output
        for ind in range(len(self.get_outputs_ids())):
            if(self.outputs[ind] == neg_node_id) :
                self.outputs[ind] = data_node_id
        #cas general, on ajoute au node d'id data_node_id les enfants du node de negation.
        children = self.get_node_by_id(neg_node_id).get_children_ids()
        for child in children :
            self.get_node_by_id(data_node_id).add_child_id(child)
        #on enleve le node de negation du graphe
        self.remove_node_by_id(neg_node_id)
        assert(self.is_well_formed())


    def apply_and_rule(self, data_node_id, and_node_id):
        '''méthode qui applique la regle de la porte ET sur un node
            @param : data_node_id : l'id du node sur lequel appliquer la regle
                     and_node_id : l'id du node representant la porte ET
            @return : none '''
        data = self.get_node_by_id(data_node_id).get_label()
        assert data in ['0','1'], "wrong data label"
        assert self.get_node_by_id(data_node_id).get_children_ids()==[and_node_id], \
            "the two nodes are not connected"
        if data == '1' :
            self.remove_node_by_id(data_node_id)
        else :
            #le cas ou le node AND etait un output
            for ind in range(len(self.get_outputs_ids())):
                if self.outputs[ind] == and_node_id :
                    self.outputs[ind] = data_node_id
            #cas general, on ajoute au node d'id data_node_id les enfants du node ET
            children = self.get_node_by_id(and_node_id).get_children_ids()
            for child in children :
                self.get_node_by_id(data_node_id).add_child_id(child)

            #on enleve le node ET du graphe
            self.remove_node_by_id(and_node_id)
            assert(self.is_well_formed())

    def apply_or_rule(self, data_node_id, or_node_id):
        '''méthode qui applique la regle de la porte OR sur un node
            @param : data_node_id : l'id du node sur lequel appliquer la regle
                     and_node_id : l'id du node representant la porte OR
            @return : none '''
        data = self.get_node_by_id(data_node_id).get_label()
        assert data in ['0','1'], "wrong data label"
        assert self.get_node_by_id(data_node_id).get_children_ids()==[or_node_id], \
            "the two nodes are not connected"
        if data == '0' :
            self.remove_node_by_id(data_node_id)
        else :
            #le cas ou le node OR est un output
            for ind in range(len(self.get_outputs_ids())):
                if self.outputs[ind] == or_node_id :
                    self.outputs[ind] = data_node_id
            #cas general, on ajoute au node d'id data_node_id les enfants du node ET
            children = self.get_node_by_id(or_node_id).get_children_ids()
            for child in children:
                self.get_node_by_id(data_node_id).add_child_id(child)
            #on enleve le node OR du graphe
            self.remove_node_by_id(or_node_id)
            assert(self.is_well_formed())

    def apply_xor_rule(self, data_node_id, xor_node_id):
        '''méthode qui applique la regle de la porte XOR sur un node
            @param : data_node_id : l'id du node sur lequel appliquer la regle
                     and_node_id : l'id du node representant la porte XOR
            @return : list id '''

        data = self.get_node_by_id(data_node_id).get_label()
        return_id = []
        assert data in ['0','1'], "wrong data label"
        assert self.get_node_by_id(data_node_id).get_children_ids()==[xor_node_id], \
            "the two nodes are not connected"
        if data == '0' :
            self.remove_node_by_id(data_node_id)
        else :
            #on crée un nouveau node, qui aura pour label ~
            new_id = self.new_id()
            new_node = node(new_id, '~', [],[])
            #on l'ajoute au graphe
            self.add_node(new_node)
            #on ajoute son id a return_id
            return_id.append(new_id)
            #dans le cas ou le XOR est un output du graphe
            for ind in range(len(self.get_outputs_ids())):
                #on remplace le xor par le ~ dans la liste des outputs
                if self.outputs[ind] == xor_node_id :
                    self.outputs[ind] = new_id
            #on regarde quels sont les enfants du xor
            children = self.get_node_by_id(xor_node_id).get_children_ids()
            #on les attribue au node ~
            for child in children :
                self.add_edge(new_id, child)
            #on met ~ comme unique enfant du xor
            self.get_node_by_id(xor_node_id).remove_child_id_all(children)
            self.add_edge(xor_node_id, new_id)
        print("in apply_xor_rule, self.inputs = ", self.get_inputs_ids())
        print("in apply_xor_rule, self.outputs = ", self.get_outputs_ids())
        print("in apply_xor_rule, self.nodes = ", self.get_node_ids())
        print("in apply_xor_rule, new_node.parents  = ", self.get_node_by_id(new_id).get_parent_ids())
        print("in apply_xor_rule, new_node.childrens  = ", self.get_node_by_id(new_id).get_children_ids())
        print("in apply_xor_rule, xor.parents  = ", self.get_node_by_id(xor_node_id).get_parent_ids())
        print("in apply_xor_rule, xor.children  = ", self.get_node_by_id(xor_node_id).get_children_ids())


        assert(self.is_well_formed())
        return list_id


    def apply_neutral_rule(self, data_node_id):
        '''méthode qui applique la regle neutre sur un node
            @param : data_node_id : l'id du node sur lequel appliquer la regle
            @return : none
        '''
        data = self.get_node_by_id(data_node_id).get_label()
        if (data == '|' or data == '^'):
            self.get_node_by_id(data_node_id).set_label('0')
        else:
            if data == '&' :
                self.get_node_by_id(data_node_id).set_label('1')
        assert(self.is_well_formed())

    def reduce_eval(self):
        ################ IL MANQUE COPY ##################
        '''methode qui applique les differentes regles possible (or, xor, and, note, copy, neutral)
        tant qu'il y a des transformation a appliquer'''
        list_graph = [self]
        nodes = list_graph[0].get_nodes()
        graph = self
        while(len(nodes)>1 ):
            label = nodes[0].get_label()
            listLabel = ['&', '^', '|' ]

            if label in listLabel :
                graph.apply_neutral_rule(nodes[0].get_id())

            if(label == '1' or label == '0'):

                label1 = nodes[1].get_label()

                data_node_id = nodes[0].get_id()
                gate_node_id = nodes[1].get_id()

                if(label1 == '&'):
                    graph.apply_and_rule(data_node_id, gate_node_id )
                if(label1 == '^'):
                    graph.apply_xor_rule(data_node_id, gate_node_id )
                if(label1 == '|'):
                    graph.apply_or_rule(data_node_id, gate_node_id )
                if(label1 == '~'):
                    graph.apply_no_rule(data_node_id, gate_node_id )

            nodes = graph.get_nodes()

            #On verifie si on a pas obtenu un node tout seul , isolé du reste du graph
            #si c'est le cas, on le sépare du reste du graph, sur lequel on va effectuer le reste des transformations.
            for ind in range(len(self.get_outputs_ids())):
                if graph.outputs[ind] == nodes[0].get_id():
                    #on met le node isolé dans un graph a lui tout seul
                    g = bool_circ([nodes[0].get_id()], [nodes[0].get_id()], [nodes[0]])
                    g.apply_neutral_rule(node[0].get_id())
                    #on crée un deuxieme graphe, semblable au premier
                    f = graph.copy()
                    #on lui enleve le node qui est déconecté du reste
                    f.remove_node_by_id(node[0].get_id())
                    #on ajoute g et f a la liste des pgraphes, qu'on va par la suite recomposé
                    list_graph[0] = g
                    list.insert(0,f)
                    nodes=f.get_nodes()
                    #on travaillera desormais sur f
                    graph = f

        #On reconnecte ici toutes les composantes du graphe qui étaient séparées
        if len(list_graph)>1 :
            while(len(list_graph)>1):
                list_graph[0].iparallel(list_graph[1])
                graph_supprime = list_graph.pop(1)
        #on attribue a self la valeur finale voulue
        self = list_graph[0]
        assert(self.is_well_formed())











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
    # Attention bug sneaky non resolu quand appel sur petit graph



#bug parse_parenthese
#rajouter s2 au label de current node ?? dans parse parenthese, seudo code
#exo 2 : fusionner, quand est il des inputs, outputs?
