# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:14:28 2019

@author: DZBZ0373
"""
import numpy as np
from random import randint
#Lecture fichier
file=open("p096_sudoku.txt")
L=file.readlines()
file.close()

#Formattage Sudokus
Sudokus=[]
for i in range(len(L)//10):
    S=[]
    for line in L[10*i+1:10*(i+1)]:
       m=np.array([int(i) for i in line.strip('\n')])
       S.append(m)
    Sudokus.append(np.array(S))

def Solve_simple(M):
    M_=np.zeros((9,9))
    while(not np.array_equal(M,M_) ):
        M_=M.copy()
        P=Pos(M)
        for x in range(9):
            for y in range(9):
                if(len(P[x][y])==1):
                    M[x,y]=P[x][y][0]             
    return M

    
def Pos(M):
    P=[[[] for _ in range(9)] for _ in range(9)]
    for x in range(9):
        for y in range(9):
            if(M[x,y]==0):
                A=[]
                for N in range(1,10):
                    if(not(N in M[x,:] or N in M[:,y] or N in M[3*(x//3):3*(x//3 +1),3*(y//3):3*(y//3 +1)])):
                        A.append(N)
                P[x][y]=A
    return np.array(P)

def Random_Solve(M,xb=0,yb=0):
    if(yb>8):
        return M
    #print(xb,yb,end=', ')
    M=Solve_simple(M)
    if(Verify(M)): return M
    P=Pos(M)
    if(len(P[xb,yb])!=0):
        for N in P[xb,yb]:
            M_=M.copy()
            M_[xb,yb]=N
            if(xb<8):
                M_=Random_Solve(M_,xb+1,yb)
            else:
                M_=Random_Solve(M_,0,yb+1)
            M_=Solve_simple(M_)
            if(Verify(M_)): return M_
        
        return M_
    else:
        if(xb<8):
            return(Random_Solve(M,xb+1,yb))
        else:
            return(Random_Solve(M,0,yb+1))
        
        
def Verify(M):
    if(0 in M): return False
    for i in range(9):
        if(sum(M[i,:])!=45 or sum(M[:,i])!=45): return False
        if(np.sum(M[3*(i%3):3*(1+ i%3),3*(i//3):3*(1+ i//3)])!=45):return False
    return True

"""
M=Sudokus[1]
print(M)
print(Random_Solve(M))
"""
S=0
n=0
for M in Sudokus:
    n+=1
    u=Random_Solve(M)[0,:3]
    print(n,"/50")
    S+=u[0]*100 + u[1]*10 + u[2]
print(S)



