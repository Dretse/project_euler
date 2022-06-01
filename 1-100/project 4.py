from math import *

def f():
    a=0
    for i in range(100,1000):
        for j in range(i,1000):
            if(is_palindrome(i*j)):
                if(a<i*j):
                    a=i*j

    return a
def is_palindrome(n):
    p=True
    N=str(n)
    for i in range(len(N)//2):
        if(N[i]!=N[len(N)-i-1]):
            p=False
    return p
    
print(f())
