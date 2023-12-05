import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def main(num = 20):
    px = 1
    py = px * math.sqrt(3) / 2
    l = px / math.sqrt(3)
    mesh_list = [[x, y] for x in range(num) for y in range(num)]
    a = np.zeros((num, num, 3))

    for x, y in mesh_list:
        cx = x * px if y % 2 == 0 else (x + 0.5) * px
        cy = y * py

        lw = 0.1
        plt.plot([cx - px / 2, cx - px / 2], [cy - l / 2, cy + l / 2], 'k', lw=lw)
        plt.plot([cx + px / 2, cx + px / 2], [cy - l / 2, cy + l / 2], 'k', lw=lw)
        plt.plot([cx - px / 2, cx], [cy + l / 2, cy + l], 'k', lw=lw)
        plt.plot([cx, cx + px / 2], [cy + l, cy + l / 2], 'k', lw=lw)
        plt.plot([cx - px / 2, cx], [cy - l / 2, cy - l], 'k', lw=lw)
        plt.plot([cx, cx + px / 2], [cy - l, cy - l / 2], 'k', lw=lw)
        plt.scatter(cx,cy,color=cm.Blues(x/num))

    print(a)
    print(a[10])
    plt.axis("off")
    plt.savefig("/Users/kotaro/Desktop/test.jpg", dpi=500)
    plt.show()
#
#
# main()

def neighbor(values,i,j):
    temp = [0, 0, 0, 0, 0, 0]
    if j % 2 == 0:
        if (0 <= i-1 < num) and (0 <= j-1 < num):
            temp[0] = values[i-1, j-1]
        if (0 <= i < num) and (0 <= j-1 < num):
            temp[1] = values[i, j-1]
        if (0 <= i-1 < num) and (0 <= j < num):
            temp[2] = values[i-1, j]
        if (0 <= i+1 < num) and (0 <= j < num):
            temp[3] = values[i+1, j]
        if (0 <= i-1 < num) and (0 <= j+1 < num):
            temp[4] = values[i-1, j+1]
        if (0 <= i < num) and (0 <= j+1 < num):
            temp[5] = values[i, j+1]
    if j % 2 == 1:
        if (0 <= i < num) and (0 <= j-1 < num):
            temp[0] = values[i, j-1]
        if (0 <= i+1 < num) and (0 <= j-1 < num):
            temp[1] = values[i+1, j-1]
        if (0 <= i-1 < num) and (0 <= j < num):
            temp[2] = values[i-1, j]
        if (0 <= i+1 < num) and (0 <= j < num):
            temp[3] = values[i+1, j]
        if (0 <= i < num) and (0 <= j+1 < num):
            temp[4] = values[i, j+1]
        if (0 <= i+1 < num) and (0 <= j+1 < num):
            temp[5] = values[i+1, j+1]
    cnt = 0
    for c in temp:
        if c != 0:
            cnt += 1
    p = (values[i, j] + sum(temp))/(1+cnt)
    values[i, j] = p
    if j % 2 == 0:
        if (0 <= i-1 < num) and (0 <= j-1 < num):
            values[i-1, j-1] = p
        if (0 <= i < num) and (0 <= j-1 < num):
            values[i, j-1] = p
        if (0 <= i-1 < num) and (0 <= j < num):
            values[i-1, j] = p
        if (0 <= i+1 < num) and (0 <= j < num):
            values[i+1, j] = p
        if (0 <= i-1 < num) and (0 <= j+1 < num):
            values[i-1, j+1] = p
        if (0 <= i < num) and (0 <= j+1 < num):
            values[i, j+1] = p
    if j % 2 == 1:
        if (0 <= i < num) and (0 <= j-1 < num):
            values[i, j-1] = p
        if (0 <= i+1 < num) and (0 <= j-1 < num):
            values[i+1, j-1] = p
        if (0 <= i-1 < num) and (0 <= j < num):
            values[i-1, j] = p
        if (0 <= i+1 < num) and (0 <= j < num):
            values[i+1, j] = p
        if (0 <= i < num) and (0 <= j+1 < num):
            values[i, j+1] = p
        if (0 <= i+1 < num) and (0 <= j+1 < num):
            values[i+1, j+1] = p
    return temp

num = 10
mesh_list = [[x, y] for x in range(num) for y in range(num)]
values = np.zeros((num, num))
values[4, 4] = 1
values[1, 0] = 1
# print(values)

def main(values):
    num = values.shape[0]
    px = 1
    py = px * math.sqrt(3) / 2
    l = px / math.sqrt(3)
    mesh_list = [[x, y] for x in range(num) for y in range(num)]
    a = np.zeros((num, num, 3))

    for x, y in mesh_list:
        cx = x * px if y % 2 == 0 else (x + 0.5) * px
        cy = y * py
        lw = 0.1
        plt.plot([cx - px / 2, cx - px / 2], [cy - l / 2, cy + l / 2], 'k', lw=lw)
        plt.plot([cx + px / 2, cx + px / 2], [cy - l / 2, cy + l / 2], 'k', lw=lw)
        plt.plot([cx - px / 2, cx], [cy + l / 2, cy + l], 'k', lw=lw)
        plt.plot([cx, cx + px / 2], [cy + l, cy + l / 2], 'k', lw=lw)
        plt.plot([cx - px / 2, cx], [cy - l / 2, cy - l], 'k', lw=lw)
        plt.plot([cx, cx + px / 2], [cy - l, cy - l / 2], 'k', lw=lw)
        if values[x,y] < 0:
            values[x, y] = 0
        if values[x,y] > 1:
            values[x,y] = 1
        plt.scatter(cx,cy,color=cm.Blues(values[x,y]))

    plt.axis("off")
    # plt.savefig("/Users/kotaro/Desktop/test.jpg", dpi=500)
    plt.show()

# for _ in range(2):
#     temp = np.zeros((num, num))
#     for i in range(num):
#         for j in range(num):
#             temp[i, j] = values[i,j] + (sum(neighbor(values, i, j))/6)
#     values = temp
# main(values)


fig = plt.figure()
ani = FuncAnimation(fig, update, frames=30, interval=500, repeat=False)

# Save the animation as a GIF
ani.save('animation.gif', writer='imagemagick')


