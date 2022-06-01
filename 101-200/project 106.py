# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:48:44 2019

@author: DZBZ0373
"""

def subsets(S,m):
    S=list(S)
    n=len(S)
    L=[[] for i in range(2**n)]
    for el in range(n):
        for case in range(2**n):
            if(case%(2**(el+1))>=(2**(el))):
                L[case].append(S[el])
    return [i for i in L if len(i)==m]

def to_test(A,B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(len(A)):
        if(A[i]<B[i]):
            return True
    return False
    
    
def number(n):
    S=set([i for i in range(n)])
    Somme=0
    for m in range(2,n//2 +1):
        A=subsets(S,m)
        print(m)
        for As in A:
            B=subsets(S-set(As),m)
            for Bs in B:
                if(to_test(As,Bs) and to_test(Bs,As)): Somme+=1

    return Somme/2


print(int(number(12)))
