from math import *

def f():
    maxi=0
    d=0
    for i in range(1, 1000):
        A=court_cycle(i)
        if(A>maxi):
            #print(str(i)+" : "+str(A))
            maxi=A
            d=i
            
    print("")
    return d

def court_cycle(N,pre=100):
    S="0."+int(log(N,10))*"0"
    S=S+str((10**pre)//N)

    if(S[-1]=='0'):
        return 0
    for i in range(1,pre//2 -10):
        if(cycle(S[10:])==i):
            return i
    print("*",end="")
    return long_cycle(N)
    
def long_cycle(N,pre=1000):
    S="0."+int(log(N,10))*"0"
    S=S+str((10**pre)//N)

    if(S[-1]=='0'):
        return 0
    for i in range(40,pre//2):
        if(cycle(S[100:])==i):
            return i
    print(" ("+str(N)+") ",end="")
    return long_long_cycle(N)

def long_long_cycle(N,pre=2000):
    S="0."+int(log(N,10))*"0"
    S=S+str((10**pre)//N)

    if(S[-1]=='0'):
        return 0
    for i in range(500,pre//2):
        if(cycle(S[100:])==i):
            return i
    print("")
    print(S)
    return 0
    
def cycle (S):
    a=S[0]
    for i in range(1,len(S)):
        if(S[i]==a):
            if(test(S,i)):
                return i
    return 0
def test(S,n):
    for i in range(n,len(S)):
        if(S[i]!=S[i%n]):
            return False
    return True
print(f())

