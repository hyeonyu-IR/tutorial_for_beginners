"""NumPy basics for radiology examples."""
import numpy as np

# HU windowing example (simulate CT slice values)
np.random.seed(42)
slice_hu = np.random.normal(loc=40, scale=100, size=(256, 256))

# window: liver (approx 50/150)
center, width = 50, 150
low, high = center - width/2, center + width/2
windowed = np.clip(slice_hu, low, high)

print("HU stats -> mean=%.1f, min=%.1f, max=%.1f" % (slice_hu.mean(), slice_hu.min(), slice_hu.max()))
print("Windowed stats -> min=%.1f, max=%.1f" % (windowed.min(), windowed.max()))
