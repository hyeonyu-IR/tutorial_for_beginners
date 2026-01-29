
# plotting_ggplot2.R — common plots

suppressPackageStartupMessages({ library(ggplot2); library(ggpubr) })

theme_set(theme_pubr(base_size = 12))

boxplot_jitter <- function(df, x, y, fill = NULL, title = NULL, ylab = NULL) {
  ggplot(df, aes_string(x = x, y = y, fill = fill %||% x)) +
    geom_boxplot(alpha = .6, outlier.shape = NA) +
    geom_jitter(width = .1, alpha = .3) +
    theme_pubr() +
    labs(title = title %||% paste(y, "by", x), x = NULL, y = ylab %||% y)
}
