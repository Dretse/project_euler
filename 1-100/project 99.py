# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:51:53 2019

@author: admin
"""
import numpy as np

#E(nlog(a))=a^n
file=open("p099_base_exp.txt")
L=[[int(j) for j in i.strip().split(',')] for i in file.readlines()]
file.close()
L_val=[i[1]*np.log(i[0]) for i in L]

print(L_val.index(max(L_val))+1)
