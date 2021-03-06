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
    '''initialise un point avec ses coordonnées
    arguments : x : abscisse du point
                y : ordonnée du point
    return : un point de coordonéee x et y'''
    def __init__(self,x,y):                                                     #initialise un point avec ses coordonnées
        self.x = x
        self.y = y



    def n(self):
        '''méthode qui retourne le couple correspondant aux coordonée du point. Méthode appliquée au point dont on veut les coordonées.
        arguments : none
        return : un couple (x,y) des coordonnes du point '''
        return (round(self.x), round(self.y)) # return a simple tuple

    def __str__(self):
        return "(" + str(self.x) +"," + str(self.y)+ ")"
        '''output : str ; the string given by str(node)'''

    def __repr__(self):
        return "point"+str(self)


    def copy(self):                                                             #copie un point
        '''méthode qui retourne une copie du point, méthode appliquée au point que l'on veut copier.
        argument : none
        return : un point de meme coordonnées que celui sur lesquel est appliqué la méthode '''
        return point(self.x, self.y)


    def __add__(self, p2):                                                      #addditionne 2 points, retourne un nouveau
        '''additionne les coordonnées de points de coordonnées (x,y) et (x', y')
        méthode appliquée a un point de coordonée (x,y)
        argument : p2 : points de coordonnées (x', y')
        return : point de coorrdonnée (x+x', y+y')'''
        return point(self.x + p2.x, self.y + p2.y)

    def __rmul__(self, s):                                                      #multiplie 2 point, retourne un nouveau

        '''Multiplie les coordonnées d'un point de coordonnées (x,y) par un scalaire
        méthode appliquée au point de coordonnée (x,y)
        argument : s : int par lequel ont veut multiplier le point
        return : point de coorrdonnée (x*s, y*s) '''
        return point(self.x*s, self.y*s)



    '''soustraie les coordonnées de points de coordonnées (x,y) et (x', y')
    méthode appliquée a un point de coordonée (x,y)
    argument : p2 : points de coordonnées (x', y')
    return : point de coorrdonnée (x-x', y-y')'''
    def __sub__(self, p2):                                                      #soustraie 2 points, retourne un nouveau
        return point(self.x - p2.x, self.y - p2.y)


def rotate(self, theta, c=point(0,0)):
    '''méthode appliquée a un point  qui calcule la position du point apres rotation d'angle
    théta autour du point c.
    arguments : theta : float : angle
                c : point
    return : point
    '''
    p = point(0,0)
    theta =theta * math.pi / 180
    p.x = self.x - c.x
    p.y = self.y - c.y
    r = point(0,0)
    r.x = p.x * math.cos(theta) + p.y * math.sin(theta) + c.x
    r.y = -p.x * math.sin(theta) + p.y * math.cos(theta) + c.y
    return r


def slope_angle(p1, p2):
    '''fonction qui calcule l'angle en radian formé entre la ligne qui passe par les point p1 et p2 et l'axe des abscisse
    argument : p1 : point
               p2 : point
    return : float (angle en radian)'''
    xneg = False
    yneg = False
    if(p2.x < p1.x):
        xneg = True
    if(p2.y < p1.y):
        yneg = False
    Ni=1
    Xvi = 1
    Yvi = 0
    Xvp1p2 = p2.x - p1.x
    Yvp1p2 = p2.y - p1.y
    Np1p2 = math.sqrt((p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y))
    scal = Xvi * Xvp1p2 + Yvi * Yvp1p2
    result = 0
    if (xneg == True):
        result = -(Xvp1p2/Np1p2)
    else :
        result = Xvp1p2/Np1p2
    if (yneg == True):
        result = -(math.acos(result))
    else :
        result = math.acos(result)
    return result

'''méthode qui dessine une courbe de bézier
arguments : p0 : point de départ de la courbe
            paux :
            p1 : point d'arrivée de la courbe
            dt : optionnal, le pas de la courbe, par défaut dt = 0.1
return : none
def Bezier(self, p0, paux, p1, dt = 0.1):'''



