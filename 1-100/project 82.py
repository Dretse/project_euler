# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:12:33 2019

@author: DZBZ0373
"""
import numpy as np

with open("p082_matrix.txt") as f:
    L=np.array([i.strip('\n').split(',') for i in f.readlines()]).astype(int)
"""
M=L.copy()
n=len(L)
"""
M=np.array([[131,673,234,103,18],
            [201,96,342,965,150],
            [630,803,746,422,111],
            [537,69,497,121,956],
            [805,732,524,37,331]])
L=M.copy()
n=5



for j in range(n-2,-1,-1):
    for i in range(n):
        a=M[i,j+1]
        if(i!=0):
            b=min([M[k,j+1]+sum([L[m,j] for m in range(k,i)]) for k in range(0,i)])
        else:
            b=1000000000000
        if(i!=n-1):
            c=min([M[k,j+1]+sum([L[m,j] for m in range(i+1,k+1)]) for k in range(i+1,n)])
        else:
            c=10000000000000
        M[i,j]+=min([a,b,c])
print(np.min(M[:,0]))