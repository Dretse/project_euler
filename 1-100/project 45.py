from math import *
import numpy as np

def T(n):
    return(int(n*(n+1)/2))
def isP(n):
    a=(1+sqrt(1+24*n))/6
    return(a%1==0)
def isH(n):
    a=(1+sqrt(1+8*n))/4
    return(a%1==0)
           
def f():
    n=286
    while(True):

        a=T(n)
        if(isP(a) and isH(a)):
            return (a)
        n+=1
    return "really?"
# c'est loooooooooooong
print(f())
