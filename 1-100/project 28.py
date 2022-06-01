from math import *
import numpy as np

def Spiral(n):
    print(n)
    if(n==1):
        return ([[1]])
    M=np.eye(n)
    for i in range(n):
        M[0][i]=n*n-(n-1-i)
    for i in range(1,n):
        M[i][0]=n*n-n-i+1
    for i in range(1,n):
        M[n-1][i]=n*(n-2) +2 -i
    for i in range(1,n-1):
        M[i][n-1]=(n-2)*(n-2) + i
    N=Spiral(n-2)
    for i in range(n-2):
        for j in range(n-2):
            M[i+1][j+1]=N[i][j]
    print(n)
    return M

def Sum_diag(n):
    M=Spiral(n)
    print("Spiral done")
    S=0
    for i in range(n):
        S+=M[i][i] + M[i][n-i-1]
    return S-1
    

print(Sum_diag(1001))
