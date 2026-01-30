"""Matplotlib quickstart, R ggplot mental map."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
age = np.random.normal(62, 10, 120)
sm  = 140 - 0.4*age + np.random.normal(0, 8, 120)

plt.figure(figsize=(6,4))
plt.scatter(age, sm, s=20, c='gray', alpha=0.7)
coef = np.polyfit(age, sm, 1)
line = np.poly1d(coef)
xs = np.linspace(age.min(), age.max(), 100)
plt.plot(xs, line(xs), color='red', lw=2)
plt.xlabel('Age'); plt.ylabel('Skeletal Muscle Area'); plt.title('Scatter with Fit')
plt.tight_layout()
plt.savefig('05_python_basics/figures/py_scatter_fit.png', dpi=300)
print('Saved figure to 05_python_basics/figures/py_scatter_fit.png')
