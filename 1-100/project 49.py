from math import *
import numpy as np

def prime(n):
    if(n==1):
        return False
    p=2
    while(p<=sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

def Lprime():
    L=[]
    for i in range(1000,10000):
        if(prime(i)):
            L.append(i)
    return L

def rot(a,b):
    La=list((str(a)))
    Lb=list((str(b)))
    La.sort()
    Lb.sort()
    for i in range(len(La)):
        if(La[i]!=Lb[i]):
            return False
    return True
    

    
def f():
    L=Lprime()
    for n in L:
        for i in range(2,3333):
            if(2*i+n>9999):
                break
            if(rot(n,n+i) and prime(n+i)):
                if( rot(n,n+ 2*i) and prime(n+2*i)):
                    print (str(n)+str(n+i)+str(n+2*i))
                
    
print(f())
