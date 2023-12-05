import numpy as np

"""
dD1/dt=a-bD1-cN1D2
dD2/dt=a-bD2-cN2D1
"""


def delta_notch(a, b, c, N1, D1_init, N2, D2_init, delta=10 * -5, n_iter=10 ** 5):
    Ds = np.zeros((n_iter+1, 2))
    D1 = D1_init
    D2 = D2_init
    Ds[0, 0] = D1
    Ds[0, 1] = D1
    for i in range(n_iter):
        dD1_dt = a - b * D1 - c * N1 * D2
        dD2_dt = a - b * D2 - c * N2 * D1
        D1 = dD1_dt * delta + D1
        D2 = dD2_dt * delta + D2
        if D1 < 0:
            D1 = 0
        if D2 < 0:
            D2 = 0
        Ds[i + 1, 0] = D1
        Ds[i + 1, 1] = D2
    return Ds

# print(delta_notch(0.5, 1, 1, 0.1, 0.1, 0.1, 0.1,delta=10 * -1, n_iter=10 ** 3))
for i in range(100):
    print(i,delta_notch(0.11000000000001, 1, 1, 0.1, 0.1, 0.1, 0.1, delta=10 * -1, n_iter=10 ** 3)[-1])