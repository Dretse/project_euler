from math import *


    
    
def f():
    #x=a^n avec x qui a n digits
    #a<10 a>3
    tot=0
    t2=-1
    n=1
    while(t2!=tot):
        t2=tot
        for a in range(1,10):
            if(len(str(a**n))==n):
                tot+=1
        n+=1
    return tot
    #+10 pour ^1, +6 pour ^2, +5 pour ^3, +4 pour ^4, +3 ^5, +3 ^6 , +2 ^7, +2 ^8, +2 ^9
print(f())
    


