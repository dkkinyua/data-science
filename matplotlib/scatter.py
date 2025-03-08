import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100 # 50 random values between 0 to 100
y_data = np.random.random(50) * 100 # same

# print(x_data)
# print(y_data)

# Let's plot a scatterplot for values above
plt.scatter(x_data, y_data, c="#000", s=75, marker='*')
plt.show()