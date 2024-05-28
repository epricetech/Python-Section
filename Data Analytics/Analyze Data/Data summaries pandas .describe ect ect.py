# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:44:53 2023

@author: geron
"""

#central Tendency for Quantitative Data - finding the typical value of the variable
# # Mean
# rentals.rent.mean()
 
# # Median
# rentals.rent.median()
 
# # Mode
# rentals.rent.mode()
 
# # Trimmed mean
# from scipy.stats import trim_mean
# trim_mean(rentals.rent, proportiontocut=0.1)  # trim extreme 10%



import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()

# Save the median to med_budget
med_budget = movies.production_budget.median()

# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()
print(mode_budget)
# Save the trimmed mean to trmean_budget
from scipy.stats import trim_mean
trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.2)
print(trmean_budget)


#Spread for quantitative data - finding the amount

# There are several common measures of spread:

# Range: The difference between the maximum and minimum values of a variable.
# Interquartile range (IQR): The difference between the 75th and 25th percentile values.
# Variance: The average of the squared distance from each data point to the mean.
# Standard deviation (SD): The square root of the variance.
# Mean absolute deviation (MAD): The mean absolute value of the distance between each data point and the mean.
# For our rentals DataFrame, we can calculate the spread for the rent column as follows:

# # Range
# rentals.rent.max() - rentals.rent.min()
 
# # Interquartile range
# rentals.rent.quantile(0.75) - rentals.rent.quantile(0.25)
 
# from scipy.stats import iqr
# iqr(rentals.rent)  # alternative way
 
# # Variance
# rentals.rent.var()
 
# # Standard deviation
# rentals.rent.std()
 
# # Mean absolute deviation
# rentals.rent.mad()


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the range to range_budget
range_budget = movies.production_budget.max() - movies.production_budget.min()
print(range_budget)
# Save the interquartile range to iqr_budget
iqr_budget = movies.production_budget.quantile(0.75) - movies.production_budget.quantile(0.25)
print(iqr_budget)

# Save the variance to var_budget
var_budget = movies.production_budget.var()
print(var_budget)

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()


#when you need to visualize quantitaive variables.  common are boxplot() and histplot()
import matplotlib.pyplot as plt 
import seaborn as sns
 
# Boxplot for rent
sns.boxplot(x='rent', data=rentals)
plt.show()
plt.close()

# Histogram for rent
sns.histplot(x='rent', data=rentals)
plt.show()
plt.close()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv('movies.csv')

# Create a boxplot for movie budget 
sns.boxplot(x='production_budget', data=movies)
plt.show()
plt.close()


# Create a histogram for movie budget
sns.histplot(x='production_budget', data=movies)
plt.show()
plt.close()



import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the counts to genre_counts

genre_counts = movies.genre.value_counts()
print(genre_counts)


# Proportions of rental listings in each borough
rentals.borough.value_counts() / len(rentals.borough)

# Alternatively, we could also obtain the proportions by specifying normalize=True to the .value_counts() method:

# df.borough.value_counts(normalize=True)


import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the proportions to genre_props
genre_props = movies.genre.value_counts(normalize=True)
print(genre_props)


# options for categorical variables
# # Pie chart for borough
# rentals.borough.value_counts().plot.pie()
# plt.show()
# plt.close()


import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

movies = pd.read_csv('movies.csv')

# Create a bar chart for movie genre 
sns.countplot(x='genre', data=movies)
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()


# bar chart uses countplot()


