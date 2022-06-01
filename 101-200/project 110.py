# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:01:16 2019

@author: DZBZ0373
"""
import numpy as np

def prime(p,L):
    for i in L:
        if(p%i==0):return False
    return True

def Lprime(n):
    L=[2]
    p=1
    while(2*p+1<=n):
        if(prime(2*p+1,L)):L.append(2*p +1)
        p+=1
    return L
def Lprime_(l):
    L=[2]
    p=1
    while(len(L)<l):
        if(prime(2*p+1,L)):L.append(2*p +1)
        p+=1
    return L
    
def diviseurs_premiers(x):
    L=[]
    Lp=Lprime(np.sqrt(x))
    for p in Lp:
        L.append(0)
        while(x%p==0):
            L[-1]+=1
            x/=p
        if(x==1):break
    return L,Lp[:len(L)]

def diviseurs(x):
    L=[]
    Ld=[]
    i=3
    while(x!=1):
        if(x%i==0):
            L.append(0)
            Ld.append(i)
            while(x%i==0):
                L[-1]+=1
                x/=i
        else: i+=1
    return L,Ld

def find_n(p):
    D=2*p -1
    N,div=diviseurs(D)
    div=[int((i-1)/2) for i in div]
    
    L=[]
    for i,v in enumerate(N):
        for _ in range(v):
            L.append(div[i])
    L.sort(reverse=True)
    
    Lp=Lprime_(len(L))
    n=1
    for i in range(len(L)):
        n*=Lp[i]**L[i]
    return n

def find_p(n):
    d,_=diviseurs_premiers(n)
    p=1
    for i in d:
        p*=(2*i +1)

    return int((p+1) /2)
"""
p=4000000
min_n=find_n(p)
while(True):
    p+=1
    print(p)
    n=find_n(p)
    if(n<min_n):
        min_n=n
        #print(p,n)
"""
print(find_n(4018613))