from math import *   # 2**5 
import numpy as np     # np.lincpace np.zeros
import matplotlib.pyplot as plt

def f(x,y):
    return x/y

a = 1
b = 3

n = 4
h = (b-a)/n

x = np.zeros(n+1)  # [0 0 0 0 0]
y = np.zeros(n+1)

x[0] = 1
y[0] = 2

for i in range(0,n):
    x[i+1] = a + (i+1)*h
    k1 = f(x[i],y[i])
    k2 = f(x[i] + (1/2)*h , y[i]+(1/2)*k1*h)
    k3 = f(x[i] + (1/2)*h , y[i]+(1/2)*k2*h)
    k4 = f(x[i] + h , y[i]+k3*h)
    y[i+1] = y[i] + (1/6)*h*(k1 + 2*k2 + 2*k3 +k4)

Y = np.sqrt(x**2 + 3)

plt.plot(x,Y, color ='g')  # sol Real
plt.plot(x,y,color = 'r')  # Sol Runge-Kutta
plt.show()
