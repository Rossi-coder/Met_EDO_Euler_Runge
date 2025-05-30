from math import *
import matplotlib.pyplot as plt 
import numpy as np

def f(x,y):
    return x/y

a = 1
b = 3
N = 4
h = (b-a)/N

x = np.zeros(N+1)
y = np.zeros(N+1)


x[0] = 1
y[0] = 2

for i in range(0,N):
    print(i)
    x[i+1] = a + (i+1)*h
    y[i+1]=y[i]+h*f(x[i],y[i])
    
plt.plot(x,y)
plt.show()
