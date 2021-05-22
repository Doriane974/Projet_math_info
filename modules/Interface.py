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


    '''méthode qui retourne le couple correspondant aux coordonée du point. Méthode appliquée au point dont on veut les coordonées.
    arguments : none
    return : un couple (x,y) des coordonnes du point '''
    def n(self):
        return (round(self.x), round(self.y)) # return a simple tuple

    def __str__(self):
        return "(" + str(self.x) +"," + str(self.y)+ ")"
        '''output : str ; the string given by str(node)'''

    def __repr__(self):
        return "point"+str(self)

    '''méthode qui retourne une copie du point, méthode appliquée au point que l'on veut copier.
    argument : none
    return : un point de meme coordonnées que celui sur lesquel est appliqué la méthode '''
    def copy(self):                                                             #copie un point
        return point(self.x, self.y)

    '''additionne les coordonnées de points de coordonnées (x,y) et (x', y')
    méthode appliquée a un point de coordonée (x,y)
    argument : p2 : points de coordonnées (x', y')
    return : point de coorrdonnée (x+x', y+y')'''
    def __add__(self, p2):                                                      #addditionne 2 points, retourne un nouveau
        return point(self.x + p2.x, self.y + p2.y)

    '''Multiplie les coordonnées d'un point de coordonnées (x,y) par un scalaire
    méthode appliquée au point de coordonnée (x,y)
    argument : s : int par lequel ont veut multiplier le point
    return : point de coorrdonnée (x*s, y*s) '''
    def __rmul__(self, s):                                                      #multiplie 2 point, retourne un nouveau
        return point(self.x*s, self.y*s)

    '''soustraie les coordonnées de points de coordonnées (x,y) et (x', y')
    méthode appliquée a un point de coordonée (x,y)
    argument : p2 : points de coordonnées (x', y')
    return : point de coorrdonnée (x-x', y-y')'''
    def __sub__(self, p2):                                                      #soustraie 2 points, retourne un nouveau
        return point(self.x - p2.x, self.y - p2.y)

'''méthode appliquée a un point  qui calcule la position du point apres rotation d'angle
théta autour du point c.
arguments : theta : float : angle
            c : point
return : point
'''
def rotate(self, theta, c=point(0,0)):
    p = point(0,0)
    theta =theta * math.pi / 180
    p.x = self.x - c.x
    p.y = self.y - c.y
    r = point(0,0)
    r.x = p.x * math.cos(theta) + p.y * math.sin(theta) + c.x
    r.y = -p.x * math.sin(theta) + p.y * math.cos(theta) + c.y
    return r

'''fonction qui calcule l'angle en radian formé entre la ligne qui passe par les point p1 et p2 et l'axe des abscisse
argument : p1 : point
           p2 : point
return : float (angle en radian)'''
################################################################################
#                        Demander une vérification                             #
def slope_angle(p1, p2):                #Beugué, il faut pouvoir avoir des angles négatif, la c'est une valeur absolue
    Ni=1
    Xvi = 1
    Yvi = 0
    Xvp1p2 = p2.x - p1.x
    Yvp1p2 = p2.y - p1.y
    Np1p2 = math.sqrt((p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y))
    scal = Xvi * Xvp1p2 + Yvi * Yvp1p2
    return math.acos(Xvp1p2/(Np1p2))

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



'''méthode qui dessine une arrete entre 2 point, en prenant en compte le fait
que le graphe soit orienté et que il puisse y avoir plusieurs arrete entre 2 point
argument : p1 : point
           p2 : point
           arretep1p2: le nomdre d'arrete entre p1 et p2 (par défaut 1)
           arretep2p1: le nombre d'arrete entre p2 et p1 (par défaut 1)
return : none '''
def drawarrows(self, p1, p2, arretep1p2 = 1, arretep2p1 = 1):
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
        pHautP1P2 = point((pFlecheP1P2.x + 10*math.cos(slope_angle(p1,p2)+math.pi/4)) , (pFlecheP1P2.y + 8*math.sin(slope_angle(p1,p2)+math.pi/4))) #une des éxtrémité des lignes de la fleche
        pBasP1P2 = pHautP1P2.rotate(100, pFlecheP1P2)                                         #l'opposé

        self.line([pFlecheP1P2.n(), pHautP1P2.n()], 'purple')                                   #une des lignes de la fleche
        self.line([pFlecheP1P2.n(), pBasP1P2.n()], 'purple')                                    #l'autre ligne
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


