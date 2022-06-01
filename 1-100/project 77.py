# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""
import numpy as np

def Lprime(n):
    L=[2]
    i=3
    while(i<n):
        prime=True
        for p in L:
            if(i%p==0):
                prime=False
                break
        if(prime):
            L.append(i)
        i+=1
    return L

target = 100
Lp=Lprime(target)
ways=np.zeros(target+1)
ways[0] = 1
 
for p in Lp:
    for val in range(p,target+1):
        ways[val] += ways[val-p]

for i in range(len(ways)):
    if(ways[i]>=5000):
        print(i,int(ways[i]))
        break

