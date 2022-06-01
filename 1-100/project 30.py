from math import *
import numpy as np

def f():
    S=0
    for i in range(10,300000):
        if(sum(i)==i):
            S+=i
    return S
    
def sum(n):
    S=0
    for i in str(n):
        S+=int(i)**5
    return S
    

print(f())
