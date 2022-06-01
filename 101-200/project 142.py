import numpy as np

Max = 1000
b=False
for i in range(3,Max):
    for j in range(i):
        if(i%2==j%2):
            x = int((i**2 + j**2)/2)
            y = int((i**2 - j**2)/2)
            if(x>y):
                for k in range(int(np.sqrt(x))):
                    z = int(x - k**2)
                    if(z<y):
                        if(np.sqrt(x+z)%1==0 and np.sqrt(y+z)%1==0 and np.sqrt(y-z)%1==0):
                            print(x+y+z,x,y,z)
                            b=True
                            break
        if(b):break
    if(b):break
    