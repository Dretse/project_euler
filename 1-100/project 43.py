from math import *
import numpy as np

def pan(n):
    a=str(n)
    if(len(a)!=10):
        a="0"+a
    return (set("0123456789")==set(a))

def verif(n):
    N=str(n)
    if(len(N)!=10):
        N="0"+N
    L=[2,3,5,7,11,13,17]
    for i in range(7):
        if(int(N[1+i]+N[2+i]+N[3+i])%L[i]!=0):
            return False
    return True
    
def f():
    S=0
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                for d4 in [0,2,4,6,8]:
                    for d5 in range(10):
                        if(int(str(d3)+str(d4)+str(d5))%3==0):
                            for d6 in [0,5]:
                                for d7 in range(10):
                                    if(int(str(d5)+str(d6)+str(d7))%7==0):
                                        for d8 in range(10):
                                            if(int(str(d6)+str(d7)+str(d8))%11==0):
                                                for d9 in range(10):
                                                    if(int(str(d7)+str(d8)+str(d9))%13==0):
                                                        for d10 in range(10):
                                                            if(set([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10])==set([1,2,3,4,5,6,7,8,9,0]) and int(str(d8)+str(d9)+str(d10))%17==0):
                                                                a=int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10))
                                                                print(a)
                                                                S+=a
    return S
        

print(f())
