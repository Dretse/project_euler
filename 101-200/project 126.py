# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:34:36 2019

@author: DZBZ0373
"""
import numpy as np

def vols(x,y,z,n):
    L=[]
    a=x*y*z
    Sx,ly=y*z,y
    #print(a,Sx,ly*hy,lz*hz)
    while(a<=n):
        L.append(a)
        a=2*(Sx + ly*x + z*x)
        Sx+=2*(ly +z)
        ly+=2
        #print(a,Sx,ly*hy,lz*hz)
    return L[1:]



def find_them_all(maxi):
    L=np.zeros(maxi+1).astype(int)
    for x in range(1,maxi//4 +1):
        if(x%1000==0):print(x//1000,end=" ")
        for y in range(1,x+1):
            if(x*y<=maxi):
                for z in range(1,y+1):
                    if(x*y*z<=maxi):
                        u=vols(x,y,z,maxi)
                        for i in u:
                            L[i]+=1
                    else:break
            else:break
    print()
    return list(L)


L=find_them_all(200000)
U=[(i,L[i]) for i in range(len(L)) if L[i]==1000]
U.sort(key=lambda x : x[0])
print(U[0][0])

#18522