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

print(multiplicacao(2,10))
print(elevado(2,3))
print(soma(6))
