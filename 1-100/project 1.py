def f(n):
    S=0
    for i in range(n):
        if(i%3==0 or i%5==0):
            S=S+i
    return S

print(f(1000))
