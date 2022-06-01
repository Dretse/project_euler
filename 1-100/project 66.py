from math import *
import numpy as np
from decimal import *
getcontext().prec=600
#Decimal(n).sqrt()

def root(n,s=300):
    a=Decimal(n).sqrt()
    L=[int(a//1)]
    a=a%1
    Ldec=[a]
    while(len(L)<s and a!=0):
        a=1/a
        L.append(int(a//1))
        a=a%1
        if (str(a)[2:s] in Ldec):
            return L[:-1]
        Ldec.append(str(a)[2:s])
    return []

def frac(iF,L,i=1):
    if i==iF:
        return(1,L[iF])
    n,d=frac(iF,L,i+1)
    n,d=d,n+L[i]*d
    return(n,d)

def Nfrac(L):
    n,d=frac(len(L)-1,L)
    return(n+ L[0]*d,d)

def f():
    Xf=0
    Df=0
    for D in range(2,1001):
        if(sqrt(D)%1!=0.0):
            x,y=Sol(D)
            if(x>Xf):
                Xf=x
                Df=D
                print("X: ",Xf)

    return Df

def Sol(n):
    L=root(n)
    if(len(L)==0):
        print(n,"failed")
        return 0,0
    if(len(L)-1)%2==0:
        L=L[:-1]
    else:
        L.extend(L[1:-1])
    x,y=Nfrac(L)
    return (x,y)
    

    
print(f())
        
