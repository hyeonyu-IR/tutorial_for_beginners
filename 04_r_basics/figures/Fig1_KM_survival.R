# Figure 1: Kaplan–Meier survival curve
# Requires: survival

set.seed(42)
suppressPackageStartupMessages(library(survival))

N <- 120
group <- factor(sample(c("TACE","TARE"), N, TRUE))
time <- rexp(N, rate= ifelse(group=="TACE", 0.06, 0.05))
status <- rbinom(N, 1, 0.8)

fit <- survfit(Surv(time, status) ~ group)

png("Fig1_KM_TACE_vs_TARE.png", width=900, height=700)
plot(fit, col=c('steelblue','tomato'), lwd=2,
     xlab='Time', ylab='Survival Probability')
legend('topright', legend=levels(group),
       col=c('steelblue','tomato'), lwd=2)
dev.off()
