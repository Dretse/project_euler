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

def f():
    S=0
    for i in range(1,1001):
        S+=i**i
    a=str(S)
    return(a[-10:])
    
print(f())
