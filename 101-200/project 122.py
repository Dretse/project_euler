# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:39:18 2019

@author: DZBZ0373
"""
import numpy as np
from itertools import permutations

def In(i,L):
    for j in L:
        if i in j:return True
    return False

def m(k,L,Ls,v=False):
    M=[]
    Sum=[]
    for i in range(1,k//2 +1):
        j=k-i
        if(i==j or In(i,Ls[j])):M.append(L[j]+1)
        else: M.append(L[i]+L[j]+1)
        
        if(i==j or In(i,Ls[j])):
            A=[]
            for x in Ls[j]:
                if(i in x):
                    A.append(x+[k])
            Sum.append(A)
            if(v):print("-",i,j,M[-1],A)
        else:
            A=[]
            for x in Ls[i]:
                for y in Ls[j]:
                    A.append(list(set(x+y+[k])))
            Sum.append(A)
            if(v):print("+",i,j,M[-1],A)
    m=min(M)
    Sum=[Sum[i] for i in range(len(Sum)) if(M[i]==m)]
    if(v):print(m,Sum)
    u=[]
    for i in Sum:
        if(type(i)==type(list())):
            for j in i:
                u.append(j)
        else:
            u.append(i)
    if(v):print("u",u)
    return m,u
    
    
              
L=[0,0,1,2]
Ls=[[],[[1]],[[1,2]],[[1,2,3]]]
for k in range(4,201):
    m_,u=m(k,L,Ls)
    #print("#",k,":",m_,"\t",u)
    print(k)
    L.append(m_)
    Ls.append(u)

print(sum(L))









