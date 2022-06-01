from math import *

def curious(n):
    a=str(n)
    S=0
    for i in a:
        S+=fact(int(i))
    return(S==n)

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return (n*fact(n-1))

        
def f():
    S=0
    for i in range(10,2540160):
        if(curious(i)):
            S+=i
        if(i%25400==0):
            print(i//25400,"%")


    return S
            



print(f())
