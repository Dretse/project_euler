from math import *

def d(n):
    L=[1]
    for i in range(2,1 + (n//2)):
        if(n%i==0):
            L.append(i)
    S=0
    for i in L:
        S+=i
    return S

def f():
    S=0
    A=0
    L=[0]
    for i in range(1,10000):
        L.append(d(i))
    for i in range(1,10000):
        if(i%100==0):
            A=i//100
            print(A)
        for j in range(1,i):
            if(L[i]==j and L[j]==i):
                S+=i+j
    return S
print(d(220))
print(f())
