# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:38:19 2019

@author: admin
"""
import numpy as np
def subsets(S):
    L=[[] for _ in range(2**len(S))]
    for ind,el in enumerate(list(S)):
        for n in range(len(L)):
            if((n//(2**(ind)))%2==0):
                L[n].append(el)
    return L[:-1]

def verif(As,Bs):
    if(sum(As)==sum(Bs)):return False
    if(len(As)>len(Bs) and sum(As)<sum(Bs)):return False
    if(len(As)<len(Bs) and sum(As)>sum(Bs)):return False
    return True

def couples(S):
    S=set(S)
    LA=subsets(S)[1:]
    for A in LA:
        As=set(A)
        LB=subsets(S-As)
        for B in LB:
            if(not(verif(As,set(B)))):return False
    return True

def min_set(n):
    if(n==1): return [1]
    L=max_set(n-1)
    return(L+[L[-1]+1])

def max_set(n):
    A=[1]
    for i in range(1,n):
        if(len(A)%2==1): b=A[len(A)//2]
        else: b=A[len(A)//2]
        B=[b]
        for j in range(i):
            B.append(A[j]+b)
        A=B
    return A


    

def find_sets(n):
    
    minS,maxS=min_set(n),max_set(n)
    if(couples(minS)):return minS
    
    minS=[i-4 for i in maxS]
    L=[minS]
    for N in range(sum(minS),sum(maxS)):
        print(N,len(L))
        NL=[]
        for i in L:
            for j in range(len(i)-1):
                if(j<len(i)+1 and i[j+1]>i[j]+1):
                    a=np.copy(i)
                    a[j]+=1
                    if(couples(a)):return a
                    if(not(list(a) in NL)): NL.append(list(a))
            if(i[-1]<sum(maxS)//2):
                j=len(i)-1
                a=np.copy(i)
                a[j]+=1
                if(couples(a)):return a
                if(not(list(a) in NL)): NL.append(list(a))
                    
        L=NL
    print("End")
    return maxS
S=(find_sets(7))
print(S)
for i in S:
    print(str(i),end="")
# {11, 18, 19, 20, 22, 25}


