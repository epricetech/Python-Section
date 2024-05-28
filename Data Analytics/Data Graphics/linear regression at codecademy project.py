# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:21:24 2023

@author: geron
"""

# Inspect the data
# 1.
# A dataset has been loaded for you in script.py and saved as a dataframe named codecademy.
#  We’re imagining that this data was collected as part of an experiment to understand factors that contribute
#  to learner performance on a quiz. The data contains three columns:

# score: student score on a quiz
# completed: the number of other content items on Codecademy that the learner has completed prior to this quiz
# lesson: indicates which lesson the learner took directly before the quiz ('Lesson A' or 'Lesson B')
# Take a look at this dataset by printing the first five rows.


# Hint
# Use the .head() method on codecademy along with print() to print the first five rows.

# Note that a solution.py file is loaded for you in the workspace, which contains the solution code for this project.

# Model the relationship between quiz score and number of completed content items
# 2.
# Plot a scatter plot of score (y-axis) against completed (x-axis) to see the relationship between quiz score and 
# number of completed content items. Make sure to show, then clear the plot.

# Is there a relationship between these two variables, and does it appear to be linear?


# Hint
# Use plt.scatter() to create a scatter plot. The first argument is the x-variable (codecademy.completed) and the 
# second argument is the y-variable (codecademy.score). After calling plt.scatter(), use the following two lines of
#  code to show, then clear the plot:

# plt.show() # Show the plot
# plt.clf() # Clear the plot
# Note that a solution.py file is loaded for you in the workspace, which contains the solution code for this project.

# 3.
# Create and fit a linear regression model that predicts score using completed as the predictor. Print out the
#  regression coefficients.


# Hint
# Below is the code to fit a model to predict weight using height as a predictor, where weight and height are columns
#  of a dataframe named body_measurements.

# Modify this code to instead predict score using completed as the predictor, where score and completed are columns 
# of a dataframe named codecademy.

# model = sm.OLS.from_formula('weight ~ height', data = body_measurements)
# results = model.fit()
# print(results.params)
# 4.
# Write a one-sentence (each) interpretation of the slope and intercept that you printed out in the previous step. 
# Make sure to comment out the interpretation so your code still runs.


# Hint
# The intercept is the expected value of the outcome variable when the predictor variable is equal to zero. 
# The slope is the expected difference in the outcome variable for a one unit increase in the predictor variable.

# 5.
# Plot the same scatter plot that you made earlier (with score on the y-axis and completed on the x-axis), 
# but this time add the regression line on top of the plot. Make sure to show, then clear the plot.

# Do you think this line fits the data well?


# Hint
# There are a few different ways to accomplish this, but one option is to use plt.plot() to create the line, 
# using the completed column from the original data as the x-coordinates (first argument) and the predicted
#  values of score (based on the model) as the y-coordinates (second argument). The code should look something 
#  like this (you’ll need to fill in the blanks):

# # Create the scatter plot:
# plt.scatter(codecademy.completed, codecademy.score)
 
# # Add the line:
# plt.plot(___, model_results.predict(___))
 
# # Show then clear the plot
# plt.show() # Show the plot
# plt.clf() # Clear the plot
# 6.
# Use your model to calculate the predicted quiz score for a learner who has previously completed 20 other content items.


# Hint
# There are a few ways to do this:

# One option is to use the .predict() method on your fitted model and pass in a new dataset with completed = 20. 
# You can create this new dataset as follows:
# newdata = {'completed':[20]}
# Another option is to use your equation of a line along with the intercept and slope you calculated when you fit the model.
#  The formula looks something like: slope * 20 + intercept.
# The answer should be about 39.3.

# 7.
# Calculate the fitted values for your model and save them as fitted_values.


# Hint
# Use the .predict() method on your fitted model and pass in the data that was used to fit the model (codecademy).

# Note that a solution.py file is loaded for you in the workspace, which contains the solution code for this project.

# 8.
# Calculate the residuals for the model and save the result as residuals.


# Hint
# Subtract the fitted_values that you calculated in the previous from the true student quiz scores (codecademy.score).

# 9.
# Check the normality assumption for linear regression by plotting a histogram of the residuals. Make sure to show and 
# clear the plot.

# Do the residuals appear to be approximately normally distributed?


# Hint
# Use plt.hist() to create a histogram and pass in the residuals that you calculated in the previous step. 
# Then, make sure to show and clear the plot using plt.show() and plt.clf().

# 10.
# Check the homoscedasticity assumption for linear regression by plotting the residuals (y-axis) against 
# the fitted values (x-axis).

# Do you see any patterns or is the homoscedasticity assumption met?


# Hint
# Use plt.scatter() to create the scatter plot and pass in fitted_values as the first argument 
# (x-variable) and residuals as the second argument (y-variable). Then, make sure to show and clear 
# the plot using plt.show() and plt.clf().

# There is no pattern in this plot; the homoscedasticity assumption is met.

# Do learners who take lesson A or B perform better on the quiz?
# 11.
# Let’s now turn our attention to the lessons column to see if learners who took different lessons scored 
# differently on the quiz.

# Use sns.boxplot to create a boxplot of score (y-variable) for each lesson (x-variable) to see the 
# relationship between quiz score and which lesson the learner completed immediately before taking the quiz. 
# Make sure to show, then clear the plot.

# Does one lesson appear to do a better job than the other of preparing students for this quiz? If so, which one?


# Hint
# Use sns.boxplot() to create a boxplot. The code is provided below (with a few blanks to fill in):

# sns.boxplot(x = 'lesson', y = '___', data = ___)
# plt.show() # Show the plot
# plt.clf() # Clear the plot
# Note that a solution.py file is loaded for you in the workspace, which contains the solution code for this project.

# 12.
# Create and fit a linear regression model that predicts score using lesson as the predictor.
#  Print out the regression coefficients.


# Hint
# Below is the code to fit a model to predict weight using height as a predictor, where weight and 
# height are columns of a dataframe named body_measurements.

# Modify this code to instead predict score using lesson as the predictor, where score and lesson
#  are columns of a dataframe named codecademy.

# model = sm.OLS.from_formula('weight ~ height', data = body_measurements)
# results = model.fit()
# print(results.params)
# 13.
# Calculate and print out the mean quiz scores for learners who took lesson A and lesson B.
# Calculate and print out the mean difference.
# Can you see how these numbers relate to the intercept and slope that you printed out in the linear regression output?


# Hint
# To calculate and print the mean quiz score for learners who took lesson A, you can use the following code:

# print(np.mean(codecademy.score[codecademy.lesson == 'Lesson A']))
# You should find that the intercept from the regression output is equal to the mean score for
#  learners who took lesson A, and the slope is equal to the mean difference.

# Next steps
# 14.
# Congratulations! You’ve used a simple linear model to understand how quiz scores are related to 
# other learner actions. In this project, we’ve focused on modeling the relationship between quiz 
# score and one other variable at a time (first we looked at completed, then we looked at lesson separately).

# The next step in linear regression is to model quiz scores as a function of multiple other variables at once! 
# To get a preview of what this might look like visually, let’s try using seaborn‘s lmplot() function to plot
#  a scatter plot of score vs. completed, colored by lesson. For context, the lm in lmplot() stands for “linear model”. 
#  This function will automatically plot a linear regression model on top of the scatter plot. The code to
#  implement this looks like:

# sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
# plt.show()
# Note that when we include a third variable in our plot using the hue parameter (which controls the
# color of each point in the scatter plot), something interesting happens! All of a sudden, we end 
# up with multiple regression lines. To find out how to fit and interpret this model, you’ll have to continue 
# learning about linear regression!


# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import codecademylib3

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head(5))
# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed,codecademy.score)
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', codecademy)
results = model.fit()
print(results.params)
#Results
#Intercept	13.21411302117958
#completed	1.306825592807168

# Intercept interpretation:
# A learner who has previously completed 0 content items is expected to earn a quiz score of 13.2 points.

# Slope interpretation:
# Students who have completed one additional prior content item are expected to score 1.3 points higher on the quiz.

# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed,codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))
plt.show()
plt.clf()
# Show then clear plot

# Predict score for learner who has completed 20 prior lessons
pred20 = results.params[0] + results.params[1]*20
#OR
#newdata = {'completed':[20]}
#pred20 = results.predict(newdata)
#print('predicted score for learner who has completed 20 #prior lessons: ', pred20)
# Calculate fitted values
fitted_values = results.predict(codecademy)
# Calculate residuals
residuals = codecademy.score - fitted_values
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
# Create a boxplot of score vs lesson
sns.boxplot(x = 'lesson', y = 'score', data = codecademy)
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', codecademy)
results = model.fit()
print(results.params)
#output
#Intercept	59.22
#lesson[T.Lesson B]	-11.64200000000001

# Calculate and print the group means and mean difference (for comparison)
mean_score_lessonA = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
mean_score_lessonB = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])
print('Mean score (A): ', mean_score_lessonA)
print('Mean score (B): ', mean_score_lessonB)
print('Mean score difference: ', mean_score_lessonA - mean_score_lessonB)
#OR alternatively
print(codecademy.groupby('lesson').mean().score)
# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()
































