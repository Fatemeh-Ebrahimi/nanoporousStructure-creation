import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from Constants import grid_size, num_waves, threshold

# Generate a 3D grid
x, y, z = np.indices((grid_size, grid_size, grid_size))
random_field = np.zeros((grid_size, grid_size, grid_size))

# Add sinusoidal waves with random directions and phases

for _ in range(num_waves):
	direction = np.random.randn(3)
	direction /= np.linalg.norm(direction)
	phase = np.random.rand() * 2 * np.pi
	wavelength = grid_size/5
	random_field += np.cos((x * direction[0] + y * direction[1] + z * direction[2]) * 2 * np.pi / wavelength + phase)

#Normalize and apply Gaussian filter for smoothness
random_field = gaussian_filter(random_field, sigma=3)
random_field = gaussian_filter(random_field, sigma=5)
random_field -= random_field.mean()

#Binarize to create solid and pore regions
binary_structure = (random_field > threshold).astype(int)

#Visualize a slice (example for 2D)
plt.imshow(binary_structure [:, :, grid_size // 2], cmap='gray')
plt.show()
