# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:12:33 2019

@author: DZBZ0373
"""
import numpy as np

with open("p081_matrix.txt") as f:
    L=np.array([i.strip('\n').split(',') for i in f.readlines()]).astype(int)

M=[[]]
for i in range(len(L)):
    for j in range(len(L)):
        if(len(M)<=i+j):
            M.append([L[i,j]])
        else:
            M[i+j].append(L[i,j])

for i in range(len(M)-2,len(M)//2-1,-1):
    for j in range(len(M[i])):
        if(j==0):
            M[i][j]+=M[i+1][j]
        elif(j==len(M[i])-1):
            M[i][j]+=M[i+1][j-1]
        else:
            M[i][j]+= min(M[i+1][j], M[i+1][j-1])

print('#')
for i in range(len(M)//2-1,-1,-1 ):
    for j in range(len(M[i])):
        M[i][j]+= min(M[i+1][j], M[i+1][j+1])


print(M[0][0])