# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:20:07 2019

@author: DZBZ0373
068
149
"""
L1=[0,0,0,1,2,3,4,6,8]
L2=[1,4,9,6,5,6,9,4,1]
def Correct(L):
    for i in range(9):
        if not(L1[i] in L or L2[i] in L):
            if(not((L1[i] in [6,9] or L2[i] in [6,9]) and (6 in L or 9 in L))):
                return False
    return True

def Correct2(L,L_):
    for i in range(9):
        if(L1[i] not in [6,9] and L2[i] not in [6,9]):
            if not((L1[i] in L and L2[i] in L_) or (L1[i] in L_ and L2[i] in L)):
                return False
        else:
            b=L2[i] if L1[i] in [6,9] else L1[i]
            if(not((b in L and (6 in L_ or 9 in L_)) or (b in L_ and(6 in L or 9 in L)))):
                return False
            
            
    return True
def First_List():
    SET=[]
    for a in range(10):
        for b in range(a):
            for c in range(b):
                for d in range(c):
                    for e in range(d):
                        for f in range(e):
                            L=[a,b,c,d,e,f]
                            if(Correct(L)):
                                SET.append(L)
    return SET

def Second_List(SET1):
    SET2=[]
    for i in SET1:
        for a in range(10):
            for b in range(a):
                for c in range(b):
                    for d in range(c):
                        for e in range(d):
                            for f in range(e):
                                L=[a,b,c,d,e,f]
                                if(Correct2(L,i)):
                                    SET2.append(L)
    return SET2

SET=First_List()
print(len(SET))

SET2=Second_List(SET)

print(len(SET2)/2)