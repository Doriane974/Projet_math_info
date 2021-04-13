print('hello world');

from modules.open_digraph import *
from modules.utils import *
from modules.Interface import *
import inspect





# print(g)
# print(open_digraph.empty()) #Question 5
# matrix = random_int_matrix(5, 2, False)
# print(matrix)
# print(graph_from_adjacency_matrix(matrix))
#print(g.random_graph(5, 2, 'oriented'))





width = 400
height = 400
image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)
#draw.line([(0,0),(150,150), (300,0)], 'black')
#draw.rectangle([(130,150), (170,190)], outline='black')
#draw.text((150,170), "& | ~", fill='black')
#draw.ellipse((100, 100, 150, 200), fill='white', outline='black')
#draw.line([(200,200), (200,400),(301,1)], 'black')
n0 = node(0, 'A', [], [1]) #l'entrée du graphe
n1 = node(1,'B',[0],[2, 2,4])
n2 = node(2,'C',[1],[3,4])
n3 = node(3,'D',[2],[]) #la sortie du graphe
n4 = node(4,'E',[1,2],[])
n5 = node(5,'F',[1,2], [] )

g = open_digraph([0],[3],[n0,n1,n2,n3,n4]);

pentree = point(10,10)
psortie = point(330, 170 )
p0 = point(30,30)
p1 = point (50, 300)
p2 = point(100,150)
p3 = point(300,200)
p4 = point(50,200)

node_pos = { 0 : p0 , 1 : p1 , 2 : p2 , 3 : p3 , 4 : p4 }
input_pos= [pentree]

output_pos= [psortie]

nodes_pos, input_pos, output_pos = DAG_layout(g)
print("test de DAG_layout , node_pos = ", node_pos)
print("test de DAG_layout , input_pos = ", input_pos)
print("test de DAG_layout , output_pos = ", output_pos)
draw.graph(g, node_pos, input_pos,output_pos, 'DAG')
#def drawgraph(self, g, method='manual', node_pos=None, input_pos=None, output_pos=None):
#draw.arrows(p1, p2)
#draw.arrete(p2,p3)
#draw.node(n0, p3, True)
#draw.node(n1, p2, True)
draw.text((5,380), "label", fill='red')
draw.text((5,390), "Id", fill='blue')
#draw.node(n1,p1,True)
pr = point(100,100)
#draw.arrows(p1,pr)

p1 = p1.rotate(90, pr)
#draw.node(n1, p1, True)
#draw.arrows(p1,pr)
draw.node(n0, p0, True)
draw.node(n4, p4, True)
angle = slope_angle(p0, p4)
print(angle)
print(slope_angle(p4,p0))

print("g is cyclic = ", g.is_cyclic())


b1 = node(1, '1', [], [3]) #l'entrée du graphe
b2 = node(2,'2',[],[4])
b3 = node(3,'~',[1],[4])
b4 = node(4,'&',[3,2],[5]) #la sortie du graphe
b5 = node(5,'~',[4],[])
b= open_digraph([1,2],[5],[b1,b2,b3,b4,b5])


'''c = bool_circ(b);
print("indice min :", c.min_id())
print("indice max :" , c.max_id())
c.shift_indices(15)
print("indice min :", c.min_id())
print("indice max :" , c.max_id())'''

'''b0 = node(0, 'a', [], [1])
b1 = node(1, 'b', [0], [2])
b2 = node(2, 'c', [1], [])
b = open_digraph([0],[2],[b0, b1, b2])
c0 = node(0, 'a', [], [1, 2])
c1 = node(1, 'b', [0], [])
c2 = node(2, 'c', [0], [])
c0 = open_digraph([0],[1,2],[c0, c1, c2])

c0.fusion_nodes(0,1)'''

'''dist, prev = b.dijkstra(3, -1)
print("dist de dijsktra :",dist)
print("previous de djilstra", prev)
print("shortest path de 2 à 5 =", b.shortest_path(2,5))
print("dist_common_ancestors, dist dist_common_ancestors de 3 et 4 :", b.dist_common_ancestors(3,4))'''

bc = bool_circ.parse_parenthese("((x0)&((x1)&(x2)))|((x1)&(~(x2)))")
print("compte generation, b.compte_generation = ",b.compte_generation(5,0,0))
#print("compte generation, c.compte_generation = ",c.compte_generation(1,0))


image.save("test.jpg")
