# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:09:00 2019

@author: DZBZ0373
"""
import numpy as np
from time import time
def prime(n,L):
    for p in L:
        if(n%p==0):return False
        if(p>np.sqrt(n)):return True
    return True

def Lprime(n):
    L=[2]
    for p in range(1,n//2):
        if(p%10000==0):print('.',end="")
        if(prime(2*p+1,L)):L.append(2*p+1)
    print()
    return L

def S(p1,p2):
    a=int(np.log(p1)/np.log(10))+1
    b=10**a
    n=p1+b
    while(n%p2!=0):
        n+=b
    return n
        

#Lp=Lprime(1000010)
start=time()
t=start
print("Lp done, last numbers =",Lp[-5:],len(Lp),"\n")
Sum=0
for p in range(2,len(Lp)-1):
    if(p%1000==0):print(".",end="")
    if(p%10000==0):
        print(Sum,p//700,"%")
        t=time()
    Sum+=S(Lp[p],Lp[p+1])
print("\n\n",Sum)
