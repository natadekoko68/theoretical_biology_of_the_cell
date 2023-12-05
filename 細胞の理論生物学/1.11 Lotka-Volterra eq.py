
"""
Lotka-Volterra eq.
dx/dt = ax-bxy
dy/dt = czy -dy
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

a, b, c, d = 0.2, 0.2, 0.2, 0.5

num = 30000
delta = 0.01

x_init = 1
y_init = 1

x = np.zeros(num+1)
x[0] = x_init

y = np.zeros(num+1)
y[0] = y_init

for i in range(num):
    dxdt = a * x[i] - b * x[i] * y[i]
    dydt = c * x[i] * y[i] - d * y[i]
    x[i+1] = x[i] + dxdt * delta
    y[i+1] = y[i] + dydt * delta

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("The relationship between x and y")
plt.show()

plt.plot([delta*i for i in range(num+1)],x,label="x")
plt.plot([delta*i for i in range(num+1)],y,label="y")
plt.legend()
plt.xlabel("time")
plt.ylabel("value")
plt.title("Chronological transition of x,y")
plt.show()