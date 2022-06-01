# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:59:02 2019

@author: DZBZ0373
"""

L1=[1]
L89=[89]

def next_(n):
    while(n!=1 and n!=89):
        n=sum([int(i)**2 for i in str(n)])
    return n==89

def perm(L):
    S=[0,0,0,0,0,0,0,0,0,0]
    for i in L:
        S[i]+=1
    p=5040
    for i in S:
        p/=fact[i]
    return p
fact=[1,1,2,6,24,120,720,5040]
    
S=0 

for a in range(1,10):
    for b in range(a+1):
        for c in range(b+1):
            for d in range(c+1):
                for e in range(d+1):
                    for f in range(e+1):
                        for g in range(f+1):
                            n=int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
                            L=[a,b,c,d,e,f,g]
                            if(next_(n)):
                                S+=perm(L)
        

print(S)
