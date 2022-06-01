from math import *
import numpy as np

def triangle(n):
    return(((-1+sqrt(1+8*n))/2)%1==0)
def square(n):
    return(sqrt(n)%1==0)
def pent(n):
    return(((1+sqrt(1+24*n))/6)%1==0)
def hexa(n):
    return(((1+sqrt(1+8*n))/4)%1==0)
def hept(n):
    return(((3+sqrt(9+40*n))/10)%1==0)
def octa(n):
    return(((2+sqrt(4+12*n))/6)%1==0)

Lf=[triangle,square,pent,hexa,hept,octa]

def nb(n):
    L=[0]
    for f in Lf:
        if(f(n)):
            L[0]+=1
            L.append(True)
        else:
            L.append(False)
    return L

def next(n,f):
    a=str(n)[-2:]
    a=100*int(a)
    L=[]
    for i in range(10,100):
        if(Lf[f](a+i)):
            L.append(a+i)
    return L
                
def f():

    for i in range(1010,10000):
        nb0=nb(i)
        if(i%100>9 and nb0[0]!=0):
            f0=0
            for x in range(1,len(nb0)):
                if(nb0[x]):
                    f0=x-1
                    break
            for f1 in range(6):
                if(f1!=f0):
                    La=next(i,f1)
                    if(len(La)!=0):
                        for j in La:
                            for f2 in range(6):
                                if(len(set([f0,f1,f2]))==3):
                                    Lb=next(j,f2)
                                    if(len(Lb)!=0):
                                        for k in Lb:
                                            for f3 in range(6):
                                                if(len(set([f0,f1,f2,f3]))==4):
                                                    Lc=next(k,f3)
                                                    if(len(Lc)!=0):
                                                        for l in Lc:
                                                            for f4 in range(6):
                                                                if(len(set([f0,f1,f2,f3,f4]))==5):
                                                                    Ld=next(l,f4)
                                                                    if(len(Ld)!=0):
                                                                        for m in Ld:
                                                                            for f5 in range(6):
                                                                                if(len(set([f0,f1,f2,f3,f4,f5]))==6):
                                                                                    Le=next(m,f5)
                                                                                    if(len(Le)!=0):
                                                                                        for n in Le:
                                                                                            if(str(n)[-2:] == str(i)[:2]):
                                                                                                return(i+j+k+l+m+n)
                    




    
print(f())
