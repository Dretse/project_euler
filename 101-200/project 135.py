# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:48:43 2019

@author: DZBZ0373
"""
import numpy as np

def N(x,a):
    return 2*x*a + 3*(x**2) - a**2

      
List_N=np.zeros(10**6)

for x in range(1,1000000):
    if(x%10000==0):print(".",end="")
    if(x<1000):mina=1
    elif(x<2000):mina=int(2.7*x)
    elif(x<5000):mina=int(2.9*x)
    elif(x<16000):mina=int(2.99*x)
    elif(x<50000):mina=int(2.999*x)
    elif(x<126000):mina=int(2.9999*x)
    else: mina=int(2.99999*x)
    for a in range(mina,3*x +1):
        n=N(x,a)
        if(n<1):
            break
        if(n<10**6):
            List_N[n]+=1

            



            
print() 

A=[(n,num) for (n,num) in enumerate(List_N) if num==10]
print(len(A))
    