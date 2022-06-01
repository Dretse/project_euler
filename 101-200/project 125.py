# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:46:29 2019

@author: DZBZ0373
"""
import numpy as np

def palindrom(n):
    n=str(n)
    for i in range(len(n)//2):
        if(n[i]!=n[len(n)-i-1]):return False
    return True
        

N=10**8
nmax=int(np.sqrt(N))//2
S=set()

for i in range(2,nmax+1):
    if(i%100==0):
        print(i//100,sum(S))
    n=i**2
    for j in range(i-1,0,-1):
        n+=j**2
        if(n<=N):
            if(palindrom(n)):
                S.add(n)

        
print(sum(S))