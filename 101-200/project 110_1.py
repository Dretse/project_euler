# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:57:02 2019

@author: admin
"""
import numpy as np
def prime(n,L):
    for i in L:
        if(n%i==0):
            return False
    return True

def Lprime(maxi):
    L=[2]
    for p in range(1,maxi//2):
        if(prime(2*p + 1,L)):L.append(2*p +1)
    return L

def num(n,L):
    S=[0]
    i=0
    while(L[i]<=n):
        if(n%L[i]==0):
            S[i]+=1
            n/=L[i]
        else:
            i+=1
            S.append(0)
    return np.prod([i+1 for i in S if i!=0])
        
Lp=Lprime(10)
obj=1000
S=[1]
S_=set(S)
for p in Lp:
    N=len(S)
    for j in range(N):
        i=1
        while(True):
            if(S[j]*(i+1)<=obj+10):
                S.append(S[j]*(i+1))
                S_.add(S[j]*(i+1))
            else:break
            i+=1
print(S_)

