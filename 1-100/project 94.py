# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:22:45 2019

@author: DZBZ0373
"""
import numpy as np

def pgcd(a,b):
    while(True):
        if(a%b==0):
            return b
        elif(a%b==1):
            return 1
        a,b=b,a%b


m=1
max_p=1
L=[]
#m max = 10864
while(max_p<1000000000 and m<10865):
    m+=1
    add=(m+1)%2
    for k in range(m//2):
        if(add==1 or k!=0):
            n=2*k + add
            if((n+m)%2==1 and pgcd(m,n)==1 ):
                b=m**2 - 3*( n**2) -1
                c=4*m*n -(m**2 + n**2) +1
    
                if(b==0):
                    max_p=4*(m**2)
                    L.append(max_p)
                    print("b:\t",m,n,b,":\t",max_p)
                if(c==0):
                    max_p=2*((m+n)**2)
                    L.append(max_p)
                    print("c:\t",m,n,c,":\t",max_p)
print("\n\n",L)



#L=[16, 50, 196, 722, 2704, 10082, 37636, 140450, 524176, 1956242, 7300804, 27246962, 101687056, 379501250]

print(sum(L))


