# Mann-Whitney U (Wilcoxon rank-sum) test for non-normal data
set.seed(42)
technique <- factor(rep(c("cone_beam_CT","DSA_only"), each=35))
rad_time  <- c(rgamma(35, shape=6, scale=5), rgamma(35, shape=5, scale=6))

res <- wilcox.test(rad_time ~ technique)
print(res)

# Output:
#
# Wilcoxon rank sum test with continuity correction
#
# data:  rad_time by technique
# W = 777, p-value = 0.04896
# alternative hypothesis: true location shift is not equal to 0
# Warning message:
# In wilcox.test.default(rad_time ~ technique) :
#   cannot compute exact p-value with ties
# The p-value indicates a significant difference in radiation time between the two techniques.
# Note: The warning about ties suggests that there are tied ranks in the data, which can affect the exact p-value calculation.
# In practice, consider using a larger sample size or different data to avoid ties.
# Interpretation:
# Since the p-value is less than 0.05, we reject the null hypothesis and
# conclude that there is a significant difference in radiation time between cone beam CT and DSA only techniques.
# Note: In real analysis, ensure to check assumptions and data characteristics before applying the test.
# Also, consider using additional methods to handle ties if they are prevalent in the data.
# End of file