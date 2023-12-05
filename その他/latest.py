from PIL import Image, ImageDraw
import tqdm
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

def visualize(values,cnt=0):
    num = values.shape[0]
    for i in range(num):
        for j in range(num):
            plt.scatter(i, j, color=cm.Blues(values[i,j]))
    plt.axis("off")
    plt.savefig("test"+str(cnt)+".jpg")
    # plt.show()

num = 10
values = np.zeros((num, num))
values[4,4] = 10
# values[1,9] = 0

ims = []
cnt1 = 1
visualize(values,cnt=cnt1)
im = Image.open("test"+str(cnt1)+".jpg").quantize()
ims.append(im)

for c in tqdm.tqdm(range(100)):
    values = neighbor(values)
    cnt1 += 1
    visualize(values, cnt=cnt1)
    im = Image.open("test"+str(cnt1)+".jpg").quantize()
    ims.append(im)

im = Image.open("test1.jpg")
ims[0].save('test.gif', save_all=True,
               append_images=ims[1:], optimize=False, duration=100, loop=0)