from math import *

def f(n):
    L=str(n)
    s=0
    for i in L:
        s+=int(i)
        print(i)
    return s

A=2**1000

print(f(A))
