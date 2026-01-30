# Logistic regression (binary outcome) with odds ratios
set.seed(42)
N <- 150
age <- rnorm(N, 63, 10)
ASA <- sample(2:4, N, TRUE)
sarcopenia <- rbinom(N, 1, 0.35)

# probability of complication increases with age and sarcopenia
linpred <- -4 + 0.04*age + 0.9*sarcopenia + 0.3*(ASA-2)
prob <- 1/(1+exp(-linpred))
complication <- rbinom(N,1,prob)

df <- data.frame(age, ASA=factor(ASA), sarcopenia=factor(sarcopenia), complication)
fit <- glm(complication ~ age + ASA + sarcopenia, data=df, family=binomial())
summary(fit)

# Odds ratios with 95% CI
OR <- exp(coef(fit)); CI <- exp(suppressMessages(confint(fit)))
print(cbind(OR, CI))

# Interpretation:
# - For a one year increase in age, the odds of complication increase by a factor of
#   exp(0.04) = 1.04, or 4%.
# - Patients with sarcopenia have exp(0.9) = 2.
#   times the odds of complication compared to those without sarcopenia, holding other variables constant.
# - Compared to ASA 2, ASA 3 patients have exp(0.3)
#   = 1.35 times the odds of complication, and ASA 4 patients have exp(0.6) = 1.82 times the odds.
# Note: Odds ratios can be misleading when the outcome is common (>10% incidence).

# Check model fit with Hosmer-Lemeshow test
install.packages("ResourceSelection")
library(ResourceSelection)
hl <- hoslem.test(df$complication, fitted(fit), g=10)
print(hl)

# A p-value > 0.05 indicates good fit.

# Visualize predicted probabilities
df$pred_prob <- fitted(fit)
library(ggplot2)
ggplot(df, aes(x=age, y=pred_prob, color=sarcopenia
)) +
  geom_point(aes(y=complication), alpha=0.3) +
  geom_smooth(method="loess") +
  labs(y="Predicted Probability of Complication", color="Sarcopenia") +
  theme_minimal()
# This plot shows how predicted probabilities of complication vary with age and sarcopenia status.

# save the model for future use 
save(fit, file="../output/logistic_regression_model.RData")

# To load later: load("../output/logistic_regression_model.RData")

# To predict on new data:
# new_data <- data.frame(age=c(60,70), ASA=factor(c(2,3)), sarcopenia=factor(c(0,1)))
# predict(fit, newdata=new_data, type="response")
# This will give predicted probabilities for the new patients.
# End of logistic regression analysis
