# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:32:30 2023

@author: geron
"""

# The data set obesity contains 18 predictor variables. Here’s a brief description of them.

# Gender is 1 if a respondent is male and 0 if a respondent is female.
# Age is a respondent’s age in years.
# family_history_with_overweight is 1 if a respondent has family member who is or was overweight, 0 if not.
# FAVC is 1 if a respondent eats high caloric food frequently, 0 if not.
# FCVC is 1 if a respondent usually eats vegetables in their meals, 0 if not.
# NCP represents how many main meals a respondent has daily (0 for 1-2 meals, 1 for 3 meals, and 2 for more than 3 meals).
# CAEC represents how much food a respondent eats between meals on a scale of 0 to 3.
# SMOKE is 1 if a respondent smokes, 0 if not.
# CH2O represents how much water a respondent drinks on a scale of 0 to 2.
# SCC is 1 if a respondent monitors their caloric intake, 0 if not.
# FAF represents how much physical activity a respondent does on a scale of 0 to 3.
# TUE represents how much time a respondent spends looking at devices with screens on a scale of 0 to 2.
# CALC represents how often a respondent drinks alcohol on a scale of 0 to 3.
# Automobile, Bike, Motorbike, Public_Transportation, and Walking indicate a respondent’s primary mode of transportation. 
# Their primary mode of transportation is indicated by a 1 and the other columns will contain a 0.
# The outcome variable, NObeyesdad, is a 1 if a patient is obese and a 0 if not.

# 2.
# In order to use a logistic regression model, you’ll need to split the data into two parts: the predictor variables 
# and an outcome variable. Do this by splitting the data into a DataFrame of predictor variables called X and a 
# Series of outcome variables y.


# Hint
# Fill in the appropriate column name in the following code.

# X = obesity.drop(["___"], axis=1)
# y = obesity.___
# 3.
# Create a logistic regression model called lr. Include the parameter max_iter=100 to make sure that the model will 
# converge when you try to fit it.


# Stuck? Get a hint
# 4.
# Use the .fit() method on lr to fit the model to X and y.


# Stuck? Get a hint
# 5.
# A model’s accuracy is the proportion of classes that the model correctly predicts. is Compute and print the
#  accuracy of lr by using the .score() method. What percentage of respondents did the model correctly predict as 
#  being either obese or not obese? You may want to write this number down so that you can refer to it during future tasks.


# Hint
# Fill in the blanks in the code print(lr.score(_, _)). The accuracy should be about 0.7659, meaning that the model 
# correctly predicts the class of about 76% of respondents.

# Sequential Forward Selection
# 6.
# Now that you’ve created a logistic regression model and evaluated its performance, you’re ready to do some 
# feature selection.

# Create a sequential forward selection model called sfs.

# Be sure to set the estimator parameter to lr and set the forward and floating parameters to the appropriate values.
# Also use the parameters k_features=9, scoring='accuracy', and cv=0.

# Hint
# Use something similar to the following. You’ll need to change the name of the model and some of the parameters.

# sffs = SFS(model, 
#           k_features=5, 
#           forward=True, 
#           floating=True, 
#           scoring='accuracy',
#           cv=0)
# 7.
# Use the .fit() method on sfs to fit the model to X and y. This step will take some time (not more than a minute) to run.


# Hint
# Fill in the blanks in the code sfs.fit(_, _).

# 8.
# Now that you’ve run the sequential forward selection algorithm on the logistic regression model with X and y 
# you can see what features were chosen and check the model accuracy on the smaller feature set.
#  Print sfs.subsets_[9] to inspect the results of sequential forward selection.


# Hint
# Use the print() function.

# 9.
# Use the dictionary sfs.subsets_[9] to print a tuple of chosen feature names. 
# Then use it to print the accuracy of the model after doing sequential forward selection.
#  How does this compare to the model’s accuracy on all available features? 
#  You may want to write this number down so that you can compare it with the accuracies of other models.


# Hint
# Fill in the keys 'feature_names' and 'avg_score' to access the feature names and accuracy.

# print(sfs.subsets_[9][___])
# print(sfs.subsets_[9][___])
# The accuracy should be about 0.7693.

# 10.
# It can be helpful to visualize the results of sequential forward selection and see how accuracy 
# is affected as each feature is added. Use the code plot_sfs(sfs.get_metric_dict()) to plot the model 
# accuracy as a function of the number of features used. Make sure to show your plot as well.


# Hint
# Use the the given code as well as plt.show().

# Sequential Backward Selection
# 11.
# Before completing this task group, you should comment out all the code you wrote for the previous 
# task group (Sequential Forward Selection). Your code will take a long time to run and this will ensure
#  that the learning environment won’t time out.

# Sequential forward selection was able to find a feature subset that performed marginally better 
# than the full feature set. Let’s use a different sequential method and see how it compares.

# Create a sequential backward selection model called sbs.

# Be sure to set the estimator parameter to lr and set the forward and floating parameters to the appropriate values.
# Also use the parameters k_features=7, scoring='accuracy', and cv=0.

# Hint
# Use something similar to the following. You’ll need to change the name of the model and some of the parameters.

# sffs = SFS(model, 
#           k_features=5, 
#           forward=True, 
#           floating=True, 
#           scoring='accuracy',
#           cv=0)
# 12.
# Use the .fit() method on sbs to fit the model to X and y.


# Hint
# Fill in the blanks in the code sbfs.fit(_, _).

# 13.
# Now that you’ve run the sequential backward selection algorithm on the logistic regression model 
# with X and y you can see what features were chosen and check the model accuracy on the smaller feature set. 
# Print sbs.subsets_[7] to inspect the results of sequential backward selection.


# Hint
# Use the print() function.

# 14.
# Use the dictionary sbs.subsets_[7] to print a tuple of chosen feature names. Then use it to print the
#  accuracy of the model after doing sequential backward selection. How does this compare to the model’s 
#  accuracy on all available features? You may want to write this number down so that you can compare it 
#  with the accuracies of other models.


# Hint
# Fill in the keys 'feature_names' and 'avg_score' to access the feature names and accuracy.

# print(sbs.subsets_[7][___])
# print(sbs.subsets_[7][___])
# The accuracy should be about 0.7821.

# 15.
# You can visualize the results of sequential backward floating selection just as you did with sequential 
# forward selection. Use the code plot_sfs(sbs.get_metric_dict()) to plot the model accuracy as a function
#  of the number of features used. Be sure to include plt.clf() in order to clear the previous graph before 
#  trying to show the new graph.


# Hint
# Use the given code as well as plt.show().

# Recursive Feature Elimination
# 16.
# Before completing this task group, you should uncomment all the code you wrote for the previous task groups 
# (Sequential Forward Selection and Sequential Backward Selection). Your code will take a long time to run and 
# this will ensure that the learning environment won’t time out.

# So far you’ve tried two different sequential feature selection methods. Let’s try one more: recursive 
# feature elimination. First you’ll standardize the data, then you’ll fit the RFE model and inspect the results.

# At a later step of this project, you’ll need to be able to access feature names. Enter the code
#  features = X.columns for use later.


# Hint
# Type features = X.columns.

# 17.
# Before doing applying recursive feature elimination it is necessary to standardize the data.
#  Standardize X and save it as a DataFrame by creating a StandardScaler() object and using the .fit_transform() method.


# Hint
# Use the code X = pd.DataFrame(StandardScaler().fit_transform(X)).

# 18.
# Create an RFE() object that selects 8 features. Be sure to set the estimator parameter to lr.


# Hint
# Use something similar to the following. You’ll need to change the parameters.

# rfe = RFE(estimator=model, n_features_to_select=5)
# 19.
# Fit the recursive feature elimination model to X and y.


# Hint
# Fill in the blanks in the code rfe.fit(_, _).

# 20.
# Now that you’ve fit the RFE model you can evaluate the results. Create a list of chosen feature 
# names and call it rfe_features. You can use a list comprehension and filter the 
# features in zip(features, rfe.support_) based on whether their support is True (meaning the model kept them) 
# or False (meaning the model eliminated them).


# Hint
# [f for (f, support) in zip(features, rfe.support_) if support] will produce the desired list of feature names.

# 21.
# Use the .score() method on rfe and print the model accuracy after doing recursive feature elimination. 
# How does this compare to the model’s accuracy on all available features?


# Hint
# Fill in the blanks in the code print(rfe.score(_, _)).

# The accuracy should be about 0.7579.


# Import libraries
import codecademylib3
import pandas as pd
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE

# Load the data
obesity = pd.read_csv("obesity.csv")

# Inspect the data
print(obesity.head(5))

# Split the data into predictor variables and an outcome variable # 2
X = obesity.drop(["NObeyesdad"], axis=1)
y = obesity.NObeyesdad
# Create a logistic regression model
lr = LogisticRegression(max_iter=100)

# Fit the logistic regression model # 4
lr.fit(X,y)

# Print the accuracy of the model # 5
print(lr.score(X,y))

# Create a sequential forward selection model  # 6
#sfs = SFS(lr,k_features = 9, forward = True, floating=False,scoring='accuracy',cv=0)

# Fit the sequential forward selection model to X and y
#sfs.fit(X,y)

# Inspect the results of sequential forward selection
#print(sfs.subsets_[9])

# See which features sequential forward selection chose
#print(sfs.subsets_[9]['feature_names'])

# Print the model accuracy after doing sequential forward selection   # 9
#print(sfs.subsets_[9]['avg_score'])

# Plot the model accuracy as a function of the number of features used
# plot_sfs(sfs.get_metric_dict())
# plt.show()
# Create a sequential backward selection model  # 11
sbs = SFS(lr,k_features=7,forward=False,floating=False,scoring='accuracy',cv=0)

# Fit the sequential backward selection model to X and y
sbs.fit(X,y)

# Inspect the results of sequential backward selection
print(sbs.subsets_[7])

# See which features sequential backward selection chose  # 14
print(sbs.subsets_[7]['feature_names'])

# Print the model accuracy after doing sequential backward selection
print(sbs.subsets_[7]['avg_score'])

# Plot the model accuracy as a function of the number of features used
plot_sfs(sbs.get_metric_dict())
plt.show()
# Get feature names
features = X.columns

# Standardize the data
X = pd.DataFrame(StandardScaler().fit_transform(X))

# Create a recursive feature elimination model
rfe = RFE(estimator=lr, n_features_to_select=8)

# Fit the recursive feature elimination model to X and y
rfe.fit(X,y)

# See which features recursive feature elimination chose
rfe_features = [f for (f, support) in zip(features, rfe.support_) if support]
print(rfe_features)

# Print the model accuracy after doing recursive feature elimination
print(rfe.score(X, y))






































