# Figure Style Guide (Radiology)

**Goals:** consistent, journal‑ready figures that are fully reproducible.

## Dimensions (inches)
- **Single‑column:** 3.5″ width
- **1.5‑column:** 5.0″ width
- **Double‑column:** 7.2″ width
- **Default height:** 5.0″ (adjust per aspect ratio)

> Use the helper `std_width('single'|'onehalf'|'double')` to set widths.

## Resolution
- **300 dpi** for print‑quality PNGs (sufficient for most journals)
- Save **PDF** for vector graphics when possible

## Fonts & Style
- Sans‑serif base (system default) is acceptable for most submissions
- Use bold axis titles; avoid minor grid lines
- Keep color palettes color‑blind‑friendly when possible

## Filenames
- Match manuscript numbering and content:
  - `Fig1_KM_TACE_vs_TARE.png`
  - `Fig2_Logistic_ORs.pdf`

## Workflow
1. Re‑run analysis scripts (`make analysis`)
2. Generate figures reproducibly (`make figures`)
3. Insert figures into reports from `04_r_basics/figures/`

## Example (ggplot)
```r
source('04_r_basics/scripts/figure_helpers.R')
library(ggplot2)

set.seed(42)
age <- rnorm(120, 62, 10)
sm  <- 140 - 0.4*age + rnorm(120,0,8)
p <- ggplot(data.frame(age, sm), aes(age, sm)) +
  geom_point(color='gray40') +
  geom_smooth(method='lm', se=FALSE, color='red') +
  labs(x='Age', y='Skeletal Muscle Area', title='Scatter with Fit') +
  rad_theme()

save_fig('04_r_basics/figures/FigX_Scatter.png', p, width = std_width('single'), height = 4, device='png')
```
