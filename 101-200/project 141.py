import numpy as np
S = set()
tot = int(0)
Max = 10**12

for k in range(2,int(np.power(Max,1/3))+1):
    for i in range(1,k):
        for j in range(1,int(Max/(i*k*k*k))+1):
            n = i*j*(j*(k**3) + i)
            if(n>Max):break
            if(np.sqrt(n)%1==0 and n not in S):
                S.add(n)
                tot+=n
                print(n,"\t", i,j,k)

print("\n###",tot)
