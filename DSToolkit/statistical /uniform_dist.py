from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1)


a, b = 10, 15
x = np.linspace(10, 15, 1000)
r = uniform(a, b-a).rvs(size=1000)

ax.axhline(y=1 / (b - a), color='r', linestyle='-')
ax.hist(r, density=True, edgecolor='black', alpha=0.5, bins=25)
ax.legend(loc='best', frameon=False)
plt.show()