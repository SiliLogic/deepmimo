import deepmimo as dm

# Load dataset
dataset = dm.load("asu_campus_3p5")

# Access dataset properties
aoa_az = dataset.aoa_az
aoa_el = dataset.aoa_el
inter_pos = dataset.inter_pos

# Compute specific channel information
los = dataset.los
channels = dataset.compute_channels()
pl = dataset.compute_pathloss()