# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:52:18 2019

@author: DZBZ0373
"""
import numpy as np

def prime(n):
    for p in range(2,int(np.sqrt(n))+1):
        if(n%p==0):return False
    return True

def PD(p):
    a,b=0,0
    if(prime((6*p)+1) and prime((6*p)-1) and prime(6*(2*p +1) -1)):a=3*p*(p-1) +2
    if(prime(6*(p+1) -1) and prime(6*p -1) and prime(6*(2*p -1) -1)):b=3*p*(p+1) +1
    return a,b

L=[0,0]
maxi=2000
p=2
while(len(L)<maxi):
    a,b=PD(p)
    if(a!=0):L.append(a)
    if(b!=0):L.append(b)
    p+=1

print(L[maxi-1])

#14516824220

                    
    
    