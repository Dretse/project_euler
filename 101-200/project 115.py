# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:52:58 2019

@author: DZBZ0373
"""

L=7
def g(a,b,L):
    for _ in range(a):
        print("_ ",end="")
    for _ in range(b-a):
        print("# ",end="")
    for _ in range(L-b):
        print("_ ",end="")
    print()

def f(L,U,m=3):
    S=1
    for a in range(L-m+1):
        for b in range(a+m,L+1):
            if(L-b>m):
                S+=U[L-b-1]
            else: 
                #g(a,b,L)
                S+=1
    return S
#30 :1089155
m=10
n=m
U=[1]*m
while(True):
    U.append(f(n,U,m))
    n+=1
    if(U[-1]>1000000):break

print(n-1)