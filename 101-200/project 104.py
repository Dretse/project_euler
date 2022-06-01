# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:17:42 2019

@author: admin
"""

e={'1','2','3','4','5','6','7','8','9'}

A=1
B=1
k=2
S1=set(list(str(B))[-9:])

while(True):
    
    B,A=A+B,B
    S1=set(list(str(B))[-9:])
    if(S1==e):
        print(".",end="")
        S2=set(list(str(B))[:9])
        if(S2==e):break
    k+=1
    if(k%329==0) : print('.',end='')
    if(k%3294==0) : print("\t",k//3294,'%')
print("\n",k+1)
#32 9468 