# survival_analysis.py — lifelines survival helpers
from __future__ import annotations
import pandas as pd
from lifelines import KaplanMeierFitter, CoxPHFitter
import matplotlib.pyplot as plt

__all__ = ['km_fit_plot', 'cox_fit', 'hr_table']

def km_fit_plot(df: pd.DataFrame, time: str, status: str, group: str | None = None):
    kmf = KaplanMeierFitter()
    fig, ax = plt.subplots(figsize=(6,4))
    if group and group in df.columns:
        for lvl, sub in df.groupby(group):
            kmf.fit(sub[time], event_observed=sub[status], label=str(lvl))
            kmf.plot_survival_function(ax=ax)
    else:
        kmf.fit(df[time], event_observed=df[status], label='overall')
        kmf.plot_survival_function(ax=ax)
    ax.set_title('Kaplan–Meier Survival')
    ax.set_xlabel('Time')
    ax.set_ylabel('Survival probability')
    plt.tight_layout()
    return ax

def cox_fit(df: pd.DataFrame, duration_col: str, event_col: str, covariates: list[str]):
    cph = CoxPHFitter()
    cols = [duration_col, event_col] + covariates
    cph.fit(df[cols].dropna(), duration_col=duration_col, event_col=event_col)
    return cph

def hr_table(cph: CoxPHFitter) -> pd.DataFrame:
    s = cph.summary.reset_index().rename(columns={'index':'term'})
    out = s[['term','exp(coef)','exp(coef) lower 95%','exp(coef) upper 95%','p']].copy()
    out.columns = ['term','HR','CI_lower','CI_upper','p_value']
    return out