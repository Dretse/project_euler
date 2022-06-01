from math import *

def prime(n):
    if(n==1):
        return False
    p=2
    while(p<=sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

def trunc(n):
    g=str(n)
    d=str(n)
    for i in range(1,len(d)):
        if(not prime(int(d[:i]))):
            return False
    for i in range(len(g)):
        if(not prime(int(g[i:]))):
            return False

    return True

def f():
    S=0
    N=1000000
    for i in range(10,N):
        #if(i%(N/100)==0):
            #print(i//(N/100),"%")
        if(trunc(i)):
            S+=i
            print(i)
    return S
        
    



print(f())
