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

def is_perm(n):
    for i in range(2,7):
        if(not perm(n,i*n)):
            return False
    return True

def perm(n,m):
    a=list(str(n))
    a.sort()
    b=list(str(m))
    b.sort()
    for i in range(len(a)):
        if(a[i]!=b[i]):
            return False
    return True

def f():
    a=5000
    while(not is_perm(a)):
        a+=1
        if(log(a,10)%1==0):
            print(a)
    return a
    
                
    
print(f())
