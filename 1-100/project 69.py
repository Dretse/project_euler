from math import *
from random import randint
from copy import copy

def prime(n):
    if(n==1):
        return False
    p=2
    while p<=sqrt(n):
        if(n%p==0):
            return False
        p+=1
    return True
def Lprime(n):
    L=[]
    p=2
    while p<n:
        if(prime(p)):
           L.append(p)
        p+=1
    return L


def phi(n,Lp):
    p=1
    for i in Lp:
        if(n%i==0):
            p=p*(i/(i-1))
        if(i>n):
            break
    return (p)

def f():
    N=1000000
    nmax=0
    phimax=0

    print("List of prime computing...")
    Lp=Lprime(N)
    print("Prime List done")
    
    for i in range(1,1000):
        p= phi(i*1001,Lp)
        if(p>=phimax):
            phimax=p
            nmax=i*1001
    return nmax
    
    
print("###",f(),"###")