'''méthode qui dessine une ligne
    arguments : p1 : point de départ de la ligne
            p2 : point d'arrivée de la ligne'''




def drawarrows(self, p1, p2, arretep1p2 = 1, arretep2p1 = 1):
    '''méthode qui dessine une arrete entre 2 point, en prenant en compte le fait
    que le graphe soit orienté et que il puisse y avoir plusieurs arrete entre 2 point
    argument : p1 : point
               p2 : point
               arretep1p2: le nomdre d'arrete entre p1 et p2 (par défaut 1)
               arretep2p1: le nombre d'arrete entre p2 et p1 (par défaut 1)
    return : none '''
    self.line([p1.n(), p2.n()], 'black')
    VectP1P2 = point(p2.x - p1.x, p2.y - p1.y)                                                  # le vecteur entre p1 et p2
    VectP2P1 = (-1)* VectP1P2                                                                   # le vecteur entre p2 et p1
    NormeVP1P2 = math.sqrt(VectP1P2.x**2 + VectP1P2.y**2)                                       #la norme du vecteur entre p1 et p2 (la meme dans les 2 sens)
    NormalizeNvP1P2 = point(10*VectP1P2.x / NormeVP1P2, 10*VectP1P2.y/ NormeVP1P2 )             #le vecteur entre p1 et p2, mais normalisé
    NormalizeNvP2P1 = (-1)*NormalizeNvP1P2                                                      #le vecteur entre p2 et p1, mais normalisé
    pMilieu = point((p1.x +p2.x)/2, (p1.y + p2.y)/2)                                            #Le point milieu
    #pBasP1P2 = point((pFlecheP1P2.x + 8*math.cos(slope_angle(p1,p2)-math.pi/6)),(pFlecheP1P2.y + 8*math.sin(slope_angle(p1,p2)-math.pi/6)))
    #pBasP2P1 = point((pFlecheP2P1.x + 8*math.cos(slope_angle(p2,p1)-math.pi/6)), (pFlecheP2P1.y + 8*math.sin(slope_angle(p2,p1)-math.pi/6)))

    if (arretep1p2>0):                                                                          #On rentre dans le if si il y au moins une arrete a tracer entre p1 et p2
        VorthoP1P2 = point(-VectP1P2.x, VectP1P2.y)                                                 #Le vecteur orthogonal

        NormalizeVorthoP1P2 = point(VorthoP1P2.x * 10 / NormeVP1P2, VorthoP1P2.y * 10 / NormeVP1P2)

        pFlecheP1P2 = point((p1.x + pMilieu.x)/2, (p1.y + pMilieu.y)/2)                             #la position ou placer les fleches pour les arretes de p1 à p2
        #PorthoFlecheHaut= point(pFlecheP1P2.x + 10 * NormalizeVorthoP1P2.x , pFlecheP1P2.y + 10 * NormalizeVorthoP1P2.y)
        #PorthoFlecheBas= point(pFlecheP1P2.x - 10 * NormalizeVorthoP1P2.x , pFlecheP1P2.y - 10 * NormalizeVorthoP1P2.y)
        #pHautP1P2=point((pFlecheP1P2.x + PorthoFlecheHaut.x)/2, (pFlecheP1P2.y + PorthoFlecheHaut.y)/2)
        #pBasP1P2=point((pFlecheP1P2.x + PorthoFlecheBas.x)/2, (pFlecheP1P2.y + PorthoFlecheBas.y)/2)

        #pCenterNoRotateUp = point(pFlecheP1P2.x - 10, pFlecheP1P2.y - 8)
        #pCenterNoRotateDown = point(pFlecheP1P2.x - 10, pFlecheP1P2.y + 8)
        #pHautP1P2 = pCenterNoRotateUp.rotate(slope_angle(p1,p2), pFlecheP1P2)
        pHautP1P2 = point((pFlecheP1P2.x + 10*math.cos(slope_angle(p1,p2)+math.pi/4)) , (pFlecheP1P2.y + 10*math.sin(slope_angle(p1,p2)+math.pi/4))) #une des éxtrémité des lignes de la fleche
        #pBasP1P2 = pCenterNoRotateDown.rotate(slope_angle(p1,p2), pFlecheP1P2)
        pBasP1P2 = point((pFlecheP1P2.x + 10*math.cos(slope_angle(p1,p2)-math.pi/4)) , (pFlecheP1P2.y + 10*math.sin(slope_angle(p1,p2)-math.pi/4)))                                         #l'opposé

        self.line([pFlecheP1P2.n(), pHautP1P2.n()], 'purple')                                   #une des lignes de la fleche
        self.line([pFlecheP1P2.n(), pBasP1P2.n()], 'orange')                                    #l'autre ligne
        ptext = point(pFlecheP1P2.x + 10*math.cos(slope_angle(p1,p2)-math.pi/2) , pFlecheP1P2.y + 10*math.sin(slope_angle(p1,p2)-math.pi/2))    #la position du texte pour dire il y a combien d'arrete entre 2 points
        self.text(ptext.n(), str(arretep1p2), 'purple')                                         #le texte

    if (arretep2p1 > 0):
        VorthoP2P1 = point(VectP1P2.x, -VectP1P2.y)                                                 #Le vecteur orthogonal opposé
        NormalizeVorthoP2P1 = point(VorthoP2P1.x * 10 / NormeVP1P2, VorthoP2P1.y * 10 / NormeVP1P2)
        pFlecheP2P1 = point((p2.x + pMilieu.x)/2, (p2.y + pMilieu.y)/2)                             #La position ou placer les fleches pour les arretes de p1 à p2
        pHautP2P1 = point((pFlecheP2P1.x + 10*math.cos(slope_angle(p2,p1)+math.pi/4)) ,( pFlecheP2P1.y + 8*math.sin(slope_angle(p2,p1)+math.pi/4))) #une des éxtrémité des lignes de la fleche#l'opposé
        pBasP2P1 = pHautP2P1.rotate(-100, pFlecheP2P1)                                       #l'opposé

        self.line([pFlecheP2P1.n(), pHautP2P1.n()], 'green')
        self.line([pFlecheP2P1.n(), pBasP2P1.n()], 'green')
        ptext = point(pMilieu.x + NormalizeVorthoP2P1.x , pMilieu.y + NormalizeVorthoP2P1.y )
        self.text(ptext.n(), str(arretep2p1), 'green')


    '''self.line([p1.n(), p2.n()], 'black')
    ph = point(0,0)
    pb = point(0,0)
    pm = point(0,0)
    pm.x = ((p1.x + p2.x)/2)
    pm.y = ((p1.y + p2.y)/2)
    ############################################################
    #                       De p1 à p2                         #
    if (n > 0):
        ph.x = (pm.x + 8*math.cos(slope_angle(p1,p2)+math.pi/6))
        ph.y = (pm.y + 8*math.sin(slope_angle(p1,p2)+math.pi/6))
        #self.text(ph.x-10,ph.y-10), str(n), fill='black')
        pb.x = (pm.x + 8*math.cos(slope_angle(p1,p2)-math.pi/6))
        pb.y = (pm.y + 8*math.sin(slope_angle(p1,p2)-math.pi/6))
        ps = point(0,0)
        ps.x = (pm.x + 10*math.cos(slope_angle(p1,p2)-math.pi/2))
        ps.y = (pm.y + 10*math.sin(slope_angle(p1,p2)-math.pi/2))
        self.text((ps.x,ps.y), str(n), fill='green')
        self.line([pm.n(), pb.n()], 'green')
        self.line([pm.n(), ph.n()], 'green')
    ############################################################
    #                       De p2 à p1                         #
    if(m > 0):
        ph.x = (pm.x + 8*math.cos(slope_angle(p2,p1)+math.pi/6))
        ph.y = (pm.y + 8*math.sin(slope_angle(p2,p1)+math.pi/6))
        #self.text(ph.x-10,ph.y-10), str(n), fill='black')
        pb.x = (pm.x + 8*math.cos(slope_angle(p2,p1)-math.pi/6))
        pb.y = (pm.y + 8*math.sin(slope_angle(p2,p1)-math.pi/6))
        ps = point(0,0)
        ps.x = (pm.x + 10*math.cos(slope_angle(p2,p1)+math.pi/2))
        ps.y = (pm.y + 10*math.sin(slope_angle(p2,p1)+math.pi/2))
        self.text((ps.x,ps.y), str(m), fill='purple')
        self.line([pm.n(), pb.n()], 'purple')
        self.line([pm.n(), ph.n()], 'purple')'''



