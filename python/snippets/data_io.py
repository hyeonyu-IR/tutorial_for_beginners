# data_io.py — robust I/O and cleaning helpers
from __future__ import annotations
import pandas as pd
import numpy as np
import re

__all__ = ["read_clean", "clean_columns", "set_categorical_ref"]

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase, snake_case, strip spaces/punctuation, collapse repeats."""
    def _clean(col: str) -> str:
        s = col.strip().lower()
        s = re.sub(r"[^0-9a-zA-Z]+", "_", s)
        s = re.sub(r"_+", "_", s).strip("_")
        return s
    df = df.copy()
    df.columns = [_clean(c) for c in df.columns]
    return df

def read_clean(path: str, sheet: int | str | None = None) -> pd.DataFrame:
    """Read CSV/TSV/Excel and standardize columns."""
    low = path.lower()
    if low.endswith((".csv", ".tsv", ".txt")):
        sep = "," if low.endswith(".csv") else "\t"
        df = pd.read_csv(path, sep=sep)
    elif low.endswith(".xlsx"):
        df = pd.read_excel(path, sheet_name=sheet)
    else:
        raise ValueError(f"Unsupported file extension: {path}")
    return clean_columns(df)

def set_categorical_ref(df: pd.DataFrame, col: str, ref: str) -> pd.DataFrame:
    out = df.copy()
    out[col] = pd.Categorical(out[col])
    cats = list(out[col].cat.categories)
    if ref in cats:
        out[col] = out[col].cat.reorder_categories([ref] + [c for c in cats if c != ref], ordered=True)
    return out
