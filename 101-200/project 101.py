# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:51:21 2019

@author: admin
"""

import numpy as np

def Seq(L):
    n=len(L)
    M=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            M[i,j]=(i+1)**(j)
    M_=np.linalg.inv(M)
    
    return np.dot(M_,np.array(L))

def f(n):
    return sum([(-n)**i for i in range(11)])

def FIT(n,f):
    L=Seq([f(i) for i in range(1,n+1)])
    return np.rint(sum([L[i]*((n+1)**i) for i in range(n)]))
#print(FIT(4,f))
print(int(sum([FIT(i,f) for i in range(1,11)])))