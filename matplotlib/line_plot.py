import matplotlib.pyplot as plt
import random

"""

Line graphs are used to display the r/ship in time series data and another variable, let's say years and weights

"""

# Let's generate weights between 70 and 90 
weights = [random.randint(70, 90) for _ in range(10)]
print(weights)

years = [2000 + x for x in range(10)]
print(years)

# Let's plot a r/ship between the years and avg weights in a company
plt.plot(years, weights, c='b')
plt.title("Avg weights of Kenyan adults from 2000 to 2025")
plt.ylabel("Weights in kilograms")
plt.xlabel("Years")
plt.show()