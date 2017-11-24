#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:19:01 2017

@author: dodo
"""

entradas=[[0, 0],[0, 1], [1, 0], [1, 1]]
pesos=[0.0, 0.0]
saidaEsperada=[0, 0, 0, 1]
txAprendizagem=0.1

saida=[]

def pesosFinais():
    calculaPeso=somatorio()
    if (calculaPeso>0):
        calculaPeso=somatorio()
    

def somatorio():    
    erro=0
    for i in range(len(entradas)):
        soma = 0
        soma = entradas[i][0]*pesos[0]+entradas[i][1]*pesos[1]
        stp=stepFunction(soma, saidaEsperada[i])
        if(stp != 1):
            erro= saidaEsperada[i] - soma
            peso1 = atualizaPesos(pesos[0],entradas[i][0],erro)
            peso2 = atualizaPesos(pesos[1],entradas[i][0],erro)
            pesos[:] = [peso1,peso2]            
            erro+=1
    return erro
    
def atualizaPesos(pesoAnterior, entrada, erro):
    # erro=respostaCorreta-respostaCalculada
    novoPeso = pesoAnterior+(txAprendizagem*entrada*erro)
    return novoPeso


def stepFunction(valor, valorEsperado):
    if (valor == valorEsperado):
        return 1
    return 0

pesosFinais()