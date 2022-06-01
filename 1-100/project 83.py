# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:12:33 2019

@author: DZBZ0373
"""
import numpy as np

with open("p082_matrix.txt") as f:
    L=np.array([i.strip('\n').split(',') for i in f.readlines()]).astype(int)

M=L.copy()
n=len(L)
"""
M=np.array([[131,673,234,103,18],
            [201,96,342,965,150],
            [630,803,746,422,111],
            [537,699,497,121,956],
            [805,732,524,37,331]])
L=M.copy()
n=5
"""
G=np.zeros((n,n))+np.float('Inf')
V=np.zeros((n,n))
V[0,0]=1
G[0,0]=M[0,0]
i,j=0,0
Dist=0
#Dijkstra
while (i!=n-1 or j!=n-1):
    #Actualiser voisins
    if(i!=0):
        if(G[i-1,j]>G[i,j]+M[i-1,j]):
            G[i-1,j]=G[i,j]+M[i-1,j]
    if(i!=n-1):
        if(G[i+1,j]>G[i,j]+M[i+1,j]):
            G[i+1,j]=G[i,j]+M[i+1,j]
    if(j!=0):
        if(G[i,j-1]>G[i,j]+M[i,j-1]):
            G[i,j-1]=G[i,j]+M[i,j-1]
    if(j!=n-1):
        if(G[i,j+1]>G[i,j]+M[i,j+1]):
            G[i,j+1]=G[i,j]+M[i,j+1]
    
    #bouger de point
    mini,minj=n-1,n-1
    for a in range(n):
        for b in range(n):
            if(V[a,b]==0 and G[a,b]<G[mini,minj]):
                mini,minj=a,b
    V[mini,minj]=1
    i,j=mini,minj
    if(Dist<max(i,j)):
        Dist=max(i,j)
        print(Dist,end='\t')


print(int(G[n-1,n-1]))

    
        
