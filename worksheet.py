print('hello world');

from modules.open_digraph import *
from modules.utils import *
from modules.Interface import *
import inspect



width = 400
height = 400
image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)
draw.line([(0,0),(150,150), (300,0)], 'black')
draw.rectangle([(130,150), (170,190)], outline='black')
draw.text((150,170), "& | ~", fill='black')
draw.ellipse((100, 100, 150, 200), fill='white', outline='black')
p1 = point(1,30)
p2 = point (30, 4)
draw.arrows(p1, p2)
n0 = node(0, 'i', [], [1])
n1 = node(0,'i',[],[1])
p3 = point(60,30)
draw.node(n0, p3, True)
image.save("test.jpg")
