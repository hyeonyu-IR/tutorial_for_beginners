# Correlation (Pearson & Spearman)
set.seed(42)
muscle_area <- rnorm(90, mean=120, sd=20)   # L3 skeletal muscle area (cm^2)
outcome     <- 0.3*muscle_area + rnorm(90,0,10)

cor.test(muscle_area, outcome, method="pearson")
cor.test(muscle_area, outcome, method="spearman")

# Visualize
library(ggplot2)
df <- data.frame(muscle_area, outcome)
ggplot(df, aes(x=muscle_area, y=outcome)) +
  geom_point() +
  geom_smooth(method="lm", col="blue") +
  labs(title="Correlation between Muscle Area and Outcome",
       x="L3 Skeletal Muscle Area (cm^2)",
       y="Outcome Measure") +
  theme_minimal()

# Save results
pearson_res <- cor.test(muscle_area, outcome, method="pearson")
spearman_res <- cor.test(muscle_area, outcome, method="spearman")
saveRDS(pearson_res, file="../results/pearson_correlation.rds")
saveRDS(spearman_res, file="../results/spearman_correlation.rds")
ggsave("../results/correlation_plot.png")

# End of file