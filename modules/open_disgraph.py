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

class open_digraph: #for open directed graph
    def __init__(self, inputs, outputs, nodes):
        #inputs: int list; the ids of the input nodes
        #outputs: int list; the ids of the output nodes
        #nodes: node list;
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict
    def __str__(self):
        return "(" + str(self.inputs) +"," + str(self.outputs) +","+ str(print(self.nodes)) + ")"

    def empty():
        '''

        '''
        return open_digraph([],[],[])
'''def __str__(self):
    print( "id =" , self.inputs , "," , "liste des output : " , self.outputs , "nodes : " , self.nodes)
'''
