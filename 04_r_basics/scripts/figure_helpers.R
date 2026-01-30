# Figure Helper Utilities (Radiology Style)
# Place in 04_r_basics/scripts/figure_helpers.R

# Minimal dependencies; ggplot2 optional (only needed for ggplot objects)
opts <- list(
  dpi = 300,                     # journal-friendly resolution
  width_single = 3.5,            # inches, single-column width
  width_onehalf = 5.0,           # inches, 1.5-column width
  width_double = 7.2,            # inches, double-column width
  height_default = 5.0           # inches, default height
)

# Return standard width (inches) by type
std_width <- function(type = c('single','onehalf','double')) {
  type <- match.arg(type)
  switch(type,
    single = opts$width_single,
    onehalf = opts$width_onehalf,
    double = opts$width_double
  )
}

# Save a figure with consistent parameters
# If 'p' is a ggplot object, uses ggsave; otherwise uses base devices
save_fig <- function(filename, p = NULL, width = std_width('single'), height = opts$height_default,
                     dpi = opts$dpi, device = c('png','pdf')) {
  device <- match.arg(device)
  dir.create(dirname(filename), showWarnings = FALSE, recursive = TRUE)

  if (!is.null(p) && inherits(p, 'ggplot')) {
    if (!requireNamespace('ggplot2', quietly = TRUE)) stop('ggplot2 not installed')
    ggplot2::ggsave(filename, plot = p, width = width, height = height, dpi = dpi, limitsize = FALSE)
  } else {
    if (device == 'png') {
      png(filename, width = width, height = height, units = 'in', res = dpi)
      on.exit(dev.off(), add = TRUE)
      if (!is.null(p)) print(p)  # if plotting object was provided
    } else {
      pdf(filename, width = width, height = height)
      on.exit(dev.off(), add = TRUE)
      if (!is.null(p)) print(p)
    }
  }

  message('Saved figure: ', filename)
}

# A minimal ggplot theme suitable for manuscripts
rad_theme <- function(base_size = 11) {
  if (!requireNamespace('ggplot2', quietly = TRUE)) stop('ggplot2 not installed')
  ggplot2::theme_minimal(base_size = base_size) +
    ggplot2::theme(
      panel.grid.minor = ggplot2::element_blank(),
      axis.title = ggplot2::element_text(face='bold'),
      plot.title = ggplot2::element_text(face='bold')
    )
}
