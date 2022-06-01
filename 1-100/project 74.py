# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""

def fact(n):
    if(n==1 or n==0):
        return 1
    return(n*fact(n-1))

L=[fact(i) for i in range(10)]

def next(n,L):
    return sum([L[int(i)] for i in str(n)])

def boucle(n,L,before):
    a=next(n,L)
    if(a in before):
        return len(before)+1
    before.add(a)
    return boucle(a,L,before)
def b(n,L):
    before=set()
    return boucle(n,L,before)

tot=0
for i in range(1000000):
    if(i%10000==0):
        print(i//10000, end=' ')
    if(b(i,L)==60):
        tot+=1
print(tot)