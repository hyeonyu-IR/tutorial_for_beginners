# Linear mixed-effects model (random intercepts)
# Requires: lme4
set.seed(42)
N <- 180
subject <- factor(rep(1:60, each=3))
visit <- factor(rep(1:3, times=60))
age <- rnorm(60, 62, 8)[subject]
# response with subject-specific random intercept
u <- rnorm(60, 0, 5)[subject]
y <- 50 - 0.3*as.numeric(visit) + 0.2*age + u + rnorm(N,0,3)

df <- data.frame(subject, visit, age, y)

suppressPackageStartupMessages(library(lme4))
fit <- lmer(y ~ visit + age + (1|subject), data=df)
summary(fit)

# Extract fixed effects
fixef(fit)

# Extract random effects
ranef(fit)

# Predictions
df$pred <- predict(fit)

# Plot observed vs predicted
plot(df$y, df$pred, xlab="Observed", ylab="Predicted
", main="LMM: Observed vs Predicted")
abline(0,1,col="red")

# Save the model summary to a text file
sink("../results/lmm_model_summary.txt")
print(summary(fit))
sink()

# Save the fitted model object
saveRDS(fit, file="../results/lmm_fitted_model.rds")

# End of script