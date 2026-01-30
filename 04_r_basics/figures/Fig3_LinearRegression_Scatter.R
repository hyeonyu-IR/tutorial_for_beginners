# Figure 3: Linear regression scatter plot with fitted line

set.seed(42)
N <- 120
age <- rnorm(N, 62, 10)
BMI <- rnorm(N, 27, 4)
sm_area <- 140 - 0.4*age + 0.8*BMI + rnorm(N,0,8)

png("Fig3_MuscleArea_vs_Age.png", width=900, height=700)
plot(age, sm_area, pch=19, col='darkgray',
     xlab='Age', ylab='Skeletal Muscle Area')
fit <- lm(sm_area ~ age)
abline(fit, col='red', lwd=2)
dev.off()
