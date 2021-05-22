class node_getters_mx:
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
