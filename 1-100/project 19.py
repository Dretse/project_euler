from math import *

def f():
    L=[1,1,1900,0]
    S=0
    while(L[0]!=1 or L[1]!=1 or L[2]!=2001):
        L=next(L)
        if(L[2]!=1900 and L[3]==6 and L[0]==1):
            S+=1
            print(L)
    return S

def next(L):
    M=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(L[2]%4==0):
        M[1]=29
        
    L[0]+=1
    
    L[3]=(L[3]+1)%7
    
    if(L[0]>M[L[1]-1]):
        L[1]+=1
        L[0]=1
        if(L[1]==13):
            L[1]=1
            L[2]+=1
    return L


        
print(f())
