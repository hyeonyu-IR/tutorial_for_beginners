# Run-all orchestrator for 04_r_basics
# Usage (from repo root in R):
#   setwd("04_r_basics")
#   source("run_all.R")

message("[1/3] Running analysis scripts...")
analysis_dir <- file.path(getwd(), "analysis")
for (f in list.files(analysis_dir, pattern = "\\\.R$", full.names = TRUE)) {
  message("  - ", basename(f))
  try(source(f), silent = TRUE)
}

message("[2/3] Generating figures...")
fig_dir <- file.path(getwd(), "figures")
for (f in list.files(fig_dir, pattern = "\\\.R$", full.names = TRUE)) {
  message("  - ", basename(f))
  try(source(f), silent = TRUE)
}

message("[3/3] Rendering report...")
if (requireNamespace("rmarkdown", quietly = TRUE)) {
  rmarkdown::render(file.path(getwd(), "reports", "analysis_report.Rmd"), quiet = TRUE)
  message("Done: reports/analysis_report.html")
} else {
  message("rmarkdown not installed; skipping render. Install with install.packages('rmarkdown').")
}
