# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:17:53 2019

@author: DZBZ0373
"""
import numpy as np
file=open("p107_network.txt")
M_=file.readlines()
"""
M_=["-,16,12,21,-,-,-",
"16,-,-,17,20,-,-",
"12,-,-,28,-,31,-",
"21,17,28,-,18,19,23",
"-,20,-,18,-,-,11",
"-,-,31,19,-,-,27",
"-,-,-,23,11,27,-"]"""
file.close()
N=len(M_)
M=np.zeros((N,N))
for x in range(N):
    L_=M_[x].strip().split(',')
    for y in range(N):
        if(L_[y]!='-'):
            M[x,y]=int(L_[y])
            
            
            
print(M)
S0=np.sum(M)/2

N_=[[M[x,y] if(x>y) else 0 for x in range(len(M))]for y in range(len(M))]
G=[]
for x in range(len(M)):
    for y in range(len(M)):
        if(N_[x][y]>0): G.append((x,y,int(M[x,y])))

def In(i,L):
    for s in L:
        if i in s:
            return True
    return False

def Boruvka(G):
    F=set()
    
    #DUOS
    for i in range(N):
        mini=(0,0,10000)
        for arc in G:
            if((i==arc[0] or i==arc[1]) and arc[2]<mini[2]):
                mini=arc
        F.add(mini)
    #RASSEMBLEMENTS
    L=[]
    for i in F:
        done=False
        if(In(i[0],L) and In(i[1],L)):
            for x in range(len(L)):
                for y in range(x):
                    if(x!=y and ((i[0] in L[x] and i[1] in L[y])or(i[1] in L[x] and i[0] in L[y]))):
                        s=L.pop(x)
                        for j in s:
                            L[y].add(j)
                        done=True
                    if(done):break
                if(done):break
        elif(In(i[0],L) or In(i[1],L)):
            for j in L:
                if(i[0] in j):j.add(i[1])
                elif(i[1] in j):j.add(i[0])
        else:
            L.append({i[0],i[1]})
    #LIAISONS
    while(len(L)>1):
        print(L,len(L))
        
        mini_A,min_B,min_val=0,0,100000
        min_x,min_y=0,0
        for ind1,S1 in enumerate(L):
            for ind2,S2 in enumerate(L):
                if(ind1>ind2):
                    for x in S1:
                        for y in S2:
                            for arc in G:
                                if(arc not in F and ((arc[0]==x and arc[1]==y)or(arc[0]==y and arc[1]==x)) and arc[2]<min_val):
                                    mini_A,min_B,min_val=arc
                                    min_x,min_y=ind1,ind2
                        
        F.add((mini_A,min_B,min_val))
        S=L.pop(min_x)
        for i in S:
            L[min_y].add(i)
        
    return F

S0=np.sum(M)/2
F=Boruvka(G)
print(F,len(F))
S=sum([i[2] for i in F])
print(S0,S,S0-S)