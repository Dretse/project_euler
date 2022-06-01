from math import *

def valide(i,j,a,b):
    if(i==j or a==b or i%10==0):
        return False
    if(str(a) in str(i) and str(b) in str(j)):
        if(a==i%10 and b==j%10):
            return (i//10==j//10)
        if(a==i//10 and b==j%10):
            return (i%10==j//10)
        if(a==i%10 and b==j//10):
            return (i//10==j%10)
        if(a==i//10 and b==j//10):
            return (i%10==j%10)
    return False

        
def f():
    N=1
    D=1
    for i in range(10,100):
        for j in range(i+1,100):
            for a in range(1,10):
                for b in range(1,10):
                    if(i/j == a/b  and valide(i,j,a,b)):
                        N*= i
                        D*= j
                        print(i,"/",j,a,"/",b)


    return D//N
            



print(f())
