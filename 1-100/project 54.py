from math import *
import numpy as np
D={'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
def High_Card(A,B):
    Ma=0
    Mb=0
    for i in A:
        if(D[i[:-1]]>Ma):
            Ma=D[i[:-1]]
    for i in B:
        if(D[i[:-1]]>Mb):
            Mb=D[i[:-1]]
    return(Ma>Mb)
    
def Pairs(A):
    p=0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if(A[i][:-1]==A[j][:-1]):
                p+=1
    return p

    
def PairsEqual(A,B):
    a=0
    b=0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if(A[i][:-1]==A[j][:-1]):
                a=tri(A[i])
    for i in range(len(B)-1):
        for j in range(i+1,len(B)):
            if(B[i][:-1]==B[j][:-1]):
                b=tri(B[i])
    if(a==b):
        return High_Card(A,B)
    return a>b

def Three_of_a_Kind(A):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if(A[i][:-1]==A[j][:-1]):
                for k in A:
                    if(k!=A[i] and k!=A[j] and k[:-1]==A[i][:-1]):
                        return True
    return False

def Straight(A):
    for i in range(4):
        if(tri(A[i])!=tri(A[i+1])-1):
            return False
    return True

def Flush(A):
    a=A[0][-1]
    for i in range(1,5):
        if(A[i][-1]!=a):
            return False
    return True

def Full_House(A):
    if(Pairs(A)==4 and Three_of_a_Kind(A)):
        return True
    return False

def Four_of_a_Kind(A):
    if(Pairs(A)==6):
        return True
    return False
def Straight_Flush(A):
    if(Straight(A) and Flush(A)):
        return True
    return False
def Royal_Flush(A):
    if(Straight_Flush(A) and A[0][:-1]=='10'):
        return True
    return False

def tri(x):
    return (int(D[x[:-1]]))
def sum(A):
    S=0
    for i in A:
        S+=tri(i)
    return S

def Winner(A,B):
    A.sort(key=tri)
    B.sort(key=tri)
    if(Royal_Flush(A) or Royal_Flush(A)):
        if(Royal_Flush(A) and Royal_Flush(A)):
            return(High_Card(A,B))
        return (Royal_Flush(A))
    
    if(Straight_Flush(A) or Straight_Flush(B)):
        if(Straight_Flush(A) and Straight_Flush(B)):
            return(High_Card(A,B))
        return(Straight_Flush(A))
    
    if(Four_of_a_Kind(A) or Four_of_a_Kind(B)):
        if(Four_of_a_Kind(A) and Four_of_a_Kind(B)):
            return(High_Card(A,B))
        return Four_of_a_Kind(A)
    
    if(Full_House(A) or Full_House(B)):
        if(Full_House(A) and Full_House(B)):
            return(High_Card(A,B))
        return Full_House(A)
    
    if(Flush(A) or Flush(A)):
        if(Flush(A) and Flush(A)):
            return(High_Card(A,B))
        return Flush(A)
    
    if(Straight(A) or Straight(B)):
        if(Straight(A) and Straight(B)):
            return(High_Card(A,B))
        return Straight(A)
    
    if(Three_of_a_Kind(A) or Three_of_a_Kind(B)):
        if(Three_of_a_Kind(A) and Three_of_a_Kind(B)):
            return(High_Card(A,B))
        return Three_of_a_Kind(A)
    
    if(Pairs(A)!=0 or Pairs(B)!=0):
        if(Pairs(A)==Pairs(B)):
            return(PairsEqual(A,B))
        return (Pairs(A)>Pairs(B))
    return High_Card(A,B)

def f():
    file=open("p054_poker.txt","r")
    S=file.readlines()
    L=[]
    for i in S:
        X=i.strip('\n').split(' ')
        A=X[:5]
        B=X[5:]
        L.append([A,B])
    total=0
    for i in L:
        if(Winner(i[0],i[1])):
            total+=1
    return total


    
A=["5H","6C","6S","6S","6D"]

A.sort(key=tri)
print(f())
