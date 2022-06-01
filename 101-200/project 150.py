import numpy as np
from tqdm import tqdm

GRID = np.array([[15, 0, 0, 0, 0, 0],
                 [-14, -7, 0, 0, 0, 0],
                 [20, -13, -5, 0, 0, 0],
                 [-3, 8, 23, -26, 0, 0],
                 [1, -4, -5, -18, 5, 0],
                 [-16, 31, 2, 9, 28, 3]])

GRID = np.zeros((1000,1000))
t, x, y = 0,0,0
for k in tqdm(range(500500)):
    t = (615949*t + 797807)%(2**20)
    GRID[x,y] = t-2**19
    if(y==x):
        y,x = 0,x+1
    else:
        y+=1

GRID = GRID.astype(int)
print(GRID.shape)

def eval_from_xy(xa,ya, xb,yb, GRID):
    return np.sum(np.tril(GRID[xa:xb+1, ya:yb+1]))

def eval_from_x(xa,ya, GRID):
    mini = 0
    for xb in range(xa+1,len(GRID)):
        yb = xb + (ya-xa)
        mini = min(mini,eval_from_xy(xa,ya,xb,yb,GRID))
    return mini

def eval_from_all(GRID):
    mini = 0#-274770067
    for xa in tqdm(range(len(GRID)-1)):
        diff= False
        for ya in range(xa+1):
            m = eval_from_x(xa,ya,GRID)
            if(m<mini):
                diff = True
                mini = m
        if(diff): print(int(mini))
        if(xa>7):break
    return mini    

print(eval_from_all(GRID))
