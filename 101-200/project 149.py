import numpy as np
from tqdm import tqdm

GRID = np.zeros(2000*2000).astype(int)
for i in tqdm(range(len(GRID))):
    k = i+1
    if(k<56): GRID[i]= (100003 - 200003*k + 300007*(k**3))%1000000 - 500000
    else: GRID[i] = (GRID[k-25] + GRID[k-56])%1000000 - 500000
print(GRID[9], GRID[99])

GRID = GRID.reshape((2000,2000))
"""
GRID = np.array([[-2, 5, 3, 2],
                 [9, -6, 5, 1],
                 [3, 2, 7, 3 ],
                 [-1, 8, -4, 8]])"""
print(GRID.shape)
total_max = 0

def best_sequence_from_line(line):
    if(len(line)<47):return 0
    starts, stops, pos = [], [], False
    for idx, el in enumerate(line):
        if(el>=0):
            if(not pos):
                pos = True
                starts.append(idx)
        else:
            if(pos):
                pos = False
                stops.append(idx)
    if(len(starts)>len(stops)):stops.append(len(line))
    starts, stops = np.array(starts).astype(int), np.array(stops).astype(int)
    #print(starts, stops)
    return np.max([np.max([np.sum(line[start:stop]) for stop in stops[idx:]]) for idx, start in enumerate(starts)])

def best_sequences_from_lines(lines):
    scores = [best_sequence_from_line(line) for line in tqdm(lines)]
    return np.max(scores)

def maxi_from_grid(GRID):
    scores = []
    rot = np.zeros((len(GRID), len(GRID)))
    for i in range(len(GRID)):
        rot[i, len(GRID)-i-1]+=1
    scores.append(best_sequences_from_lines(GRID))
    #scores.append(47107641)
    print(scores)
    tGRID = np.transpose(GRID)
    scores.append(best_sequences_from_lines(tGRID))
    #scores.append(52852124)
    print(scores)
    dGRID = np.array([np.diagonal(GRID,offset=i) for i in range(2-len(GRID),len(GRID)-1)])
    scores.append(best_sequences_from_lines(dGRID))
    #scores.append(43441203)
    print(scores)
    rGRID = np.dot(rot,GRID).astype(int)
    drGRID = np.array([np.diagonal(rGRID,offset=i) for i in range(2-len(rGRID),len(rGRID)-1)])
    scores.append(best_sequences_from_lines(drGRID))
    #scores.append(42783189)
    print(scores)
    return(np.max(scores))


# 52852124
print("##################", maxi_from_grid(GRID), "################")
        