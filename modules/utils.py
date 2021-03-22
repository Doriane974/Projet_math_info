import operator
import random

def remove_all(l,x):                                    # retire toutes les occurrences de x dans l
    for i in l:
        if i == x :
            l.remove(i)
    return l

def count_occurrences(l,x):                             # compte toutes les occurrences de x dans l
    cpt = 0
    for i in l :
        if i == x :
            cpt += 1
    return cpt


def random_int_list(n, bound):
    l=[0]*n
    for i in range(0, n):
        l[i] = random.randrange(0,bound,i+1)
    return l

def random_int_matrix(n,bound, null_diag=True):
    l=[0]*n
    for i in range(0,n):
        l[i]=random_int_list(n,bound)
    if(null_diag==True):
        for i in range(0,n):
            l[i][i]=0
    return l

#def random_symetric_int_matrix
