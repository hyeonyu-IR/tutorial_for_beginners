
# run_analysis.R — minimal end-to-end driver script

isntall.packages <- function(pkg){
  new.pkg <- pkg[!(pkg %in% installed.packages()[, "Package"])]
  if (length(new.pkg)) 
    install.packages(new.pkg, dependencies = TRUE)
}

required.packages <- c("tidyverse", "janitor", "survival", "survminer", "broom")
isntall.packages(required.packages)


suppressPackageStartupMessages({
  library(tidyverse); library(janitor)
})

source("r/snippets/data_io.R")
source("r/snippets/analysis_linear_logistic.R")
source("r/snippets/analysis_survival.R")

# ---- Parameters (edit here) ----
DATA_PATH <- "data/analysis_dataset.csv"
OUTCOME    <- "outcome"              # 0/1
TIME       <- "time"                 # numeric time
STATUS     <- "status"               # 0/1
COVARS     <- c("age","sex","group","bmi")
GROUP      <- "group"
# --------------------------------

# Load and clean data
DF <- read_clean(DATA_PATH)

# View summary
print(glimpse(DF))

# Logistic (multivariable)
fit_log <- run_logistic(DF, OUTCOME, COVARS)
print(or_table(fit_log))

# Survival (Cox)
fit_cox <- run_cox(DF, TIME, STATUS, COVARS)
print(hr_table(fit_cox))

# Kaplan–Meier by group
km <- run_km(DF, TIME, STATUS, GROUP)
# To display, call: print(plot_km(km, DF)) in an interactive session
