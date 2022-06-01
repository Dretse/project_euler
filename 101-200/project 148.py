import numpy as np

def C(n,k):
    return (28**n)*k*(k+1)//2

N = 10**9
S = 0
factor = 1


n=0
while(7**n<N):n+=1
n-=1
print(n)

while (N!=0):
    k = N//(7**n)
    S+= factor*C(n,k)
    N = N - k*(7**n)
    factor*=k+1
    print(n,k, N, factor, S)
    while(7**n>N and N!=0):n-=1
    #if(n==0):break

#2129970655314432
