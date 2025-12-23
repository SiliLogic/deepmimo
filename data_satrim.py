import deepmimo as dm

# ==========================================
# 0. 加载原始数据集 (公共基础)
# ==========================================
dataset = dm.load("asu_campus_3p5")
print(f"【原始】用户数量: {dataset.rx_pos.shape[0]}")


# ==========================================
# 实验 A: 单独测试 "均匀采样" (Uniform Sampling)
# ==========================================
print("\n--- 实验 A: 仅进行空间均匀采样 ---")

# 在原始数据集上获取均匀采样索引
# [2, 2] 表示每隔1个点取1个
uniform_idxs = dataset.get_uniform_idxs([2, 2])

# 生成仅经过采样的新数据集
dataset_sampled = dataset.subset(uniform_idxs)

print(f"实验 A 结果 (Sampling Only): {dataset_sampled.rx_pos.shape[0]}")
# 此时 dataset_sampled 包含无效用户(在建筑物内的)，只是密度变稀疏了


# ==========================================
# 实验 B: 单独测试 "移除无效用户" (Trimming Active)
# ==========================================
print("\n--- 实验 B: 仅移除无效用户 (保留 Active) ---")

# 在原始数据集上获取活跃用户索引
# 这一步会检查 dataset 中哪些用户有有效的信道
active_idxs_raw = dataset.get_active_idxs()

# 生成仅移除无效用户的新数据集
dataset_active_only = dataset.subset(active_idxs_raw)

print(f"实验 B 结果 (Active Only): {dataset_active_only.rx_pos.shape[0]}")
# 此时 dataset_active_only 密度很高(原始密度)，但剔除了所有无信号的用户


# ==========================================
# (可选) 实验 C: 组合操作 (先采样，再移除)
# ==========================================
print("\n--- 实验 C: 组合操作 (采样 + 移除) ---")

# 1. 先利用实验 A 得到的 dataset_sampled
# 2. 对 dataset_sampled 进行活跃用户检测
# 注意：必须在 dataset_sampled 上调用 get_active_idxs，不能用原始的
active_idxs_sampled = dataset_sampled.get_active_idxs()

dataset_final = dataset_sampled.subset(active_idxs_sampled)

print(f"实验 C 结果 (Final): {dataset_final.rx_pos.shape[0]}")