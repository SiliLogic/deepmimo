import deepmimo as dm
from scipy.io import savemat
import numpy as np

# 1. 加载数据集
# 请确保 'asu_campus_3p5' 文件夹在当前目录下
dataset = dm.load("asu_campus_3p5")

# ===== [核心修改] 按照 Core Properties 表格补全属性 =====

# 准备要保存的数据字典
data_to_save = {
    # --- 位置信息 (Locations) ---
    # 建议将键名修改为 tx_pos/rx_pos 以匹配官方表格
    "tx_pos": np.array(dataset.tx_pos),      # 对应表格: tx_pos
    "rx_pos": np.array(dataset.rx_pos),      # 对应表格: rx_pos

    # --- 路径物理属性 (这是你代码里缺失的重要部分) ---
    "power": np.array(dataset.power),        # 对应表格: power (路径功率 dBm)
    "phase": np.array(dataset.phase),        # 对应表格: phase (路径相位)
    "delay": np.array(dataset.delay),        # 对应表格: delay (路径延迟 s)

    # --- 角度信息 (Angles) ---
    "aoa_az": np.array(dataset.aoa_az),
    "aoa_el": np.array(dataset.aoa_el),
    "aod_az": np.array(dataset.aod_az),
    "aod_el": np.array(dataset.aod_el),

    # --- 交互信息 (Interactions) ---
    "inter": np.array(dataset.inter),        # 对应表格: inter (交互类型, 如反射/绕射)
    "inter_pos": np.array(dataset.inter_pos),# 对应表格: inter_pos (交互点坐标)

    # --- 其他计算/辅助信息 ---
    "los": np.array(dataset.los),            # LoS 指示器
    
    # 信道冲激响应 (复数) - 这是一个计算属性
    "channels": dataset.compute_channels(),
    # 路径损耗
    "pathloss": dataset.compute_pathloss()
}

# ===== 保存为 .mat 文件 =====
# 移除 dtype=object 可以让 MATLAB 读取为标准矩阵，除非你的路径数是不定长的
savemat("dataset_full.mat", data_to_save)

print("保存成功: dataset_full.mat")
print(f"包含接收机数量: {len(dataset.rx_pos)}")