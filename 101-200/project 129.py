# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:24:37 2019

@author: DZBZ0373
"""
import numpy as np

def R(k):
    return int("1"*k)

def A(n):
    k=3
    while(R(k)%n!=0):
        if(k%10000==0):print(".",end="")
        k+=1
        if(k>n):print(k)
    return k

def prime(n):
    for p in range(2,int(np.sqrt(n))+1):
        if(n%p==0):return False
    return True

def A2(n):
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

n=1000001
An=0
while(An<1000000):
    n+=2
    if(n%5!=0):
        An=A2(n)
        #print(n,":",An)

print(n)



