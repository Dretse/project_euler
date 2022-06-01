def f():
    n1=1
    n2=2
    S=2
    while (n2< 4000000):
       a=n1+n2
       n1=n2
       n2=a
       if(n2%2==0):
           S=S+n2
    return S

print(f())
