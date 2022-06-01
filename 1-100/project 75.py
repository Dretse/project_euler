# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""
from numpy import sqrt
def pgcd(a,b):
    if(b>a):
        return pgcd(b,a)
    if(a%b==0):
        return b
    return pgcd(b,a%b)

maxi= 1500000
maximum=int(sqrt(maxi/2))
D=dict()
for m in range(2,maximum):

    for n in range(1,m):
        if(not(m%2==1 and n%2==1) and pgcd(m,n)==1):
            L=2*m*(n+m)
            a=1
            while(a*L<=maxi):
                if(D.get(a*L)==None):
                    D[a*L]=1
                else:
                    D[a*L]+=1
                a+=1

tot=0
for i in D:
    if(D[i]==1):
        tot+=1


print('\n',tot)