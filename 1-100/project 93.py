# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:03:37 2019

@author: DZBZ0373
"""

def a_b_c_d():
    L=[]
    for a in range(4,10):
        for b in range(3,a):
            for c in range(2,b):
                for d in range(1,c):
                    L.append([a,b,c,d])
    return L

def op(x,y):
    L=[x+y,x*y,x-y,y-x]
    if(y!=0): L.append(x/y)
    if(x!=0): L.append(y/x)
    return set(L)

def f(L):
    S1=op(L[0],L[1])
    S2=set()
    for i in S1:
        S2=S2.union(op(i,L[2]))
        
    S3=set()
    for i in S2:
        S3=S3.union(op(i,L[3]))
        
    S4=set([int(i) for i in S3 if (i>0 and int(i)==i)])
    return S4
    
def g(comb):
    S=set()
    N={0,1,2,3}
    for i in N:
        for j in N-{i}:
            for k in N-{i,j}:
                l=6-i-j-k
                S=S.union(f([comb[i],comb[j],comb[k],comb[l]]))
    return S
    
def long(comb):
    S=list(g(comb))
    S.sort()
    for i in range(len(S)-1):
        if(S[i+1]-S[i]>1):
            return S[i]
L=a_b_c_d()

maxi=1
combi=[]
for i in L:
    n=long(i)
    if(n>maxi):
        combi=i
        maxi=n

print(combi[3],combi[2],combi[1],combi[0])
