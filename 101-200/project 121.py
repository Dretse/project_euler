# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:17:07 2019

@author: DZBZ0373
"""
from copy import deepcopy 
import numpy as np

def combis(n,L=[[1],[0]]):
    La=deepcopy(L)
    Lb=deepcopy(L)
    for i in range(len(L)):
        La[i].append(0)
        Lb[i].append(1)
    L2=La+Lb
    if(len(L2[0])==n):return L2
    else: return combis(n,L2)

def proba(L,P):
    a=1
    for i in [(P[i]-1) for i in range(len(L)) if L[i]==0]:
        a*=i
    return(a)   

def fact(n):
    a=1
    for i in range(2,n+1):
        a*=i
    return a

def price(N):
    P=[n+2 for n in range(N)]
    Pos=[tuple(i) for i in combis(N) if sum(i)>N//2]

    S=0
    d=fact(N+1)
    for i in Pos: 
        n=proba(i,P)
        S+=n
    #print(S/d,S,d,d/S)
    return (int(d/S))


print(price(15))

