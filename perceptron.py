#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:44:21 2017

@author: dodo
"""
import numpy as np

entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])
# somatório do produto das entradas pelos pesos
def soma(e, p):
    #produto escalar de dois arrays.
    s= e.dot(p)
    return s;

def stepFunction(valor):
    if (valor >=1):
        return 1
    return 0

somatorio = soma(entradas, pesos)
resultado = stepFunction(somatorio)