from math import *
import numpy as np
from copy import copy

def valid(s):
    for i in range(2,8):
        for j in range(1,i-1):
            if(int(s[:j])*int(s[j:i])==int(s[i:])):
                print("Found :  "+s[:j]+" * "+s[j:i]+" = "+s[i:])
                return (int(s[i:]))
    return 0

def f():
    S=set()
    A=set([1,2,3,4,5,6,7,8,9])
    for a in A:
        B=A.difference(set([a]))
        for b in B:
            print(str(a)+str(b)+"%")
            C=A.difference(set([a,b]))
            for c in C:
                D=A.difference(set([a,b,c]))
                for d in D:
                    E=A.difference(set([a,b,c,d]))
                    for e in E:
                        F=A.difference(set([a,b,c,d,e]))
                        for f in F:
                            G=A.difference(set([a,b,c,d,e,f]))
                            for g in G:
                                H=A.difference(set([a,b,c,d,e,f,g]))
                                for h in H:
                                    I=A.difference(set([a,b,c,d,e,f,g,h]))
                                    i=list(I)[0]
                                    X=valid(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i))
                                    if(X!=0):
                                        S.add(X)
    somme=0
    for i in S:
        somme+=i
    return somme

print(f())
