# diagnostics.py — logistic & Cox diagnostics
from __future__ import annotations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, brier_score_loss
from sklearn.calibration import calibration_curve
from lifelines.statistics import proportional_hazard_test

__all__ = [
    "logistic_diagnostics", "save_roc_plot", "save_calibration_plot",
    "cox_ph_test_table"
]

def logistic_diagnostics(y_true: pd.Series, y_prob: pd.Series) -> dict:
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    roc_auc = auc(fpr, tpr)
    bs = brier_score_loss(y_true, y_prob)
    return {"auc": float(roc_auc), "brier": float(bs)}

def save_roc_plot(y_true: pd.Series, y_prob: pd.Series, path: str):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(5,4))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0,1],[0,1], 'k--', lw=1)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve (Logistic)')
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

def save_calibration_plot(y_true: pd.Series, y_prob: pd.Series, path: str, n_bins: int = 10):
    frac_pos, mean_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy='quantile')
    plt.figure(figsize=(5,4))
    plt.plot(mean_pred, frac_pos, 'o-', label='Calibration')
    plt.plot([0,1],[0,1], 'k--', lw=1, label='Perfect')
    plt.xlabel('Mean predicted probability')
    plt.ylabel('Fraction of positives')
    plt.title('Calibration Plot (Logistic)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

def cox_ph_test_table(cph, df: pd.DataFrame, duration_col: str, event_col: str) -> pd.DataFrame:
    # Lifelines PH test per covariate
    results = proportional_hazard_test(cph, df, time_transform='rank')
    tbl = results.summary.reset_index().rename(columns={'index':'term'})
    return tbl[['term','test_statistic','p']]
