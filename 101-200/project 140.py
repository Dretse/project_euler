# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:53:13 2019

@author: DZBZ0373
"""

import numpy as np

def pgcd(a,b):
    while(a%b!=1):
        if(a%b==0):return b
        a,b=b,a%b
    return a%b

def Af(p,q):
    return int((p*q + 3*(p**2))/(q**2 -p*q - p**2))
    
phi=(np.sqrt(5)-1)/2

#L=[2, 15, 104, 714, 4895, 33552, 229970, 1576239, 10803704, 74049690,507544127]
#q=28657
q=1

L=[]
Qs=[]
pq=0.4
while(len(L)<30):
    q+=1
    for p in range(int(q*pq),int(q*phi)+1 ):
        if(pgcd(p,q)==1 and (p*q + 3*(p**2))%(q**2 -p*q - p**2)==0 and Af(p,q)>0):
            pq=p/q
            Qs.append(q)
            #print(len(L)+1,p,'/',q,"\t",p/q,Af(p,q))
            
            L.append(int(Af(p,q)))
            if(len(Qs)>4):q=int(Qs[-2]*Qs[-2]/Qs[-4])-1
            #break
    
L.sort()
#print(L[19])
print(np.sum(L[:30]))
