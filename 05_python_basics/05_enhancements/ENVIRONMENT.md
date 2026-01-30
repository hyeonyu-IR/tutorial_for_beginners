# Reproducible Python Environments

Two recommended options:

## Option A: **uv** (fast, modern)
1. Install uv (Windows/macOS/Linux): https://docs.astral.sh/uv/
2. From repo root:
```bash
uv venv
uv pip install -e .
uv pip compile pyproject.toml -o requirements.lock.txt
uv pip sync requirements.lock.txt
```

## Option B: **pip-tools** (classic)
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install pip-tools
pip-compile pyproject.toml -o requirements.lock.txt
pip-sync requirements.lock.txt
```

> `requirements.lock.txt` should be **committed** for exact reproducibility across Home/UNC.
