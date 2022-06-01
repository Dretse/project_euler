# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:10:21 2019

@author: DZBZ0373
"""

import numpy as np

def N(x,a):
    return 2*x*a + 3*(x**2) - a**2

maxi=(5*(10**7))
List_N=np.zeros(maxi)
mina=1
fact=1
for x in range(1,maxi):
    if(x<5000):mina=1
    else:mina=int(fact*x)
    
    
    if(x%1000==0 and x<100000):print(".",end="")
    if(x%10000==0 and x<500000):print(x//10000,mina,end="_")
    elif(x%10000==0):print(x/500000,end="\t")
    
    over=False
    for a in range(mina,3*x +1):
        n=N(x,a)
        if(n<1):
            if(x%10000==0):print(a)
            break
        if(n<maxi):
            List_N[n]+=1
            if(over):
                over=False
                if(x%100000==0 and x<500000):
                    print(a,end="_")
                if(x%100==0 and x>5000):fact=a/x
        elif(not over):
            over=True
            if(x%10000==0 and x<500000):print(a,end="-")

            

#2544559

            
print() 

A=0
for i in List_N:
    if i==1:A+=1
print(A)