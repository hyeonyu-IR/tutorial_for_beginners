<#
Build.ps1 — Windows PowerShell helper for Python/Radiology workflows

Usage examples (run from repo root in PowerShell):
  # Create/activate venv + install requirements for Python basics
  ./Build.ps1 Setup-Python

  # Run the full R pipeline (analysis → figures → report) if Make is unavailable
  ./Build.ps1 Run-R-All

  # Run Python basics examples (NumPy/Pandas/Matplotlib)
  ./Build.ps1 Run-Python-Core

  # Imaging pipeline (DICOM→NIfTI, QC panel, resample, preprocessing)
  ./Build.ps1 Run-Python-Imaging -DicomDir "C:\data\ct_series" -OutDir "05_python_basics\figures"

Switch list:
  Setup-Python | Run-R-All | Run-Python-Core | Run-Python-Imaging

Notes:
- Uses local venv at .\.venv .
- Requires PowerShell execution policy allowing local scripts (e.g., Set-ExecutionPolicy -Scope CurrentUser RemoteSigned)
#>
param(
  [Parameter(Mandatory=$true, Position=0)]
  [ValidateSet('Setup-Python','Run-R-All','Run-Python-Core','Run-Python-Imaging')]
  [string]$Task,

  # Optional parameters for imaging task
  [string]$DicomDir,
  [string]$OutDir = '05_python_basics/figures',
  [double]$WL = 50,
  [double]$WW = 350,
  [double]$IsoSpacing = 1.0
)

function Ensure-Venv {
  if (!(Test-Path .\.venv)) {
    Write-Host "[Setup] Creating venv at .\\.venv" -ForegroundColor Cyan
    python -m venv .venv
  }
  Write-Host "[Setup] Activating venv" -ForegroundColor Cyan
  . .\.venv\Scripts\Activate.ps1
}

switch ($Task) {
  'Setup-Python' {
    Ensure-Venv
    Write-Host "[Setup] Installing Python requirements for basics" -ForegroundColor Cyan
    pip install -r 05_python_basics/requirements.txt
    if (Test-Path 05_python_basics/05_enhancements/pyproject.toml) {
      Write-Host "[Setup] Installing enhancements dependencies (pyproject)" -ForegroundColor Cyan
      pip install -e 05_python_basics/05_enhancements
    }
  }

  'Run-R-All' {
    # Fallback when GNU Make is not available on Windows
    Write-Host "[R] Running 04_r_basics/run_all.R" -ForegroundColor Green
    Rscript -e "setwd('04_r_basics'); source('run_all.R')"
  }

  'Run-Python-Core' {
    Ensure-Venv
    Write-Host "[Py] NumPy" -ForegroundColor Green
    python 05_python_basics/02_python_core/numpy_basics.py

    Write-Host "[Py] Pandas" -ForegroundColor Green
    python 05_python_basics/02_python_core/pandas_basics.py

    Write-Host "[Py] Matplotlib figure" -ForegroundColor Green
    python 05_python_basics/03_plotting/matplotlib_vs_ggplot.py
  }

  'Run-Python-Imaging' {
    if (-not $DicomDir) { throw "Run-Python-Imaging requires -DicomDir <path>" }
    Ensure-Venv

    if (!(Test-Path $OutDir)) { New-Item -ItemType Directory -Force -Path $OutDir | Out-Null }

    $npy = Join-Path $OutDir 'ct_volume.npy'
    $nii = Join-Path $OutDir 'ct_volume.nii.gz'

    Write-Host "[Py] DICOM → volume (.npy/.nii.gz)" -ForegroundColor Green
    python 05_python_basics/05_enhancements/dicom_series_loader.py --dicom_dir $DicomDir --out_np $npy --out_nii $nii

    Write-Host "[Py] Window/Level QC panel" -ForegroundColor Green
    $qc = Join-Path $OutDir 'qc_panel.png'
    python 05_python_basics/05_enhancements/window_level_qc.py --in_vol $nii --out_png $qc --center $WL --width $WW --rows 4 --cols 4

    Write-Host "[Py] Resample to isotropic" -ForegroundColor Green
    $iso = Join-Path $OutDir 'ct_volume_iso1mm.nii.gz'
    python 05_python_basics/05_enhancements/resample_isotropic_sitk.py --in_nii $nii --out_nii $iso --spacing $IsoSpacing

    Write-Host "[Py] Preprocessing panel" -ForegroundColor Green
    $prep = Join-Path $OutDir 'preproc_panel.png'
    python 05_python_basics/05_enhancements/preprocessing_skimage.py --in_vol $iso --out_png $prep
  }
}
