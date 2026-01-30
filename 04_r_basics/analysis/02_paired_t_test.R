# Paired t-test: biomarker before vs after IR procedure
set.seed(42)
pre  <- rnorm(40, mean=2.1, sd=0.4)
post <- pre - rnorm(40, mean=0.2, sd=0.2)  # improvement

res <- t.test(pre, post, paired=TRUE)
print(res)

# Visualize the results
library(ggplot2)
install.packages("reshape2")
library(reshape2)

data <- data.frame(
  Subject = 1:40,
  Pre = pre,
  Post = post
)

data_melted <- melt(data, id.vars = "Subject", variable.name = "Time", value.name = "Biomarker")

# plot
ggplot(data_melted, aes(x=Time, y=Biomarker, group=Subject)) +
  geom_line(alpha=0.3) +
  geom_point() +
  stat_summary(fun=mean, geom="point", size=4, color="red") +
  stat_summary(fun=mean, geom="line", aes(group=1), color="red", size=1) +
  labs(title="Paired t-test: Biomarker Before vs After IR Procedure",
       y="Biomarker Level") +
  theme_minimal()

ggsave("../results/paired_t_test_biomarker.png")
ggsave("../results/paired_t_test_biomarker.pdf")

# Save results
sink("../results/paired_t_test_results.txt")
cat("Paired t-test Results:\n")
print(res)
sink()

# End of file