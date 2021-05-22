class open_digraph_calc_degrees_mx:
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
