import deepmimo as dm
from scipy.io import savemat
import numpy as np

# ==========================================
# 辅助函数：将 Dataset 对象保存为 .mat 文件
# ==========================================
def save_dataset_to_mat(dataset_obj, filename, description):
    """
    输入: DeepMIMO dataset 对象, 文件名, 描述信息
    输出: 保存 .mat 文件
    """
    print(f"\n正在处理并保存: {description} ...")
    
    # 1. 提取基础属性
    # 注意: los 和 pathloss 需要 reshape 为 (N, 1) 以便在 MATLAB 中显示为纵向向量
    try:
        los_data = np.array(dataset_obj.los).reshape(-1, 1)
        pathloss_data = np.array(dataset_obj.compute_pathloss()).reshape(-1, 1)
        channels_data = dataset_obj.compute_channels() # 复数信道
    except Exception as e:
        print(f"计算信道或 Pathloss 时出错: {e}")
        return

    data_to_save = {
        # --- 位置信息 ---
        "tx_pos": np.array(dataset_obj.tx_pos),
        "rx_pos": np.array(dataset_obj.rx_pos),

        # --- 路径物理属性 ---
        "power": np.array(dataset_obj.power),
        "phase": np.array(dataset_obj.phase),
        "delay": np.array(dataset_obj.delay),

        # --- 角度信息 ---
        "aoa_az": np.array(dataset_obj.aoa_az),
        "aoa_el": np.array(dataset_obj.aoa_el),
        "aod_az": np.array(dataset_obj.aod_az),
        "aod_el": np.array(dataset_obj.aod_el),

        # --- 交互信息 ---
        "inter": np.array(dataset_obj.inter),
        "inter_pos": np.array(dataset_obj.inter_pos),

        # --- 计算属性 (已修正维度) ---
        "los": los_data,
        "pathloss": pathloss_data,
        "channels": np.array(channels_data, dtype=object)
    }

    # 2. 保存
    savemat(filename, data_to_save)
    print(f"✅ 已保存: {filename}")
    print(f"📊 用户数量: {dataset_obj.rx_pos.shape[0]}")


# ==========================================
# 主程序
# ==========================================

# 0. 加载原始数据集
print("正在加载原始数据集...")
dataset = dm.load("asu_campus_3p5")
print(f"【原始】用户数量: {dataset.rx_pos.shape[0]}")

# ==========================================
# 实验 A: 仅进行空间均匀采样 (Uniform Sampling)
# ==========================================
print("\n--- 实验 A: 仅进行空间均匀采样 ---")
uniform_idxs = dataset.get_uniform_idxs([2, 2]) # 采样率 [2, 2]
dataset_A = dataset.subset(uniform_idxs)

# 导出实验 A 数据
save_dataset_to_mat(dataset_A, "exp_A_sampled.mat", "实验 A (Sampling Only)")


# # ==========================================
# # 实验 B: 仅移除无效用户 (Active Only)
# # ==========================================
# print("\n--- 实验 B: 仅移除无效用户 ---")
# active_idxs_raw = dataset.get_active_idxs()
# dataset_B = dataset.subset(active_idxs_raw)

# # 导出实验 B 数据
# save_dataset_to_mat(dataset_B, "exp_B_active.mat", "实验 B (Active Only)")


# ==========================================
# 实验 C: 组合操作 (采样 + 移除)
# ==========================================
print("\n--- 实验 C: 组合操作 (采样 + 移除) ---")
# 注意：基于 dataset_A (已经采样过的数据) 进行 Active 检测
active_idxs_sampled = dataset_A.get_active_idxs()
dataset_C = dataset_A.subset(active_idxs_sampled)

# 导出实验 C 数据
save_dataset_to_mat(dataset_C, "exp_C_final.mat", "实验 C (Final Combined)")

print("\n========================================")
print("所有实验运行完毕，已生成三个 .mat 文件。")