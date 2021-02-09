import operator
import random

def remove_all(l,x):
    for i in l:
        if i == x :
            l.remove(i)
    return

def random_int_list(n, bound):
    l=[0]*bound
    for i in range(0, bound):
        l[i] = random.randrange(0,bound,i+1)
    return l
