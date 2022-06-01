from math import *

def f():
    S=0
    N=1
    i=1
    A=1
    while(A<=500):
        A=divisor(N)
        if(A>S):
            S=A
            print(str(S)+" : "+str(N))
        i+=1
        N+=i
    return N-i

def divisor(n):
    S=[]
    p=2
    while (n!=1):
        if(n%p==0):
            S.append(p)
            n=n/p
        else:
            p=p+1
            while(not is_prime(p)):
                p+=1
    A=set(S)
    N=1
    for i in A:
        B=1
        for j in S:
            if(j==i):
                B+=1
        N*=B
        
    return (N)

def is_prime(n):
    p=1
    while (p<=sqrt(n)):
        p=p+1
        if(n%p==0):
            return False
    return True
    
print(f())
    
