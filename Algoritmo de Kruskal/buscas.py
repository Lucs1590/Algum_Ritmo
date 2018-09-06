# -*- encoding: utf-8 -*-


def geraLista():
    n = input('Quantidade de Vertices: ')
    lista = []
    for i in range(int(n)):
        lista.append([i])
    imprimeLista(lista)
    return lista


def imprimeLista(lis):
    for m in lis:
        print (m)


def insereAresta(lis):
    x, y = input('Informe a aresta (x,y): ').split(',')
    x = int(x)
    y = int(y)
    if (x!=y):
        lis[x].append(y)
        lis[y].append(x)
    else:
        lis[x].append(y)

    imprimeLista(lis)


def verticesAdj(lis, vertice):
	adj = []
	for i in range(1, len(lis[vertice])):
		adj.append(lis[vertice][i])
	return adj


def existeAresta(lis, x, y):
    existe = False
    for i in range(1,len(lis[x])):
        if lis[x][i] == y:
            existe = True
            break
    return existe


def grauVertice(lis, vertice):
	if (lis, vertice, vertice):
		return len(verticesAdj(lis, vertice)) + 1
	else:
		return len(verticesAdj(lis, vertice))


def buscaLargura(atual):
	print ('\n')
	visitados = []
	vizinhos = [atual]

	while vizinhos != '[]':
		try:
			visitados.append(int(vizinhos[0]))
			print ('\n')

			adj = verticesAdj(grafo, int(vizinhos.pop(0)))
			for vertice in adj:
				if vertice not in visitados and vertice not in vizinhos:
					vizinhos.append(vertice)
			print ('Visitados: ', visitados)
		except:
			print ('-- FINALIZADO --')
			break


def buscaProfundidade(grafo, atual):
	print ('\n')

	visitados = []
	ultimo = atual
	vizinhos = [atual]

	while vizinhos != '[]':
		try:
			visitados.append(int(vizinhos[0]))

			adj = verticesAdj(grafo, int(vizinhos.pop(0)))
			vizinhos = adj
			for vertice in vizinhos:
				ultimo = vertice
				if vertice not in visitados and vertice not in vizinhos:
					visitados.append(vertice)
					vizinhos.append(vertice)

		except:
			print ('--'*30)
			break


# ###########################################################################################################
menu = {}
menu['1'] = 'Criar Lista' 
menu['2'] = 'Insere Aresta'
menu['3'] = 'Visualiza Lista'
menu['4'] = 'Vertices Adjacentes'
menu['5'] = 'Existe Aresta Entre'
menu['6'] = 'Grau do Vertice'
menu['7'] = 'Busca em Largura'
menu['8'] = 'Busca em Profundidade'
menu['9'] = 'Sair'
grafo = []

while True: 
	options = menu.keys()
	options_order = sorted(options)
	print ('\n')
	for entry in options_order:
		print (entry, menu[entry])
	selection = input('Selecione a opção:')
	print ('\n')
	if selection == '1':
		grafo = geraLista()

	elif selection == '2':
		insereAresta(grafo)

	elif selection == '3':
		imprimeLista(grafo)

	elif selection == '4':
		vertice = input('Informe o vertice: ')
		print ('Vertices adjacentes a ', vertice, ': ', verticesAdj(grafo, int(vertice)))

	elif selection == '5':
		v1, v2 = input('Informe os vertices (v1,v2): ').split(',')
		if existeAresta(grafo, int(v1), int(v2)):
			print ('Existe!')

		else:
			print ('Não existe!')

	elif selection == '6':
		vertice = input('Informe o vertice: ')
		print ('Grau do vertice ', vertice, ':', grauVertice(grafo, int(vertice)))

	elif selection == '7':
		atual = input('Digite o vertice inicial: ')
		buscaLargura(atual)

	elif selection == '8':
		atual = input('Digite o vertice inicial: ')
		buscaProfundidade(grafo, atual)

	elif selection == '9':
		break

	else:
		print ('Opção selecionada INVÁLIDA!')
