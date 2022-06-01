# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:52:58 2019

@author: DZBZ0373
"""



def f(L,U,ma,mb):
    S=0
    for a in range(L-ma+1):
        for b in range(a+ma,L+1):
            if(ma<=b-a<=mb):
                S+=1
                if(L-b>=ma):
                    S+=U[L-b]
    return S

def g(ma,mb,long):
    U=[0]*ma
    for n in range(ma,long+1):
        U.append(f(n,U,ma,mb))
    return U[-1]+1

print(g(2,4,50))