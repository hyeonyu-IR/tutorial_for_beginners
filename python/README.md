# Python for Statistical Analysis (Beginner → Research-Ready)

This folder provides a tidy, **research-focused** Python setup for data analysis using:
- **pandas** (data wrangling), **numpy** (numerics), **scipy** (tests)
- **statsmodels** (regression; ORs/CI; robust SE)
- **lifelines** (survival analysis: Kaplan–Meier, Cox)
- **seaborn / matplotlib** (EDA & publication-quality plots)
- **scikit-learn** (train/test split, metrics when needed)

## 1) Environment setup (recommended)
```bash
conda create -n research_py3.11 python=3.11 -y
conda activate research_py3.11
pip install -r python/requirements.txt
```

If you prefer `pipx`/`venv`:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r python/requirements.txt
```

## 2) Contents
- `snippets/data_io.py` – CSV/Excel I/O; clean column names; type helpers
- `snippets/eda_plotting.py` – quick EDA and seaborn/matplotlib plots
- `snippets/logistic_regression.py` – statsmodels logistic (ORs + CI, clustered SE)
- `snippets/survival_analysis.py` – lifelines KM & Cox with checks and plots
- `templates/research_notebook.ipynb` – Jupyter template wired for your workflow
- `templates/report_template.html` – Jinja2 HTML template for summary report
- `run_analysis.py` – end-to-end example (logistic + Cox) with params or YAML config
- `config.example.yaml` – example configuration file

## 3) Minimal quick start (CLI params)
```bash
python python/run_analysis.py --data data/analysis_dataset.csv \
  --outcome complication --time time_to_event --status event \
  --covars age sex group bmi --group group
```

## 4) Preferred: single YAML config
1. Copy `python/config.example.yaml` to `config.yaml` and edit.
2. Run:
```bash
python python/run_analysis.py --config config.yaml
```

## 5) Outputs
- Tables (CSV): `outputs/logistic_or_table.csv`, `outputs/cox_hr_table.csv`
- Figure: `outputs/km_plot.png`
- Report: `outputs/report.html`

> Tip: Keep **PHI/PII** out of the repo; store raw data under `data/` (gitignored).