
# Makefile for single-command rebuilds of the 04_r_basics module
# Usage (from repo root):
#   make all        # run analyses, generate figures, render report
#   make analysis   # run only analysis scripts
#   make figures    # generate only figures
#   make report     # render report only
#   make install-deps  # install required R packages
#   make clean      # remove generated HTML (and optional figures)

R := Rscript --vanilla
MOD := 04_r_basics
ANALYSIS := $(MOD)/analysis
FIGURES := $(MOD)/figures
REPORTS := $(MOD)/reports

.PHONY: all analysis figures report install-deps clean

all:
	@$(R) -e "setwd('$(MOD)'); source('run_all.R')"

analysis:
	@$(R) -e "d <- list.files('$(ANALYSIS)', pattern='\\\.R$$', full.names=TRUE); for (f in d) { message('Running: ', basename(f)); try(source(f), silent=TRUE) }"

figures:
	@$(R) -e "d <- list.files('$(FIGURES)', pattern='\\\.R$$', full.names=TRUE); for (f in d) { message('Plotting: ', basename(f)); try(source(f), silent=TRUE) }"

report:
	@$(R) -e "if (!requireNamespace('rmarkdown', quietly=TRUE)) quit(status=1); rmarkdown::render(file.path('$(REPORTS)', 'analysis_report.Rmd'), quiet=TRUE)"
	@echo "Report generated: $(REPORTS)/analysis_report.html"

install-deps:
	@$(R) -e "pkgs <- c('rmarkdown','survival','lme4','ggplot2','knitr'); ins <- setdiff(pkgs, rownames(installed.packages())); if (length(ins)) install.packages(ins, repos='https://cloud.r-project.org')"

clean:
	@rm -f $(REPORTS)/analysis_report.html
	@echo "Cleaned generated report. (Remove figures manually if needed)"
