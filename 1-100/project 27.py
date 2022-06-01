from math import *


def is_prime(n):
    p=2
    while(p<sqrt(n)):
        if(n%p==0):
            return False
        p+=1
    return True

def How_much(a,b):
    n=0
    while((n**2 +a*n + b>0) and is_prime(n**2 +a*n + b)):
        n+=1
    return n-1

def Prime_list(n):
    L=[]
    for i in range(2,n):
        if(is_prime(i)):
            L.append(i)
    return L

##def Diff_list(L):
##    S=set()
##    for i in L:
##        for j in L:
##            if(not(abs(i-j) in S)):
##                S.add(abs(i-j))
##    S.remove(0)
##    L=[]
##    for i in S:
##        L.append(i-1)
##    return L

def f():
    L_b=Prime_list(1000)
    print("lists done, starting research")
    A=0
    B=0
    maxi=0
    for a in range(-9999,1000):
        for b in L_b:
            N=How_much(a,b)
            if(N>maxi):
                print(N)
                maxi=N
                A=a
                B=b
    return (A*B)
    

print(f())
