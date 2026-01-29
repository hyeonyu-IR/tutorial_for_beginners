# Python for Statistical Analysis (V2) — Config + Diagnostics + Report

This V2 scaffold adds a single-config workflow, diagnostics, imputation, and HTML/DOCX reports.

**Highlights**:
- **Single `config.yaml`** as the source of truth (CLI exists for fallback).
- **Logistic diagnostics**: ROC/AUC, Brier score, ROC plot, calibration plot.
- **Cox diagnostics**: Concordance index (c-index), proportional hazards (PH) test table.
- **Imputation**: `none` | `simple` (median/mode) | `iterative` (MICE-like via `sklearn`'s `IterativeImputer`).
- **Reports**: Clean **HTML** + optional **Word (DOCX)** with parameters, tables, metrics, and figures.

## 1) Environment
```bash
conda create -n research_py3.11 python=3.11 -y
conda activate research_py3.11
pip install -r python/requirements.txt
```

## 2) Configure
Copy `python/config.example.yaml` → `config.yaml` and edit paths/variables.

## 3) Run
```bash
python python/run_analysis.py --config config.yaml
```

## 4) Outputs
- Tables: `outputs/logistic_or_table.csv`, `outputs/cox_hr_table.csv`, `outputs/cox_ph_test.csv`
- Figures: `outputs/km_plot.png`, `outputs/roc_curve.png`, `outputs/calibration_plot.png`
- Report: `outputs/report.html` and (optional) `outputs/report.docx`
