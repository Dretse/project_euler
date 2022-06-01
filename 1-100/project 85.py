# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:49:38 2019

@author: DZBZ0373
"""

def n(N,M):
    S=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            S+=(N-i+1)*(M-j+1)
    return abs(S-2000000)

def s(N,M):
    S=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            S+=(N-i+1)*(M-j+1)
    return S

A=1
B=1
L=[]
for A in range(1,2000):
    if(A%200==0):
        print(A//200,end=' ')
    for B in range(1,A+1):
        sq=s(A,B)
        if(sq>2000000):
            break
    L.append(n(A,B-1))

A=L.index(min(L))+1
print("\nA :",A)
for B in range(1,A):
    if(n(A,B)==min(L)):
        print(A*B,A,B)
    
    