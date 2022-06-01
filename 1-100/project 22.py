from math import *

def f():
    file=open("p022_names.txt","r")
    S=file.readlines()
    A=S[0]
    L=A.strip('"').split('","')
    L.sort()
    Somme=0
    for i in range(len(L)):
        Somme+=(i+1)*value(L[i])
    return Somme
def value(s):
    tot=0
    for i in s:
        tot+=ord(i)-64
    return tot

print(value("COLIN"))
print(f())

