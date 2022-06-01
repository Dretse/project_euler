from math import *
import numpy as np

def prime(n):
    if(n==1):
        return False
    p=2
    while(p<=sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

def Lprime(digits=1):
    mini=digits-1
    maxi=digits
    L=[]
    i=10**mini + 1
    while(i<10**maxi):
        if(i%(10**(maxi-2))==0):
            print(i//(10**(maxi-2)))
        if(prime(i)):
            L.append(i)
        i+=1
    return L

def How_much(n,L):
    a=set(str(n))
    maxi=0
    for i in a:
        b=How_much_n(n,i,L)
        if b>maxi:
            maxi=b
    return maxi

def How_much_n(n,a,L):
    N=list((str(n)))
    Alph=set("0123465789")
    Total=0
    for x in Alph:
        s=""
        for i in range(len(N)):
            if(N[i]==a):
                s+=x
            else:
                s+=N[i]
        if(int(s) in L):
            Total+=1
    return Total
        
    
    
def f():
    L=Lprime(6)
    print("prime list done")
    Maxi=1
    n=1
    for i in L:
        if(Maxi==8):
            break
        a=How_much(i,L)
        if(a>Maxi):
            Maxi=a
            n=i
            print(Maxi,n)
    return(n,Maxi)
    
                
    
print(f())
