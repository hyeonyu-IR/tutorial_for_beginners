# Reports

This folder contains **analysis narratives** (R Markdown) that assemble results and figures into a shareable document.

## Rendering
Open in R/RStudio and knit to **HTML** (default) or **PDF** if LaTeX is available.

From R:
```r
rmarkdown::render("analysis_report.Rmd")
```

## Contents
- `analysis_report.Rmd` – main example report (sources analysis and figures)
- `supplement.Rmd` – short supplement skeleton
- `_output.yml` – unified HTML theming
```
