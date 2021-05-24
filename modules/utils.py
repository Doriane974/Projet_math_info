import operator
import random


def remove_all(l,x):                                      # retire toutes les occurrences de x dans l
    '''Fonction qui retire toutes les occurences de x dans l
    arguments : l : 'a list
                x : 'a
    return : none '''
    while x in l:
        l.remove(x)
    return l


def count_occurrences(l,x):                               # compte toutes les occurrences de x dans l
    '''Fonction qui compte toutes les occurences de x dans l
    arguments : l : 'a list
                x : 'a
    return : int '''
    cpt = 0
    for i in l :
        if i == x :
            cpt += 1
    return cpt


def random_int_list(n, bound):                             # renvoie une liste d'entiers aléatoire
    '''Fonction qui renvoie une liste d'entiers aléatoire
    argument : bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
    return : int list '''
    l=[0]*n
    for i in range(0, n):
        l[i] = random.randrange(0,bound)
    return l


def random_int_matrix(n,bound, null_diag=True):            # renvoie une matrice d'entier aléatoire
    '''Fonction qui renvoie une matrice carrée d'entier aléatoire
    argument : n : int : taille de la matrice
               bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
               null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
    return : int list list '''
    l=[0]*n
    for i in range(0,n):
        l[i]=random_int_list(n,bound)
    if(null_diag==True):
        for i in range(0,n):
            l[i][i]=0
    return l


def random_symetric_int_matrix(n, bound, null_diag=True):   #renvoie une matrice symétrique d'entier aléatoire
    '''Fonction qui renvoie une matrice carrée d'entier aléatoire symétrique
    argument : n : int : taille de la matrice
               bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
               null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
    return : int list list '''
    l = random_int_matrix(n, bound, null_diag)
    for i in range(0,n):
        for j in range(0,i):
            l[j][i]=l[i][j]
    return l


def random_oriented_int_matrix(n, bound, null_diag=True):   #renvoie une matrice d'entier aléatoire correspondant a un graphe orienté
    '''Fonction qui renvoie une matrice carrée d'entier aléatoire correspondant a un graphe orienté
    argument : n : int : taille de la matrice
               bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
               null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
    return : int list list '''
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


def random_triangular_int_matrix(n, bound, null_diag=True): #renvoie une matrice triangulaire d'entier aléatoire
    '''Fonction qui renvoie une matrice triangulaire carrée d'entier aléatoire
    argument : n : int : taille de la matrice
               bound : int : la borne maximum de l'intervalle dans lequel on choisit les élements de la liste, bound exclus
               null_diag : bool, par défaut True, si True : Diagonale de la matrice nulle
    return : int list list '''
    l=random_int_matrix(n, bound, null_diag)
    for i in range(0,n):
        for j in range(i+1, n):
            l[i][j]=0
    return l


def list_cleaner(list1):
    '''Fonction qui permet de retirer les doublons d une liste, en utilisant une propriete des dictionnaires Python
    arguments : list, une liste contenant potentiellement des doublons
    return : cleaned_list, une liste contenant les elements de list, mais sans doublon'''
    return list(dict.fromkeys(list1))


def perm_calc(list1, list2):
    '''Fonction qui permet de calculer la permutation a appliquer a list1 pour obtenir list2
    arguments : list1, liste avant permutation
                list2, liste apres permutation
                (list1 et list2 doivent avoir la meme taille, et la presence de doublons peut causer des problemes)
    return : perm, permutation pour passer de list1 a list2'''
    perm = [0] * len(list1)
    if len(list1) == len(list2):
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    perm[i] = j
    return perm

def inv_perm(perm):
    '''Fonction qui calcule l inverse d une permutation (algorithme inspire de StackOverflow)
    arguments : perm, un liste representant une permutation
    return : inv_perm, l inverse de perm'''
    inv_perm = [0] * len(perm)
    for i, p in enumerate(perm):
        inv_perm[p] = i
    return inv_perm

def appl_perm(list1, perm):
    '''Fonction qui permet d appliquer une permutation a list1 pour obtenir list2
    arguments : list1, liste avant permutation
                perm, permutation a appliquer
                (list1 et perm doivent avoir la meme taille, et la presence de doublons peut causer des problemes)
    return : list2, list apres permutation'''
    list2 = [0] * len(list1)
    for i in range(len(list1)):
        list2[perm[i]] = list1[i]
    return list2
