from math import *
from itertools import permutations

def numbers(a):
    L=[0,0,0,0,0,0,0,0,0,0]
    for i in str(a):
        L[int(i)]+=1
    return L
    
    
def f(n):
    i=0
    L=[]
    while(i**3<10**(n)):
        L.append([numbers(i**3),i])
        i+=1
    L.sort()
    N=[]
    for j in range(len(L)-4):
        if(L[j][0]==L[j+1][0] and L[j][0]==L[j+2][0] and L[j][0]==L[j+3][0] and L[j][0]==L[j+4][0]  ):
            N.append(L[j][1])
    return (len(N)>0,N)

def g():
    a=False
    i=2
    while(not a):
        a,result=f(i)
        i+=1
    return (min(result)**3)

print(g())
