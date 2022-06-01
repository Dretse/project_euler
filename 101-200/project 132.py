# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:09:00 2019

@author: DZBZ0373
"""
import numpy as np
def prime(n,L):
    for p in L:
        if(n%p==0):return False
    return True

def Lprime(n):
    L=[2]
    for p in range(1,n//2):
        if(prime(2*p+1,L)):L.append(2*p+1)
    return L[3:]

def A(n):
    k=1
    r=1
    while(r!=0 and k<n):
        #print(r,k)
        r=r%n
        if(r==0):break
        while(r<n):
            k+=1
            r=r*10 +1
       
    return k

Lp=Lprime(200000)
print("Lp done, last number =",Lp[-1],"\n")
Tot=10**9
L_sol=[]
for p in Lp:
    k=A(p)
    if(Tot%k==0):
        L_sol.append(p)
        print(p,k,"\t",len(L_sol))
    if(len(L_sol)==40):break

print(np.sum(L_sol))

#843296