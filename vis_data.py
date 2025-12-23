import deepmimo as dm
import numpy as np

# ================= 1. 核心步骤：使用 generate =================
SCENARIO_NAME = 'asu_campus_3p5'

print(f"🔄 1. 正在生成场景数据: {SCENARIO_NAME} ...")
# 关键点：一定要用 generate，不要用 load。
# generate 会自动计算 Distance, Pathloss, LOS, Channel 等所有数据。
dataset = dm.generate(SCENARIO_NAME)

# ================= 2. 提取所有矩阵 (直接读取属性) =================
print("\n📦 2. 正在提取数据 (作为属性读取)...")

# --- A. 基础矩阵 (Fundamental) ---
# 这些是原始数据
data_warehouse = {
    'rx_pos': dataset.rx_pos,
    'tx_pos': dataset.tx_pos,
    'power': dataset.power,
    'phase': dataset.phase,
    'delay': dataset.delay,
    'aoa_az': dataset.aoa_az,
    'aoa_el': dataset.aoa_el,
    'aod_az': dataset.aod_az,
    'aod_el': dataset.aod_el,
}

# --- B. 计算矩阵 (Computed) ---
# 关键修改：直接访问属性，不要加括号 ()
# 如果 dataset 中没有这些属性，说明 generate 配置里没开，或者该场景不支持

# 1. LOS 状态
if hasattr(dataset, 'los'):
    data_warehouse['los'] = dataset.los
else:
    print("⚠️ Warning: 'los' not found.")

# 2. 路径损耗
if hasattr(dataset, 'pathloss'):
    # 有时是一维，有时是二维，统一转成 numpy 数组方便查看
    data_warehouse['pathloss'] = np.array(dataset.pathloss)
else:
    print("⚠️ Warning: 'pathloss' not found.")

# 3. 距离 (Distance)
if hasattr(dataset, 'distance'):
    data_warehouse['distance'] = dataset.distance
else:
    # 万一真的没有 distance 属性，我们可以手动算！(容错处理)
    print("ℹ️ 'distance' 属性未找到，正在手动计算几何距离...")
    # 计算公式：sqrt((x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2)
    # 假设单基站场景：tx_pos[0]
    tx = dataset.tx_pos[0] 
    rx = dataset.rx_pos
    dist = np.linalg.norm(rx - tx, axis=1) # 欧氏距离
    data_warehouse['distance'] = dist

# 4. 多径数量
if hasattr(dataset, 'num_paths'):
    data_warehouse['num_paths'] = dataset.num_paths

# 5. 信道矩阵 (Channel)
# 注意：Channel 矩阵可能非常大，打印 shape 即可
if hasattr(dataset, 'channel'):
    data_warehouse['channel'] = dataset.channel
    print(f"   [Channel Matrix] Loaded. Shape: {dataset.channel.shape}")
else:
    print("⚠️ Warning: 'channel' not found (Check if 'generate_channels' is True in parameters).")


# ================= 3. 打印结果清单 =================
print("\n✅ 数据提取完毕！当前内存中的数据矩阵清单：")
print("-" * 40)
print(f"{'Name':<15} | {'Shape/Dimension':<20}")
print("-" * 40)

for key, val in data_warehouse.items():
    if val is not None:
        try:
            shape_str = str(val.shape)
        except:
            shape_str = "Scalar/List"
        print(f"{key:<15} | {shape_str:<20}")

print("-" * 40)
print("提示：所有数据已保存在 'data_warehouse' 字典中。")