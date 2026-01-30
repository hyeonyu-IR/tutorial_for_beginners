"""Simple segmentation example (threshold) using numpy and skimage (optional).
This is a placeholder for didactic purposes.
"""
import sys
import numpy as np

try:
    from skimage.filters import threshold_otsu  # type: ignore
except Exception:
    threshold_otsu = None

# simulate a 2D image
np.random.seed(42)
img = np.random.normal(50, 20, (128,128)).astype(np.float32)

# either Otsu (if available) or fixed threshold
if threshold_otsu:
    th = threshold_otsu(img)
else:
    th = 60.0
mask = (img >= th).astype(np.uint8)

print("Segmentation summary → threshold:", round(float(th),1), 
      " foreground pixels:", int(mask.sum()))
