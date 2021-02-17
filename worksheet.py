print('hello world');

from modules.open_digraph import *
import inspect


n0 = node(0, 'papa', [], [1]);
n1 = node(1, 'maman', [], [1]);
n2 = node(1, 'enfant',['papa', 'maman'],[])

g = open_digraph([0],[1],[n0,n1]);

# print(g)
# print(open_digraph.empty()) #Question 5
# matrix = random_int_matrix(5, 2, False)
# print(matrix)
# print(graph_from_adjacency_matrix(matrix))
print(g.random_graph(5, 2, 'oriented'))
