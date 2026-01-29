# R for Clinical Research: Structured, Practical Commands

## Focused on immediately usable commands for data management, statistical testing, modeling, survival analysis, and publication-ready output.
### 0) Setup & reproducibility
```
# Install core packages once
install.packages(c(
  "tidyverse","readxl","janitor","lubridate","forcats","stringr",
  "skimr","gtsummary","broom","ggpubr","survival","survminer",
  "lme4","lmerTest","car","emmeans","pwr","mice","tableone"
))

# Project workflow (use RStudio Projects or Quarto)
getwd()        # check working dir
set.seed(20260129)

# Reproducible environments
install.packages("renv")
renv::init()         # snapshot package versions for the project
renv::snapshot()
```
### 1) Data I/O
```
library(tidyverse); library(readxl); library(janitor)

# CSV / TSV
df <- readr::read_csv("data/analysis_dataset.csv") %>% janitor::clean_names()

# Excel
df_xl <- readxl::read_excel("data/raw.xlsx", sheet = 1) %>% clean_names()

# RDS (fast, preserves types)
saveRDS(df, "data/df.rds")
df <- readRDS("data/df.rds")

# Write back to disk
readr::write_csv(df, "outputs/df_clean.csv")
```
### 2) Data wrangling (tidyverse)
```
library(dplyr); library(tidyr); library(stringr); library(forcats); library(lubridate)

# Select / filter / mutate / summarize
df2 <- df %>%
  select(patient_id, age, sex, bmi, group, outcome, event_time, event_status) %>%
  filter(!is.na(outcome), age >= 18) %>%
  mutate(
    sex = factor(sex, levels = c("F","M")),
    group = fct_relevel(group, "control", "treatment"),
    bmi_cat = cut(bmi, breaks = c(-Inf,18.5,25,30,Inf), labels=c("under","normal","over","obese")),
    event_time_days = as.numeric(event_time),        # ensure numeric time
    admit_date = ymd(admit_date)                     # parse date
  )

# Grouped summaries
df2 %>% group_by(group) %>% summarize(n = n(), mean_age = mean(age, na.rm = TRUE))

# Pivot longer/wider
long <- df %>% pivot_longer(cols = starts_with("lab_"), names_to="lab", values_to="value")
wide <- long %>% pivot_wider(names_from = lab, values_from = value)
```
### 3) Quick EDA
```
library(skimr)
skimr::skim(df2)

df2 %>% count(group, sex)
df2 %>% summarize(across(c(age, bmi), ~mean(.x, na.rm=TRUE)))
```
### 4) Visualization (ggplot2)
```
library(ggplot2); library(ggpubr)

# Boxplot + jitter
ggplot(df2, aes(x = group, y = bmi, fill = group)) +
  geom_boxplot(alpha=.6) +
  geom_jitter(width=.1, alpha=.3) +
  theme_bw() + labs(title="BMI by group", x=NULL, y="BMI")

# Publication-friendly theme
theme_set(theme_pubr(base_size = 12))
```
### 5) Common statistical tests
```
# t-test (two independent groups)
t.test(bmi ~ group, data = df2)

# Paired t-test (pre vs post)
t.test(df2$lab_pre, df2$lab_post, paired = TRUE)

# Nonparametric (Mann-Whitney)
wilcox.test(bmi ~ group, data = df2)

# Chi-squared / Fisher’s exact
tbl <- table(df2$group, df2$event_status)
chisq.test(tbl)    # if expected counts >= 5; otherwise:
fisher.test(tbl)

# One-way ANOVA
fit_aov <- aov(bmi ~ group, data = df2)
summary(fit_aov)
car::Anova(fit_aov, type=3)     # Type III SS if needed
emmeans::emmeans(fit_aov, pairwise ~ group, adjust="tukey")
```
### 6) Regression models
6.1 Linear regression
```
fit_lm <- lm(bmi ~ age + sex + group, data = df2)
summary(fit_lm)
broom::tidy(fit_lm, conf.int = TRUE)
broom::glance(fit_lm)
```
6.2 Logistic regression (binary outcome)
```
# outcome: 0/1 (e.g., complication)
fit_log <- glm(outcome ~ age + sex + group + bmi, data = df2, family = binomial)
summary(fit_log)
broom::tidy(fit_log, exponentiate = TRUE, conf.int = TRUE)   # Odds ratios with CI
```
6.3 Poisson / Negative Binomial (counts)
```
# outcome: 0/1 (e.g., complication)
fit_pois <- glm(events ~ offset(log(followup)) + group + age, data=df2, family=poisson)
broom::tidy(fit_pois, exponentiate = TRUE, conf.int = TRUE)  # Incidence rate ratios
```
### 7) Mixed-effects models (clustered/longitudinal)
```
library(lme4); library(lmerTest)

# Random intercepts by patient (e.g., repeated measures)
fit_lmer <- lmer(value ~ time + group + (1 | patient_id), data = df_long)
summary(fit_lmer)

# Logistic mixed model
fit_glmer <- glmer(event_status ~ time + group + (1 | patient_id), data = df_long, family=binomial)
summary(fit_glmer)
```
### 8) Survival analysis (time-to-event)
```
library(survival); library(survminer)

# Define survival object
s <- Surv(time = df2$event_time_days, event = df2$event_status)

# Kaplan-Meier curves
fit_km <- survfit(s ~ group, data = df2)
ggsurvplot(fit_km, data=df2, risk.table=TRUE, conf.int=TRUE, pval=TRUE)

# Cox proportional hazards
fit_cox <- coxph(s ~ age + sex + group + bmi, data = df2)
summary(fit_cox)
broom::tidy(fit_cox, exponentiate=TRUE, conf.int=TRUE)  # Hazard ratios

# Check proportional hazards
cox.zph(fit_cox)  # global and covariate-specific tests
```
### 9) Multiple testing, effect sizes, power
```
# Multiple testing adjustment
pvals <- c(.01, .03, .2, .0005)
p.adjust(pvals, method = "BH")   # FDR control

# Effect sizes (examples)
ES_t <- (mean(df2$bmi[df2$group=="treatment"], na.rm=TRUE) -
         mean(df2$bmi[df2$group=="control"], na.rm=TRUE)) /
         sd(df2$bmi, na.rm=TRUE)

# Power / sample size (simple examples)
library(pwr)
pwr.t.test(d=0.5, power=0.8, sig.level=0.05, type="two.sample") # n per group
pwr.chisq.test(w=0.3, df=1, power=0.8, sig.level=0.05)
```
### 10) Missing data
```
library(mice)
md.pattern(df2)                        # pattern
imp <- mice(df2, m = 5, method = "pmm", seed = 20260129)
fit_imp <- with(imp, glm(outcome ~ age + sex + group + bmi, family=binomial))
pool(fit_imp)                          # pooled estimates
```
### 11) Publication-ready tables & export
```
library(gtsummary)
# Descriptive table by group
tbl1 <- df2 %>%
  select(group, age, sex, bmi, outcome) %>%
  tbl_summary(by = group, missing = "no") %>%
  add_n() %>%
  add_p() %>%
  bold_labels()

tbl1

# Model table (logistic regression)
fit_log <- glm(outcome ~ age + sex + group + bmi, data = df2, family=binomial)
tbl_mod <- tbl_regression(fit_log, exponentiate = TRUE) %>% bold_p(t = 0.05)
tbl_mod

# Save as Word/RTF
library(flextable); library(officer)
doc <- read_docx() %>% body_add_flextable(as_flextable(tbl1)) %>%
  body_add_par("") %>%
  body_add_flextable(as_flextable(tbl_mod))
print(doc, target = "outputs/tables.docx")
```
### 12) Diagnostics & model checks
```
# Linear model assumptions
par(mfrow=c(2,2)); plot(fit_lm); par(mfrow=c(1,1))
car::vif(fit_lm)          # multicollinearity
broom::augment(fit_lm)    # residuals, leverage etc.

# Logistic model calibration
library(ResourceSelection)
# install.packages("ResourceSelection") if needed
ResourceSelection::hoslem.test(df2$outcome, fitted(fit_log))
```
### 13) Reusable reporting (Quarto / R Markdown)
Quarto (templates/quarto-report.qmd)
```
---
title: "Clinical Analysis Report"
author: "Hyeon Yu, MD"
format:
  html: default
  pdf: default
execute:
  echo: true
  warning: false
  message: false
---

```{r}
library(tidyverse); library(gtsummary); library(broom)
df <- readr::read_csv("data/analysis_dataset.csv") %>% janitor::clean_names()
# your analysis...
```
Render with:
```
# In R console:
quarto::quarto_render("templates/quarto-report.qmd")
```
### 14) Handy idioms (copy/paste)
```
# Relevel reference category
df2$group <- relevel(df2$group, ref = "control")

