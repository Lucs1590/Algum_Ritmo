#!/usr/bin/python
# -*- encoding: utf-8 -*-

def trocomin(moedas,r):
    s=[]
    for i in range(0,len(moedas)):
        while moedas[i]<=r:
            s.append(moedas[i]) 
            r=round(r-moedas[i],2) 
    print(s)

def select(moedas):
    if (len(moedas)):
        return max(moedas)
    return None

def valida(x,s,n):
    if (x==None):
        return None
    else:        
        if(round(s+x,2)<=n):
            return True
        else:
            return False

def objetivo(x,s,r):    
    r.append(x)
    return round(s+x,2)

def solucao(s,n):
    if s==n:
        return True
    else: 
        return False

def troco(moedas,n):
    r = []
    s = 0
    while (s!=n):        
        x = select(moedas)
        while (valida(x,s,n)):
            if(x==None):
                print 'Solução não exite!'
            else:
                s = objetivo(x,s,r)
                if solucao(s,n):
                    print r
        moedas.pop(0)

n=float(input("Digite o valor:"))
lista=[1,0.25,0.1,0.05,0.01]
lista2=[1,0.25,0.1,0.05,0.01]
troco(lista,n)
trocomin(lista2,n)

