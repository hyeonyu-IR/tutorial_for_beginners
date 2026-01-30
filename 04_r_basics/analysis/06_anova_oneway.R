# One-way ANOVA (3+ groups) with Tukey post-hoc
set.seed(42)
technique <- factor(rep(c("TACE","TARE","PAE"), times=c(35,35,30)))
los <- c(rnorm(35, 3.5, 1.1), rnorm(35, 2.9, 0.9), rnorm(30, 2.7, 1.0))

fit <- aov(los ~ technique)
summary(fit)
TukeyHSD(fit)
plot(TukeyHSD(fit))
par(mfrow=c(2,2))
plot(fit)
par(mfrow=c(1,1))
library(ggplot2)
ggplot(data=data.frame(technique, los), aes(x=technique, y=los)) +
  geom_boxplot(fill="lightblue") +
  geom_jitter(width=0.2, alpha=0.5) +
  labs(title="Length of Stay by Treatment Technique",
       x="Treatment Technique",
       y="Length of Stay (days)") +
  theme_minimal()
ggsave("../figures/06_anova_oneway_boxplot.png")
# End of file
# Save results
anova_results <- summary(fit)
tukey_results <- TukeyHSD(fit)
save(anova_results, tukey_results, file="../results/06_anova_oneway_results
.RData")

# End of file
