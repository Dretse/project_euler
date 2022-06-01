from math import *

def pandigital(n):
    return (set(n)==set("123456789") and len(n)==9)

def concat(A,n):
    s=""
    for i in range(1,n+1):
        s+=str(A*i)
    return (pandigital(s),int(s))

def f():
    maxi=0
    for n in range(1,10):
        for A in range(1, 9999):
            B,m=concat(A,n)
            if(B and m>maxi):
                maxi=m
                print(n,A,m)
    return maxi
        
        
    

print(f())
