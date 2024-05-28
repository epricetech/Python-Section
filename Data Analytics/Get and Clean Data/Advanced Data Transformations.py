# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:32:11 2023

@author: geron
"""

#  when data is skewed you can use transformation to get a more  normal distributions
#  log transformation is a method that replaces x with log(x)
#  when log transformation is applied to data that is not normally distrubuted the result in that data will be less skewed
#  To do so you would us the numpy library and the np.log(variable) method
#  you can also use PowerTransfromer from sklearn
# from sklearn.preprocessing import PowerTransformer
# # log transformation
# log_transform = PowerTransformer()
# log_transfrom.fit_transfrom(variable)


#example
import numpy as np
import pandas as pd
import seaborn as sns


# read in data file
home_data = pd.read_csv('home_data.csv')


# store home price data
home_prices = home_data['SalePrice']

# plot data
sns.distplot(home_prices)

#  resultes show a right skewed distribution
print(home_prices.skew())
# we can print the skew and the reult is 1.88
#  if skew is less than -1 or grater than 1 the more the skew

#now we need to transform the data to get a more normal distribution
log_home_prices = np.log(home_prices)

#Next, let’s plot the transformed data to see the shape of the distribution:
sns.distplot(log_home_prices)
#The distribution is more normalized and the skew is closer to 0
print(home_prices.skew())
#0.12133506220520406













