#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:53:21 2019

@author: 3412847
"""

from constraint import *

# Dimension du probl`eme
n = 8
# Cr ́eation du probl`eme
pb = Problem()
# Cr ́eation d’une variable python de dimension n
cols = range(n)
# Cr ́eation d’une variable cols dont le domaine est {1, ..., n}
pb.addVariables(cols, range(n))
# Ajout de la contrainte AllDiff
pb.addConstraint(AllDifferentConstraint())
# R ́ecup ́eration de l’ensemble des solutions possibles
s = pb.getSolution()
print(s)