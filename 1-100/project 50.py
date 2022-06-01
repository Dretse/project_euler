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

def Lprime(maxi=1000000):
    L=[]
    i=2
    while(i<maxi):
        if(i%10000==0):
            print(i/10000)
        if(prime(i)):
            L.append(i)
        i+=1
    return L

def cons(n,L,maxi=1000000):
    S=L[n]
    count=1
    
    while(S<maxi):
        n+=1
        S+=L[n]
        count+=1
    S-=L[n]
    count-=1
    while(not S in L):
        n-=1
        S-=L[n]
        count-=1
    return(count,S) 

    
def f():
    L=Lprime()
    print("prime list done")
    Maxi=1
    c=0
    for i in range(len(L)//50):
        if(i==10):
            break
        A,b=cons(i,L)
        if(A>Maxi):
            Maxi=A
            c=b
    return c
    
                
    
print(f())
