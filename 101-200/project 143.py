import numpy as np
from time import time
tot=0
S=set()
Max = 120000
s=time()
for q in range(1,int(Max//3) +1):
    if(q%40==39):
        x=int((Max//3)*(time()-s)/(q+1))
        print((q+1)//40,"\t", x//3600,":",(x%3600)//60)
    for p in range(q,int((Max-q)//2) +1):
        b_ = p**2 + q**2 + p*q
        if(np.sqrt(b_)%1==0):
            #b = int(np.sqrt(b_))
            for r in range(p,Max-q-p+1):
                a_,c_ = q**2 + r**2 + q*r, p**2 + r**2 + p*r
                if(np.sqrt(a_)%1==0 and np.sqrt(c_)%1==0):
                    #a,c = int(np.sqrt(a_)), int(np.sqrt(c_))
                    sum_ = p+q+r
                    if(sum_ not in S):
                        S.add(sum_)
                        tot+=sum_

print(tot)
print(int(time()-s))