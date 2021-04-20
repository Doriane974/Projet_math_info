class open_digraph_getters_mx:
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

    '''Méthode appliquée au graphe qui renvoie le node dont l'id correspond a id
    argument : id : id dont ont veut obtenir le node correspondant
    return : node '''
    def get_node_by_id(self, id):            # renvoie le node dont l'id correspond a id
        return self.nodes.get(id) #get() se fait sur un dictionnaire, ici self.nodes est bien un dictionnaire

    '''méthode appliquée au graphe qui renvoie une liste de noeuds a partir d'une liste d'id
    argument : node_ids : id list
    return : node list '''
    def get_node_by_ids(self, node_ids):              # renvoie une liste de noeuds a partir d’une liste d’ids
        return [self.nodes.get(i) for i in node_ids]













    
