# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:12:33 2019

@author: DZBZ0373
chains de markov
"""
import numpy as np
from random import randint
np.set_printoptions(precision=2)

CC=[0,10]
CH=[0,10,11,39,24,5,-3,-2,-2,-4]

M=np.zeros((40,40))

#dice_proba=np.array([0,0,1,2,3,4,5,6,5,4,3,2,1])/36
dice_proba=np.array([0,0,1,2,3,4,3,2,1])/16

for i in range(40):
    for j in range(len(dice_proba)):
        M[i,(i+j)%40]+=dice_proba[j]

#doubles
#p=1/(6*6*6)
p=1/(4*4*4)

for i in range(40):
    if(i!=10):
        M[:,10]+=M[:,i]*p
        M[:,i]*=(1-p)

#CC
M[:,0]+=(M[:,2]+M[:,17]+M[:,33])/16
M[:,10]+=(M[:,2]+M[:,17]+M[:,33])/16
M[:,2]*=7/8
M[:,17]*=7/8
M[:,33]*=7/8

#CH
M[:,0]+=(M[:,7]+M[:,22]+M[:,36])/16
M[:,10]+=(M[:,7]+M[:,22]+M[:,36])/16
M[:,11]+=(M[:,7]+M[:,22]+M[:,36])/16
M[:,24]+=(M[:,7]+M[:,22]+M[:,36])/16
M[:,39]+=(M[:,7]+M[:,22]+M[:,36])/16
M[:,5]+=(M[:,7]+M[:,22]+M[:,36])/16

M[:,15]+=M[:,7]/8
M[:,5]+=M[:,22]/8
M[:,25]+=M[:,36]/8

M[:,12]+=M[:,7]/16
M[:,28]+=M[:,22]/16
M[:,12]+=M[:,36]/16

M[:,4]+=M[:,7]/16
M[:,19]+=M[:,22]/16
M[:,33]+=M[:,36]/16

M[:,7]*=3/8
M[:,22]*=3/8
M[:,36]*=3/8

#G2J
M[:,10]+=M[:,30]
M[:,30]*=0

for i in range(10):
    M=np.dot(M,M)


L=list(np.sum(M,axis=0))
print([L.index(i) for i in sorted(L)[-10:]])

for i,v in enumerate(L):
    print(i,':',int(v*1000)/400,end='   \t')
    if(i%5==0):
        print()
        

