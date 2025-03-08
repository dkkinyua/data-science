import matplotlib.pyplot as plt
import numpy as np

"""
Histograms are used to visualize frequencies between data for example, the distribution of ages of the participant's of a Data Science hackathon at Google

"""

ages = np.random.normal(25, 1.5, 500) # np.random.normal(mean, standard deviation, sample_size)

plt.hist(ages)
plt.title("Age distribution of participants at the DS Hackathon by Google")
plt.ylabel("Number of participants")
plt.xlabel("Ages")
plt.show()