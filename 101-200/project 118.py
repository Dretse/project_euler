# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:31:53 2019

@author: admin
"""
import numpy as np
import itertools

def prime(n,L):
    if(n==1):return False
    for p in L:
        if(n%p==0):
            return False
        if(np.sqrt(n)<=p):
            return True
    return True

def Lp(n):
    L=[2]
    for p in range(1,n//2):
        if (prime(2*p+1,L)):L.append(2*p+1)
    return L

def permut(n,L):
    S=list(itertools.permutations(list(range(1,10))))
    Lp=[]
    
    for i in S:
        if(i[0] not in {2,4,6,8,5}):
            a=sum([i[x]*(10**x) for x in range(len(i)-(9-n))])
            if(prime(a,L)):
                Lp.append(a)
    return list(set(Lp))
  

L=Lp(10**5)
print("Lp done",len(L))
L2=[i for i in L if len(str(i))==len(set(str(i))) and ("0" not in str(i)) ]
print("tri done",len(L))

for n in range(5,9):
    X=permut(n,L)
    print(n,len(X))
    L2+=X

L2=list(set(L2))
print(len(L2))


def f(L,s={1,2,3,4,5,6,7,8,9},done={0},pmin=0):
    if(len(s)==0):return 1
    somme=0
    for x,p in enumerate(L[pmin:]):
        if(len(s)==9):
            print("\n\t",p,end="\t")
            if(p>10000):break
        if(len(s)==8 and p<1000):print('.',end="")
        good=True
        for i in str(p):
            if(int(i) not in s):
                good=False
                break
        if(good):
            a=set([i for i in s if str(i) not in str(p)])
            somme+=f(L,a,done.union({p}),x+pmin+1)
    return somme

print("\n\n\n")          
print(f(L2))
    
#44680
#1h30 pour fire tourner ça...
