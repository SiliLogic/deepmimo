import deepmimo as dm
import numpy as np
import matplotlib.pyplot as plt

# ================= 1. 用户配置区域 =================
# 场景名称
SCENARIO_NAME = 'asu_campus_3p5'

# 【核心修改点】在这里输入你想画的矩阵名称
# 可选值参考下方的 keys 列表
TARGET_KEY = 'pathloss'  

# --- 可用 Key 列表 (复制到上面 TARGET_KEY) ---
# [基础矩阵]: 'power', 'phase', 'delay', 'aoa_az', 'aoa_el', 'aod_az', 'aod_el'
# [计算矩阵]: 'los', 'pathloss', 'distance', 'num_paths', 'power_linear', 'doppler'
# ==================================================

def get_plot_config(key):
    """
    定义每个数据类型的显示配置：单位、颜色映射(cmap)
    """
    configs = {
        # --- 基础矩阵 ---
        'power':      {'unit': 'dB', 'cmap': 'jet', 'desc': 'Received Power (Strongest Path)'},
        'phase':      {'unit': '°',  'cmap': 'hsv', 'desc': 'Phase (Strongest Path)'},
        'delay':      {'unit': 'ns', 'cmap': 'plasma', 'scale': 1e9, 'desc': 'Delay (Strongest Path)'}, # 自动转 ns
        'aoa_az':     {'unit': '°',  'cmap': 'twilight', 'desc': 'AoA Azimuth (Strongest Path)'},
        'aoa_el':     {'unit': '°',  'cmap': 'twilight', 'desc': 'AoA Elevation (Strongest Path)'},
        'aod_az':     {'unit': '°',  'cmap': 'twilight', 'desc': 'AoD Azimuth (Strongest Path)'},
        'aod_el':     {'unit': '°',  'cmap': 'twilight', 'desc': 'AoD Elevation (Strongest Path)'},
        
        # --- 计算矩阵 ---
        'los':        {'unit': 'Status', 'cmap': 'binary', 'desc': 'LOS Status (1=LOS, 0=NLOS)'},
        'pathloss':   {'unit': 'dB', 'cmap': 'viridis_r', 'desc': 'Path Loss'}, # _r 表示反转颜色，深色代表大损耗
        'distance':   {'unit': 'm',  'cmap': 'YlGnBu', 'desc': 'Distance TX-RX'},
        'num_paths':  {'unit': 'Count', 'cmap': 'cool', 'desc': 'Number of Paths'},
        'power_linear': {'unit': 'W', 'cmap': 'hot', 'desc': 'Linear Power'},
        'doppler':    {'unit': 'Hz', 'cmap': 'seismic', 'desc': 'Doppler Shift'}
    }
    return configs.get(key, {'unit': '', 'cmap': 'viridis', 'desc': key}) # 默认配置

# ================= 2. 数据加载与处理 =================
print(f"🔄 正在生成场景 [{SCENARIO_NAME}] 的数据...")
# 使用 generate 确保所有 computed 矩阵都存在
dataset = dm.generate(SCENARIO_NAME)

# 检查 key 是否存在
if not hasattr(dataset, TARGET_KEY):
    print(f"❌ 错误：在数据集中找不到属性 '{TARGET_KEY}'")
    print("请检查拼写，或者该数据未在此次配置中生成。")
    exit()

# 获取原始数据
raw_data = getattr(dataset, TARGET_KEY)
plot_config = get_plot_config(TARGET_KEY)

# --- 【智能数据适配逻辑】 ---
# 自动处理 1D 和 2D 数据，防止 Index Error
plot_data = None

if raw_data is None:
    print("❌ 数据为空。")
    exit()

# 1. 如果数据是多维的 (例如 [用户数, 路径数]) -> 取第0条路径 (通常是最强路径)
if raw_data.ndim > 1:
    print(f"ℹ️ 检测到多维数据 {raw_data.shape}，将提取第 0 条路径(最强径)进行绘制。")
    plot_data = raw_data[:, 0]
else:
    # 2. 如果数据是一维的 (例如 [用户数]) -> 直接使用
    print(f"ℹ️ 检测到一维数据 {raw_data.shape}，直接绘制。")
    plot_data = raw_data

# --- 特殊缩放处理 (例如 Delay 转 ns) ---
if 'scale' in plot_config:
    plot_data = plot_data * plot_config['scale']

# ================= 3. 绘图 =================
title_str = f"{plot_config['desc']} [{plot_config['unit']}]"

print(f"🎨 正在绘制: {title_str}")
try:
    dm.plot_coverage(
        dataset.rx_pos,
        plot_data,
        bs_pos=dataset.tx_pos.T,
        title=title_str,
        cmap=plot_config['cmap']
    )
    plt.show()
    print("✅ 完成！")
except Exception as e:
    print(f"❌ 绘图出错: {e}")