
# analysis_linear_logistic.R — logistic regression helpers

suppressPackageStartupMessages({
  library(tidyverse); library(broom); library(gtsummary)
})

run_logistic <- function(data, outcome, covariates) {
  # outcome: string (binary 0/1); covariates: character vector
  fml <- as.formula(paste(outcome, "~", paste(covariates, collapse = "+")))
  glm(fml, data = data, family = binomial)
}

or_table <- function(fit) {
  broom::tidy(fit, exponentiate = TRUE, conf.int = TRUE) %>%
    dplyr::select(term, estimate, conf.low, conf.high, p.value)
}

gts_logistic <- function(fit) {
  gtsummary::tbl_regression(fit, exponentiate = TRUE) %>% gtsummary::bold_p(t=0.05)
}

run_univariable_logistics <- function(data, outcome, predictors) {
  # returns a combined tibble of ORs for each predictor alone
  purrr::map_dfr(predictors, function(p) {
    fit <- run_logistic(data, outcome, p)
    or_table(fit) %>% dplyr::mutate(model = paste0("uni:", p))
  })
}
