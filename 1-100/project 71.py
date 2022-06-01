from math import *
from random import randint
from copy import copy


def pgcd(a,b):
    #a>b
    while(True):
        r=a%b
        a=b
        if(r==0):
            return b==1
        b=r
        
def f(N=1000000):
    L=[]
    pour=N//10
    for d in range(100,N):
        n=int(3*d/7)-1
        if(n/d<3/7 and pgcd(d,n)):
            L.append([n/d,n,d])
    a=max(L)                      
    return a[1]


print("###",f(),"###")
