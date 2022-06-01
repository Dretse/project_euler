# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:45:39 2019

@author: DZBZ0373
"""

def rmax(a):
    rm=0
    for n in range(a**2):
        r=((a-1)**n + (a+1)**n)% (a**2)
        if(r>rm):
            rm=r
    return rm

def rmax2(a):
    r=0
    for n in range(2*a):
        if(r< (2*a*(2*n+1))%(a**2)):r=(2*a*(2*n+1))%(a**2)
    return r

def test(m=100):
    for a in range(3,m):
        if(rmax2(a) != rmax(a)):
            print(a,rmax2(a),rmax(a))
            return False
    return(True)
            

S=0
for a in range(3,1001):
    S+=rmax2(a)


print(S)
