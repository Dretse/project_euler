# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:24:37 2019

@author: DZBZ0373
"""
import numpy as np

def R(k):
    return int("1"*k)

def prime(n):
    for p in range(2,int(np.sqrt(n))+1):
        if(n%p==0):return False
    return True

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

p=5
Sum=0
tot=0
while(tot<25):
    p+=1
    if(not(prime(p))):
        if((p-1)%A(p)==0):
            Sum+=p
            tot+=1
            print(tot,p,p-1,A(p))

print(Sum)



