from math import *
from random import randint
from copy import copy


def conv():
    file=open("p067_triangle.txt","r")
    S=file.readlines()    
    M=[]
    L=[]
    a=0
    for i in S:
        A=i.strip('\n').split(' ')
        L=[]
        for j in A:
            L.append(int(j))
        M.append(L)
    return M

M=conv()
print("Matrix done")

def f(M):
    for l in range(len(M)-2,0,-1):
        for i in range(len(M[l-1])):
            M[l][i]=M[l][i] + max(M[l+1][i],M[l+1][i+1])
    return (M[0][0]+ max(M[1][0],M[1][1]))
        
        

#6658 < w < 9565

print(f(M))
