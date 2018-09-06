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


def alvaro(grafo, vertice):
	adjascente = []
	visitados = []
	profundidadeReversa = []

	adjascente.append(vertice)
	visitados.append(vertice)
	

	while len(adjascente) or len(profundidadeReversa):
		if len(adjascente) > 0:
			print (len(adjascente))
			print (adjascente)
			print (visitados)
			pop_adjacente = adjascente
			busca = pop_adjacente.pop(0)
			print ('BUSCA ' + str(busca))
			vizinhos = verticesAdj(grafo, int(busca))
			print ('VIZINHOS ' + str(vizinhos))
			count = 0
			print ('COUNT ' + str(count))
			for j in vizinhos:
				if j not in visitados and count < 1:
					print ('olá1')
					# count += 1
					adjascente.append(j)
					visitados.append(j)
					# print('JOTINHA ' + str(j))
				elif j in visitados:
					profundidadeReversa.append(j)
					print ('olá2')
		else:
			for i in reversed(visitados):
				visitados.append(i)
				if visitados.count('0') < 3:
					print ('looooooop')
					adjascente.append(visitados[0])
			for i in profundidadeReversa:
				count2 = 0
				profundidadeReversa.pop(count2)
				print ('LAUAOAPPIIIIII')


def samuel(grafo, atual):
	print ('\n')

	visitados = []
	# ultimo = atual
	vizinhos = [atual]
	j = 0

	visitados.append(int(atual))
	print (visitados)

	while vizinhos != []:
		try:
			vizinhos = verticesAdj(grafo, int(visitados[j]))
			print (vizinhos)
			print ('ok')

			i = 0
			for vizinho in vizinhos:
				if vizinho not in visitados:
					atual = vizinho
					# print ('atual ' + str(atual))
					break

				else:
					i += 1
					# print ('i ' + str(i))

			if i == len(vizinhos):
				k = 0
				for vertice in grafo:
					# print ('VÉRTICE 0')
					# print (vertice[0])
					if vertice[0] in visitados:
						k += 1
						
					else:
						m = 1
						while m < len(visitados):
							vizinhos_fernando = verticesAdj(grafo, int(visitados[j-m]))
							# print (vizinhos_fernando)
							l = 0
							find = False
							for vizinho_fernando in vizinhos_fernando:
								print (vizinho_fernando)
								if vizinho_fernando not in visitados:
									atual = visitados[j-m]
									print (atual)
									print ('ATUEL')
									# m += 1
									print ('ENTROU GOSTOSINHO')
									find = True
									break

								else:
									l += 1

							if l == len(vizinhos_fernando):
								print ('SAIU GOSTOSINHO')
								m += 1

							if find:
								break

				if len(grafo) == k:
					vizinhos = []
					resultado = visitados

			print ('VISITADOS BUSCA EM profundidade')
			print (visitados)

			visitados.append(int(atual))
			j += 1

		except:
			print ('--'*45)
			print ('TRAVOU')
			break

	return resultado


# ###########################################################################################################
menu = {}
menu['1'] = 'Criar Lista' 
menu['2'] = 'Insere Aresta'
menu['3'] = 'Visualiza Lista'
menu['4'] = 'Vertices Adjacentes'
menu['5'] = 'Existe Aresta Entre'
menu['6'] = 'Grau do Vertice'
menu['7'] = 'Busca em Largura'
menu['8'] = 'Samuel'
menu['9'] = 'Alvaro'
menu['10'] = 'Sair'
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
		atual = int(atual)
		print ('ASSALABASSURIAS')
		print (samuel(grafo, atual))
		print ('CANTARAI')

	elif selection == '9':
		atual = input('Digite o vertice inicial: ')
		# atual = int(atual)
		alvaro(grafo, atual)

	elif selection == '10':
		break

	else:
		print ('Opção selecionada INVÁLIDA!')
