# -*- encoding: utf-8 -

from itertools import product

arvore = [] #resultado final (menor árvore)
arestas = [('UN','PM',200),('UN','BH',650),('PM','BH',400),('MT','BH',350),
('NQ','BH',600),('UB','PM',280),('JF','BH',300),('MT','NQ',250)]
#Lista de cidades com a distância em quilômetros assim como o exemplo


count = 0
valorKM = []

for i in arestas: 
    valorKM.append(arestas[count][2]) #passo para o vetor valorKM apenas os kilômetros
    count += 1 

ordem = sorted(valorKM) #KM em ordem crescente (200, 250,280,...)

novaOrdem = []

for ordem,arestas in product(ordem,arestas):
    if ordem in arestas: 
        novaOrdem.append(arestas) #Com isso ordeno as cidades pela distância em km
#[(UN,PM,200),(MT,NQ,250),...]

for i in novaOrdem:
    if i[0:1] not in arvore or i[1:2] not in arvore: #vejo se o valor não está na arvore
        arvore.append(i)                             #a ideia era colocar apenas valores não repetidos
    else:
        print ('Valores repetidos: ', i)

#ele está tratando (BH,NQ) e (NQ,BH) como coisas diferentes
print (arvore)
