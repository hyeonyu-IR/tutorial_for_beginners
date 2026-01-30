# 05_python_basics: Radiology‑First Python Module

This module introduces **Python for radiology research**, designed to complement your R workflows:

- **R** → statistics, tables, reports
- **Python** → imaging I/O (DICOM/NIfTI), automation, ML foundations

We start with plain **scripts (.py)** for maintainability and version control. Notebooks can be added later.

## Structure
```
05_python_basics/
├── 00_orientation/
│   └── python_vs_r.md
├── 01_environment/
│   ├── install_python.md
│   └── virtual_envs.md
├── 02_python_core/
│   ├── python_for_r_users.md
│   ├── numpy_basics.py
│   └── pandas_basics.py
├── 03_plotting/
│   └── matplotlib_vs_ggplot.py
├── 04_imaging/
│   ├── dicom_basics.py
│   ├── nifti_basics.py
│   └── simple_segmentation.py
├── figures/
└── requirements.txt
```

## How to run
From the repo root (recommended inside a virtual environment):
```bash
pip install -r 05_python_basics/requirements.txt
python 05_python_basics/02_python_core/numpy_basics.py
python 05_python_basics/02_python_core/pandas_basics.py
python 05_python_basics/03_plotting/matplotlib_vs_ggplot.py
python 05_python_basics/04_imaging/dicom_basics.py
```

> If `pydicom`/`nibabel` emit warnings, that’s normal for simulated examples.
