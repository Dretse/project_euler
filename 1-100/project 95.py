# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:08:56 2019

@author: DZBZ0373
"""
import numpy as np

def divisors(n):
    if(n==1): return [1]
    L=[1]
    for i in range(2,int(np.sqrt(n))+1):
        if(n%i==0):
            L.append(i)
            L.append(n//i)
            
    return set(L)



def amicable(n,S):
    if(n in S):
        return [],S
    L=[n]
    a=1
    while(n<1000000):
        n=sum(divisors(n))
        
        if(n==L[0]):
            S=S.union(set(L))
            return L,S
        
        if(n in S):
            L.append(n)
            S=S.union(set(L))
            return [],S
        
        if(n in L):
            ind=L.index(n)
            S=S.union(set(L))
            return L[ind:],S
        
        
        
        L.append(n)


    L.append(n)
    S=S.union(set(L))
    return [],S


maxi=10000
L_general=[]
S=set()
maxL=[1]
for n in range(2,maxi):
    L,S=amicable(n,S)
    if(len(L)!=0):
        #print("\t",n,len(L))
        L_general.append(L)
        
        if(len(L)>len(maxL)):
            maxL=L


print("\n",min(maxL))



