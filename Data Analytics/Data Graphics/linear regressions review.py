# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:37:31 2023

@author: geron
"""

# A new dataset named website has been loaded for you in the workspace containing simulated data for a sample of visitors to a
#  website, including the amount of time in seconds they spent on the website (time_seconds), their age (age), 
#  and information about whether they accessed the website using Chrome or Safari (browser).

# Try to work through the following steps (solution code is provided in solution.py). Note that after 
# showing each plot with plt.show(), we’ve included the command plt.clf() in the starting code to ensure 
# that plots are not layered on top of each other.

# Create a plot of time_seconds (vertical axis) versus age (horizontal axis). Is there a linear 
# relationship between these variables?
# Fit a linear model to predict time_seconds using the age variable
# Use the coefficients from the linear model to plot the regression line on top of your original plot.
# Calculate the fitted values and residuals
# Check the normality assumption by plotting a histogram of the residuals. Are they approximately normally distributed?
# Check the homoscedasticity assumption by plotting a the residuals against the fitted values. Is this assumption satisfied?
# Use your model to predict the amount of time that a 40 year old person will spend on the website.
# Fit another model that predicts time_seconds based on browser.
# Print out the coefficients. What is the difference in average time spent on each browser?




# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
website = pd.read_csv('website.csv')

# Print the first five rows
print(website.head())

# Create a scatter plot of time vs age
plt.scatter(website.age, website.time_seconds)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict time_seconds based on age
model = sm.OLS.from_formula('time_seconds ~ age', website)
results = model.fit()
print(results.params)

# Plot the scatter plot with the line on top
plt.scatter(website.age, website.time_seconds)
plt.plot(website.age, results.params[0] + results.params[1]*website.age)

# Show then clear plot
plt.show()
plt.clf()

# Calculate fitted values
fitted_values = results.predict(website)

# Calculate residuals
residuals = website.time_seconds - fitted_values

# Check normality assumption
plt.hist(residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Predict amount of time on website for 40 year old
pred40 = results.params[0] + results.params[1]*40
print('predicted time on website for a 40 year old: ', pred40)

# Fit a linear regression to predict time_seconds based on age
model = sm.OLS.from_formula('time_seconds ~ browser', website)
results = model.fit()
print(results.params)

# Calculate and print the group means (for comparison)
mean_time_chrome = np.mean(website.time_seconds[website.browser == 'Chrome'])
mean_time_safari = np.mean(website.time_seconds[website.browser == 'Safari'])
print('Mean time (Chrome): ', mean_time_chrome)
print('Mean time (Safari): ', mean_time_safari)
print('Mean time difference: ', mean_time_chrome - mean_time_safari)

# results   graphs showed all normal distributions
#    time_seconds   age browser
# 0         486.0  47.1  Safari
# 1         645.7  64.6  Chrome
# 2         345.0  45.4  Safari
# 3         413.4  34.4  Chrome
# 4         426.4  31.3  Safari
# Intercept    128.967945
# age            6.913758
# dtype: float64
# predicted time on website for a 40 year old:  405.5182489324498
# Intercept            489.704255
# browser[T.Safari]    -99.057086
# dtype: float64
# Mean time (Chrome):  489.70425531914884
# Mean time (Safari):  390.64716981132074
# Mean time difference:  99.0570855078281





