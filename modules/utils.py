import operator

def remove_all(l,x):
    for i in l:
        if i == x :
            l.remove(i)
    return

def count_occurrences(l,x):
    cpt = 0
    for i in l :
        if i == x :
            cpt += 1
    return cpt
