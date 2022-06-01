# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:02:24 2019

@author: DZBZ0373
"""
import numpy as np

def K(S):
    return np.prod(S)-np.sum(S) + len(S)

def f(L,i,mk):
    k=K(L)
    if(k==mk):
        return {k:np.prod(L)}
    elif(k<mk):
        if(len(L)>i+1):
            D1 =fus(f(L.copy(),i+1,mk), {k:np.prod(L)})
            if(i==0 or L[i]<L[i-1]):
                L[i]+=1
                D2=f(L.copy(),i,mk)
                return fus(D1,D2)
            else:
                return D1
        else:
            if(i==0 or L[i]<L[i-1]):
                P={k:np.prod(L)}
                L[i]+=1
                return fus(f(L.copy(),i,mk), P)
            else:
                return {k:np.prod(L)}
    return {0:0}


def fv2(L,i,mk):
    k=K(L)
    D={0:0}
    while(k<=mk):
        D=fus(D,{k:np.prod(L)})
        if(k<mk):
            
            D=fus(D,f(L.copy(),i+1,mk))
            L[i]+=1
        else:
            break
        k=K(L)
    return D
            
            
            
        
def fus(D1,D2):
    for i in D1:
        if(i in D2 and D2[i]<D1[i]):
            D1[i]=D2[i]
    for i in D2:
        if(not(i in D1)):
            D1[i]=D2[i]
            
    return D1

def g(mk):
    D={0:0}
    ND={1:1}
    n=2
    while(ND!={0:0}):
        print(n,"/14")
        L=np.zeros(n)+2
        ND=fv2(L.astype(int),0,mk)
        D=fus(D,ND)
        n+=1
    D.pop(0)
    return D

D=g(12000)
S=set()
#print(D)
for i in D:
    S.add(D[i])
    
print("#",sum(S))
