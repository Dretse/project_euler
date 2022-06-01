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

def C(n,r):
    return(int(fact(r+1,n)/fact(1,n-r)))
def fact(a,b):
    if(b==a):
        return b
    else:
        return (b*fact(a,b-1))

def f():
    S=0
    for n in range(1,101):
        for r in range(1,n):
            if(C(n,r)>1000000):
                S+=1
    return S
                
    
print(f())
