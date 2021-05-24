from modules.open_digraph import *
from modules.open_digraph_composition_mx import *
class bool_circ_mx(open_digraph):
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
        bc = bool_circ_mx(g);
        current_node = 0
        s2 = ''
        for char in s :
            if(char == '('):
                bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2) # il faut concatener
                new = bc.add_node(label = '', parents =[], children =[current_node])
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
        bc = bool_circ_mx(g)
        current_node = 0
        s2 = ''
        for char in s :
            if(char == '('):
                bc.get_node_by_id(current_node).set_label(bc.get_node_by_id(current_node).get_label() + s2) # il faut concatener
                new = bc.add_node(label = '', parents =[], children =[current_node])
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
        graph_list = []
        bc = open_digraph([],[],[])
        for chaine in s:
            graph_list.append(bool_circ_mx.parse_parenthese_2(chaine))
        #print("pp3", graph_list)
        bc = bc.parallel2(graph_list, None, None)
        return bc


    ########################################################################
    ################                A tester                ################
    def int_to_bool_circ(self, n, size_register=8):
        debut = 8 - size_register
        j = 2
        binaire = bin(n)
        for c in range(8):
            if(c<debut):
                new_id = self.add_node(label = '0', parents =[], children =[])
                #self.add_input_id(new_id)
                self.add_output_id(new_id)
            else:
                new_id = self.add_node(label = str(binaire[j]), parents = [], children = [])
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
                    g = bool_circ_mx([nodes[0].get_id()], [nodes[0].get_id()], [nodes[0]])
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
