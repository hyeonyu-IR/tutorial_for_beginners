
# data_io.R — simple helpers for I/O and cleaning

suppressPackageStartupMessages({
  library(tidyverse); library(janitor)
})

read_clean <- function(path, ...) {
  if (grepl("\\.csv$", path, ignore.case = TRUE)) {
    df <- readr::read_csv(path, ...)
  } else if (grepl("\\.tsv$|\\.txt$", path, ignore.case = TRUE)) {
    df <- readr::read_tsv(path, ...)
  } else if (grepl("\\.xlsx$", path, ignore.case = TRUE)) {
    df <- readxl::read_excel(path, ...)
  } else {
    stop("Unsupported file extension: ", path)
  }
  janitor::clean_names(df)
}

# Safe factor relevel
relevel_safe <- function(x, ref) {
  x <- as.factor(x)
  if (!(ref %in% levels(x))) return(x)
  stats::relevel(x, ref = ref)
}
