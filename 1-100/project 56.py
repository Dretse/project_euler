from math import *
import numpy as np

def sum(a,b):
    s=str(a**b)
    n=0
    for i in s:
        n+=int(i)
    return n

def f():
    maxi=0
    for a in range(90,100):
        for b in range(90,100):
            s=sum(a,b)
            if(s>maxi):
                maxi=s
    return maxi
print(f())
