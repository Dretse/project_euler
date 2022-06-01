from math import *
import numpy as np

def root(n):
    a=[0,1]
    for i in range(n):
        a=[a[1], a[1]*2 + a[0]]
    n=a[0]+a[1]
    d=a[1]
    return(len(str(n))>len(str(d)))

def rec(n):
    if(n==0):
        return [0,1]
    L=rec(n-1)
    return [L[1],2*L[1] + L[0]]


def f():
    s=0
    for i in range(1,1000):
        if(root(i)):
            s+=1
    return s

print(f())
