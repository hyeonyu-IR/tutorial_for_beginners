
# R for Clinical Research (Tidyverse-first)

Focused on **logistic regressions**, **Cox survival models**, and **multivariable analysis** with reusable patterns for minimal modification across projects.

## 0) Setup & reproducibility

```r
install.packages(c(
  "tidyverse","readxl","janitor","lubridate","forcats","stringr",
  "skimr","gtsummary","broom","ggpubr","survival","survminer",
  "lme4","lmerTest","car","emmeans","pwr","mice","tableone",
  "flextable","officer"
))

install.packages("renv")
renv::init(); renv::snapshot()
```

## 1) Data I/O & cleaning

```r
library(tidyverse); library(readxl); library(janitor)

df <- readr::read_csv("data/analysis_dataset.csv") %>% clean_names()
# Excel: df <- readxl::read_excel("data/raw.xlsx", sheet = 1) %>% clean_names()
```

## 2) Wrangling essentials

```r
library(dplyr); library(tidyr); library(forcats); library(lubridate)

df <- df %>%
  mutate(
    sex = factor(sex, levels=c("F","M")),
    group = fct_relevel(group, "control","treatment"),
    bmi_cat = cut(bmi, breaks=c(-Inf,18.5,25,30,Inf), labels=c("under","normal","over","obese"))
  )
```

## 3) Quick EDA

```r
library(skimr)
skimr::skim(df)

df %>% count(group, sex)
```

## 4) Visualization

```r
library(ggplot2); library(ggpubr)

ggplot(df, aes(group, bmi, fill=group)) +
  geom_boxplot(alpha=.6) + geom_jitter(width=.1, alpha=.3) +
  theme_pubr() + labs(x=NULL, y="BMI", title="BMI by group")
```

## 5) Logistic regression (binary outcomes)

```r
library(broom); library(gtsummary)

fit_log <- glm(outcome ~ age + sex + group + bmi, data=df, family=binomial)
# Odds ratios with 95% CI
broom::tidy(fit_log, exponentiate=TRUE, conf.int=TRUE)

# Publication-ready
tbl_log <- tbl_regression(fit_log, exponentiate=TRUE) %>% bold_p(t = 0.05)
```

## 6) Cox proportional hazards (survival)

```r
library(survival); library(survminer)

s <- Surv(time=df$time, event=df$status)
fit_cox <- coxph(s ~ age + sex + group + bmi, data=df)
# Hazard ratios
broom::tidy(fit_cox, exponentiate=TRUE, conf.int=TRUE)

# KM plot
fit_km <- survfit(s ~ group, data=df)
pp <- ggsurvplot(fit_km, data=df, risk.table=TRUE, conf.int=TRUE, pval=TRUE)
```

## 7) Diagnostics & checks

```r
# Logistic: calibration (Hosmer-Lemeshow)
# install.packages("ResourceSelection")
ResourceSelection::hoslem.test(df$outcome, fitted(fit_log))

# Cox proportional hazards assumption
cox.zph(fit_cox)
```

## 8) Multiple testing & power

```r
p.adjust(c(.01, .03, .2, .0005), method="BH")
# Power example
pwr::pwr.t.test(d=0.5, power=0.8, sig.level=0.05, type="two.sample")
```

## 9) Tables to Word

```r
library(flextable); library(officer)

doc <- read_docx() %>%
  body_add_flextable(as_flextable(tbl_log))
print(doc, target="outputs/tables.docx")
```

## 10) Reusable templates

See `r/templates/` for parameterized Quarto and Rmd that run logistic or Cox models with minimal edits. See `r/snippets/` for reusable functions.
