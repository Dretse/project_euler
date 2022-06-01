import numpy as np
from time import time
from tqdm import tqdm

def compute_grids(a,b):
    return compute_full_rectangle(a,b) + compute_diagonal_grid(2*a,2*b)
    
def compute_full_rectangle(a,b):
    S = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            S+=compute_partial_rectangle(a,b,i,j)
    return S

def compute_partial_rectangle(a,b,i,j):
    return (a-i+1)*(b-j+1)

def compute_diagonal_grid(a,b):
    grid = np.zeros((a,b)).astype(int)
    for i in range(1,a):
        for j in range(1,b):
            if((i+j)%2==1):grid[i,j]+=1
    grid = grid[1:,1:]
    S = 0
    #print(grid)
    for i,row in enumerate(grid):
        for j,el in enumerate(row):
            if(el==1):
                S+=compute_from_angle(grid,i,j)

    #print(grid)
    #print(S)
    return S

def compute_from_angle(grid, i,j):
    S = 0
    a,b = i,j
    x,y = a,b
    prev_x = len(grid)
    #print("compute :",i,j)
    while(0<=a<grid.shape[0] and 0<=b<grid.shape[1] and grid[a,b]==1):
        if(0<=x<grid.shape[0] and 0<=y<grid.shape[1] and grid[x,y]==1 and x-1<=prev_x):
            S+=1
            #print(i,j,"\t", a,b,"\t", x,y,"\t",S, prev_x)
            x+=1
            y-=1
        else:
            a+=1
            b+=1
            prev_x = x-1
            x,y=a,b
    return S

A,B = 47, 43
S=0
for i in tqdm(range(1,A+1)):
    for j in range(1,B+1):
        tot = compute_grids(i,j)
        S+=tot
        #print(i,j,"\t", S)
print(S)
