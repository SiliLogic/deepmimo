import deepmimo as dm
import numpy as np  # 【修复1】必须导入 numpy 才能用 np.array

# dataset = dm.load("asu_campus_3p5")
scen_name = 'asu_campus_3p5'

#1. 配置发射机 (TX)
#通常 TX Set 1 是合法的
# 字典格式：{ Set_ID : [该Set里的第几个基站] }
tx_sets_dict = {1: [0]}
# 2. 配置接收机 (RX) - 【关键修改】
# 原来的 {4: ...} 是错的，因为没有 4 号区域
# 我们改成 0 号区域，取前 10 个点
# 字典格式：{ Set_ID : [该Set里的用户索引列表] }
# np.arange(10) 生成 [0, 1, 2, ..., 9]
rx_sets_dict = {0: np.arange(1000, 1010)}

# Example 1 :加载数据
dataset1 = dm.load(
    scen_name,
    tx_sets=tx_sets_dict,     # 指定刚才定义的发射机
    rx_sets=rx_sets_dict,     # 指定刚才定义的接收机
    matrices=['rx_pos', 'aoa_az', 'aoa_el', 'inter_pos', 'inter'], # 【重要】只加载这几个矩阵
    max_paths=25              # 每个用户最多取10条路径
)

# ==========================================
# 请把这段代码加到你的文件最后面
# ==========================================

print("\n" + "="*30)
print("🎉 数据加载成功，开始展示结果")
print("="*30)

# 1. 看看加载了多少个用户？
# 预期输出: (10, 25) -> 10个用户，每个用户25条路径
if dataset1.aoa_az is not None:
    print(f"1. 水平方位角 (AoA Azimuth) 的形状: {dataset1.aoa_az.shape}")#维度解读 (10, 10)
    print(f"   数值预览 (第0个用户的前5条路径):\n   {dataset1.aoa_az[0, :5]}")
else:
    print("1. AoA Azimuth 未加载")

# 2. 看看交互点坐标 (Interaction Positions)
# 这通常用于画图，看射线撞到了哪里
if dataset1.inter_pos is not None:
    print(f"\n2. 交互点坐标矩阵形状: {dataset1.inter_pos.shape}")
    # 维度含义: (用户数, 路径数, 反射次数, xyz坐标)
else:
    print("2. 交互点坐标未加载")

# 3. 验证一下没加载的东西是否真的为空
# 因为我们在 matrices 里没写 'power'，所以这里应该是 None
if dataset1.power is None:
    print("\n3. 验证成功：Power 属性为 None (因为我们没请求加载它)")
else:
    print(f"\n3. Power 竟然加载了？形状: {dataset1.power.shape}")

# # Example 2: Load all points of specific TX/RX sets using lists
# dataset2 = dm.load(scen_name, tx_sets=[1], rx_sets=[0])

# # Example 3: Load all TX/RX sets (default)
# dataset3 = dm.load(scen_name, tx_sets='all', rx_sets='all')
