from math import *

def f():
    for a in range(1,334):
        for b in range(a,500):
            if(a*a + b*b == (1000-a-b)*(1000-a-b)):
               return(a*b*(1000-a-b))

    
print(f())
    
