import deepmimo as dm

# Load a scenario
dataset = dm.load('asu_campus_3p5')

# Instantiate channel parameters
params = dm.ChannelParameters()

# Configure BS antenna array
params.bs_antenna.shape = [8, 1]  # 8x1 array
params.bs_antenna.spacing = 0.5  # Half-wavelength spacing
params.bs_antenna.rotation = [0, 0, 0]  # No rotation

# Configure UE antenna array
params.ue_antenna.shape = [1, 1]  # Single antenna
params.ue_antenna.spacing = 0.5
params.ue_antenna.rotation = [0, 0, 0]

# Configure OFDM parameters
params.ofdm.subcarriers = 512  # Number of subcarriers
params.ofdm.bandwidth = 10e6  # 10 MHz bandwidth
params.ofdm.selected_subcarriers = [0]  # Which subcarriers to generate

# Generate frequency-domain channels
params.doppler = False
params.freq_domain = True
channels = dataset.compute_channels(params)