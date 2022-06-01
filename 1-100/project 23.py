from math import *

def abundant(n):
    L=[1]
    for i in range(2,1 + (n//2)):
        if(n%i==0):
            L.append(i)
    S=0
    for i in L:
        S+=i
    return (S>n)

def f():
    L_ab=[]
    for i in range(1,28123):
        if(i%280==0):
            print(str(i//280)+"% ")
        if(abundant(i)):
            L_ab.append(i)
    print("List of abundants done")
    L=set(range(1,28123))
    for i in range(len(L_ab)):
        if(i%(len(L_ab)//100)==0):
            print(str(i//(len(L_ab)//100))+"% ")
        for j in range(i,len(L_ab)):
            a=L_ab[i]+L_ab[j]
            if(a in L):
                L.remove(a)
    L=list(L)
    print("list of others done")
    S=0
    for i in L:
        S+=i
    return (S)

print(f())

