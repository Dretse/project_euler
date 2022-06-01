# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:12:39 2019

@author: DZBZ0373
"""
def Sq(xa,xb,ya,yb):
    a=xa**2 + ya**2
    b=xb**2 + yb**2
    c=(xa-xb)**2 + (ya-yb)**2
    
    if(a+b==c or a+c==b or b+c==a):
        return True
    return False
    
m=50

S=0
for xa in range(m+1):
    print(xa,end="\t")
    for xb in range(xa+1):
        for yb in range(m+1):
            for ya in range(yb+1):
                if((xa!=0 or ya!=0) and (xb!=0 or yb!=0) and (xa-xb!=0 or ya-yb!=0)):
                    if(Sq(xa,xb,ya,yb)):
                        #print(xa,ya,',',xb,yb)
                        S+=1
print("\n",S)