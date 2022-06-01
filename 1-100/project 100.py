# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:03:55 2019

@author: admin
"""
from decimal import *

a=4684660
while(a<10**12):
    a=a*5.82842
print(a)
a=int(a)
#a=10**12 + 527* 100000

while(Decimal(1+(2*a*(a-1))).sqrt()%2!=1): 
    a+=1
    if(a%100000==0):
        print((a-10**12)//100000,end=" ")

print(a)
b= (Decimal(1+(2*a*(a-1))).sqrt()+1)/2
print(b)
print((b/a)*((b-1)/(a-1)))