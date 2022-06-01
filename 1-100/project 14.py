from math import *

def next(n):
    if(n%2==0):
        return n/2
    else:
        return (3*n +1)
def l(n):
    A=1
    while(n!=1):
        n=next(n)
        A+=1
    return A
def f():
    S=0
    for i in range(10,1000000):
        A=l(i)
        if(A>S):
            S=A
            print(i)
    return S

print(f())
