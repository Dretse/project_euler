# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:28:31 2019

@author: DZBZ0373
"""
import numpy as np
def pgcd(a,b):
    while(a%b!=1):
        if(a%b==0):return b
        a,b=b,a%b
    return a%b

def Af(p,q):
    return((p*q)/(q**2 -p*q - p**2))
phi=(np.sqrt(5)-1)/2

#L=[2, 15, 104, 714, 4895, 33552, 229970, 1576239, 10803704, 74049690,507544127]
#q=28657
q=1
L=[]
pq=0.5
while(len(L)<14):
    q+=1
    for p in range(int(pq*q),int(phi*q)+1 ):
        if(pgcd(p,q)==1 and (p*q)%(q**2 -p*q - p**2)==0):
            pq=p/q
            #print(p,'/',q,"\t",pq,Af(p,q))
            
            L.append(int(Af(p,q)))
            
            q= int(q/0.383)
            break
            

print(L[-1])