from math import *

def f(n):
    a=2520
    end=True
    while(end):
        f=False
        for i in range(1,n+1):
            if(a%i!=0):
                f=True
                print(a)
                break
        if(f):
            a=a+10
        else:
            end=False
                

    return a

    
print(f(20))
#232792560
