import numpy as np
import matplotlib.pyplot as plt
import sys

"""
dA/dt = k_A * S - gamma_A * A
dI/dt = k_I * S - gamma_I * I
dR/dt = k_R * A * (R_T-R) - gamma_R * I * R
"""

num = 23000
delta = 0.01

# square wave
S = np.zeros(num + 1)
for i in range(len(S)):
    if 3000 <= i <= 14000:
        S[i] = 1
    else:
        S[i] = 0.1
plt.plot([delta * i for i in range(num + 1)], S)
plt.show()

# param #未完成TT
k_A = 5.8
k_I = 3.4
k_R = 2
gamma_A = 0.2
gamma_I = 0.2
gamma_R = 4
R_T = 1
A_init = 3
I_init = 2
R_init = 0.4

# for record
A = np.zeros(num + 1)
I = np.zeros(num + 1)
R = np.zeros(num + 1)
A[0] = A_init
I[0] = I_init
R[0] = R_init

for j in range(10):
    k_R = 0.3 * j
    gamma_R = 0.3 * j
    for i in range(0, num):
        dAdt = k_A * S[i] - gamma_A * A[i]
        dIdt = k_I * S[i] - gamma_I * I[i]
        dRdt = k_R * A[i] * (R_T - R[i]) - gamma_R * I[i] * R[i]
        A[i + 1] = A[i] + dAdt * delta
        I[i + 1] = I[i] + dIdt * delta
        R[i + 1] = R[i] + dRdt * delta
    plt.plot([delta * i for i in range(num + 1)], R, label="R")
    plt.ylim([0.2, 0.6])
    plt.legend()
    plt.show()
sys.exit()

# calculate
for i in range(0, num):
    dAdt = k_A * S[i] - gamma_A * A[i]
    dIdt = k_I * S[i] - gamma_I * I[i]
    dRdt = k_R * A[i] * (R_T - R[i]) - gamma_R * I[i] * R[i]
    A[i + 1] = A[i] + dAdt * delta
    I[i + 1] = I[i] + dIdt * delta
    R[i + 1] = R[i] + dRdt * delta
plt.plot([delta * i for i in range(num + 1)], A, label="A")
plt.plot([delta * i for i in range(num + 1)], I, label="I")
plt.legend()
plt.show()

plt.plot([delta * i for i in range(num + 1)], R, label="R")
plt.ylim([0.2, 0.6])
plt.legend()
plt.show()
