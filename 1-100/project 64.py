from math import *
from decimal import *

    
    
def root(n,s):
    a=Decimal(n).sqrt()
    L=[int(a//1)]
    a=a%1
    Ldec=[a]
    while(len(L)<s and a!=0):
        a=1/a
        L.append(int(a//1))
        a=a%1
        if (str(a)[2:s] in Ldec):
            return len(Ldec)-1
        Ldec.append(str(a)[2:s])
    return 0

            

def f(n=10000,s=300):
    N=0
    L=[]
    for i in range(2,n+1):
        if(sqrt(i)%1!=0.0):
            cycle=root(i,s)
            if(cycle==0):
                print(sqrt(i))
            if(i%500==0):
                print(i//100,"%",end=" ; ")
            if(cycle%2==1):
                N+=1
    print("")
    return N

getcontext().prec=600
print(f())


