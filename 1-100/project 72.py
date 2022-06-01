# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""
import numpy as np
def Lprime(n):
    L=[2]
    for i in range(3,n):
        p=True
        for prime in L:
             if(i%prime ==0):
                 p=False
                 break
        if(p) : L.append(i)
        if(n>1000 and i%10000==0): print(i//10000,end='% ')
    print()
    return L


def phi(n,Lp):
    tot=n
    i=0
    while(i<len(Lp) and Lp[i]<=n):
        if(n%Lp[i]==0):
            tot*=(1-1/Lp[i])
        i+=1
    return int(tot)

def mobius(n,Lp):
    i=0
    tot=0
    while(i<len(Lp) and Lp[i]<=n):
        if(n%(Lp[i]**2)==0):
            return 0
        if(n%Lp[i]==0):
            tot+=1
        i+=1
    if(tot%2==0):
        return 1
    else:
        return -1
    
def sum_phi(n,Lp):
    tot=1
    for k in range(1,n+1):
        tot+=(mobius(k,Lp)*(int(n/k)**2))
        if(k%10000==0): print(k//10000,end='% ')
    return int(tot/2)-1


maxi=1000000
Lp=Lprime(maxi+1)
print("prime compiled")
#print(sum_phi(maxi,Lp))

d=0
for i in range(2,maxi+1):
    d+=phi(i,Lp)
    if(i%1000==0): print(".",end="")
    if(i%10000==0):print(i//10000,"%")
print('\n',d)
