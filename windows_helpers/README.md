# Windows PowerShell Helper

This helper lets you run common Python/R tasks **without GNU Make**.

## Usage (from repo root)
```powershell
# Allow local scripts if needed (once per user)
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# Create venv and install dependencies
./Build.ps1 Setup-Python

# Run full R pipeline (analysis → figures → report)
./Build.ps1 Run-R-All

# Run Python core demos (NumPy, Pandas, Matplotlib)
./Build.ps1 Run-Python-Core

# Imaging pipeline (DICOM → NIfTI/NumPy, QC, resample, preprocessing)
./Build.ps1 Run-Python-Imaging -DicomDir "C:\\data\\ct_series" -OutDir "05_python_basics\\figures"
```