'''méthode apppliquée a draw qui dessine un noeud
arguments : n : noeud que l'on veut dessiner
            p : point ou l'on veut placer le noeud
            verbose : bool, par défaut false, si True : affiche l' Id, sinon la fonction n'affiche que le label par défaut'''
def drawnode(self, noeud, p, verbose = False):                                  #méthode qui dessine un point avec son label, et avec ou sans son id
    self.ellipse((p.x-10, p.y-10, p.x+10, p.y+10), fill='white', outline='black')
    self.text((p.x - 2  ,p.y - 9), str(noeud.get_label()) , fill='red')
    if(verbose):
        self.text((p.x-2 ,p.y ), str(noeud.get_id()) , fill='blue')

'''fonction qui définit des positions aléatoire pour les noeuds du graphe
arguments : g : graphe
            node_pos : dictionnaire de positions. keyx : ids des noeuds. Values : positions de noeud ayant l'Id
            input_pos : liste de position correspondants aux inputs du graph
            output_pos : liste de position correspondants aux outputs du graph'''
def random_layout(g, node_pos, input_pos, output_pos):                          #fonction qui définit des positions aléatoire pour les noeuds du graphe
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

'''fonction qui définit des positions équiréparties sur un cercle pour les noeuds du graphe
arguments : g : graphe
            node_pos : dictionnaire de positions. keys : ids des noeuds. Values : positions de noeud ayant l'Id
            input_pos : liste de position correspondants aux inputs du graph
            output_pos : liste de position correspondants aux outputs du graph'''
def circle_layout(g, node_pos=dict(), input_pos=[], output_pos=[]):
    nbnode = len(g.get_nodes())
    center = point(200, 200)
    rayon = 175
    i=0
    for id in g.get_node_ids():# la c
        print("in circle layout, node_pos = ", node_pos)
        node_pos[id]=point(rayon * math.cos(i*2*math.pi/nbnode) + center.x, rayon*math.sin(i*2*math.pi/nbnode)+ center.y )
        i=i+1
    j=0
    print("in circle layout, g.get_inputs_ids() = ", g.get_inputs_ids())
    for id in g.get_inputs_ids():
        input_pos.append(point(node_pos[id].x - 25, node_pos[id].y - 25))
        j=j+1
    k = 0;
    for id in g.get_outputs_ids():
        output_pos.append(point(node_pos[id].x + 25, node_pos[id].y + 25))
        k=k+1
    return node_pos, input_pos, output_pos

def DAG_layout(g):
    height = 400
    j = g.copy()
    couche = 1
    for input_id in g.get_inputs_ids():
        cpt = j.compte_generation(input_id, 0,0)
        if(couche < cpt):
            couche = cpt
    ecarthauteur = height/couche
    ecarthauteur = ecarthauteur - 1
    #il y a surement unbug au dessus la, à verifier
    nodes = g.get_node_ids()
    #print("in DAG_layout, apres creation de nodes, nodes = ", nodes)
    nodes_pos = {}
    input_pos = []
    output_pos = []
    #On place tous les inputs
    for input_id in g.get_inputs_ids(): #Cette boucle fontionne normalemnt
        abs = random.randrange(25,375)
        nodes_pos[input_id] = point(abs, ecarthauteur)
        input_pos.append(point(abs, ecarthauteur-25))
        nodes.remove(input_id)
    '''print("in DAG_layout, avant la deuxieme boucle for, input_pos = ", input_pos)
    print("in DAG_layout, avant la deuxieme boucle for, nodes = ", nodes)
    print("in DAG_layout, avant la deuxieme boucle for,g.get_output_ids() = ", g.get_outputs_ids())'''
    for output_id in g.get_outputs_ids(): #cette boucle fonctionne bien
        abs = random.randrange(25,375)
        nodes_pos[output_id] = point(abs, ecarthauteur)
        output_pos.append(point(abs, ecarthauteur-25))
        if(output_id in nodes):
            nodes.remove(output_id)
    '''print("in DAG_layout, avant la derniere boucle for, output_pos = ", output_pos)
    print("in DAG_layout, avant la derniere boucle for, nodes = ", nodes)'''
    for id_node in nodes :
        i=0
        id_parent = id_node
        while(g.get_node_by_id(id_parent).get_parent_ids()!=[]):
            i = i+1
            id_parent = g.get_node_by_id(id_parent).get_parent_ids()[0]
        abs = random.randrange(25,375)
        nodes_pos[id_node] = point(abs, ecarthauteur*i)
    #print("in DAG_layout, apres la derniere boucle for, nodes_pos = ", nodes_pos)
    return nodes_pos, input_pos, output_pos

