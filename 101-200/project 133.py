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
    return L

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

def Ok(k):
    while(k%5==0):k=k//5
    while(k%2==0):k=k//2
    return k!=1


#453647705

Lp=Lprime(100000)
print("Lp done, last number =",Lp[-1],"\n")
Tot=10**16
Sum=0
for p in Lp[3:]:
    k=A(p)
    if(not(Ok(k))):
        Sum+=p
        print(p,'\t',k,"\t",Sum)

print(np.sum(Lp)-Sum)