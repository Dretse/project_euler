from math import *

def f():
    S=0
    for i in range(10):
        if(is_prime(i)):
            S+=i
            print(i)
    return S+1

def is_prime(n):
    p=1
    while (p<=sqrt(n)):
        p=p+1
        if(n%p==0):
            return False
    return True
    
print(f())
    
