import deepmimo as dm
import numpy as np
import matplotlib.pyplot as plt  # <--- 1. 添加这行引入

# Load scenario
dataset = dm.load('asu_campus_3p5')

# Plot power coverage map
dm.plot_coverage(dataset.rx_pos, dataset.power[:, 0],
    bs_pos=dataset.tx_pos.T,
    title="Power Coverage Map (dB)")

plt.show()  # <--- 2. 在代码最后添加这行