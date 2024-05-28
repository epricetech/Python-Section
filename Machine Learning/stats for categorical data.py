# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:27:23 2023

@author: geron
"""

#  Normall you summarize data using numbers like quantitative data summarizing central tendency with mean, median, mode or
#  spread with standard deviation, variance or percentiles.   Categorical data are words not numbers so these ways wont always work
#  
# Nominal Categories  - has no intrinsic ordering to categoriy.  - cant calculate mean or median or deviation only 
# mode using value_counts() function  
#  Example  - looking in categorical columns and counting the values to find the most common
counts = df['marital.status'].value_counts()
print(counts)
#  this actually takes the code from above and results and assing to this variable and prints
modal_cat = counts.index[0]
print(modal_cat) # Output: Married-civ-spouse


#  Another example
# Read NYC Trees Data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Get tree counts by neighborhood
tree_counts = nyc_trees['neighborhood'].value_counts()

# Get neighborhoods with most trees
greenest_neighborhood = tree_counts.index[0]
print(greenest_neighborhood)



#  ordinal categorical variables - Central Tendency
#  these have an order to them  - we can find the mode just like before but we can also find the median
#  in order to calculate numerical stats for ordered categories we first have to assign a numerical value to those categories
#  example education level - high school, college, some college - assign an ordered value to each
#  We will also use the pd.Categorical() function to convert and use ordered = True to indicate ordering
#  Variables stored as type category have an attribute (cat.codes) that converts the categories to numbers. 
#This allows us to perform numerical operations on this categorical field. This allows us to calculate the median 
#category using numpy’s median() function:
# one key thing when converting the numbers the numbers will be evenly spaced, however the values ordinal categorical 
# might not be evenly spaced.  example education level 1st grade, 2nd-4th grade, high school, 10th grade - these values
# not evenly spaced and some are grouped together so the median might be skewed because of this
    # Example

import pandas as pd
import numpy as np
# this variable takes the current list of values and puts them in a specific order you want to convert for values
correct_order = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'HS-grad', 'Some-college', 'Assoc-voc', 'Assoc-acdm', 'Bachelors', 'Masters', 'Prof-school', 'Doctorate']
 
df['education'] = pd.Categorical(df['education'], correct_order, ordered=True)

median_index = np.median(df['education'].cat.codes)
print(median_index) # Output: 9
 
median_category = correct_order[int(median_index)]
print(median_category) # Output: Some college
#By using .cat.codes on education, we’re able to calculate that the median value for education level is '9' 
#which translates to 'Some college'.




import pandas as pd
import numpy as np

# Read NYC trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

tree_health_statuses = nyc_trees['health'].unique()
print(tree_health_statuses)
health_categories = ['Poor', 'Fair', 'Good']

nyc_trees['health'] = pd.Categorical(nyc_trees['health'], health_categories, ordered=True)
#  these lines find and caluculate the median
median_index = np.median(nyc_trees['health'].cat.codes)
median_health_status = health_categories[int(median_index)]
print(median_health_status)

#  ordinal categories that are not evenly spread finding the mean - whcih doesnt really work in this example because
# of the ordinal categorical values not being evenly spaced.  

import pandas as pd
import numpy as np

# Read NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census2.csv")

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)'], ordered=True)

# Get Mean Diam of diameter variable, `trunk_diam`
mean_diam = np.mean(nyc_trees['trunk_diam'])
print(mean_diam)

# Get Mean Category of `tree_diam_category`
mean_diam_cat = np.mean(nyc_trees['tree_diam_category'].cat.codes)
print(mean_diam_cat)



#  ordinal categories - spread - Unable to find standard deviation and variance because you cant always depend on 
# an accurate mean with unevenly spread out ordinal categorical values  Instead we can find ranges or percentiles/quantiles
#  We can use the np.percentile() function along with .cat.codes  
#  example - calculates a range containing 80% of the data
tenth_perc_ind = np.percentile(df['education'].cat.codes, 10)
tenth_perc_cat = correct_order[int(tenth_perc_ind)]
print(tenth_perc_cat) # output: 11th
 
nintieth_perc_ind = np.percentile(df['education'].cat.codes, 90)
nintieth_perc_cat = correct_order[int(nintieth_perc_ind)]
print(nintieth_perc_cat): #output: Bachelors


#  example  Then we can use this to find the IQR
import pandas as pd
import numpy as np

# Read NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census2.csv")

size_labels_ordered = ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)']

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, size_labels_ordered, ordered=True)

# Calculate 25th Percentile Category
convert = np.percentile(nyc_trees.tree_diam_category.cat.codes,25)
p25_tree_diam_category = size_labels_ordered[int(convert)]
print(p25_tree_diam_category)

# Calculate 75th Percentile Category
p75_convert = np.percentile(nyc_trees.tree_diam_category.cat.codes,75)

p75_tree_diam_category = size_labels_ordered[int(p75_convert)]
print(p75_tree_diam_category)



#  Table of proportions - instead of just looking at the frequency with .valucounts() we look at the propotion of values
#  we calculate proportions by dividing the frequency by the number of overbservations in the data
# Example
df['education'].value_counts()/len(df['education'])
# or this way
df['education'].value_counts(normalize = True).head()

#  example of above
import pandas as pd

# Read NYC Trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

tree_status_proportions = nyc_trees['status'].value_counts()/len(nyc_trees['status'])
print(tree_status_proportions)


#  tables of proportions - missing data - you can set the dropna paramater in the value_counts() function to determine
# how to handle NaN values 
#  example
df.workclass.value_counts(dropna = False, normalize = True)
# In contrast, using .value_counts(normalize = True) (or .value_counts(normalize = True, dropna = True) to be explicit) 
#returns proportion of a specific workclass group as a portion of people in the dataset who responded to this question.
#  which will not keep the nan values in calculations
#  if use dropna=False it means we want to include the Nan in our calculations  dropna=True means we dont caluculate them
import pandas as pd

# Get NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census.csv")

health_proportions = nyc_trees['health'].value_counts(normalize=True)
print(health_proportions)

health_proportions_2 = nyc_trees['health'].value_counts(dropna=False, normalize=True)



#  Binary Categorical Variables - only have 2 categories - np.sum() - True = 1 False = 0 np.mean
#  a nifty trick  or any variable by using a conditional to translate a non-binary variable into True and False values. 
#For example, recall the workclass variable from the previous exercise. Suppose that you want to calculate the number
# (or proportion) of people who work in local government. We could translate the workclass column to a binary variable
# indicating whether a person works in local government (True) or not (False) by using a conditional.
#print(df.workclass == 'Local-gov')
#Then, we can use the sum or mean to calculate a frequency or proportion of Trues in the data.
#(df.workclass == 'Local-gov').sum()  #output: 2093
#(df.workclass == 'Local-gov').mean() #output: 0.064


import pandas as pd
import numpy as np

# Get NYC Trees Data
nyc_trees = pd.read_csv('nyc_tree_census.csv')
print(nyc_trees)
#  finding frequency and proportion
living_frequency = np.sum(nyc_trees.status == 'Alive')
living_proportion= (nyc_trees.status == 'Alive').mean()
print(living_frequency)
print(living_proportion)
#  finding frequency and proportion for values with trunk diam > 30
giant_frequency = np.sum(nyc_trees.trunk_diam > 30)
giant_proportion = (nyc_trees.trunk_diam > 30).mean()
print(giant_frequency)
print(giant_proportion)



