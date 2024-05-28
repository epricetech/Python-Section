# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:26:25 2023

@author: geron
"""
#covariance using np.cov() puting the variables in the () np means numPy function

import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision = 1) 

housing = pd.read_csv('housing_sample.csv')

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.sqfeet, housing.beds)
print(cov_mat_sqfeet_beds)

# store the covariance as cov_sqfeet_beds
cov_sqfeet_beds = 228.2    #  this was the matching number from the above code.  


#Correlation using pearsonr() function from scipy.state

import pandas as pd
import matplotlib.pyplot as plt 

from scipy.stats import pearsonr

housing = pd.read_csv('housing_sample.csv')

# calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p=pearsonr(housing.sqfeet,housing.beds)
print(corr_sqfeet_beds)

# create the scatter plot here:
plt.scatter(x=housing.beds,y=housing.sqfeet)
plt.xlabel('Square Feet')
plt.ylabel('Number of beds')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt 

from scipy.stats import pearsonr

sleep = pd.read_csv('sleep_performance.csv')

# create your scatter plot here:
plt.scatter(x=sleep.hours_sleep, y=sleep.performance)
plt.xlabel('Hours slept')
plt.ylabel('How well')
plt.show()

# calculate the correlation for `hours_sleep` and `performance`:
corr_sleep_performance, p=pearsonr(sleep.hours_sleep, sleep.performance)
print(corr_sleep_performance)



#Overall review
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import codecademylib3
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1) 

penguins = pd.read_csv('penguins.csv')

#print the first few rows
print(penguins.head())

#create a scatter plot
plt.scatter(penguins.flipper_length_mm, penguins.body_mass_g)
plt.show()

#calculate covariance:
covariance_mat = np.cov(penguins.flipper_length_mm, penguins.body_mass_g)
print("covariance matrix: ")
print(covariance_mat)

print("covariance: ", covariance_mat[1][0])

#calculate correlation:
correlation, p = pearsonr(penguins.flipper_length_mm, penguins.body_mass_g)
print("correlation: ", correlation)