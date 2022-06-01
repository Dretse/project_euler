from math import *

def f():
    n=1
    a=1
    while(n<10001):
        a=a+1
        if(is_prime(a)):
            n=n+1
            print(str(n) + " : "+ str(a))
                

    return a

def is_prime(n):
    p=1
    while (p<sqrt(n)):
        p=p+1
        if(n%p==0):
            return False
    return True

print(f())
    
