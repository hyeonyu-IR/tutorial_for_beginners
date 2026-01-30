"""
Preprocessing with scikit-image: denoise, edges, morphology; save quick panels.

Usage:
  python 05_python_basics/05_enhancements/preprocessing_skimage.py \
      --in_vol 05_python_basics/figures/ct_volume.nii.gz \
      --out_png 05_python_basics/figures/preproc_panel.png
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

try:
    import nibabel as nib
except Exception:
    nib = None  # type: ignore

from skimage.filters import gaussian, sobel
from skimage.morphology import opening, disk


def _load(path: str) -> np.ndarray:
    if path.lower().endswith('.npy'):
        return np.load(path)
    if nib is None:
        raise SystemExit('nibabel required for NIfTI files. Install with: pip install nibabel')
    img = nib.load(path)
    return img.get_fdata().astype(np.float32)


def _panel(img2d: np.ndarray, out_png: str):
    g = gaussian(img2d, sigma=1.0, preserve_range=True)
    e = sobel(img2d)
    m = opening(img2d > np.percentile(img2d, 75), selem=disk(2))

    fig, axes = plt.subplots(1,4, figsize=(12,3))
    titles = ['Original', 'Gaussian σ=1', 'Sobel edges', 'Morph opening']
    ims = [img2d, g, e, m]
    for ax, im, t in zip(axes, ims, titles):
        ax.imshow(im, cmap='gray'); ax.set_title(t, fontsize=9); ax.axis('off')
    plt.tight_layout(); os.makedirs(os.path.dirname(out_png), exist_ok=True)
    plt.savefig(out_png, dpi=200)
    print('Saved preprocessing panel to', out_png)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in_vol', required=True)
    ap.add_argument('--out_png', required=True)
    ap.add_argument('--z', type=int, default=None, help='Slice index; default uses mid-slice')
    args = ap.parse_args()

    vol = _load(args.in_vol)
    if vol.ndim == 2:
        img = vol
    else:
        z = args.z if args.z is not None else vol.shape[-1]//2
        img = vol[..., z]
    # Normalize to 0..1 for visualization
    vmin, vmax = np.percentile(img, (1, 99))
    img = np.clip((img - vmin) / max(vmax - vmin, 1e-6), 0, 1)
    _panel(img, args.out_png)

if __name__ == '__main__':
    main()
