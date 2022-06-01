# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:01:22 2019

@author: DZBZ0373
"""

import numpy as np

def pgcd(a,b):
    while(a%b!=1):
        if(a%b==0):return b
        a,b=b,a%b
    return a%b

S=0
m=1
n=1
P=3+4+5
while(P<100000000):
    m+=1
    if((n%2==0 or m%2==0) and pgcd(m,n)==1):
        a,b,c=m**2 - n**2,2*m*n, m**2 + n**2
        if(c%(max(a,b)-min(a,b))==0):
            print(S+1,a,b,c,'\t\t',m,n)
            m,n=2*m,m
            P=a+b+c
            S+=10**8//P
print(S)

