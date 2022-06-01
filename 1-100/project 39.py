from math import *
import numpy as np


def f():
    L=np.zeros(1000)
    for i in range(10,1000):
        for j in range(1,i):
            a=sqrt(i**2 + j**2)
            if(a%1==0 and i+j+int(a)<=1000):
                L[int(i+j+int(a)-1)]+=1
    maxi=1
    a=max(L)
    for i in range(len(L)):
        if(L[i]==a):
            return i+1
            
    
    
        
        
    

print(f())
