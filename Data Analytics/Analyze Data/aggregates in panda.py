# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:13:35 2023

@author: geron
"""


# mean
# Average of all values in column
# std
# Standard deviation
# median
# Median
# max
# Maximum value in column
# min
# Minimum value in column
# count
# Number of values in column
# nunique
# Number of unique values in column
# unique
# List of unique values in column





import pandas as pd

orders = pd.read_csv('orders.csv')

print(orders.head(10))

most_expensive = orders.price.max()
print(most_expensive)

num_colors = orders.shoe_color.nunique()
print(num_colors)



#this is a way to get an average grade for each student across all assignments- this pandas option can be used instead of doing a loop
#grades = df.groupby('student').grade.mean()
#groupby syntax
#df.groupby('column1').column2.measurement()



import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)

print(type(pricey_shoes))
#<class 'pandas.core.series.Series'>
#for the code above if you add .reset_index() to the end of pricey shoes you can see the type change
#<class 'pandas.core.frame.DataFrame'>

#renames the colummn
#teas_counts = teas_counts.rename(columns={"id": "counts"})


# np.percentile can calculate any percentile over an array of values
# high_earners = df.groupby('category').wage 
#     .apply(lambda x: np.percentile(x, 75))  \
#     .reset_index()

import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')


cheap_shoes = orders.groupby('shoe_color').price.apply(
  lambda x: np.percentile(x,25)).reset_index()

print(cheap_shoes)

#selecting mulitple columns for groupby
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()

print(shoe_counts)


#pivot tables to reorganize data in groupby statments
# First use the groupby statement:
# unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# # Now pivot the table
# pivoted = unpivoted.pivot(
#     columns='Day of Week',
#     index='Location',
#     values='Total Sales')

#creates a pivot table
shoe_counts_pivot = shoe_counts.pivot(
  columns='shoe_color',
  index='shoe_type',
  values='id'
).reset_index()

print(shoe_counts_pivot)




