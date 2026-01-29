# imputation.py — simple/iterative imputation for covariates
from __future__ import annotations
import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import SimpleImputer, IterativeImputer

__all__ = ["impute_covariates"]

def impute_covariates(df: pd.DataFrame, covars: list[str], method: str = 'none', iterative_max_iter: int = 10) -> pd.DataFrame:
    method = (method or 'none').lower()
    if method not in {'none','simple','iterative'}:
        raise ValueError("imputation.method must be one of: none | simple | iterative")
    if method == 'none':
        return df
    out = df.copy()
    X = out[covars]
    num_cols = X.select_dtypes(include=['number']).columns.tolist()
    cat_cols = [c for c in covars if c not in num_cols]
    if method == 'simple':
        if num_cols:
            sim_num = SimpleImputer(strategy='median')
            out[num_cols] = sim_num.fit_transform(out[num_cols])
        if cat_cols:
            sim_cat = SimpleImputer(strategy='most_frequent')
            out[cat_cols] = sim_cat.fit_transform(out[cat_cols])
    else:
        if num_cols:
            iim = IterativeImputer(max_iter=int(iterative_max_iter), random_state=123)
            out[num_cols] = iim.fit_transform(out[num_cols])
        if cat_cols:
            sim_cat = SimpleImputer(strategy='most_frequent')
            out[cat_cols] = sim_cat.fit_transform(out[cat_cols])
    return out
