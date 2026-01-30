"""
Window/Level QC panel: load a NIfTI (.nii/.nii.gz) or NumPy (.npy) volume and save a grid PNG.

Usage:
  python 05_python_basics/05_enhancements/window_level_qc.py \
      --in_vol 05_python_basics/figures/ct_volume.nii.gz \
      --out_png 05_python_basics/figures/qc_panel.png \
      --center 50 --width 350 --rows 4 --cols 4
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt

try:
    import nibabel as nib
except Exception:
    nib = None  # type: ignore


def _load(path: str) -> np.ndarray:
    if path.lower().endswith('.npy'):
        return np.load(path)
    if nib is None:
        raise SystemExit('nibabel required for NIfTI files. Install with: pip install nibabel')
    img = nib.load(path)
    data = img.get_fdata().astype(np.float32)
    return data


def _window(data: np.ndarray, center: float, width: float) -> np.ndarray:
    low, high = center - width/2, center + width/2
    data = np.clip(data, low, high)
    data = (data - low) / max(width, 1e-6)
    return (data * 255).astype(np.uint8)


def _pick_slices(n_slices: int, depth: int) -> np.ndarray:
    idx = np.linspace(0, depth-1, num=n_slices, dtype=int)
    return np.unique(idx)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in_vol', required=True)
    ap.add_argument('--out_png', required=True)
    ap.add_argument('--center', type=float, default=50)
    ap.add_argument('--width', type=float, default=350)
    ap.add_argument('--rows', type=int, default=4)
    ap.add_argument('--cols', type=int, default=4)
    args = ap.parse_args()

    vol = _load(args.in_vol)
    if vol.ndim == 2:
        vol = vol[..., None]
    depth = vol.shape[-1]
    total = args.rows * args.cols
    sel = _pick_slices(total, depth)

    wl = _window(vol, args.center, args.width)

    plt.figure(figsize=(args.cols*2.5, args.rows*2.5))
    for i, z in enumerate(sel[:total]):
        plt.subplot(args.rows, args.cols, i+1)
        plt.imshow(wl[..., z], cmap='gray', vmin=0, vmax=255)
        plt.axis('off'); plt.title(f'z={z}', fontsize=8)
    plt.tight_layout()
    os.makedirs(os.path.dirname(args.out_png), exist_ok=True)
    plt.savefig(args.out_png, dpi=200)
    print('Saved QC panel to', args.out_png)

if __name__ == '__main__':
    main()
