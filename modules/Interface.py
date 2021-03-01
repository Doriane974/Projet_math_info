import math
import operator
import sys
import random

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




def drawarrete(self, p1, p2):

    if(p2.x >= p1.x and p2.y > p1.y) :
        p_depart=point(p1.x, p1.y)
        p_arrivee=point(p2.x, p2.y)
        self.arrows(p_depart, p_arrivee)
    if(p2.x < p1.x and p2.y >= p1.y) :
        p_depart=point(p1.x, p1.y)
        p_arrivee=point(p2.x, p2.y)
        self.arrows(p_depart, p_arrivee)
    if(p2.x <= p1.x and p2.y < p1.y) :
        p_depart=point(p1.x, p1.y)
        p_arrivee=point(p2.x, p2.y)
        self.arrows(p_depart, p_arrivee)
    if(p2.x > p1.x and p2.y <= p1.y) :
        p_depart=point(p1.x, p1.y)
        p_arrivee=point(p2.x, p2.y)
        self.arrows(p_depart, p_arrivee)


def random_layout(g, node_pos, input_pos, output_pos):
    for id in g.nodes.keys():# la c
        node_pos[id]=point(random.randrange(25,375), random.randrange(25,375))
    j=0
    for id in g.inputs:
        input_pos[id]=point(node_pos[id].x - 25, node_pos[id].y - 25)
        j=j+1
    i = 0;
    for id in g.outputs:
        x = node_pos[id].x
        y = node_pos[id].y

        output_pos[i]=point(node_pos[id].x + 25, node_pos[id].y + 25)
        i=i+1
    return node_pos, input_pos, output_pos


def drawgraph(self, g, method='manual', node_pos=None, input_pos=None, output_pos=None, verbose=False):
    if (method=='random'):
        node_pos, input_pos, output_pos = random_layout(g, node_pos, input_pos, output_pos)

    for i in range(len(g.get_inputs_ids())): #on trace l'entrée
        self.arrows(input_pos[i], node_pos[g.get_inputs_ids()[i]])
    for i in range(len(g.get_outputs_ids())): #on trace la sortie
            self.arrows(node_pos[g.get_outputs_ids()[i]],output_pos[i])
    for id in g.nodes.keys(): # on trace les arrete entre les nodes et leurs enfant
        for child in g.nodes[id].get_children_ids():
            self.arrete(node_pos[id], node_pos[child])
    for id in g.nodes.keys(): # on trace les nodes
        self.node(g.get_node_by_id(id),node_pos[id], verbose)




    #parcourir les nodes de g, tracer une arrete entre chaque node et ses enfants.
    #faire : tracer une fl`eche de input_pos[i] vers le noeud d’id g.get_input_ids[i]. output_pos quand tu auras compris






ImageDraw.ImageDraw.arrows = drawarrows # we define the method 'arrows'
                                        # from the function 'arrows' above
ImageDraw.ImageDraw.node = drawnode

ImageDraw.ImageDraw.arrete = drawarrete

ImageDraw.ImageDraw.graph = drawgraph
