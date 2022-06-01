# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:49:38 2019

@author: DZBZ0373
369
"""
import numpy as np

def comb(M):
    S=0
    for a in range(1,M+1):
        for bc in range(2,2*a):
            if(np.sqrt(a**2 + bc**2)%1==0):
                S+=bc//2

    return S
def add(M,N):
    S=0
    for a in range(M+1,N+1):
        for b in range(1,a+1):
            for c in range(1,b+1):
                if(np.sqrt(a**2 + (b+c)**2)%1==0):
                    S+=1
    return S


M=1815
tot=998665
p=1
print('starting')
while tot<1000000:
    tot+=add(M,M+p)
    M+=p
    print(M,tot)

print('Finished!')
print('Solution :',M)