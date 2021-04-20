class open_digraph_add_mx:
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
