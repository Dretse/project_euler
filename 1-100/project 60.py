from math import *
import numpy as np

def prime(n):
    p=2
    if (n==1 or n==5):
        return False
    while p<=sqrt(n):
        if(n%p==0):
            return False
        p+=1
    return True

def Lprime(n):
    L=[]
    i=1
    while(i<n):
        if((i-1)%10000==0):
            print(i/int(n/100))
        i+=2
        if(prime(i)):
            L.append(i)
    return L

def PairPrime(a,b):
    return(prime(int(str(a)+str(b))) and prime(int(str(b)+str(a))))

def f():
    L=Lprime(10000)
    N=len(L)
    print("total = ",L[-1])
    print("len= ",len(L))
    for a in range(N -4):
        print("### ",int(a/(N-4))," ###")
        for b in range(a,N -3):
            if(PairPrime(L[a],L[b])):
                for c in range(b,N -2):
                    if(c!=a and c!= b and PairPrime(L[a],L[c]) and PairPrime(L[b],L[c])):
                        for d in range(c,N -1):
                            if(d!=a and d !=b and d!=c and PairPrime(L[a],L[d]) and PairPrime(L[b],L[d]) and PairPrime(L[d],L[c])):
                                for e in range(d,N):
                                    if(e!=a and e!=b and e!=c and e!=d and PairPrime(L[a],L[e]) and PairPrime(L[b],L[e]) and PairPrime(L[c],L[e]) and PairPrime(L[d],L[e])):
                                        return (L[a]+L[b]+L[c]+L[d]+L[e])
                        
                        
    return  "none"



print(f())
