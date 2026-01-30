"""
DICOM series loader: read a folder of DICOM files, sort slices, stack into a 3D volume,
optionally convert to HU (CT), and save as .npy and/or .nii.gz (if nibabel available).

Usage (from repo root):
  python 05_python_basics/05_enhancements/dicom_series_loader.py \
      --dicom_dir path/to/series_folder \
      --out_np 05_python_basics/figures/ct_volume.npy \
      --out_nii 05_python_basics/figures/ct_volume.nii.gz

Notes:
- Sorting prefers ImagePositionPatient with ImageOrientationPatient; falls back to InstanceNumber.
- HU conversion is attempted for CT if RescaleSlope/Intercept and (0028,1052)/(1053) exist.
- NIfTI affine is constructed from IOP + PixelSpacing + slice spacing estimate.
"""
import argparse
import os
from pathlib import Path
from typing import List, Tuple, Optional

import numpy as np

try:
    import pydicom
except Exception:
    raise SystemExit("pydicom is required. Install with: pip install pydicom")

# nibabel optional
try:
    import nibabel as nib
except Exception:
    nib = None  # type: ignore


def _slice_key(ds) -> float:
    """Compute a sorting key for slices using ImagePositionPatient and orientation.
    If unavailable, fall back to InstanceNumber, else 0.
    """
    ipp = getattr(ds, 'ImagePositionPatient', None)
    iop = getattr(ds, 'ImageOrientationPatient', None)
    if ipp is not None and iop is not None and len(iop) >= 6:
        # normal = row x col
        import numpy as _np
        row = _np.array(iop[0:3], dtype=float)
        col = _np.array(iop[3:6], dtype=float)
        normal = _np.cross(row, col)
        pos = _np.array(ipp, dtype=float)
        return float(_np.dot(pos, normal))
    # Fallbacks
    if hasattr(ds, 'InstanceNumber'):
        try:
            return float(ds.InstanceNumber)
        except Exception:
            pass
    return 0.0


def _to_hu(pixel_array: np.ndarray, ds) -> np.ndarray:
    """Convert to Hounsfield Units if possible (CT)."""
    arr = pixel_array.astype(np.float32)
    slope = getattr(ds, 'RescaleSlope', 1.0)
    intercept = getattr(ds, 'RescaleIntercept', 0.0)
    # Some vendors store in (0028,1052/1053) WindowCenter/Width, not needed here
    try:
        arr = arr * float(slope) + float(intercept)
    except Exception:
        pass
    return arr


def _get_affine(first, last, nslices) -> Optional[np.ndarray]:
    """Construct a best-effort affine from DICOM orientation and spacing.
    Returns 4x4 affine or None if insufficient tags.
    """
    try:
        import numpy as _np
        iop = np.array(first.ImageOrientationPatient, dtype=float)
        row = iop[0:3]
        col = iop[3:6]
        normal = np.cross(row, col)
        ps = np.array(first.PixelSpacing, dtype=float)  # [row, col]
        # slice spacing: prefer spacing between IPP of first/last
        z_spacing = None
        if hasattr(first, 'ImagePositionPatient') and hasattr(last, 'ImagePositionPatient'):
            ipp0 = np.array(first.ImagePositionPatient, dtype=float)
            ipp1 = np.array(last.ImagePositionPatient, dtype=float)
            dist = np.dot((ipp1 - ipp0), normal)
            if nslices > 1:
                z_spacing = abs(dist) / (nslices - 1)
        if z_spacing is None:
            z_spacing = float(getattr(first, 'SpacingBetweenSlices', getattr(first, 'SliceThickness', 1.0)))
        # Construct affine
        origin = np.array(first.ImagePositionPatient, dtype=float) if hasattr(first, 'ImagePositionPatient') else np.zeros(3)
        R = np.column_stack((row*ps[1], col*ps[0], normal*z_spacing))
        A = np.eye(4)
        A[:3,:3] = R
        A[:3, 3] = origin
        return A
    except Exception:
        return None


def load_series(dicom_dir: Path) -> Tuple[np.ndarray, Optional[np.ndarray]]:
    files = [p for p in dicom_dir.rglob('*') if p.is_file()]
    dsets = []
    for f in files:
        try:
            ds = pydicom.dcmread(str(f), stop_before_pixels=False, force=True)
            if hasattr(ds, 'SOPInstanceUID'):
                dsets.append(ds)
        except Exception:
            continue
    if not dsets:
        raise RuntimeError("No DICOM slices found.")
    dsets.sort(key=_slice_key)
    # Stack
    vol_list = []
    for ds in dsets:
        arr = ds.pixel_array
        arr = _to_hu(arr, ds)
        vol_list.append(arr)
    vol = np.stack(vol_list, axis=-1)  # HxWxZ
    affine = _get_affine(dsets[0], dsets[-1], len(dsets))
    return vol, affine


def main():
    ap = argparse.ArgumentParser(description='DICOM series → NumPy/NIfTI')
    ap.add_argument('--dicom_dir', required=True, type=str)
    ap.add_argument('--out_np', type=str, default=None)
    ap.add_argument('--out_nii', type=str, default=None)
    args = ap.parse_args()

    vol, affine = load_series(Path(args.dicom_dir))
    print('Volume shape (HxWxZ):', vol.shape, 'dtype:', vol.dtype)

    if args.out_np:
        np.save(args.out_np, vol)
        print('Saved NumPy volume to', args.out_np)

    if args.out_nii:
        if nib is None or affine is None:
            print('NIfTI output requested but nibabel/affine missing; skipping.')
        else:
            img = nib.Nifti1Image(vol, affine)
            nib.save(img, args.out_nii)
            print('Saved NIfTI to', args.out_nii)

if __name__ == '__main__':
    main()
