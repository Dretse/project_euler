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

    return n
def Lprime(n):
    L=[]
    i=1
    while(len(L)<n):
        if(prime(i)):
            L.append(i)
        i+=1
    return L


def is_fact(n,fact,L):
    compt=0
    for i in L:
        if(n%i==0):
            compt+=1
        if(compt==fact):
            return True
        if(i>n/2):
            return False

def f():
    L=Lprime(1000)
    fact=4
    n=10
    while(n<800000):
        if(n%8000==0):
            print("#",n//8000)

        if(is_fact(n,fact,L)):
            n+=1
            if(is_fact(n,fact,L)):
                n+=1
                if(is_fact(n,fact,L)):
                    n+=1
                    if(is_fact(n,fact,L)):
                        return n-3
        n+=1
    return "failed"
    
print(f())