# Winsorize extreme values
wins <- function(x, p=.01){ q <- quantile(x, c(p,1-p), na.rm=TRUE); pmin(pmax(x,q[1]),q[2]) }
df2$bmi_w <- wins(df2$bmi, .01)

# Pipe-friendly ORs / HRs from models
or_table <- broom::tidy(fit_log, exponentiate=TRUE, conf.int=TRUE) %>%
  select(term, estimate, conf.low, conf.high, p.value)

hr_table <- broom::tidy(fit_cox, exponentiate=TRUE, conf.int=TRUE) %>%
  select(term, estimate, conf.low, conf.high, p.value)
```
### 15) Session info (for methods sections)
```
sessionInfo()
renv::snapshot()  # lock dependencies
```
### 16) Minimal end-to-end example (logistic + survival)
```
library(tidyverse); library(survival); library(broom); library(survminer)

set.seed(20260129)
n <- 300
sim <- tibble(
  patient_id = 1:n,
  age = rnorm(n, 62, 12),
  sex = factor(sample(c("F","M"), n, TRUE)),
  group = factor(sample(c("control","treatment"), n, TRUE)),
  bmi = rnorm(n, 27, 5)
) %>%
  mutate(
    linpred = -2 + 0.02*age + 0.3*(sex=="M") - 0.4*(group=="treatment") + 0.03*bmi,
    outcome = rbinom(n, 1, plogis(linpred)),
    time = rexp(n, rate = 0.08 * exp(-0.4*(group=="treatment"))),
    status = rbinom(n, 1, 0.7)
  )

# Logistic regression
fit_log <- glm(outcome ~ age + sex + group + bmi, data=sim, family=binomial)
broom::tidy(fit_log, exponentiate=TRUE, conf.int=TRUE)

# Cox model
fit_cox <- coxph(Surv(time, status) ~ age + sex + group + bmi, data = sim)
broom::tidy(fit_cox, exponentiate=TRUE, conf.int=TRUE)

# KM plot
fit_km <- survfit(Surv(time,status) ~ group, data = sim)
ggsurvplot(fit_km, data=sim, risk.table=TRUE, pval=TRUE)
```