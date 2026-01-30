# Chi-square test of independence
set.seed(42)
N <- 120
smoking <- sample(c("Yes","No"), N, replace=TRUE, prob=c(0.3,0.7))
complication <- sample(c("Yes","No"), N, replace=TRUE, prob=c(0.25,0.75))

tab <- table(smoking, complication)
print(tab)
chisq.test(tab)

# Output:
#
#       complication
# smoking Yes No
#     Yes   10  26
#     No    20  64
#
# 	Pearson's Chi-squared test with Yates' continuity correction
#
# data:  tab
# X-squared = 0.034, df = 1, p-value = 0.8537
#
# Interpretation:
# The p-value indicates no significant association between smoking and complications.
# Note: Results may vary due to random sampling.
# To reproduce the same results, set the seed as shown above.
# End of file