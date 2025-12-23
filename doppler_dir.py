import numpy as np
import deepmimo as dm
# Save as .mat
from scipy.io import savemat

# =============================================
# 1. Load Dataset
# =============================================
dataset = dm.load("asu_campus_3p5")

print(f"Number of UEs: {dataset.n_ue}")
print(f"Max paths per UE: {dataset.max_paths}")

# =============================================
# 2. Case 1: Same Doppler shift for all users
# =============================================

# dopplers1 = 10  # Hz
# dataset.set_doppler(dopplers1)
# dataset.compute_channels(dm.ChannelParameters(doppler=True))
# print("Case 1 done: All users same Doppler = 10 Hz")

# =============================================
# 3. Case 2: Different Doppler per UE
# np.random.randint(20, 51)：在 20Hz ~ 50Hz 之间随机取整数
# size=(dataset.n_ue,)：生成 一维向量，长度 = 用户数
# =============================================

dopplers2 = np.random.randint(20, 51, size=(dataset.n_ue,))
dataset.set_doppler(dopplers2)
dataset.compute_channels(dm.ChannelParameters(doppler=True))
print(f"Case 2 done: Per-UE Doppler shape = {dopplers2.shape}")

# =============================================
# 4. Case 3: Different Doppler per UE and per path
# 行：UE（用户）
# 列：Path（多径路径）
# 每个元素是 20~50Hz 之间的随机 Doppler
# =============================================

# dopplers3 = np.random.randint(20, 51, size=(dataset.n_ue, dataset.max_paths))
# dataset.set_doppler(dopplers3)
# dataset.compute_channels(dm.ChannelParameters(doppler=True))
# print(f"Case 3 done: Per-UE-per-path Doppler shape = {dopplers3.shape}")


# =============================================
# 5. Inspect the final result (Optional)
# =============================================
h = dataset.channels
print("Channel tensor shape:", h.shape)

# =============================================
# 6. Export final Doppler matrix to file
# =============================================
final_doppler = dataset.doppler
print("Final doppler matrix shape:", final_doppler.shape)

savemat("doppler_matrix.mat", {"doppler": final_doppler})
print("Doppler matrix saved to doppler_matrix.mat")
