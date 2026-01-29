# eda_plotting.py — quick EDA and plotting helpers
from __future__ import annotations
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')

__all__ = [
    'summarize_numeric', 'summarize_categorical',
    'boxplot_jitter', 'histogram', 'countplot'
]

def summarize_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    return df[cols].describe(percentiles=[0.25, 0.5, 0.75]).T

def summarize_categorical(df: pd.DataFrame, cols: list[str]) -> dict[str, pd.Series]:
    return {c: df[c].value_counts(dropna=False) for c in cols}

def boxplot_jitter(df: pd.DataFrame, x: str, y: str, title: str | None = None):
    ax = sns.boxplot(data=df, x=x, y=y)
    sns.stripplot(data=df, x=x, y=y, color='0.3', alpha=0.4, jitter=0.15)
    ax.set_title(title or f'{y} by {x}')
    plt.tight_layout()
    return ax

def histogram(df: pd.DataFrame, col: str, bins: int = 30, title: str | None = None):
    ax = sns.histplot(df[col].dropna(), bins=bins, kde=True)
    ax.set_title(title or f'Distribution of {col}')
    plt.tight_layout()
    return ax

def countplot(df: pd.DataFrame, col: str, title: str | None = None):
    ax = sns.countplot(data=df, x=col)
    ax.set_title(title or f'Counts of {col}')
    plt.tight_layout()
    return ax