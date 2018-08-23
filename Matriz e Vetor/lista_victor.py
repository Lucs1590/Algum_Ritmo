#!/usr/bin/python
# -*- encoding: utf-8 -*-

def geraLista():
    n = raw_input("Quantidade de Vertices:")
    lista=[]
    for i in range(int(n)):
        lista.append([i])
    imprimeLista(lista)
    return lista

def imprimeLista(lis):
    for m in lis:
        print m

def insereAresta(lis):
    x,y = raw_input("Informe a aresta:").split()
    x = int(x)
    y = int(y)
    if(x!=y):
        lis[x].append(y)
        lis[y].append(x)
    else:
        lis[x].append(y)

    imprimeLista(lis)

def verticesAdj(lis,vertice):
	adj=[]
	for i in range(1,len(lis[vertice])):
		adj.append(lis[vertice][i])
	return adj

def existeAresta(lis,x,y):
    existe = False
    for i in range(1,len(lis[x])):
        if lis[x][i]==y:
            existe = True
            break
    return existe

def grauVertice(lis,vertice):
	if existeAresta(lis,vertice,vertice): #verifica se existe laço (obs. apenas 1 laço)
		return len(verticesAdj(lis,vertice))+1
	else:
		return len(verticesAdj(lis,vertice))

menu = {}
menu['1']="Criar Lista" 
menu['2']="Insere Aresta"
menu['3']="Visualiza Lista"
menu['4']="Vertices Adjacentes"
menu['5']="Existe Aresta Entre"
menu['6']="Grau do Vertice"
menu['7']="Busca em Largura"
menu['8']="Sair"
grafo = []
while True: 
	options=menu.keys()
	options.sort()
	print '\n'
	for entry in options:
		print entry, menu[entry]
	selection=raw_input("Selecione a opção:")
	print '\n'
	if selection =='1':
		grafo = geraLista()
	elif selection == '2':
		insereAresta(grafo)
	elif selection == '3':
		imprimeLista(grafo)
	elif selection == '4':
		vertice = raw_input("Informe o vertice:")
		print 'Vertices adjacentes a ',vertice,': ',verticesAdj(grafo,int(vertice))
	elif selection == '5':
		v1,v2 = raw_input("Informe os vertices:").split()
		if existeAresta(grafo,int(v1),int(v2)):
			print 'Existe!'
		else:
			print 'Não existe!'
	elif selection == '6':
		vertice = raw_input("Informe o vertice:")
		print 'Grau do vertice ',vertice,':',grauVertice(grafo,int(vertice))
	elif selection == '7':
		atual = raw_input("Digite o vertice inicial: ")

		visitados = []
		vizinhos = verticesAdj(grafo, int(atual))

		while vizinhos != '[]':
			visitados.append(atual)
			print 'vertice atual: ',atual
			print 'vertices vizinhos: ', vizinhos
			print 'visitados: ', visitados
			if vizinhos[0] not in visitados:
				atual = vizinhos[0]
				# Fazer a parte de cima virar uma função de verificação de grafos atuais e vizinhos e jogar o [0] de vizinhos virar index dentro do for

		print 'Não há grafos adjacentes ao vertice ', atual, ' que não tenha sido visitado'

	elif selection == '8':
		break
	else:
		print "Opção selecionada INVÁLIDA!" 

