#!/usr/bin/python
# -*- encoding: utf-8 -*-

#CODIGO APENAS DAS FUNÇÕES SEM O MAIN DA APLICAÇÃO, A FUNÇÃO buscaLargura DEVE RECEBER UMA LISTA DE ADJACENCIAS DE UM GRAFO E O VERTICE DE INICIO DA BUSCA
def verticesAdj(grafo, vertice):
	adj = []
	for i in range(1, len(grafo[vertice])):
		adj.append(grafo[vertice][i])
	return adj

def buscaLargura(grafo, vertice):
    fila = []
    # insere primeiro vertice na fila e marca como visitado
    fila.append(vertice)
    visitados = [vertice[0]]

    # percorrer todos os vertices (Obs.: Somente grafos conexos)
    while len(fila):
        v = fila.pop(0)  # pega o proximo vertice da fila
        # percorrer vizinhos
        for vizinho in verticesAdj(grafo,v[0]):            
            # verifica se ja foi visitado, caso nao, faz a visita e coloca na fila para verificar os vizinhos
            if not vizinho[0] in visitados:
                # ... colocamos na fila para visitar
                fila.append(vizinho)
                visitados.append(vizinho[0])

            # MOMENTO da visita
            # print v, '->', vizinho
    # print 'fila: ',fila
    print 'visitados em Largura: ',visitados

def buscaProfundidade(lis, vertice, visitados):
    #condição de parada, se o vertice ja foi visitado, a função volta para o anterior
    if vertice[0] in visitados: 
        return False
    #visita o vertice
    visitados.append(vertice[0])
    #percorre os vizinhos
    for f in verticesAdj(lis,vertice[0]):
        #se nao estiver visitado inicia busca novamente começando pelo vertice que nao foi visitado
        if f[0] not in visitados:
            buscaProfundidade(lis, f, visitados)

def menorCaminhoSemPesosProfundidade(grafo, vertice, visitados, distancia):
    #condição de parada, se o vertice ja foi visitado, a função volta para o anterior
    if vertice[0] in visitados: 
        return False
    #visita o vertice
    visitados.append(vertice[0])
    distancia.append(vertice)
    #percorre os vizinhos
    for f in verticesAdj(grafo,vertice[0]):
        #se nao estiver visitado inicia busca novamente começando pelo vertice que nao foi visitado
        if f[0] not in visitados:
            # if (f[1]==None):
                f[1] = vertice[1]+1
                menorCaminhoSemPesosProfundidade(grafo, f, visitados,distancia)

def menorCaminhoSemPesos(grafo, inicial):
    for v in grafo :
        for i in range(1, len(v)):
            v[i][1] = None
    inicial[1] = 0
    fila = [inicial]
    distancias = [inicial]
    visitados = [inicial[0]]
    while len(fila):
        v = fila.pop(0) 
        for vizinho in verticesAdj(grafo,v[0]):
            if not vizinho[0] in visitados:
                # if (vizinho[1] == None) :
                    vizinho[1] = v[1] + 1
                    fila.append(vizinho)
                    distancias.append(vizinho)
                    visitados.append(vizinho[0])
    print 'distancias em Largura: ',distancias

grafo = [
    [[0,-1],[1,-1],[3,-1]],
    [[1,-1],[3,-1],[4,-1]],
    [[2,-1],[0,-1],[5,-1]],
    [[3,-1],[2,-1],[4,-1],[5,-1],[6,-1]],
    [[4,-1],[6,-1]],
    [[5,-1]],
    [[6,-1],[5,-1]]
]

menorCaminhoSemPesos(grafo,grafo[2][0])
buscaLargura(grafo,grafo[2][0])
for v in grafo :
    for i in range(1, len(v)):
        v[i][1] = None
distancia = []
visitados = []
menorCaminhoSemPesosProfundidade(grafo,grafo[2][0],visitados,distancia)
print 'distancias em Profundidade: ',distancia
visitados = []
buscaProfundidade(grafo,grafo[2][0],visitados)
print 'visitados em Profundidade', visitados
