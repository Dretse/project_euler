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


def Sum_diag(n):
    S=0
    for i in range(1,4):
        if(prime(n**2 - i*(n-1))):
            S+=1
            
    return S

def f():
    n=7
    S=8
    while(S/(2*n -1)>0.1):
        if((n-1)%1000==0):
            print(S/(2*n -1))
        n+=2
        S+=Sum_diag(n)
    return n


print(f())
