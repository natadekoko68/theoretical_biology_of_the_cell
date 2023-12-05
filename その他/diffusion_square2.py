import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

num = 10
values = np.zeros((num, num))
values[4,4] = 10
values[6,6] = 10

def update(frame):
    global values
    plt.clf()
    values = neighbor(values)
    visualize(values)

def neighbor(values):
    move_x = [1,-1,0,0]
    move_y = [0,0,1,-1]
    for i in range(num):
        for j in range(num):
            temp = values[i, j]
            for k in random.sample([i for i in range(4)],4):
                next_x = i + move_x[k]
                next_y = j + move_y[k]
                if (0 <= next_x < num) and (0 <= next_y < num):
                    if temp > values[next_x, next_y]:
                        delta = (temp - values[next_x, next_y])
                        temp -= delta * 0.1
                        values[next_x, next_y] += delta * 0.1
                    elif temp == values[next_x, next_y]:
                        pass
                    else:
                        delta = (values[next_x, next_y]-temp)
                        temp += delta *0.1
                        values[next_x, next_y] -= delta*0.1

    return values

def visualize(values):
    num = values.shape[0]
    for i in range(num):
        for j in range(num):
            plt.scatter(i,j,color=cm.Blues(values[i,j]))
    plt.show()

visualize(values)
for _ in range(30):
    values = neighbor(values)
    visualize(values)

