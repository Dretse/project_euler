# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:57:02 2019

@author: admin
"""
import numpy as np
def prime(n,L):
    for i in L:
        if(n%i==0):
            return False
    return True

def Lprime(maxi):
    L=[2]
    for p in range(1,maxi//2):
        if(prime(2*p + 1,L)):L.append(2*p +1)
    return L

def num(n,L):
    S=[0]
    i=0
    while(L[i]<=n):
        if(n%L[i]==0):
            S[i]+=1
            n/=L[i]
        else:
            i+=1
            S.append(0)
    return np.prod([i+1 for i in S if i!=0])
        
Lp=Lprime(50)
print("L done")
maxi=10000000000000
S=[]
ENS=set()
i=0
while(Lp[0]**(2*i) <maxi):
    if(Lp[0]**(2*i) not in ENS):
        S.append((2*i +1,Lp[0]**(2*i)))
        ENS.add(Lp[0]**(2*i))
    i+=1

for p in range(1,len(Lp)):
    N=len(S)
    print(Lp[p],N)
    for j in range(N-1):
        i=0
        while(S[j][1]*(Lp[p]**(2*i))<maxi):
            if(S[j][1]*(Lp[p]**(2*i)) not in ENS):
                ENS.add(S[j][1]*(Lp[p]**(2*i)))
                S.append((S[j][0]*(2*i+1),S[j][1]*(Lp[p]**(2*i))))
                
            i+=1
            if(S[j][0]*(i)>1000):break

print("\n=====================\n")
S.sort(key=lambda x : x[0], reverse=True)
#n=min([i[0] for i in S if i[0]>1000])
A=[i for i in S if i[0]>=2001 and np.sqrt(i[1])%1==0]
A.sort()
print(np.sqrt(A[0][1]))


