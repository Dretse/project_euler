# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""
import numpy as np

def pgcd(a,b):
    if(b>a):
        return pgcd(b,a)
    if(a%b==0):
        return b
    return pgcd(b,a%b)
"""
def Lprime(n):
    L=[2]
    for i in range(3,n):
        p=True
        for prime in L:
             if(i%prime ==0):
                 p=False
                 break
        if(p) : L.append(i)
        if(n>1000 and i%10000==0): print(i//10000,end='% ')
    print()
    return L


def phi(n,Lp):
    tot=n
    i=0
    while(i<len(Lp) and Lp[i]<=n):
        if(n%Lp[i]==0):
            tot*=(1-1/Lp[i])
        i+=1
    return int(tot)

"""

maxi=12000

tot=0
for d in range(3,maxi+1):
    if(d%1000==0):
        print(d//1000,end='/12 ')
    for n in [i for i in range(int(d/3)+1,int(d/2)+1)]:
        if(pgcd(n,d)==1):
            tot+=1
print('\n',tot)
