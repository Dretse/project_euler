# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:53 2019

@author: DZBZ0373
"""
import numpy as np

target = 100
ways=np.zeros(target+1)
ways[0]= 1
 
for i in range(1,target+1):
    for j in range(i,target+1):
        ways[j] += ways[j - i]

print(int(ways[-1])-1)