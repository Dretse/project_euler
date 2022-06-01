from math import *
from random import randint
from copy import copy

def prime(n,L):
    if(n==1):
        return False
    for p in L:
        if(n%p==0):
            return False
        if(p>sqrt(n)):
            break
        p+=1
    return True
def Lprime(n):
    L=[2]
    p=3
    while p<n:
        if(prime(p,L)):
           L.append(p)
        p+=2
    return L


def phi(n,Lp):
    p=n
    for i in Lp:
        if(i>n/2):
            break
        if(n%i==0):
            p=p*((i-1)/i)
    if(n in Lp):
        p=p*(n-1)/n
    return (int(p))

def pgcd(a,b):
    #a>b
    while(True):
        r=a%b
        a=b
        if(r==0):
            return b==1
        b=r
    
def Lphi(N,Lp):
    L=[]
    for i in range(2,N):
        L.append([i,phi(i,Lp)])
    return L

def f(N=10000000):
    print("List of prime computing...")
    Lp=Lprime(N/2)
    print("Prime List done")
    
    print("List of phi computing...")
    La=Lphi(int(10**4),Lp)
    print("List of phi done")

    L=[]
    pour=len(La)//100
    minip=1.03
    mini=0
    for a in range(len(La)):
        if(a%pour==0):
            print(a//pour,"%")
        for b in range(a+1,len(La)):
            if(pgcd(La[b][0],La[a][0])):
                i,p=La[a][0]*La[b][0],La[a][1]*La[b][1]
                if(i<N):
                    x,y=list(str(i)),list(str(p))
                    x.sort()
                    y.sort()
                    if(x==y and i/p<minip):
                        minip=i/p
                        mini=i
                        print(i/p,i)
                    
                
    return mini
    
def comp(phi,n):
    a=list(str(phi))
    a.sort()
    b=list(str(n))
    b.sort()
    return a==b

print("###",f(),"###")
