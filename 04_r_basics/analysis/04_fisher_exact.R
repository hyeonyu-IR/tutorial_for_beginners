# Fisher's exact test (small counts)
# Example: technical success (yes/no) by device type

mat <- matrix(c(18,2, 10,7), nrow=2, byrow=TRUE)
colnames(mat) <- c("Success","Failure")
rownames(mat) <- c("Device_A","Device_B")

print(mat)
res <- fisher.test(mat)
print(res)

# Odds ratio and confidence interval
print(res$estimate)
print(res$conf.int)

# p-value
print(res$p.value)

# Interpretation
if (res$p.value < 0.05) {
  cat("There is a significant association between device type and technical success (p <", res$p.value, ").\n")
} else {
  cat("There is no significant association between device type and technical success (p =", res$p.value, ").\n")
}
# End of file