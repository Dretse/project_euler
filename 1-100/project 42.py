from math import *
import numpy as np

def f():
    file=open("p042_words.txt","r")
    S=file.readlines()
    A=S[0]
    L=A.strip('"').split('","')
    N=liste(50)
    total=0
    for i in L:
        if(value(i) in N):
            total+=1
    return total
    
def value(s):
    tot=0
    for i in s:
        tot+=ord(i)-64
    return tot

def liste(n):
    L=[]
    for i in range(1,n):
        L.append(int(i*(i+1)/2))
    return L
            
    
    
        
        

print(f())
