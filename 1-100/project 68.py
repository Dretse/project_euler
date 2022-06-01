from math import *
from random import randint
from copy import copy


def f():
    L=[1,2,3,4,5,6,7,8,9,10]
    Ltot=[]
    for a in L:
        for b in range(1,10):
            if(b!=a):
                for c in range(1,10):
                    if(a!=c and b!=c):
                        tot=a+b+c
                        for d in range(a+1,11):
                            if(d not in set([a,b,c])):
                                e=int(tot-c-d)
                                if(e not in set([a,b,c,d]) and e!=10):
                                    for f in range(a+1,11):
                                        if(f not in set([a,b,c,d,e])):
                                            for g in L:
                                                if(g not in set([a,b,c,d,e,f]) and e+f+g==tot and g!=10):
                                                    for h in range(a+1,11):
                                                        if(h not in set([a,b,c,d,e,f,g])):
                                                            for i in L:
                                                                if(i not in set([a,b,c,d,e,f,g,h]) and i!=10 and g+h+i==tot):
                                                                    j=int(tot-i-b)
                                                                    if(j>a and set([a,b,c,d,e,f,g,h,i,j])==set(L)):
                                                                        Ltot.append(lit([[a,b,c],[d,c,e],[f,e,g],[h,g,i],[j,i,b]]))
    return (max(Ltot))

def lit(L):
    S=""
    for i in L:
        for c in i:
            S+=str(c)
    return int(S)
                                        
        
print(f())
