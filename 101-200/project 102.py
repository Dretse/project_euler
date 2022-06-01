# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:15:05 2019

@author: admin
"""


def Eq(x0,x1,y0,y1):
    if(x0==x1):
        return (1,-x0,0)
    else:
        a=(y0-y1)/(x0-x1)
        return(a,y0-a*x0,1)

def Is_In(L):
    xa,ya,xb,yb,xc,yc=L
    a,b,c=Eq(xa,xb,ya,yb)
    if(((a*xc+b-c*yc)*b)<=0):return False
    
    a,b,c=Eq(xa,xc,ya,yc)
    if(((a*xb+b-c*yb)*b)<=0):return False
    
    a,b,c=Eq(xc,xb,yc,yb)
    if(((a*xa+b-c*ya)*b)<=0):return False
    return True

file=open("p102_triangles.txt")
L=file.readlines()
file.close()
L=[[int(j) for j in i.strip().split(',')] for i in L]
S=0
for i in L:
    if(Is_In(i)):
        S+=1
print(S)
