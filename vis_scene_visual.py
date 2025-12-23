import deepmimo as dm
import matplotlib.pyplot as plt

# Load scenario
dataset = dm.load('asu_campus_3p5')

# Plot the scene
# 这一步会生成默认的标题（比如 "Buildings: 35..."）
dataset.scene.plot()

# --- 修改标题的核心代码 ---
# 使用 matplotlib 的 title 函数覆盖默认标题
plt.title("DeepMIMO Scene Example: ASU Campus 3.5 GHz (Buildings: 35, Terrain: 1)")

# 显示图像
plt.show()