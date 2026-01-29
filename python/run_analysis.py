# run_analysis.py — end-to-end driver (logistic + Cox) with YAML config and HTML report
from __future__ import annotations
import argparse
from pathlib import Path
import datetime as _dt

import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader

from snippets.data_io import read_clean, set_categorical_ref
from snippets.logistic_regression import fit_logistic, or_table
from snippets.survival_analysis import km_fit_plot, cox_fit, hr_table

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', help='Path to YAML config')
    ap.add_argument('--data')
    ap.add_argument('--outcome')
    ap.add_argument('--time')
    ap.add_argument('--status')
    ap.add_argument('--covars', nargs='+')
    ap.add_argument('--group')
    ap.add_argument('--ref_group')
    ap.add_argument('--cluster')
    ap.add_argument('--or_table_csv')
    ap.add_argument('--hr_table_csv')
    ap.add_argument('--km_plot')
    ap.add_argument('--report_html')
    ap.add_argument('--title')
    ap.add_argument('--author')
    ap.add_argument('--institution')
    return ap.parse_args()

def load_config(args):
    cfg = {
        'data': 'data/analysis_dataset.csv',
        'outcome': 'outcome',
        'time': 'time',
        'status': 'status',
        'covars': ['age','sex','group','bmi'],
        'group': 'group',
        'ref_group': 'control',
        'cluster': None,
        'outputs': {
            'or_table_csv': 'outputs/logistic_or_table.csv',
            'hr_table_csv': 'outputs/cox_hr_table.csv',
            'km_plot': 'outputs/km_plot.png',
            'report_html': 'outputs/report.html',
        },
        'report': {
            'title': 'Project Analysis Report',
            'author': 'Analyst',
            'institution': None,
            'include_tables': True,
            'include_km_plot': True,
        }
    }
    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            loaded = yaml.safe_load(f) or {}
        def merge(d, u):
            for k, v in u.items():
                if isinstance(v, dict) and isinstance(d.get(k), dict):
                    merge(d[k], v)
                else:
                    d[k] = v
            return d
        cfg = merge(cfg, loaded)
    if args.data: cfg['data'] = args.data
    if args.outcome: cfg['outcome'] = args.outcome
    if args.time: cfg['time'] = args.time
    if args.status: cfg['status'] = args.status
    if args.covars: cfg['covars'] = args.covars
    if args.group: cfg['group'] = args.group
    if args.ref_group: cfg['ref_group'] = args.ref_group
    if args.cluster: cfg['cluster'] = args.cluster
    if args.or_table_csv: cfg['outputs']['or_table_csv'] = args.or_table_csv
    if args.hr_table_csv: cfg['outputs']['hr_table_csv'] = args.hr_table_csv
    if args.km_plot: cfg['outputs']['km_plot'] = args.km_plot
    if args.report_html: cfg['outputs']['report_html'] = args.report_html
    if args.title: cfg['report']['title'] = args.title
    if args.author: cfg['report']['author'] = args.author
    if args.institution: cfg['report']['institution'] = args.institution
    return cfg

def render_report(cfg, or_df: pd.DataFrame, hr_df: pd.DataFrame, km_plot_path: str | None):
    env = Environment(loader=FileSystemLoader('python/templates'))
    tpl = env.get_template('report_template.html')
    or_html = or_df.to_html(index=False, float_format=lambda x: format(x, '.3g')) if or_df is not None else ''
    hr_html = hr_df.to_html(index=False, float_format=lambda x: format(x, '.3g')) if hr_df is not None else ''
    html = tpl.render(
        title=cfg['report']['title'],
        author=cfg['report']['author'],
        institution=cfg['report']['institution'],
        generated=_dt.datetime.now().strftime('%Y-%m-%d %H:%M'),
        params={
            'data': cfg['data'],
            'outcome': cfg['outcome'],
            'time': cfg['time'],
            'status': cfg['status'],
            'covars': cfg['covars'],
            'group': cfg['group'],
            'ref_group': cfg['ref_group'],
        },
        include_tables=bool(cfg['report'].get('include_tables', True)),
        include_km_plot=bool(cfg['report'].get('include_km_plot', True)),
        or_table_html=or_html,
        hr_table_html=hr_html,
        km_plot_path=km_plot_path,
    )
    out_path = Path(cfg['outputs']['report_html'])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding='utf-8')
    return str(out_path)

def main():
    args = parse_args()
    cfg = load_config(args)

    df = read_clean(cfg['data'])

    if cfg['group'] in df.columns:
        df = set_categorical_ref(df, cfg['group'], cfg['ref_group'])

    log_res = fit_logistic(df, cfg['outcome'], cfg['covars'], cluster=cfg.get('cluster'))
    or_df = or_table(log_res)
    or_csv = Path(cfg['outputs']['or_table_csv']); or_csv.parent.mkdir(parents=True, exist_ok=True)
    or_df.to_csv(or_csv, index=False)

    cph = cox_fit(df, cfg['time'], cfg['status'], cfg['covars'])
    hr_df = hr_table(cph)
    hr_csv = Path(cfg['outputs']['hr_table_csv']); hr_csv.parent.mkdir(parents=True, exist_ok=True)
    hr_df.to_csv(hr_csv, index=False)

    km_plot_path = None
    if cfg['report'].get('include_km_plot', True):
        ax = km_fit_plot(df, cfg['time'], cfg['status'], group=cfg['group'])
        km_png = Path(cfg['outputs']['km_plot']); km_png.parent.mkdir(parents=True, exist_ok=True)
        ax.figure.savefig(km_png, dpi=300, bbox_inches='tight')
        km_plot_path = str(km_png)

    report_path = render_report(cfg, or_df, hr_df, km_plot_path)
    print('Saved OR table →', or_csv)
    print('Saved HR table →', hr_csv)
    if km_plot_path:
        print('Saved KM plot →', km_plot_path)
    print('Saved HTML report →', report_path)

if __name__ == '__main__':
    main()