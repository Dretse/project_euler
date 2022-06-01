from math import *
import numpy as np

def prime(n):
    p=2
    while(p<=sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

    return n
def decomp(A):
    n=1
    while(True):
        if(2*(n**2)>=A-1):
            return False
        if(prime(A-2*(n**2))):
            return True
        n+=1
def f():
    n=5
    while(decomp(n) or prime(n)):
        n+=2
    print("that's :",end="")
    return (n)
# c'est loooooooooooong
print(f())
