"""
Resample a NIfTI volume to isotropic spacing with SimpleITK.

Usage:
  python 05_python_basics/05_enhancements/resample_isotropic_sitk.py \
      --in_nii path/in.nii.gz --out_nii path/out_iso1mm.nii.gz --spacing 1.0
"""
import argparse

try:
    import SimpleITK as sitk
except Exception:
    raise SystemExit("SimpleITK is required. Install with: pip install SimpleITK")


def resample_iso(in_path: str, out_path: str, iso_spacing: float = 1.0):
    img = sitk.ReadImage(in_path)
    orig_spacing = img.GetSpacing()
    orig_size = img.GetSize()

    new_spacing = [iso_spacing, iso_spacing, iso_spacing]
    new_size = [int(round(osz*ospc/nspc)) for osz, ospc, nspc in zip(orig_size, orig_spacing, new_spacing)]

    resampler = sitk.ResampleImageFilter()
    resampler.SetOutputSpacing(new_spacing)
    resampler.SetSize(new_size)
    resampler.SetOutputDirection(img.GetDirection())
    resampler.SetOutputOrigin(img.GetOrigin())
    resampler.SetInterpolator(sitk.sitkLinear)

    out = resampler.Execute(img)
    sitk.WriteImage(out, out_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in_nii', required=True)
    ap.add_argument('--out_nii', required=True)
    ap.add_argument('--spacing', type=float, default=1.0)
    args = ap.parse_args()

    resample_iso(args.in_nii, args.out_nii, args.spacing)
    print('Saved isotropic NIfTI to', args.out_nii)

if __name__ == '__main__':
    main()
