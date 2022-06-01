from math import *
import numpy as np

def pan(n):
    N=len(str(n))
    s=set()
    for i in range(N):
        s.add(str(i+1))
    return (s==set(str(n)))

def prime(n):
    p=2
    while(p<=sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

def f():
    maxi=0
    for i in range(1000,10000000):
        if(pan(i) and prime(i)):
            if(i>maxi):
                maxi=i
    return maxi
            
    
    
        
        

print(f())
