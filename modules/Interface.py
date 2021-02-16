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
