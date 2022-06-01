# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:25:56 2019

@author: DZBZ0373
"""

Scores=dict()
for i in range(1,21):
    for j in range(1,4):
        if(j==1):
            Scores["S"+str(i)]=i*j
        elif(j==2):
            Scores["D"+str(i)]=i*j
        else:
            Scores["T"+str(i)]=i*j
Scores["S25"]=25
Scores["D25"]=50
#print(Scores)

def combis(n,Scores):
    S=[]
    for i in Scores:
        if(Scores[i]==n and i[0]=="D"): S.append([i])
        elif(i[0]=="D"):
            x=n-Scores[i]
            for j in Scores:
                if(Scores[j]==x): S.append([i,j])
                else:
                    y=x-Scores[j]
                    for k in Scores:
                        if(Scores[k]==y):S.append([i,j,k])
    if(len(S)==0):
        return 0
    L=[S[0]]
    for i in S:
        a=True
        for j in L:
            if(i[0]==j[0] and len(i)==len(j)):
                if(len(i)==1):a=False
                elif(len(i)==2 and i[1]==j[1]):a=False
                elif(len(i)==3):
                        if((i[1]==j[1] and i[2]==j[2])or(i[1]==j[2] and i[2]==j[1])):a=False
        if(a):L.append(i)
    return (len(L))

S=0
for i in range(2,100):
    S+=combis(i,Scores)

print(S)