# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:30:04 2019

@author: DZBZ0373
"""
from time import time
import numpy as np
def f(n):
    S=1
    n+=1
    for a in range(n):
        n0=n-a
        for b in range(n0):
            n1=n0-b
            for c in range(n1):
                n2=n1-c
                for d in range(n2):
                    for e in range(n-a-b-c-d):
                        x=n-a-b-c-d-e
                        S+=x*(x**3 +10*(x**2) + 23*x  +14)//24



    S-=11
    return S
S=0
AS=time()
for i in range(1,101):
    start=time()
    S+=f(i)
    a,b=time()-start,time()-AS
    print(i,'%',S,
          '\ttime :',int(a//60),':',int(a%60),',',int((1000*a)%1000),
          '\ttotal time :',int(b//60),":",int(b%60))
    
print("\n\n")
print(S)

#51161058134250