def drawnode(self, noeud, p, verbose = False):                                  #méthode qui dessine un point avec son label, et avec ou sans son id
    '''méthode apppliquée a draw qui dessine un noeud
    arguments : n : noeud que l'on veut dessiner
                p : point ou l'on veut placer le noeud
                verbose : bool, par défaut false, si True : affiche l' Id, sinon la fonction n'affiche que le label par défaut'''
    self.ellipse((p.x-10, p.y-10, p.x+10, p.y+10), fill='white', outline='black')
    self.text((p.x - 2  ,p.y - 9), str(noeud.get_label()) , fill='red')
    if(verbose):
        self.text((p.x-2 ,p.y ), str(noeud.get_id()) , fill='blue')

def Bezier(self, p0, paux, p1, de=0.1):
    '''Fonction qui dessine les arretes comme des courbes de bezier quadratique '''

    N = int(1/0.05)
    dt = 1/N
    Ts = [i*dt for i in range(N+1)]
    #La liste contenant tous les poins de l'arrete
    points = [p0*(1-t)*((1-t) + t*paux)+t*((1-t)*paux+t*p1) for t in Ts ]
    for ind in range(len(points)-1) :
        self.line([points[ind].n(), points[ind+1].n()], 'black')






def random_layout(g, node_pos, input_pos, output_pos):                          #fonction qui définit des positions aléatoire pour les noeuds du graphe
    '''fonction qui définit des positions aléatoire pour les noeuds du graphe
    arguments : g : graphe
                node_pos : dictionnaire de positions. keyx : ids des noeuds. Values : positions de noeud ayant l'Id
                input_pos : liste de position correspondants aux inputs du graph
                output_pos : liste de position correspondants aux outputs du graph'''
    for id in g.get_node_ids():# la c
        node_pos[id]=point(random.randrange(25,375), random.randrange(25,375))
    j=0
    for id in g.get_inputs_ids():
        input_pos[id]=point(node_pos[id].x - 25, node_pos[id].y - 25)
        j=j+1
    i = 0;
    for id in g.get_outputs_ids():
        output_pos[i]=point(node_pos[id].x + 25, node_pos[id].y + 25)
        i=i+1
    return node_pos, input_pos, output_pos


