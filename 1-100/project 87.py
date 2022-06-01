# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:49:38 2019

@author: DZBZ0373
369
"""
import numpy as np

def Lp(n):
    L=[2]
    for i in range(3,n):
        p=True
        for j in L:
            if(i%j==0):
                p=False
                break
        if(p):
            L.append(i)
    return L

maxi=50000000
n1=int(np.sqrt(maxi))+1
n2=int(np.power(maxi,1/3))+1
n3=int(np.power(maxi,1/4))+1

L1=Lp(n1)
L2=Lp(n2)
L3=Lp(n3)

print(len(L1),len(L2),len(L3))

S=set()
for a in L1:
    for b in L2:
        for c in L3:
            d=a**2 + b**3 + c**4
            if(d<maxi): S.add(d)
            
print(len(S))