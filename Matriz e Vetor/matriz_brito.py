#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gerar_matriz (vertices):
    matriz = []
    for _ in range(vertices):
        matriz.append( [1] * vertices)
    return matriz


def imprimir_matriz(func):
    for linha in func:
        print (linha)
    return True


def inserirAresta_matriz(func, aresta):
    v1 = aresta[0]
    v2 = aresta[1]
    
    valor = func[(v1-1)][v2-1] = 1
    print (valor)
    return (valor)


def verticeLurde(func, vertice):
    valor = func[(vertice-1)]
    val_vertice = 1
    adj = []

    for v in valor:
        if v == 1:
            adj.append(val_vertice)
        
        val_vertice += 1

    print('Os vertices adjacentes são: ', adj)    


def acharValorVertice_matriz(func, aresta):
    v1 = aresta[0]
    v2 = aresta[1]
    
    valor = func[(v1-1)][v2-1]
    print (valor)
    return (valor)


def existeAresta_matriz(func, aresta):
    v1 = aresta[0]
    v2 = aresta[1]
    
    valor = func[(v1-1)][v2-1]
    if valor == 1:
        print ('Há uma aresta entre ' , v1 , ' e ' , v2)
    else:
        print('Não há aresta entre os vertices ' , v1 , ' e ' , v2)


def grauVertice(func, vertice):
    valor = func[(vertice-1)]
    val_vertice = 1
    adj = []

    for v in valor:
        if v == 1:
            adj.append(val_vertice)
        
        val_vertice += 1
    print('Os vertices possui ', len(adj), ' graus')

# TESTES

# GERAR MATRIZ
# gerar_matriz(2)

# IMPRIMIR MATRIZ
# imprimir_matriz(gerar_matriz(2))

# INSERIR ARESTA
# inserirAresta_matriz(gerar_matriz(3),(2,2))

# VERTICE ADJACENTE
#verticeLurde(gerar_matriz(4),4)

# ACHAR VALOR DO VÉRTICE
# acharValorVertice_matriz(gerar_matriz(3),(3,1))

# EXISTENCIA DE ARESTA
# existeAresta_matriz(gerar_matriz(4),(2,1))

# QUANTIDADE DE GRAUS
grauVertice(gerar_matriz(5),3)
