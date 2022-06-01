from math import *
import numpy as np

def pen(n):
    return(int(n*(3*n-1)/2))
def is_pen(n):
    a=(1+sqrt(1+24*n))/6
    return(a%1==0)
           
def f(n):

    for j in range(1,n):
        
        if(j%(n//100)==0):
            print(j//(n//100))

        for i in range(j+1,n):
            if(is_pen(pen(i)+pen(j)) and is_pen(pen(i)-pen(j))):
                print(i,j,"success")
                return(pen(i)-pen(j))
# c'est loooooooooooong
print(f(2500))
