# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:03:40 2019

@author: DZBZ0373
"""

def f(n):
    N=1
    for _ in range(n):
        N=(N*2)%10000000000
    N=(N*28433)%10000000000
    return N+1

print(f(7830457))