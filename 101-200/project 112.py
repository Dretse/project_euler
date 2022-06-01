# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:03:13 2019

@author: DZBZ0373
"""
def up(n):
    for i in range(1,len(n)):
        if(int(n[i])<int(n[i-1])):return False
    return True

def down(n):
    for i in range(len(n)-1):
        if(int(n[i])<int(n[i+1])):return False
    return True

def bouncy(n):
    if(n<100):return False
    n=str(n)
    return not(up(n) or down(n))

i=50
p=0

while(p/(i-1) <0.99):
    if(bouncy(i)):
        #print(i)
        p+=1
    

    i+=1
print(i-1)

