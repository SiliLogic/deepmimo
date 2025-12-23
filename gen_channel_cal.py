import deepmimo as dm
import numpy as np # 必需库，用于定义数组（如天线形状、旋转角度）

dataset = dm.generate('asu_campus_3p5')  # 这是从头生成
# dataset = dm.load("asu_campus_3p5")        # 这是加载之前生成过的缓存
# Get default channel parameters
ch_params = dm.ChannelParameters()

# Base station antenna parameters

# 1. 机械旋转 [x轴, y轴, z轴] (单位：度)
# 作用：模拟基站天线并不是正对着正前方的，而是有一定的倾斜。
# 这里表示：绕X轴转30度(下倾)，绕Y轴转40度，绕Z轴转30度。
ch_params.bs_antenna.rotation = np.array([30, 40, 30])

# 2. 视场角 (Field of View) [水平, 垂直] (单位：度)
# 作用：限制天线的覆盖范围。
# [360, 180] 表示这是一个全向覆盖的阵列，没有死角。
ch_params.bs_antenna.fov = np.array([360, 180])

# 3. 天线阵列形状 [行数, 列数]
# 作用：定义 MIMO 的规模。
# [8, 8] 表示这是一个 8行 x 8列 的平面阵列 (UPA)，总共 64 根天线。
ch_params.bs_antenna.shape = np.array([8, 8])

# 4. 天线间距 (单位：波长 λ)
# 0.5 是最经典的半波长间距，用于避免栅瓣 (Grating Lobes)。
ch_params.bs_antenna.spacing = 0.5

# User equipment antenna parameters
# 1. 用户天线形状
# [4, 2] 表示用户设备上有 4行 x 2列，总共 8 根天线。
ch_params.ue_antenna.shape = np.array([4, 2])

# 2. 辐射方向图 (Radiation Pattern)
# 'halfwave-dipole': 半波偶极子天线（最常用的全向性较好的天线模型）。
# 也可以设为 'isotropic' (理想全向点源)。
ch_params.ue_antenna.radiation_pattern = 'halfwave-dipole'

# Channel computation parameters
# 1. 开启频域模式
# True = 生成 OFDM 信道 (频域响应)。
# False = 生成 时域信道 (冲激响应 taps)。
ch_params.freq_domain = True

# 2. 系统带宽 (单位：Hz)
# 这里设为 1 MHz。带宽越大，时间分辨率越高。
ch_params.bandwidth = 1e6

# 3. OFDM 子载波总数 (FFT Size)
# 表示把带宽分成了 64 份。
ch_params.num_subcarriers = 64

# 4. 子载波筛选 (Downsampling)
# np.arange(32)*2 -> [0, 2, 4, ..., 62]
# 作用：虽然FFT大小是64，但我只想要偶数位置的子载波，一共取 32 个。
# 结果：生成的信道矩阵最后一维的大小将是 32，而不是 64。
ch_params.selected_subcarriers = np.arange(32)*2

# Generate channels

# 它利用dataset里的射线数据 + ch_params 里的天线定义 -> 算出复数矩阵 H
dataset.compute_channels(ch_params)

print(f'channel parameters = {ch_params}')

# 打印最终信道的形状
# 我们可以预测一下这个 shape 是多少：
# (用户总数, 接收天线数, 发射天线数, 子载波数量)
# (131931,      8,         64,         32      )
print(f'channel.shape = {dataset.channel.shape}')