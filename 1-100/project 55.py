from math import *
import numpy as np

def palindrome(n):
    s=str(n)
    for i in range(len(s)//2):
        if(s[i]!=s[-i-1]):
            return False
    return True

def Next(n):
    s=str(n)
    a=""
    for i in range(len(s)):
        a+=s[-i-1]
    return (int(a))

def Howmuch(n):
    n=n+Next(n)
    i=0
    while(not palindrome(n) and i<=50):
        i+=1
        n=n+Next(n)
    return i

def f():
    s=0
    for i in range(1,10000):
        if(Howmuch(i)==51):
            s+=1
    return s
print(f())
