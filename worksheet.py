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
n1 = node(1,'B',[0],[2,4])
n2 = node(2,'C',[1],[3,4])
n3 = node(3,'D',[2],[]) #la sortie du graphe
n4 = node(4,'E',[1,2],[])

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

draw.graph(g, node_pos, input_pos,output_pos)
#def drawgraph(self, g, method='manual', node_pos=None, input_pos=None, output_pos=None):
#draw.arrows(p1, p2)
draw.arrete(p2,p3)
draw.node(n0, p3, True)
#draw.node(n1, p2, True)
draw.text((5,380), "label", fill='red')
draw.text((5,390), "Id", fill='blue')
image.save("test.jpg")
