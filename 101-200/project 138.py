# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:02:32 2019

@author: DZBZ0373
"""
import numpy as np

def pgcd(a,b):
    while(a%b!=1):
        if(a%b==0):return b
        a,b=b,a%b
    return a%b

S=[]
m=1
n=1
while(len(S)<12):
    m+=1
    #if(m%10000==0):print(m)
    if((n%2==0 or m%2==0) and pgcd(m,n)==1):
        x,y,L=m**2 - n**2,2*m*n, m**2 + n**2
        h,b=max(x,y),2*min(x,y)
        if(h==b+1 or h==b-1):
            print(h,b,L,)
            m,n=4*m,m
            S.append(L)
                
Sum=0
for i in S: Sum+=i
print(Sum)

