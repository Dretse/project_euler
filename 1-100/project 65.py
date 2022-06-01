from math import *
from decimal import *

    
    
def Liste(s):
    L=[2]
    k=1
    while(k<s):
        L.append(1)
        L.append(2*k)
        L.append(1)
        k+=1
    return L

def frac(iF,L,i=1):
    if i==iF:
        return(1,L[iF])
    n,d=frac(iF,L,i+1)
    n,d=d,n+L[i]*d
    return(n,d)


L=Liste(50)

n,d=frac(99,L)
n,d=n+2*d,d
print(n,d)



