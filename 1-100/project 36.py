from math import *

def palindrome(n):
    for i in range(len(n)//2):
        if(n[i]!=n[-i-1]):
            return False
    return True
def base2(n):
    s=""
    while n!=0:
        s=s+str(n%2)
        n=n//2
    return s

def TrueP(n):
    return(palindrome(str(n)) and palindrome(base2(n)))
    
def f():
    S=0
    for i in range(1000000):
        if(TrueP(i)):
            S+=i

    return S
    



print(f())
