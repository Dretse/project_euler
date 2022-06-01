from math import *

def f(n):
    p=1
    s=2
    while (p<sqrt(n)):
        p=p+1
        if(n%p==0):
            if(is_prime(p)):
                s=p

    return s
def is_prime(n):
    prime=True
    p=2
    while (p<sqrt(n)):
        p=p+1
        if(n%p==0):
            prime=False
    return prime
    
print(f(600851475143 ))
