# Virtual Environments (Avoid "dependency hell")

Create a project‑specific environment:

## Using venv (built‑in)
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r 05_python_basics/requirements.txt
```

## Using conda (optional)
```bash
conda create -n radpy python=3.10 -y
conda activate radpy
pip install -r 05_python_basics/requirements.txt
```

Deactivate when done:
```bash
deactivate   # venv
# or
conda deactivate
```
