from math import *
import numpy as np

def XOR(letter, key):
    a=bin(letter)[2:]
    b=bin(key)[2:]
    a=(8-len(a))*'0' + a
    b=(8-len(b))*'0' + b
    c=0
    for i in range(8):
        c=c*2
        if(a[i]!=b[i]):
            c+=1
        else:
            c+=0
    return (chr(c))

def Decipher(L,Key):
    s=""
    a=0
    
    for i in L:
        s+=XOR(int(i),Key[a])
        a=(a+1)%3
    return s
def is_english(s):
    L=[35,124,126]
    for i in s:
        if(ord(i) in L):
            return False
    return True
def f():
    file=open("p059_cipher.txt","r")
    S=file.readlines()
    L=S[0].strip('\n').split(',')
    s=Decipher(L,[103,111,100])
    print(s)
    i=0
    for x in s:
        i+=ord(x)
    return i
                


print(f())
