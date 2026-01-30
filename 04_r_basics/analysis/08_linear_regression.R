# Multiple linear regression + diagnostics
set.seed(42)
N <- 120
age <- rnorm(N, 62, 10)
sex <- factor(sample(c("F","M"), N, TRUE))
BMI <- rnorm(N, 27, 4)
sm_area <- 140 - 0.4*age + 5*(sex=="M") + 0.8*BMI + rnorm(N,0,8)

df <- data.frame(age, sex, BMI, sm_area)
fit <- lm(sm_area ~ age + sex + BMI, data=df)
summary(fit)

# Diagnostics
par(mfrow=c(2,2)); plot(fit)
par(mfrow=c(1,1))

install.packages("car")
library(car)

# Check for non-constant variance
ncvTest(fit)

# Check for influential points
influencePlot(fit)

# Check for multicollinearity
vif(fit)

# Added-variable plots
avPlots(fit)

# Component + residual plots
crPlots(fit)

# Residuals vs leverage plot
residuals <- rstandard(fit)
leverage <- hatvalues(fit)
plot(leverage, residuals,
     xlab="Leverage", ylab="Standardized Residuals",
     main="Residuals vs Leverage")
abline(h=0, lty=2)
cutoff <- 2*mean(leverage)
abline(v=cutoff, lty=2, col="red")
text(leverage[leverage > cutoff],
     residuals[leverage > cutoff],
     labels=which(leverage > cutoff), pos=4, col="red")     

# Reset plotting layout
par(mfrow=c(1,1))

# Prediction with confidence and prediction intervals
new_data <- data.frame(age=c(50,70
), sex=c("F","M"), BMI=c(22,30))
pred_conf <- predict(fit, newdata=new_data, interval="confidence")
pred_pred <- predict(fit, newdata=new_data, interval="prediction")
pred_conf
pred_pred

# Compare models with ANOVA
fit_reduced <- lm(sm_area ~ age + BMI, data=df)
anova(fit_reduced, fit)

# Stepwise model selection
fit_step <- step(fit_reduced, scope=list(lower=fit_reduced, upper=
fit), direction="both")
summary(fit_step)

# Final model diagnostics
par(mfrow=c(2,2)); plot(fit_step)
par(mfrow=c(1,1))
ncvTest(fit_step)
influencePlot(fit_step)
vif(fit_step)
avPlots(fit_step)
crPlots(fit_step)
residuals_step <- rstandard(fit_step)
leverage_step <- hatvalues(fit_step)

plot(leverage_step, residuals_step,
     xlab="Leverage", ylab="Standardized Residuals",
     main="Residuals vs Leverage (Final Model)")
abline(h=0, lty=2)

cutoff_step <- 2*mean(leverage_step)
abline(v=cutoff_step, lty=2, col="red")

text(leverage_step[leverage_step > cutoff_step],
     residuals_step[leverage_step > cutoff_step],
     labels=which(leverage_step > cutoff_step), pos=4, col="red")
par(mfrow=c(1,1))

# End of analysis/08_linear_regression.R
# save the workspace
save.image(file = "analysis/08_linear_regression.RData")

# To load the workspace in future R sessions, use:
# load("analysis/08_linear_regression.RData")
