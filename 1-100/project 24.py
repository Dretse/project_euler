from math import *


def f():
    n=362880*2 + 40320*6 + 5040*6
    for i in range(2780000000,9876543211):
        A=str(i)
        if(len(set(A))==len(A)):
            n+=1

            if(n==1000000):
                return (i)          
    return (n)
#pencil paper
print(f())

