from modules.utils import *
class open_digraph_composition_mx:

    def iparallel(self,g):
        '''methode qui compose parallelement deux open_digraph, en en modifiant un mais pas l'autre
        arguments : g, le graphe a composer dans self
        return : None
        '''
        list_edges = []
        for input_id in g.get_inputs_ids():
            self.add_input_id(input_id)
        for output_id in g.get_outputs_ids():
            self.add_output_id(output_id)
        for node_id in g.get_node_ids():
            node = g.get_node_by_id(node_id)
            list_edges.append([node_id, node.get_children_ids()])               # il ne devrait pas y avoir d arete entre self et g
            # print("node1 =", node_id, node)
            # print("nodesi1 =", self.get_node_ids())
            self.add_node(node_id, str(node.get_label()), [], [])            # il faut d abord ajouter le nosdes sans liens pour pouvoir les lier plus tard
        #     print("nodesi2 =", self.get_node_ids())
        # print("list_edges =", list_edges)
        for edge in list_edges:
            self.add_edges(edge[0], edge[1])

    def parallel(self,g):
        '''methode qui compose parallelement deux open_digraph, sans les modifier
        arguments : g, le graphe a composer avec self
        return : graph, un nouveau graph qui est la composition parallele de g et de self
        '''
        graph = self.copy()
        graph.iparallel(g)
        return graph


    def icompose(self, g):
        '''methode qui compose séquentiellement deux open_digraph, en en modifiant un (self) mais pas l'autre
        arguments : g, le graphe a composer dans self
        return : none
        '''
        if(len(self.get_inputs_ids()) != len(g.get_outputs_ids())):
            raise Exception("les entrées de self ne coincident pas avec les sorties de g")
        Lg_outputs = []
        lg_inputs = []
        for id in g.get_node_ids():
            new_id = self.add_node(label = g.get_node_by_id(id).get_label(), parents = g.get_node_by_id(id).get_parent_ids(), children = g.get_node_by_id(id).get_children_ids())
            if id in g.get_outputs_ids() :
                Lg_outputs.append(new_id)
            if id in g.get_inputs_ids():
                lg_inputs.append(new_id)
        for output_de_g, input_de_self in zip(Lg_outputs, self.get_inputs_ids()):
            self.add_edges(output_de_g, self.get_node_by_id(input_de_self).get_children_ids())
        for id in self.get_inputs_ids():
            print()
            self.remove_node_by_id(id)
        self.set_input_ids(lg_inputs)



    def compose(self, g):
        '''methode qui compose séquentiellement 2 open_digraphs, sans les modifier
        arguments : g, le graphe a composer avec self
        return : graph, un nouveau graph qui est la composition parallele de g et de self
        '''
        graph = self.copy()
        graph.icompose(g)
        return graph


    def iparallel2(self, graphs, perm_inputs = None, perm_outputs = None):
        '''methode qui compose parallelement des open_digraph, en en modifiant un mais pas les autres
        arguments : graphs, list de graphes a composer dans self
                    perm_inputs, permutation des inputs
                    perm_outputs, permutation des outputs
        return : None
        '''
        list_edges = []
        inputs_ids = [self.get_inputs_ids()]
        outputs_ids = [self.get_outputs_ids()]
        if perm_inputs is None:
            perm_inputs = [i for i in range(len(inputs_ids))]
        if perm_outputs is None:
            perm_outputs = [i for i in range(len(outputs_ids))]
        for g in graphs:
            inputs_ids.append(g.get_inputs_ids())
            outputs_ids.append(g.get_outputs_ids())
            for node_id in g.get_node_ids():
                node = g.get_node_by_id(node_id)
                list_edges.append([node_id, node.get_children_ids()])               # il ne devrait pas y avoir d arete entre self et g
                self.add_node(node_id, str(node.get_label()), [], [])            # il faut d abord ajouter le nosdes sans liens pour pouvoir les lier plus tard
        inputs_ids = appl_perm(inputs_ids, perm_inputs)
        self.set_input_ids(inputs_ids)
        outputs_ids = appl_perm(outputs_ids, perm_outputs)
        self.set_output_ids(outputs_ids)
        for edge in list_edges:
            self.add_edges(edge[0], edge[1])

    def parallel2(self, graphs, perm_inputs, perm_outputs):
        '''methode qui compose parallelement des open_digraph, sans les modifer
        arguments : graphs, list de graphes a composer avec self
                    perm_inputs, permutation des inputs
                    perm_outputs, permutation des outputs
        return : graph, un nouveau graph qui est la composition parallele de g et de self
        '''
        graph = self.copy()
        graph.iparallel2(graphs, perm_inputs, perm_outputs)
        return graph
