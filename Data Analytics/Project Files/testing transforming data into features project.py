# # -*- coding: utf-8 -*-
# """
# Created on Fri May 12 09:22:54 2023

# @author: geron
# """

# Transforming Data into Features
# You are a data scientist at a clothing company and are working with a data set of customer reviews. 
#This dataset is originally from Kaggle and has a lot of potential for various machine learning purposes. 
#You are tasked with transforming some of these features to make the data more useful for analysis. 
#To do this, you will have time to practice the following:

# Transforming categorical data
# Scaling your data
# Working with date-time features
# Let’s get started!

# Tasks
# 0/16 Complete
# Mark the tasks as complete by checking them off
# Basic Exploration
# 1.
# Let’s start with some basic exploring by performing the following:

# First, import your dataset. It is stored under a file named reviews.csv. Save it to a variable called reviews.


# Hint
# You should have something similar to the following line of code:

# df = pd.read_csv('filename.csv')
# 2.
# Next, we want to look at the column names of our dataset along with their data types. Do the following two steps:

# Print the column names of your dataset.
# Check your features’ data types by printing .info().

# Hint
# To view the column names, use the .columns attribute. If we had a data frame called df, 
#we would use the following line of code:

# print(df.columns)
# To view the data types of each feature, use the .info() method:

# print(df.info())
# Data Transformations
# 3.
# Transform the recommended feature. Start by printing the feature’s .value_counts().


# Hint
# To look at the counts of a feature, do the following:

# #look at the counts
# print(df['col_name'].value_counts())
# You should see the following output:

# True     4166
# False     834
# 4.
# Since this is a True/False feature, we want to transform it to 1 for True and 0 for False.

# To do this, create a dictionary called binary_dict where:

# The keys are what is currently in the recommended feature.
# The values are what we want in the new column (0s and 1s).
# Click the hint if you get stuck.


# Hint
# We want the keys to be True and False, with the values as 1 and 0.

# #create a binary dictionary
# binary_dict = {True:1, False:0}
# 5.
# Using binary_dict, transform the recommended column so that it will now be binary. 
#Print the results using .value_counts() to confirm the transformation.


# Hint
# Your code should look similar to this:

# #create a new column
# df['col_name'] = df['col_name'].map(binary_dict)
 
# #print your transformed column
# print(df['col_name'].value_counts())
# 6.
# Let’s run through a similar process to transform the rating feature. 
#This is ordinal data so our transformation should make that more clear. Again, start by printing the .value_counts().

# To check your output, click the hint.


# Hint
# After printing out the value_counts(), you should have the following output:

# Loved it     2798
# Liked it     1141
# Was okay      564
# Not great     304
# Hated it      193
# 7.
# We want to make the following changes to the values:

# ‘Loved it’ → 5
# ‘Liked it’ → 4
# ‘Was okay’ → 3
# ‘Not great’ → 2
# ‘Hated it’ → 1
# Create a dictionary called rating_dict where the keys are what is currently in the 
#feature and the values are what we want in the new column. You can use the hierarchy listed above to make your dictionary.


# Hint
# Remember that when we made the binary dictionary, we used the following line of code:

# #create a binary dictionary
# binary_dict = {True:1, False:0}
# This time we will have five keys and five values.

# 8.
# Using rating_dict, transform the rating column so it contains numerical values. 
#Print the results using .value_counts() to confirm the transformation.


# Hint
# Your code should look similar to this:

# #create a new column
# df['col_name'] = df['col_name'].map(binary_dict)
 
# #print your transformed column
# print(df['col_name'].value_counts())
# 9.
# Let’s now transform the department_name feature. This process will be slightly different, 
#but start by printing the .value_counts() of the feature.

# Use Panda’s get_dummies to one-hot encode our feature.
# Attach the results back to our original data frame.
# Print the column names to see!

# Hint
# #get the number of categories in a feature
# print(df['col_name'].value_counts())
# 10.
# Use panda’s get_dummies() method to one-hot encode our feature. Assign this to a variable called one_hot.


# Hint
# To perform one-hot encoding, use code similar to the following:

# #perform get_dummies
# one_hot = pd.get_dummies(df['col_name'])
# 11.
# Join the results from one_hot back to our original data frame. Then print out the column names. What has been added?


# Hint
# Use similar code to the following:

# #join the new columns back onto the original
# df = df.join(one_hot)
 
# #print column names
# print(df.columns)
# We now have the following new columns:

# 'Bottoms'
# 'Dresses'
# 'Intimate'
# 'Jackets'
# 'Tops'
# 'Trend'
# 12.
# Let’s make one more feature transformation!

# Transform the review_date feature.

# This feature is listed as an object type, but we want this to be transformed into a date-time feature.

# Transform review_date into a date-time feature.
# Print the feature type to confirm the transformation.
# Click the hint if you get stuck.


# Hint
# Your code should be similar to the following:

# df['new_col'] = pd.to_datetime(df['col'])
 
# print(df['new_col'].dtype)
# Scaling the Data
# 13.
# The final step we will take in our transformation project is scaling our data. 
#We notice that we have a wide range of numbers thus far, so it is best to put everything on the same scale.

# Let’s get our data frame to only have the numerical features we created. If you get stuck, click the hint.


# Hint
# Use the following line of code:

# #get numerical columns
# reviews = reviews[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 
#'Intimate', 'Jackets', 'Tops', 'Trend']].copy()
# 14.
# Reset the index to be our clothing_id feature.


# Hint
# Use the .set_index() method:

# #reset index
# df = df.set_index(col)
# 15.
# We are ready to scale our data! Perform a .fit_transform() on our data set, 
#and print the results to see how the features have changed.


# Hint
# Create a StandardScaler() and then use .fit_transform() on reviews. Your code should be similar to 
#the following two lines of code:

# scaler = StandardScaler()
# scaler.fit_transform(df)
# 16.
# Congratulations!

# You have successfully completed this transformation project. Transformations are an incredibly 
#valuable skill to have. Great job!



import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import data
reviews = pd.read_csv('reviews.csv')
 
#print column names
print(reviews.columns)

#print .info
print(reviews.info()) 

#look at the counts of recommended
print(reviews['recommended'].value_counts())
 
#create binary dictionary
binary_dict = {True:1, False:0}
 
#transform column
reviews['recommended'] = reviews['recommended'].map(binary_dict)

 
#print your transformed column
print(reviews['recommended'].value_counts())

#look at the counts of rating
print(reviews['rating'].value_counts())
 
#create dictionary
rating_dict = {'Loved it':5, 'Liked it':4, 'Was okay':3, 'Not great':2, 'Hated it':1}
 
#transform rating column
reviews['rating'] = reviews['rating'].map(rating_dict)
 
#print your transformed column values
print(reviews['rating'].value_counts())

#get the number of categories in a feature
print(reviews['department_name'].value_counts())
 
#perform get_dummies
one_hot = pd.get_dummies(reviews['department_name'])
 
#join the new columns back onto the original
reviews = reviews.join(one_hot)

#print column names
print(reviews.columns)

#transform review_date to date-time data
reviews['review_date'] = pd.to_datetime(reviews['review_date'])

#print review_date data type 
print(reviews['review_date'].dtype)

#get numerical columns
reviews = reviews[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops', 'Trend']].copy()
 
#reset index
reviews = reviews.set_index('clothing_id')

#instantiate standard scaler
scaler = StandardScaler()
 
#fit transform data
scaler.fit_transform(reviews)





















































