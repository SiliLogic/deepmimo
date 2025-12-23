import deepmimo as dm
import numpy as np
import matplotlib.pyplot as plt  # <--- 1. 引入画图库

# Load scenario
dataset = dm.load('asu_campus_3p5')

# Plot ray paths for user with most paths
user_idx = np.argmax(dataset.num_paths)

# 这里是画图指令
dm.plot_rays(dataset.rx_pos[user_idx],
             dataset.tx_pos[0],
             dataset.inter_pos[user_idx],
             dataset.inter[user_idx],
             proj_3D=True,
             color_by_type=True)

# --- 两种选择 ---

# 选择 A: 直接弹窗显示（不保存，手动截图或点击保存按钮）
plt.show()

# 选择 B: 自动保存到当前文件夹（不弹窗，或者弹窗前保存）
# plt.savefig('my_ray_tracing.png', dpi=300)  # 去掉注释就能保存了