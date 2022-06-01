# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:52:58 2019

@author: DZBZ0373
"""



def f(L,U,m):
    S=0
    for a in range(L-m+1):
        for b in range(a+m,L+1):
            if(b-a==m):
                S+=1
                if(L-b>=m):
                    S+=U[L-b]
    return S

def g(m,long):
    U=[0]*m
    for n in range(m,long+1):
        U.append(f(n,U,m))
    return U[-1]

print(g(2,50)+g(3,50)+g(4,50))