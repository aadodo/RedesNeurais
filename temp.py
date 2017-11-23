# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

entradas = [-1, 7, 5]
pesos=[0.8, 0.1, 0]

def soma(e, p):
    s=0
    for i in range(len(entradas)):
        s+=entradas[i]*pesos[i]
    return s

def stepFunction (valor):
    if valor>0:
        return 1
    return 0

somatorio=soma(entradas,pesos)
resultado=stepFunction(somatorio)