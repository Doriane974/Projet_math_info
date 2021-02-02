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
        return "(" + str(self.id) +"," + self.label +","+ str(self.parents) + "," + str(self.children) + ")"
        '''
        output : str ; the string given by str(node)
        '''
    def __repr__(self):
        return "node"+str(self)

    def copy(self):
        return node(self.id, self.label, self.parents.copy(),self.children.copy())

    def get_id(self):
        return self.id

    def get_label(self):
        return self.label

    def get_parent_ids(self):
        return self.parents

    def get_children_ids(self):
        return self.children


    def set_id (self, id) :
        self.id = id

    def set_label (self, label) :
        self.label = label

    def set_parent_ids (self, parent_ids) :
        self.parent = parent_ids

    def set_children_ids (self, children_ids) :
        self.children = children_ids

    def add_child_id (self, child_id) :
        self.children.append(child_id)

    def add_parent_id (self, parent_id) :
        self.parent.append(parent_id)

class open_digraph: #for open directed graph
    def __init__(self, inputs, outputs, nodes):
        #inputs: int list; the ids of the input nodes
        #outputs: int list; the ids of the output nodes
        #nodes: node list;
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict
    def __str__(self):
        return "(" + str(self.inputs) +"," + str(self.outputs) +","+ str(print(self.nodes)) + ")" #il faut utiliser __repr__

    def __repr__(self):
        return "open_digraph" + str(self)

    def copy(self):
        return open_digraph(self.inputs.copy(), self.outputs.copy(), [node.copy() for node in self.nodes.values()])


    def empty():
        return open_digraph([],[],[])

    def get_inputs_ids(self):
        return self.inputs

    def get_outputs_ids(self):
        return self.outputs

#<<<<<<< HEAD
    def set_input_ids (self, input_ids) :
        self.inputs = input_ids

    def set_output_ids (self, output_ids) :
        self.outputs= output_ids

    def add_input_id (self, input_id) :
        self.inputs.append(input_id)

    def add_output_id (self, output_id) :
        self.outputs.append(output_id)
#=======
    def get_id_node_map(self): #renvoie un dictionnaire id:nodes
        return self.nodes

    def get_nodes(self):
        L = []
        for i in self.nodes.values():
            L.append(i)
        return L
#>>>>>>> bdd0aad2e7d2716837860a3520e7eb5f3db35012
