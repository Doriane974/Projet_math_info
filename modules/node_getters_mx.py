class node_getters_mx:

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
