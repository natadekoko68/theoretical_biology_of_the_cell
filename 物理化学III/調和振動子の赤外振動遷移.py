import math
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.special import eval_hermite

a = np.linspace(-10, 10, 100)

def u(n,x,b=1):
    return (1/(np.pi*b**2)*1/4)*(1/np.sqrt(2**n*math.factorial(n)))*np.exp(-x**2/2/b**2)*eval_hermite(n, x/b)

def ivt(i,f,x):
    return u(i,x)*u(f,x)*x

def plt_ivt(i,f,x_min=-10,x_max=10,num=100000):
    a = np.linspace(x_min,x_max,num)
    plt.plot(a,ivt(i,f,a))
    max_a = max(ivt(i,f,a))
    sumi = sum(ivt(i,f,a))
    if sumi <= 10*-10:
        print("禁制")
    else:
        print("許容")
    plt.title("v="+str(i)+"$\leftrightarrow$"+str(f)+"の遷移の強さ")
    plt.ylim([-max_a*3,max_a*3])
    plt.tick_params(bottom=False, left=False, right=False, top=False)
    plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
    plt.show()

plt_ivt(1,3)