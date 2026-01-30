# Figure 2: Odds ratios from logistic regression

set.seed(42)
N <- 150
age <- rnorm(N, 63, 10)
ASA <- sample(2:4, N, TRUE)
sarc <- rbinom(N, 1, 0.35)
linpred <- -4 + 0.04*age + 0.9*sarc + 0.3*(ASA-2)
prob <- 1/(1+exp(-linpred))
complication <- rbinom(N,1,prob)

df <- data.frame(age, ASA=factor(ASA), sarc=factor(sarc), complication)
fit <- glm(complication ~ age + ASA + sarc, data=df, family=binomial())

OR <- exp(coef(fit))
CI <- exp(confint(fit))

# Simple forest-style plot
png("Fig2_Logistic_ORs.png", width=900, height=600)
par(mar=c(5,8,4,2))
plot(OR[-1], seq_along(OR[-1]), xlim=range(CI[-1,]),
     xlab='Odds Ratio', ylab='', yaxt='n', pch=19)
segments(CI[-1,1], seq_along(OR[-1]), CI[-1,2], seq_along(OR[-1]))
abline(v=1, lty=2)
axis(2, at=seq_along(OR[-1]), labels=names(OR[-1]), las=2)
dev.off()
