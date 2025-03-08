import numpy as np
import matplotlib.pyplot as plt

"""
Boxplots check the distribution of certain feature, let's say heights of male students in a university.

"""

heights = np.random.normal(170, 1.5, 500) # Mean = 170cm, Std Deviation = 1.5, Sample size = 500
plt.boxplot(heights)
plt.title("Distribution of Male student heights in a university")
plt.ylabel("Heights in cm")
plt.show()
