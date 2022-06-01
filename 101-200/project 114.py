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

def f(L,U):
    S=1
    for a in range(L-2):
        for b in range(a+3,L+1):
            if(L-b>3):
                S+=U[L-b-1]
            else: 
                #g(a,b,L)
                S+=1
    return S
#30 :1089155
U=[1,1,1,2]
for i in range(4,51):
    U.append(f(i,U))

print(U[-1])