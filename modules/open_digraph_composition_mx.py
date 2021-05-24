class open_digraph_composition_mx:

    def iparallel(self,g):
        '''methode qui compose parallelement deux open_digraph, en en modifiant un mais pas l'autre
        arguments : g, le graphe a composer dans self
        return : none
        '''
        for input_id in g.get_inputs_ids():
            self.add_input_id(input_id)
        for output_id in g.get_outputs_ids():
            self.add_output_id(output_id)
        for node_id in g.get_node_ids():
            slef.add_node(str(g.get_node_by_id(node_id).get_label()), g.get_parent_ids(), g.get_children_ids())


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
            new_id = self.add_node(g.get_node_by_id(id).get_label(), g.get_node_by_id(id).get_parent_ids(), g.get_node_by_id(id).get_children_ids())
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
