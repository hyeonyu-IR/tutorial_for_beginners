# 05_enhancements: Imaging Pipeline & Reproducible Environments

This module adds five capabilities on top of `05_python_basics`:

1. **DICOM series loader** → folder → sorted 3D NumPy volume → optional NIfTI
2. **Window/level QC panel** → quick PNG grids for visual checks
3. **SimpleITK resample** → isotropic voxels (e.g., 1.0 mm)
4. **scikit‑image preprocessing** → denoise, edges, morphology
5. **Reproducible env** → `pyproject.toml` + `ENVIRONMENT.md` (uv / pip‑tools)

> All scripts are **safe defaults** with clear CLI help.
