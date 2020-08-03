#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:59:34 2019

@author: 3412847
"""
from constraint import *

# Dimension du probl`eme
n = 4
# Cr ́eation du probl`eme (colorer la figure en attribuant une couleur (rouge, 
# vert ou bleu a chaque zone) de sorte que deux zones voisines soient de
# couleur differentes)
P1 = Problem()
# Creation d’une variable python de dimension n
z = range(1,n+1)
# Cr ́eation d’une variable z dont le domaine est {"rouge","vert","bleu"}
P1.addVariables(z, ["rouge","vert","bleu"])
# Ajout des contraintes de couleurs
P1.addConstraint(InSetConstraint(["rouge","bleu"]),[1])
P1.addConstraint(InSetConstraint(["bleu","vert"]),[2,3])
P1.addConstraint(InSetConstraint(["rouge"]),[4])

P1.addConstraint(lambda x, y : x != y, [1,2])
P1.addConstraint(lambda x, y : x != y, [1,3])
P1.addConstraint(lambda x, y : x != y, [1,4])
P1.addConstraint(lambda x, y : x != y, [2,3])
P1.addConstraint(lambda x, y : x != y, [3,4])

def solve_p1():
    return P1.getSolution()

print("Solution P1 :", solve_p1())

# Cette fonction retourne None. On en déduit que le problème P1 est trop
# contraignant, il n'admet aucune solution.

# Dimension du probl`eme
n = 4
# Cr ́eation du probl`eme (colorer la figure en attribuant une couleur (rouge, 
# vert ou bleu a chaque zone) de sorte que deux zones voisines soient de
# couleur differentes)
P2 = Problem()
# Creation d’une variable python de dimension n
z = range(1,n+1)
# Cr ́eation d’une variable z dont le domaine est {"rouge","vert","bleu"}
P2.addVariables(z, ["rouge","vert","bleu"])
# Ajout des contraintes de couleurs
P2.addConstraint(InSetConstraint(["rouge","vert"]),[1])
P2.addConstraint(InSetConstraint(["bleu","vert"]),[2,3])
P2.addConstraint(InSetConstraint(["vert"]),[4])

P2.addConstraint(lambda x, y : x != y, [1,2])
P2.addConstraint(lambda x, y : x != y, [1,3])
P2.addConstraint(lambda x, y : x != y, [1,4])
P2.addConstraint(lambda x, y : x != y, [2,3])
P2.addConstraint(lambda x, y : x != y, [3,4])

def solve_p2():
    return P2.getSolution()

print("Solution P2 :",solve_p2())

# Cette fonction retourne {1: 'rouge', 2: 'vert', 3: 'bleu', 4: 'vert'}. On en 
# déduit que le problème P2 est une réduction du problème initial permettant de
# trouver une solution a celui-ci

# Dimension du probl`eme
n = 4
# Cr ́eation du probl`eme (colorer la figure en attribuant une couleur (rouge, 
# vert ou bleu a chaque zone) de sorte que deux zones voisines soient de
# couleur differentes)
P = Problem()
# Creation d’une variable python de dimension n
z = range(1,n+1)
# Cr ́eation d’une variable z dont le domaine est {"rouge","vert","bleu"}
P.addVariables(z, ["rouge","vert","bleu"])

z1 = {"bleu" : 1, "vert" : 0.3, "rouge" : 0.8}
z2 = {"bleu" : 0.2, "vert" : 0.6, "rouge" : 1}
z3 = {"bleu" : 1, "vert" : 0.7, "rouge" : 0.4}
z4 = {"bleu" : 0.5, "vert" : 1, "rouge" : 0.9}

U = [z1,z2,z3,z4]
print(U)

def branch_and_bound():
    A = dict()
    V = z
    alpha = 0
    l = 0
    if not V:
        return A
    

u = []
i = 0
for sol in solve_p2().values():
    u.append(U[i][sol])
    i += 1
print(u)
    