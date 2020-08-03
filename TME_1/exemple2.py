#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:56:12 2019

@author: 3412847
"""

from constraint import *

# Dimension du probl`eme
n = 3
# Cr ́eation du probl`eme
p = Problem()
# Creation d’une variable python representant les nombres `a placer dans la grille
x = range(1, n**2 + 1)
# Cr ́eation d’une variable x dont le domaine est {1, ..., n**2 + 1}
p.addVariables(x, x)
# Ajout de la contrainte AllDiff
p.addConstraint(AllDifferentConstraint())
# Variable contenant la somme de chaque ligne/colonne/diagonale
s = n*n * (n*n + 1) / 6
# Ajout des contraintes du carr ́e magique
for k in range(n):
    # ligne k
    p.addConstraint(ExactSumConstraint(s), [x[k*n+i] for i in range(n)])
    # colonne k
    p.addConstraint(ExactSumConstraint(s), [x[k+n*i] for i in range(n)])
    # premi`ere diagonale
    p.addConstraint(ExactSumConstraint(s), [x[n*i+i] for i in range(n)])
    # deuxi`eme diagonale
    p.addConstraint(ExactSumConstraint(s), [x[(n-1)*i] for i in range(1, n+1)])

s = p.getSolution()
print(s)