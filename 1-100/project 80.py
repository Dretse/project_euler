# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:55:28 2019

@author: admin
"""
import numpy as np
from decimal import *
getcontext().prec = 120

def S(i):
    if( i in [i**2 for i in range(1,11)]): return 0
    b=Decimal(i).sqrt()
    a=str(b*(10**100))[:100]
    return sum([int(i) for i in str(a)])

print(sum([S(i) for i in range(1,101)]))
print(S(2))
    