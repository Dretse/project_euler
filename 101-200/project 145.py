import numpy as np
import matplotlib.pyplot as plt

def r(n):
    return int(str(n)[::-1])
def reversible(n):
    return (set(str(n))-{"1","3","5","7","9"}==set())
S=set()
tot=0
for n in range(12,10**9):
    if(n%1000000==0):print(n/10000000,"%")
    n_r = r(n)
    if(n%10!=0 and n_r>n and reversible(n+n_r)):
        S.add(n_r)
        S.add(n)
print(len(list(S)))
#608720