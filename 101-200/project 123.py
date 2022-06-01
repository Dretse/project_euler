# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:25:21 2019

@author: DZBZ0373
"""

def prime(n,L):
    for p in L:
        if(n%p==0):return False
    return True

def Lp(n):
    L=[2]
    p=0
    while(len(L)<n):
        p+=1
        if(prime(2*p +1,L)):
            L.append(2*p+1)
    return L

def r(n,p):
    if(n%2==0):return 2
    else: return 2*n*p
    
L=[2]
r_=r(1,2)
p=0
while(r_<10**10):
    p+=1
    if(prime(2*p +1,L)):
        L.append(2*p+1)
        r_=r(len(L),2*p+1)
print(len(L))