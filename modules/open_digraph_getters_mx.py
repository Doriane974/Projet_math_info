class open_digraph_getters_mx:

    def get_inputs_ids(self):               # extrait la liste des ids des inputs du graphe (int list)
        '''méthode appliquée au graphe qui extrait la liste des ids des inputs du graphe
        argument : none
        return : int list '''
        return self.inputs


    def get_outputs_ids(self):              # extrait la liste des ids des outputs du graphe (int list)
        '''méthode appliquée au graphe qui extrait la liste des ids des outputs du graphe
        argument : none
        return : int list '''
        return self.outputs


    def get_id_node_map(self): #renvoie un dictionnaire id:nodes
        '''méthode appliquée au graphe qui extrait le dictinnaire des nodes du graphe
        argument : none
        return : dictionnaire : keys : ids, values : nodes  '''
        return self.nodes


    def get_nodes(self):    # renvoie une liste de tous les noeuds
        '''méthode appliquée au graphe qui renvoie une liste de tous les nodes du graphes
        argument : none
        return : node list '''
        return list(self.nodes.values())


    def get_node_ids(self):                 # renvoie une liste des ids des nodes (int list)
        '''méthode appliquée au graphe qui renvoie une liste de tous les ids des nodes du graphes
        argument : none
        return : int list '''
        return [i for i in self.nodes.keys()]


    def get_node_by_id(self, id):            # renvoie le node dont l'id correspond a id
        '''Méthode appliquée au graphe qui renvoie le node dont l'id correspond a id
        argument : id : id dont ont veut obtenir le node correspondant
        return : node '''
        return self.nodes.get(id) #get() se fait sur un dictionnaire, ici self.nodes est bien un dictionnaire


    def get_node_by_ids(self, node_ids):              # renvoie une liste de noeuds a partir d’une liste d’ids
        '''méthode appliquée au graphe qui renvoie une liste de noeuds a partir d'une liste d'id
        argument : node_ids : id list
        return : node list '''
        return [self.nodes.get(i) for i in node_ids]
