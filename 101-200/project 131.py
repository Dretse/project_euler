# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:36:24 2019

@author: DZBZ0373
"""
import numpy as np
def prime(n,L):
    for p in L:
        if(n%p==0):return False
    return True

def Lprime(n):
    L=[2]
    for p in range(1,n//2):
        if(prime(2*p+1,L)):L.append(2*p+1)
    return L

def cube(n,p):
    a=n**3 + n*n*p
    b=np.power(a,1/3)
    if(b%1>0.99):return (int(b+1)**3==a)
    elif(b%1<0.01):return(int(b)**3==a)
    return False

"""
Lp=Lprime(100)
m=0
print("Lprime Done",len(Lp))
for p in range(1,len( Lp)):
    for n in range(1,2*Lp[p]):
        if(cube(n,Lp[p])):
            print(Lp[p],n,n**3 + n**2 *Lp[p])
            break"""

Lp=Lprime(1000000)
print("Lprime Done",len(Lp))
sum_=0
for b in range(1,600):
    n=b**3
    #print("\n",b,end=" ")
    for p in Lp:
        if(cube(n,p)):
            #print(p,n,n**3 + n**2 *p,end=" ")
            sum_+=1
            print(sum_,b,p)
            break
        
print("\n\nsum =",sum_)
        
        
