# Kaplan–Meier survival analysis (base survival)
set.seed(42)
N <- 120
group <- factor(sample(c("TACE","TARE"), N, TRUE))

# simulate survival times with modest group effect
time <- rexp(N, rate= ifelse(group=="TACE", 0.06, 0.05))
status <- rbinom(N, 1, 0.8)  # 1=event, 0=censored

suppressPackageStartupMessages(library(survival))
fit <- survfit(Surv(time, status) ~ group)
print(summary(fit))

# Basic plot
plot(fit, col=c('steelblue','tomato'), lwd=2, xlab='Time', ylab='Survival')
legend('topright', legend=levels(group), col=c('steelblue','tomato'), lwd=2)

# Log-rank test
logrank_test <- survdiff(Surv(time, status) ~ group)
print(logrank_test)
p_value <- 1 - pchisq(logrank_test$chisq, length(logrank_test$n) - 1)
cat("Log-rank test p-value:", p_value, "\n")

# Add p-value to plot
text(x= max(time)*0.6, y=0.2, labels=paste
     ("Log-rank p =", signif(p_value, 3)))

# Cox proportional hazards model
cox_model <- coxph(Surv(time, status) ~ group)
summary(cox_model)

# Extract hazard ratio and confidence intervals
hr <- exp(coef(cox_model))
ci <- exp(confint(cox_model))
cat("Hazard Ratio (TARE vs TACE):", hr, "\n")
cat("95% CI:", ci, "\n")

# Add risk table
install.packages("survminer")
library(survminer)
ggsurv <- ggsurvplot(fit, data = data.frame(time, status, group),
                     risk.table = TRUE,
                     pval = TRUE,
                     conf.int = TRUE,
                     palette = c('steelblue','tomato'),
                     xlab = "Time",
                     ylab = "Survival Probability",
                     legend.title = "Group",
                     legend.labs = levels(group))
print(ggsurv)

# Save plot
ggsave("kaplan_meier_plot.png", plot = ggsurv$plot,
       width = 8, height = 6, dpi = 300)
ggsave("kaplan_meier_risk_table.png", plot = ggsurv$table
       , width = 8, height = 4, dpi = 300)

# End of file