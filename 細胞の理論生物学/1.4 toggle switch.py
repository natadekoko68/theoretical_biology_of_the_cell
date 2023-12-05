import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

output_path = "/Users/kotaro/Desktop/"

# パラメータ
alpha = 3.0
width = 2
grid_size = 0.08

# プロット
p1, p2 = np.meshgrid(np.arange(0, width + grid_size, grid_size), np.arange(0, width + grid_size, grid_size))
u, v = alpha / (1 + p2 ** 2) - p1, alpha / (1 + p1 ** 2) - p2

plt.title("トグルスイッチ($\\alpha$= " + str(alpha) + ")")
plt.xlabel("p1")
plt.ylabel("p2")
plt.quiver(p1, p2, u, v, color="r")
plt.tight_layout()
plt.savefig(output_path + "toggle.jpg", dpi=300)
plt.show()

# ヌルクライン
p1, p2 = np.meshgrid(np.arange(0, width + grid_size, grid_size), np.arange(0, width + grid_size, grid_size))
u, v = alpha / (1 + p2 ** 2) - p1, alpha / (1 + p1 ** 2) - p2
x = np.linspace(0, width, 100)

plt.title("互いに抑制し合う2遺伝子系とヌルクライン")
plt.xlabel("p1")
plt.ylabel("p2")
plt.quiver(p1, p2, u, v, color="r")
plt.plot(x, x, color="blue")
plt.show()