def circle_layout(g, node_pos=dict(), input_pos=[], output_pos=[]):
    '''fonction qui définit des positions équiréparties sur un cercle pour les noeuds du graphe
    arguments : g : graphe
                node_pos : dictionnaire de positions. keys : ids des noeuds. Values : positions de noeud ayant l'Id
                input_pos : liste de position correspondants aux inputs du graph
                output_pos : liste de position correspondants aux outputs du graph'''
    nbnode = len(g.get_nodes())
    center = point(200, 200)
    rayon = 175
    i=0
    for id in g.get_node_ids():# la c
        node_pos[id]=point(rayon * math.cos(i*2*math.pi/nbnode) + center.x, rayon*math.sin(i*2*math.pi/nbnode)+ center.y )
        i=i+1
    j=0
    for id in g.get_inputs_ids():
        input_pos.append(point(node_pos[id].x - 25, node_pos[id].y - 25))
        j=j+1
    k = 0;
    for id in g.get_outputs_ids():
        output_pos.append(point(node_pos[id].x + 25, node_pos[id].y + 25))
        k=k+1
    return node_pos, input_pos, output_pos

def DAG_layout(g):
    '''fonction qui renvoie des positions pour les noeuds, les entrées et les sorties du graphe donné en paramètre
    arguments : g : graphe, supposé acyclique
                '''
    height = 400
    j = g.copy()
    listNiveau = g.tri_topologique()

    couche = 0
    for _ in listNiveau :
        couche = couche + 1 + 0.5
    ecarthauteur = height/couche

    i = 0
    nodes_pos = {}
    input_pos = []
    output_pos = []

    for list in listNiveau :
        i = i+1
        for j in list:
            abs = random.randrange(25,375)
            nodes_pos[j] = point(abs, ecarthauteur*(i))
            if g.get_node_by_id(j) in g.get_inputs_ids() :
                input_pos.append(point(abs, ecarthauteur-25))
            if g.get_node_by_id(j) in g.get_inputs_ids() :
                output_pos.append(point(abs, ecarthauteur+25))
    print("in DAG_layout nodes_pos = ", nodes_pos )
    print("in Dag_layout, input_pos = ", input_pos)
    print("in Dag_layout, output_pos = ", output_pos)
    return nodes_pos, input_pos, output_pos



