from math import *
import numpy as np

def S(n):
    s=""
    i=0
    while (len(s)<n):
        s+=str(i)
        i+=1
    return s

def f():
    s=S(1000001)
    P=1
    for i in range(7):
        print(i)
        P*=int(s[10**i])
    return P
            
    
    
        
        
    

print(f())
