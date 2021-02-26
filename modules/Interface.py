import math
import operator
import sys

sys.path.append('../')
from modules.utils import *
from modules.open_digraph import *
import inspect
from PIL import Image, ImageDraw

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def n(self):
        return (round(self.x), round(self.y)) # return a simple tuple
    def copy(self):
        return point(self.x, self.y)
    def __add__(self, p2):
        return point(self.x + p2.x, self.y + p2.y)


    def __rmul__(self, s):
        return point(self.x*s, self.y*s)

    def __sub__(self, p2):
        return point(self.x - p2.x, self.y - p2.y)

#méthode qui dessine une ligne
#arguments : p1 : point de départ de la ligne
#            p2 : point d'arrivée de la ligne
def drawarrows(self, p1, p2):
    #'''doc : todo'''
    self.line([p1.n(), p2.n()], 'black')

def drawnode(self, noeud, p, verbose = False):
    self.ellipse((p.x-10, p.y-10, p.x+10, p.y+10), fill='white', outline='black')
    self.text((p.x - 2  ,p.y - 9), str(noeud.get_label()) , fill='red')
    if(verbose):
        self.text((p.x-2 ,p.y ), str(noeud.get_id()) , fill='blue')

def drawgraph(self, g, method='manual', node_pos=None, input_pos=None, output_pos=None):
    




ImageDraw.ImageDraw.arrows = drawarrows # we define the method 'arrows'
                                        # from the function 'arrows' above

ImageDraw.ImageDraw.node = drawnode

#ImageDraw.ImageDraw.graph = drawgraph
