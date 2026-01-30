"""NIfTI basics with nibabel.
Loads a NIfTI file and prints shape/voxel size.
"""
import sys
try:
    import nibabel as nib  # type: ignore
except Exception as e:
    print("nibabel not installed. Install with: pip install nibabel")
    sys.exit(0)

if len(sys.argv) < 2:
    print("Usage: python 05_python_basics/04_imaging/nifti_basics.py <path_to_nifti.nii.gz>")
    sys.exit(0)

path = sys.argv[1]
img = nib.load(path)
print("Shape:", img.shape)
print("Voxel sizes (mm):", img.header.get_zooms())
