print('hello world');

from modules.open_digraph import *
from modules.utils import *
from modules.Interface import *
import inspect



g = open_digraph([0],[1],[n0,n1]);

# print(g)
# print(open_digraph.empty()) #Question 5
# matrix = random_int_matrix(5, 2, False)
# print(matrix)
# print(graph_from_adjacency_matrix(matrix))
print(g.random_graph(5, 2, 'oriented'))





width = 400
height = 400
image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)
#draw.line([(0,0),(150,150), (300,0)], 'black')
#draw.rectangle([(130,150), (170,190)], outline='black')
#draw.text((150,170), "& | ~", fill='black')
#draw.ellipse((100, 100, 150, 200), fill='white', outline='black')
#draw.line([(200,200), (200,400),(301,1)], 'black')
p1 = point(1,30)
p2 = point (30, 4)
draw.arrows(p1, p2)
n0 = node(0, 'i', [], [1])
n1 = node(0,'i',[],[1])
p3 = point(60,30)
draw.node(n0, p3, True)
image.save("test.jpg")
