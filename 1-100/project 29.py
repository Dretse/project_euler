from math import *
import numpy as np

def f(n):
    S=set()
    for a in range(2,n+1):
        for b in range(2,n+1):
            S.add(a**b)
    return(len(list(S)))
    

print(f(100))