'''méthode appiquée à draw qui dessine un graph
arguments : g : graph que l'on veut dessiner
            node_pos : dictionnaire de positions. keys : ids des noeuds. Values : positions de noeud ayant l'Id (va etre modifié si verbose = 'random')
            input_pos : liste de position correspondants aux inputs du graph (va etre modifié si verbose = 'random')
            output_pos : liste de position correspondants aux outputs du graph (va etre modifié si verbose = 'random')
            méthode : string qui précise la manière de choisir les positions des noeuds. Par défaut 'manual'. Sinon préciser 'random', 'circle' ou 'DAG'
            verbose : bool, par défaut false, si True : affiche l' Id des noeuds, sinon la fonction n'affiche que le label par défaut'''
def drawgraph(self, g, node_pos={}, input_pos=[], output_pos=[], method='manual', verbose=False):     #méthode qui dessine un graphe, choix des positins aléatoire ou manuelle.
    if (method=='random'):                                                                                  #verifier les paramétres
        node_pos, input_pos, output_pos = random_layout(g, node_pos, input_pos, output_pos)
    elif(method=='circle'):
        print("####################on rentre dans method=='circle #########################")
        node_pos, input_pos, output_pos = circle_layout(g, node_pos, input_pos, output_pos)
        print("in, drawGraph, dans le if method = circle, node_pos = ", node_pos)
    elif(method == 'DAG'):
        node_pos, input_pos, output_pos = DAG_layout(g)
    print("in draw_graph,avant premier for , input_pos = ", input_pos)
    for i in range(len(g.get_inputs_ids())): #on trace l'entrée
        self.arrows(input_pos[i], node_pos[g.get_inputs_ids()[i]], 0, 1)
        print("in draw_graph, premier for, i = ", i, ", input_pos[i] = ", input_pos[i])

    for i in range(len(g.get_outputs_ids())): #on trace la sortie
            self.arrows(node_pos[g.get_outputs_ids()[i]],output_pos[i], 1, 0)
    for id in g.get_node_ids(): # on trace les arrete entre les nodes et leurs enfant
        #if(g.nodes()[id].get_children_ids() != []):
        print("in drawGraph, ",g.get_nodes()[id].get_children_ids())
        print("node_pos = ",node_pos)
        for child in g.get_nodes()[id].get_children_ids():
            print("in drawgraph, child =", child)
            n = count_occurrences(g.get_nodes()[id].get_children_ids(), child)
            m = count_occurrences(g.get_nodes()[id].get_parent_ids(), child)
            print("Dans drawGraph, n = ",n, " et m = ",m)
            print("Dans drawGraph, node_pos[id] =", node_pos.get(id, None), " et node_pos[child] = ",node_pos.get(child, -1))
            self.arrows(node_pos[id], node_pos[child], n, m)
    for id in g.get_node_ids(): # on trace les nodes
        self.node(g.get_node_by_id(id),node_pos[id], verbose)









point.rotate = rotate

ImageDraw.ImageDraw.arrows = drawarrows # we define the method 'arrows'
                                        # from the function 'arrows' above
ImageDraw.ImageDraw.node = drawnode

ImageDraw.ImageDraw.graph = drawgraph
