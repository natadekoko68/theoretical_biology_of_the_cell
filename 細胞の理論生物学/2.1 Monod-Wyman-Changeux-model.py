"""
T <--> R
hemogrobin 4-mer
"""
import numpy as np
import matplotlib.pyplot as plt

num = 100

n = 0

K_T = 0.0072
K_R = 0.24

T = np.zeros(num+1)
R = np.zeros(num+1)
O2 = np.zeros(num+1)

c = K_T/K_R

L0 = 1200
# L = np.array([L0*c**i for i in range(4)])
n=4
x = np.linspace(0,100,10000)
Y_tilde = (x*(1*x)**(n-1) + L0*c*x*(1+c*x)**(n-1))/((1+x)**n+L0*(1+c*x)**n)

plt.plot(x,Y_tilde)
plt.title("MWC model")
plt.xscale("log")
plt.xlabel("X")
plt.ylabel("$\\tilde{Y}$")
plt.show()


