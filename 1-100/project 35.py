from math import *

def prime(n):
    p=2
    while(p<=sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

def rotations(n):
    L=[n]
    n=str(n)
    for i in range(len(n)-1):
        n=n[1:]+n[0]
        L.append(int(n))
    return L

def prime_rot(n):
    L=rotations(n)
    P=[]
    for i in L:
        if(prime(i)):
            P.append(i)
    if(len(P)==len(L)):
        return P,True
    else:
        return L,False

def f():
    L=range(2,1000000)
    P=set()
    for i in L:
        if(i%10000==0):
            print(i//10000,"%")
        if(prime(i)):
            A,okay=prime_rot(i)
            if(okay):
                for j in A:
                    P.add(j)

    return len(P)
    



print(f())
