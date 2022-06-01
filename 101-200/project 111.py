# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:24:57 2019

@author: DZBZ0373
"""
import numpy as np
from copy import copy

def prime(p,L):
    for i in L:
        if(i>=p):return True
        if(p%i==0):return False
    return True

def Lprime(n):
    L=[2]
    p=1
    while(2*p+1<=n):
        if(prime(2*p+1,L)):L.append(2*p +1)
        p+=1
    return L



def S_n(n):
    Lp=[i for i in Lprime(10**(n/2))]
    print("L done (len =",len(Lp),")")
    S=0
    for d in range(10):
        S+=S_nd(Lp,d,n)
    return S

def S_nd(Lp,d,n):
    L=[]
    i=n-1
    while(len(L)==0):
        L=Combi_d(Lp,d,i,n,[])
        i=i-1
    print(i+1,len(L))
    return sum(L)
        
def Combi_d(L,d,n,long,A):
    """ L liste des nombres premiers
    d chiffre à placer
    n nombre de chiffre à placer
    long la longueur totale
    A le chiffre en question """
    howmuch=len([ i for i in A if i==d])
    if(howmuch==n):
        while(len(A)!=long):
            A.append(-1)
        return Combi_nond(L,d,copy(A))
    elif(len(A)>=long):return []
    else:
        A.append(d)
        LA=Combi_d(L,d,n,long,copy(A))
        B=copy(A)
        B[-1]=-1
        LB=Combi_d(L,d,n,long,copy(B))
        return LA+LB

def Combi_nond(L,d,C):
    if(not(-1 in C)):
        N=int(sum([C[i]*(10**i) for i in range(len(C)) ]))
        if(prime(N,L) and N>=10**(len(C)-1)): 
            return [N]

    
    else:
        j=C.index(-1)
        L_=[]
        mini=1 if j==len(C)-1 else 0
        for i in range(mini,10):
            if(i!=d):
                A=copy(C)
                A[j]=i
                L_+=Combi_nond(L,d,copy(A))
        return L_
    return []

Lp=Lprime(10000)
print(S_n(10))



