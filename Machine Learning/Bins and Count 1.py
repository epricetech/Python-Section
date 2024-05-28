# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:46:43 2023

@author: geron
"""

#  2 key features of histograms - bins and counts
# Bins - is a sub-range of values that falls within the range of a dataset.  all bins must be the same width
# count - is the number of values that fall within a bins range


# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

# Set the minimum and maximums of the array below
min_days_old = np.amin(days_old_bread)
max_days_old = np.amax(days_old_bread)
# Set the number of bins to 3
bins = 3

# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")


#  histogram

# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use numpy.histogram() below
times_hist = np.histogram(times, range = (0, 24), bins = 4)

print(times_hist)


import codecademylib3
import numpy as np
import pandas as pd

# import pyplot as plt
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use plt.hist() below
plt.hist(times,range=(0,24),bins=4)
plt.show()




