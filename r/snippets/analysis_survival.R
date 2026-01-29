
# analysis_survival.R — survival analysis helpers

suppressPackageStartupMessages({
  library(tidyverse); library(survival); library(broom); library(gtsummary); library(survminer)
})

run_km <- function(data, time, status, group) {
  survfit(as.formula(paste0("Surv(", time, ", ", status, ") ~ ", group)), data = data)
}

plot_km <- function(fit, data) {
  ggsurvplot(fit, data = data, risk.table = TRUE, conf.int = TRUE, pval = TRUE)
}

run_cox <- function(data, time, status, covariates) {
  s <- Surv(time = data[[time]], event = data[[status]])
  fml <- as.formula(paste("s ~", paste(covariates, collapse = "+")))
  coxph(fml, data = data)
}

hr_table <- function(fit) {
  broom::tidy(fit, exponentiate = TRUE, conf.int = TRUE) %>%
    dplyr::select(term, estimate, conf.low, conf.high, p.value)
}

gts_cox <- function(fit) {
  gtsummary::tbl_regression(fit, exponentiate = TRUE) %>% gtsummary::bold_p(t=0.05)
}

check_ph <- function(fit) { cox.zph(fit) }
