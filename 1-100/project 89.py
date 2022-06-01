# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:52:11 2019

@author: DZBZ0373
"""
D={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

def Diff(S):
    n=Rom_Num(S)
    l=len(S)
    NS=Num_Rom(n)
    return l-len(NS)

def Rom_Num(S):
    Sum=0
    i=0
    while(i<len(S)-1):
        a=S[i:i+2]
        if(D[a[0]]<D[a[1]]):
            Sum+=D[a[1]]-D[a[0]]
            i+=2
        else:
            Sum+=D[a[0]]
            i+=1
    if(i==len(S)-1):
        Sum+=D[S[-1]]
    return Sum

def Num_Rom(n):
    S=""
    if(n>999):
        n,a=n%1000,n//1000
        S+=a*"M"
    if(n>99):
        n,a=n%100,n//100
        if(a==9):S+="CM"
        elif(a>4):S+="D"+(a-5)*"C"
        elif(a==4):S+="CD"
        else:S+=a*"C"
    if(n>9):
        n,a=n%10,n//10
        if(a==9):S+="XC"
        elif(a>4):S+="L"+(a-5)*"X"
        elif(a==4):S+="XL"
        else:S+=a*"X"
    a=n
    if(a==9):S+="IX"
    elif(a>4):S+="V"+(a-5)*"I"
    elif(a==4):S+="IV"
    else:S+=a*"I"
    return S


file=open("p089_roman.txt")
L=file.readlines()
file.close()

print(sum([Diff(i.strip('\n')) for i in L]))