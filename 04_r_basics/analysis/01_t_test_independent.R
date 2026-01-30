# Independent two-sample t-test (Radiology example)
# Compare mean age between two IR treatment groups (TACE vs TARE)
# Replace simulated data with your study dataset as needed.

set.seed(42)

# Simulate data
group <- factor(rep(c("TACE","TARE"), each=50))
age   <- c(rnorm(50, mean=64, sd=9), rnorm(50, mean=61, sd=10))

df <- data.frame(group, age)

# Assumptions (normality per group, equal variances)
shapiro_p <- by(df$age, df$group, shapiro.test)
cat("Shapiro-Wilk p-values by group:\n")
print(sapply(shapiro_p, function(x) x$p.value))

var_p <- var.test(age ~ group, data=df)$p.value
cat("F-test for equal variances p=", signif(var_p,3),"\n")

# Welch t-test by default (robust to unequal variances)
res <- t.test(age ~ group, data=df)
print(res)

# Effect size (Cohen's d)
cohen_d <- (mean(df$age[df$group=="TACE"]) - mean(df$age[df$group=="TARE"])) / sd(df$age)
cat("Cohen's d:", round(cohen_d,3),"\n")
# Interpretation of Cohen's d
if (abs(cohen_d) < 0.2) {
  cat("Effect size: negligible\n")
} else if (abs(cohen_d) < 0.5) {
  cat("Effect size: small\n")
} else if (abs(cohen_d) < 0.8) {
  cat("Effect size: medium\n")
} else {
  cat("Effect size: large\n")
}
# Visualization
library(ggplot2)
ggplot(df, aes(x=group, y=age, fill=group)) +
  geom_boxplot(alpha=0.7) +
  geom_jitter(width=0.2, alpha=0.5) +
  labs(title="Age by Treatment Group", x="Treatment Group", y="Age") +
  theme_minimal()
# Save plot
ggsave("../figures/01_t_test_independent_age_by_treatment.png", width=
6, height=4)

# End of script
