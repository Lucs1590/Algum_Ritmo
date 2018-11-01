#!/usr/bin/python
# -*- encoding: utf-8 -*-

def cadMoeda(moeda):
    cad = True
    while cad == True:
        print('1 - 0.01')
        print('2 - 0.05')
        print('3 - 0.10')
        print('4 - 0.25')
        print('5 - 0.50')
        print('6 - 1.00')
        classe_moeda = input('Que moeda deseja cadastrar?')
        quantidade = input('Quantas moedas deseja cadastrar?')
        lista_moeda = addMoeda(moeda, separarKeyValue(int(classe_moeda)) , int(quantidade))
        res = input('Deseja cadastrar mais moedas? [1/0]')
        if res == 1:
            cad == True
        else:
            cad = False
            return lista_moeda

def troco(lista_moedas,total, valor):
    total = float(total)
    valor = float(valor)
    troco = total - valor
    if troco >= 0:
        pass
    else:
        return ('Estamos sem troco.')


def printcaixa(moedas):
    for moeda in moedas:
        print(moeda)

def addMoeda(moeda,classe_moeda, quantidade):
    moeda.append([classe_moeda, quantidade])
    return moeda

def separarKeyValue(keys):
    if keys == 1:
        return(0.01)
    elif keys == 2:
        return(0.05)
    elif keys == 3:
        return(0.10)
    elif keys == 4:
        return(0.25)
    elif keys == 5:
        return(0.50)
    elif keys == 6:
        return(1.00)
    else:
        return(None)

def totalCaixa(moedas):
    soma = 0
    for moeda in moedas:
        soma += float(moeda[0])*float(moeda[1])
    return soma

menu = {}
menu['1']='Adicionar Moeda' 
menu['2']='Mostrar Caixa'
menu['3']='Dar troco'
menu['4']='Total Caixa'
menu['0']='Sair'
moedas = []

while True:
    options=menu.keys()
    options.sort()
    print ('\n')
    for entry in options:
        print (entry, menu[entry])
    selection = input('Selecione a opção:')
    print ('\n')
    if selection == 1:
        moedas = cadMoeda(moedas)
    elif selection == 2:
        print(printcaixa(moedas))
    elif selection == 3:
        valor = input('Digite o valor recebido: ')
        print(troco(moedas, printcaixa(moedas), valor))
    elif selection == 4:
        print(totalCaixa(moedas))
    elif selection == 0:
        break
    else:
        print ('Opção selecionada INVÁLIDA!')
