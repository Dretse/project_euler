# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:03:32 2019

@author: admin
"""

file=open("p105_sets.txt")
L=file.readlines()
file.close()
L=[[int(j) for j in i.strip().split(',')] for i in L]
def subsets(S):
    L=[[] for _ in range(2**len(S))]
    for ind,el in enumerate(list(S)):
        for n in range(len(L)):
            if((n//(2**(ind)))%2==0):
                L[n].append(el)
    return L[:-1]

def verif(As,Bs):
    if(sum(As)==sum(Bs)):return False
    if(len(As)>len(Bs) and sum(As)<sum(Bs)):return False
    if(len(As)<len(Bs) and sum(As)>sum(Bs)):return False
    return True

def couples(S):
    S=set(S)
    LA=subsets(S)[1:]
    for A in LA:
        As=set(A)
        LB=subsets(S-As)
        for B in LB:
            if(not(verif(As,set(B)))):return False
    return True

S=0
for i in L:
    if(couples(i)):
        S+=sum(i)

print(S)