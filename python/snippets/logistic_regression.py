# logistic_regression.py — statsmodels logistic regression utilities
from __future__ import annotations
import pandas as pd
import numpy as np
import statsmodels.api as sm
from typing import Sequence, Optional

__all__ = ['fit_logistic', 'or_table']

def fit_logistic(df: pd.DataFrame, outcome: str, covariates: Sequence[str], cluster: Optional[str] = None):
    X = df[list(covariates)].copy()
    X = pd.get_dummies(X, drop_first=True)
    X = sm.add_constant(X)
    y = df[outcome]

    model = sm.GLM(y, X, family=sm.families.Binomial())
    if cluster and cluster in df.columns:
        res = model.fit(cov_type='cluster', cov_kwds={'groups': df[cluster]})
    else:
        res = model.fit()
    res.design_info = {'columns': X.columns.tolist()}
    return res

def or_table(res) -> pd.DataFrame:
    params = res.params
    conf = res.conf_int()
    out = pd.DataFrame({
        'term': params.index,
        'OR': np.exp(params.values),
        'CI_lower': np.exp(conf[0].values),
        'CI_upper': np.exp(conf[1].values),
        'p_value': res.pvalues.values,
    })
    return out[out['term'] != 'const'].reset_index(drop=True)