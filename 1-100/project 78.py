# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""
import numpy as np

def p(n,P,L):
    S=0
    k=1
    k1,k2=L[k-1]
    while(k1<=n):
        if(k2<=n):
            if(k%2==0):
                S-=P[n-k2]
            else:
                S+=P[n-k2]
        if(k%2==0):
            S-=P[n-k1]
        else:
            S+=P[n-k1]
        k+=1
        k1,k2=L[k-1]
    P.append(S%1000000)
    return P

def f(k):
    return int(k*(3*k - 1)/2),int(k*(3*k + 1)/2)
def Lf(km):
    return [f(k) for k in range(1,km)]

maxi=60000
L=Lf(int(np.sqrt(maxi)))
P=[1,1]
for i in range(2,maxi):
    P=p(i,P,L)

for i,v in enumerate(P):
    if v==0 : print(i)

