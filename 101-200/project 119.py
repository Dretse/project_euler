# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:31:59 2019

@author: DZBZ0373
"""
L=[]
for a in range(2,500):
    s=a**2
    i=2
    while(s< 1000000000000000):
        if(sum([int(x) for x in str(s)])==a):
            #print(a,"^",i,"=",s)
            L.append(s)
        s*=a
        i+=1
L.sort()
print(L[-1])