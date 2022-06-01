# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:37:58 2019

@author: DZBZ0373
"""

def rad(n):
    s=set()
    p=2
    while(n!=1):
        while(n%p==0):
            n/=p
            s.add(p)
        p+=1
    p=1
    for i in s: p*=i
    return p

L=[]
for i in range(1,100001):
    L.append((rad(i),i))
    if(i%1000==0):print(i//1000,end=" ")
print()
L.sort(key=lambda x:x[0])
print(L[9999][0])