def drawgraph(self, g, node_pos={}, input_pos=[], output_pos=[], method='manual', verbose=False):    
    '''méthode appiquée à draw qui dessine un graph
    arguments : g : graph que l'on veut dessiner
                node_pos : dictionnaire de positions. keys : ids des noeuds. Values : positions de noeud ayant l'Id (va etre modifié si verbose = 'random')
                input_pos : liste de position correspondants aux inputs du graph (va etre modifié si verbose = 'random')
                output_pos : liste de position correspondants aux outputs du graph (va etre modifié si verbose = 'random')
                méthode : string qui précise la manière de choisir les positions des noeuds. Par défaut 'manual'. Sinon préciser 'random', 'circle' ou 'DAG'
                verbose : bool, par défaut false, si True : affiche l' Id des noeuds, sinon la fonction n'affiche que le label par défaut'''

    if (method=='random'):
        node_pos, input_pos, output_pos = random_layout(g, node_pos, input_pos, output_pos)
    elif(method=='circle'):
        node_pos, input_pos, output_pos = circle_layout(g, node_pos, input_pos, output_pos)
    elif(method == 'DAG'):
        node_pos, input_pos, output_pos = DAG_layout(g)
    for i in range(len(input_pos)): #on trace l'entrée
        self.arrows(input_pos[i], node_pos[g.get_inputs_ids()[i]], 0, 1)

    for i in range(len(output_pos)): #on trace la sortie
            self.arrows(node_pos[g.get_outputs_ids()[i]],output_pos[i], 1, 0)
    for id in g.get_node_ids(): # on trace les arrete entre les nodes et leurs enfant
        #if(g.nodes()[id].get_children_ids() != []):
        for child in g.get_nodes()[id].get_children_ids():
            n = count_occurrences(g.get_nodes()[id].get_children_ids(), child)
            m = count_occurrences(g.get_nodes()[id].get_parent_ids(), child)
            self.arrows(node_pos[id], node_pos[child], n, m)
    for id in g.get_node_ids(): # on trace les nodes
        self.node(g.get_node_by_id(id),node_pos[id], verbose)









point.rotate = rotate

ImageDraw.ImageDraw.arrows = drawarrows # we define the method 'arrows'
                                        # from the function 'arrows' above
ImageDraw.ImageDraw.node = drawnode

ImageDraw.ImageDraw.graph = drawgraph

ImageDraw.ImageDraw.bezier = Bezier
