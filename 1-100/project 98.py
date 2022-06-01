# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:52:41 2019

@author: admin
"""
import numpy as np

file=open("p098_words.txt")
L=file.readlines()[0].strip('"')
L=L.split('","')
file.close()

def Anagramme(A,B):
    if (len(A)!=len(B)): return False
    if (set(list(A))!=set(list(B))): return False 
    S=set(list(A))
    for i in S:
        na,nb=0,0
        for a in A:
            if(a==i):
                na+=1
        for b in B:
            if(b==i):
                nb+=1
        if(nb!=na): return False
    return True
    
Anagrams=[]
for i in range(1,len(L)):
    for j in range(i):
        if(Anagramme(L[i],L[j])):
            Anagrams.append([L[i],L[j]])


def Square(A,B):
    L=[i**2 for i in range(int(np.sqrt(10**(len(A)-1))),int(np.sqrt(10**(len(A))))+1) 
    if(len(set(list(str(i**2))))==len(set(list(A))))]
    
    for chiffre in L:
        n=""
        C=str(chiffre)
        for i in range(len(A)):
            n+=C[list(A).index(B[i])]
        n=int(n)
        if(n in L):
            return max(n,chiffre)
    return (0)

maxi=0

for i in Anagrams:
    N=Square(i[0],i[1])
    if(N>maxi):
        maxi=N
print(maxi)
   
    
            
print(len(Anagrams))