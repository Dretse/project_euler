import numpy as np
import matplotlib.pyplot as plt

X0 = np.array([0,10.1])
V0 = np.array([1.4,-9.6]) - X0
#V0 /= np.linalg.norm(V0)

def find(X,V):
    #find X1
    g = V[1]/V[0]
    a,b,c = 4 + g**2, 2*(g*X[1] - X[0]*(g**2)), X[1]**2 + (X[0]*g)**2 - 2*X[1]*X[0]*g - 100

    d = b**2 - 4*a*c
    x_1, x_2 = (-1*b - np.sqrt(d))/(2*a), (-1*b + np.sqrt(d))/(2*a)
    if(np.abs(x_1-X[0])>np.abs(x_2-X[0])):
        x = x_1
    else : x = x_2
    y_1, y_2 = np.sqrt(100 - 4*(x**2)), -np.sqrt(100 - 4*(x**2))
    if(abs(V[1]*(x-X[0]) - V[0]*(y_1-X[1]))<abs(V[1]*(x-X[0]) - V[0]*(y_2-X[1]))):
        y = y_1
    else : y = y_2 
    X1= np.array([x,y])

    #Find V1
    M1 = np.array([4*x/y,1])
    M1/=np.linalg.norm(M1)
    V1 = V - 2*np.dot(V,M1)*M1
    #V1/=np.linalg.norm(V1)
    return X1,V1

n=0
X,V = find(X0,V0)
while(not(abs(X[0])<0.01 and X[1]>0)):
    X,V = find(X,V)
    n+=1

print(n,X)