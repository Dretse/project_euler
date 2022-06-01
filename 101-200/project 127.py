# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:52:57 2019

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

def List_cs(Lp,maxi):
    N=[set() for _ in range(maxi)]
    for i in range(1,maxi):
        if i%12000==0:print(".",end=" ")
        a=i
        for p in Lp:
            if(a%p==0):
                N[i].add(p)
                while(a%p==0):a/=p
    print()
    return N
            
def List_rad(Lp,maxi):
    N=[1 for _ in range(maxi)]
    for i in range(1,maxi):
        if i%12000==0:print(".",end=" ")
        a=i
        for p in Lp:
            if(a%p==0):
                N[i]*=p
                while(a%p==0):a/=p
            if(a==1):break
        if(a!=1): 
            print(a,i)
            N[i]*=a
    print()
    return N

def pgcd(a,b):
    if(a%b==0):return b
    while(b!=1 and a%b!=0):
        a,b=b,a%b
    return b
#    sum = 11656638828012 ????
#New sum = 22673775675747 ??!?
#New sum =

Sum=0
s=0
#c >= 77000
maxi=120000
Lp=Lprime(maxi)
print("\nLp done, len =",len(Lp))
N=List_rad(Lp,maxi)
print("N done, len = ",len(N))

Nc=[(i,N[i]) for i in range(2,len(N)) if N[i]!=i]
print("len Nc without voids and simple factors numbers:",len(Nc))


Nf=[]
for c,rc in Nc:
    if(c%50==0):print(".",end="")
    if(c%1000==0):
        print(c//1000,"\t",sum(Nf),"\t",len(Nf))
    Nf+=[c for a,ra in enumerate(N[:c//2 + c%2]) if (a!=0 and (a==1 or pgcd(c-a,a)==1) and ra*rc*N[c-a]<c)]


    
print("###",sum(Nf),"###")
#print("\nSolution :",sum(Nf),len(Nf))











