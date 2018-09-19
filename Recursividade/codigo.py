#!/usr/bin/python
# -*- encoding: utf-8 -*-


def multiplicacao(num, vezes):
    if vezes == 0:
        return (num)
    else:
        return (num + multiplicacao(num,vezes-1))


def elevado(num,por):
    if por == 0:
        return(1)
    else:
        return num * elevado(num,por-1)


def soma(num):
    if num <= 1:
        return(num)
    else:
        return(num + soma(num-1))


def prim_alg(num):
    num = round(num, 2)
    num_str = str(num)
    if (len(num_str) == 4):
        num = (num / 10)
        num = round(num, 2)
        num_str = str(num)
        print(num)
        if (len(num_str) >= 3):
            return int(num)
        else:
            return int(num*10)
    else:
        return (prim_alg(num / 10))


def num_lista(L, N):
    if N not in L:
        return (L)
    else:
        L.remove(N)
        return (num_lista(L, N))


def num_perfeito(num, contador = 1, soma = 0):
    if (contador == num):
        return soma == num
    else:
        if(num%contador==0): 
            soma+=contador
            return num_perfeito(num,contador+1,soma)



lista = [1,2,3,2,4,5]
# print(multiplicacao(2,10))
# print(elevado(2,3))
# print(soma(6))
# print(prim_alg(150))
# print(num_lista(lista,2))
print(num_perfeito(6))
