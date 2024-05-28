# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:36:37 2023

@author: geron
"""

# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
mu, sigma = 800, 100 # mean and standard deviation
burrito_calories = np.random.normal(mu, sigma, 320)

# Save transaction times to a separate numpy array
plt.hist(burrito_calories, range=(250, 1250), bins=100,  edgecolor='black')
plt.title("Calories in a Burrito Bowl", fontsize = 24)
plt.xlabel("Calories", fontsize=18)
plt.ylabel("Count", fontsize=18)

plt.show()

# finding the average
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")
transactions = transactions.drop(["Unnamed: 0"], axis = 1)

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Print transactions below
print(transactions)

# Print the average times below
print(np.average(times))



#  Range      range = max(data) - min(data)

exercise_ages = np.array([22, 27, 45, 62, 34, 52, 42, 22, 34, 26])
min_age = np.amin(exercise_ages) # Answer is 22
max_age = np.amax(exercise_ages) # Answer is 62
age_range = max_age - min_age


import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction data to numpy arrays
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Find the minimum time, maximum time, and range
min_time = np.amin(times)
max_time = np.max(times)
range_time = max_time - min_time

# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))










