from math import *
import numpy as np
from copy import copy

def decompose():
    #200 100 50 20 10 5 2 1
    L=[]
    for one in range(2):
        for half in range(4):
            for tw in range(10):
                for ten in range(20):
                    for five in range(40):
                        for two in range(100):
                            if(one*100+half*50+tw*20+ten*10+five*5+two*2 <=200):
                                L.append([0,one, half, tw, ten, five, two, 200 - (one*100+tw*20+ten*10+five*5+two*2)])
    print("first list done")
    L.sort()
    print("Sort done")
    doubles=[]
    for i in range(len(L)-1):
        if(L[i]==L[i+1]):
                print(L[i])
                doubles.append(i)

    print("doubles detected")
    print(len(doubles))
    print(len(set(doubles)))
    print(L[:20])
    return (len(L)+7)
    
    
    

print(decompose())
