from math import *

def fact(n):
    if(n<=2):
        return n
    else:
        return (n*fact(n-1))

def f(n):
    S=0
    for i in str(n):
        S+=int(i)
    return S
print(f(fact(100)))
