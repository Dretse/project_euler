import numpy as np

batches = [[[(1,1),1,1,1,1]]]

def next_(pos, size):
    proba = simpl((pos[0][0]*pos[size],pos[0][1]*np.sum(pos[1:])))
    new_pos = [proba]
    for i in range(4):
        if(i+1<size):
            new_pos.append(pos[i+1])
        elif(i+1==size):
            new_pos.append(pos[i+1]-1)
        else:
            new_pos.append(pos[i+1]+1)
    return new_pos

def pgcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return pgcd(b,a%b) 

def simpl(f):
    p = pgcd(f[0],f[1])
    return (f[0]//p, f[1]//p)

def sum_frac(f1,f2):
    p = pgcd(f1[1],f2[1])
    nf = (f1[0]*(f2[1]//p) + (f1[1]//p)*f2[0], f1[1]*(f2[1]//p))
    if(nf[0]<0 or nf[1]<0):print(nf,"###",f1, f2)
    
    return simpl(nf)

def clean(batch):
    new_batch = []
    for pos in batch:
        is_in = False
        for i in range(len(new_batch)):
            if(tuple(pos[1:])==tuple(new_batch[i][1:])):
                new_batch[i][0]= sum_frac(pos[0],new_batch[i][0])
                is_in = True
                break
        if not is_in : new_batch.append(pos)
    #print(len(batch), len(new_batch))
    return new_batch

for batch in range(13):
    batches.append([])
    for pos in batches[batch]:
        for size in range(1,5):
            if(pos[size]!=0):
                batches[batch+1].append(next_(pos, size))
    batches[batch+1] = clean(batches[batch+1])

print("possible batches computed")

expected = (0,1)

for batch in batches:
    for pos in batch:
        if(np.sum(pos[1:])==1):
            expected = sum_frac(pos[0], expected)

print(round(expected[0]/expected[1],6))


