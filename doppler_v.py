import numpy as np
import deepmimo as dm
from scipy.io import savemat

# ===========================================================
# 1. Load DeepMIMO dataset
# ===========================================================
dataset = dm.load("asu_campus_3p5")
print(f"Number of UEs: {dataset.n_ue}")
print(f"Max paths per UE: {dataset.max_paths}")

# ===========================================================
# 2. (A) Set UE velocity — same for all users
# ===========================================================

# dataset.rx_vel = [5, 0, 0]  # 所有用户朝 x 方向以 5 m/s 移动
# print("UE velocity (same for all):", dataset.rx_vel)

# ===========================================================
# 3. (B) Set UE velocity — different for each UE
# ===========================================================

min_speed, max_speed = 0, 10  # m/s

# 创建 n_ue × 3 的速度矩阵
random_velocities = np.zeros((dataset.n_ue, 3))

# x, y 方向0~10m/s的随机速度；z 保持 0（假设用户在地面）
random_velocities[:, :2] = np.random.uniform(
    min_speed, max_speed, size=(dataset.n_ue, 2)
)

dataset.rx_vel = random_velocities
print("Random per-UE velocities shape:", dataset.rx_vel.shape)

# ===========================================================
# 4. Set BS transmitter velocity
# ===========================================================
dataset.tx_vel = [0, 0, 0]  # 基站不移动
print("TX velocity:", dataset.tx_vel)

# ===========================================================
# 5. Set velocities of objects in the scene
# ===========================================================
# obj_idx 要与 dataset.scene.objects 中的对象编号一致
dataset.set_obj_vel(
    obj_idx=[1, 3, 6],
    vel=[
        [0, 5, 0],  # 物体 1
        [0, 5, 6],  # 物体 3
        [0, 0, 3]   # 物体 6
    ]
)

# print("Object velocities:", dataset.obj_vel)

# ===========================================================
# 6. Compute channels (Doppler included)
# ===========================================================
dataset.compute_channels(dm.ChannelParameters(doppler=True))
print("Channels computed with Doppler.")

# ===========================================================
# 7. Extract results
# ===========================================================
H = dataset.channels        # 信道张量 (UE × BS × Antenna × Paths)
doppler = dataset.doppler   # 每条路径的多普勒频移
delay = dataset.delay       # 路径时延
power = dataset.power       # 路径功率增益

# 对每个用户(131931)，有 1 根 TX 天线发射，8 根 RX 天线接收，在单1频点上生成的复数窄带信道系数
print("Channel tensor shape:", H.shape)
print("Doppler matrix shape:", doppler.shape)
print("Delay shape:", delay.shape)
print("Power shape:", power.shape)

# ===========================================================
# 8. (Optional) Export everything to .mat file
# ===========================================================
savemat("deepmimo_velocity_results.mat", {
    "channels": H,
    "doppler": doppler,
    "delay": delay,
    "power": power,
    "rx_vel": dataset.rx_vel,
    "tx_vel": dataset.tx_vel
})

print("Saved deepmimo_velocity_results.mat successfully!")
