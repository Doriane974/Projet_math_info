import operator
import random

'''Fonction qui retire toutes les occurences de x dans l
arguments : l : 'a list
            x : 'a
return : none '''
def remove_all(l,x):                                      # retire toutes les occurrences de x dans l
    while x in l:
        l.remove(x)
    return l

'''Fonction qui compte toutes les occurences de x dans l
arguments : l : 'a list
            x : 'a
return : int '''
def count_occurrences(l,x):                               # compte toutes les occurrences de x dans l
    cpt = 0
    for i in l :
        if i == x :
            cpt += 1
    return cpt

'''Fonction qui renvoie une liste d'entiers aléatoire
argument : bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
return : int list '''
def random_int_list(n, bound):                             # renvoie une liste d'entiers aléatoire
    l=[0]*n
    for i in range(0, n):
        l[i] = random.randrange(0,bound)
    return l

'''Fonction qui renvoie une matrice carrée d'entier aléatoire
argument : n : int : taille de la matrice
           bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
           null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
return : int list list '''
def random_int_matrix(n,bound, null_diag=True):            # renvoie une matrice d'entier aléatoire
    l=[0]*n
    for i in range(0,n):
        l[i]=random_int_list(n,bound)
    if(null_diag==True):
        for i in range(0,n):
            l[i][i]=0
    return l

'''Fonction qui renvoie une matrice carrée d'entier aléatoire symétrique
argument : n : int : taille de la matrice
           bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
           null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
return : int list list '''
def random_symetric_int_matrix(n, bound, null_diag=True):   #renvoie une matrice symétrique d'entier aléatoire
    l = random_int_matrix(n, bound, null_diag)
    for i in range(0,n):
        for j in range(0,i):
            l[j][i]=l[i][j]
    return l

'''Fonction qui renvoie une matrice carrée d'entier aléatoire correspondant a un graphe orienté
argument : n : int : taille de la matrice
           bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
           null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
return : int list list '''
def random_oriented_int_matrix(n, bound, null_diag=True):   #renvoie une matrice d'entier aléatoire correspondant a un graphe orienté
    l=random_int_matrix(n, bound, null_diag)
    for i in range(0,n):
        for j in range(i+1, n):
            if(l[i][j] != 0):
                l[j][i] = 0
    for i in range(1,n):
        for j in range(i-1, 0): #verifier le range
            if(l[i][j] != 0):
                l[j][i] = 0
    return l

'''Fonction qui renvoie une matrice triangulaire carrée d'entier aléatoire
argument : n : int : taille de la matrice
           bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
           null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
return : int list list '''
def random_triangular_int_matrix(n, bound, null_diag=True): #renvoie une matrice triangulaire d'entier aléatoire
    l=random_int_matrix(n, bound, null_diag)
    for i in range(0,n):
        for j in range(i+1, n):
            l[i][j]=0
    return l


'''Fonction qui permet de retirer les doublons d une liste, en utilisant une propriete des dictionnaires Python
arguments : list, une liste contenant potentiellement des doublons
return : cleaned_list, une liste contenant les elements de list, mais sans doublon'''
def list_cleaner(list1):
    return list(dict.fromkeys(list1))
