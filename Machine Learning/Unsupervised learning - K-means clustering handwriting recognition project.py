# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:13:38 2023

@author: geron
"""

# The U.S. Postal Service has been using machine learning and scanning technologies since 1999. Because its postal offices have to look at roughly half a billion pieces of mail every day, they have done extensive research and developed very efficient algorithms for reading and understanding addresses. And not only the post office:

# ATMs can recognize handwritten bank checks
# Evernote can recognize handwritten task lists
# Expensify can recognize handwritten receipts
# But how do they do it?

# In this project, you will be using K-means clustering (the algorithm behind this magic) 
#and scikit-learn to cluster images of handwritten digits.




# Tasks
# 1/18 Complete
# Mark the tasks as complete by checking them off
# Getting Started with the Digits Dataset:
# 1.
# The sklearn library comes with a digits dataset for practice.

# In script.py, we have already added three lines of code:

# import codecademylib3_seaborn
# import numpy as np
# from matplotlib import pyplot as plt
# From sklearn library, import the datasets module.

# Then, load in the digits data using .load_digits() and print digits.


# Hint
# At this point, your code should look like:

# import codecademylib3_seaborn
# import numpy as np
# from matplotlib import pyplot as plt
# from sklearn import datasets
 
# digits = datasets.load_digits()
# print(digits)
# The terminal output should display all the information that comes with the dataset.

digits = datasets.load_digits()
print(digits)


# 2.
# When first starting out with a dataset, it’s always a good idea to go through the data description 
#and see what you can already learn.

# Instead of printing the digits, print digits.DESCR.

# What is the size of an image (in pixel)?
# Where is this dataset from?

# Hint
# Print out the description of the digits data:

# print(digits.DESCR)
# The result should look like:

# Recognition of Handwritten Digits Data Set
# ==========================================
 
# Notes
# -----
 
# Data Set Characteristics:
 
#   :Number of Instances: 5620
#   :Number of Attributes: 64
#   :Attribute Information: 8x8 image of integer pixels in the range 0-16
#   :Missing Attribute Values: None
#   :Creator: E. Alpaydin
#   :Date: July; 1998
# The digit images are 8 x 8. And the dataset is from Bogazici University (Istanbul, Turkey).

print(digits.DESCR)


# 3.
# Let’s see what the data looks like!

# Print digits.data.


# Hint
# Print out the data:

# print(digits.data)
# [[ 0.  0.  5. ...,  0.  0.  0. ]
#  [ 0.  0.  0. ..., 10. 0.  0. ]
#  [ 0.  0.  0. ..., 16.  9.  0. ]
# ... 
# Each list contains 64 values which respent the pixel colors of an image (0-16):

# 0 is white
# 16 is black

print(digits.data)



# 4.
# Next, print out the target values in digits.target.


# Hint
# Print out the target values:

# print(digits.target)
# The result should look like:

# [ 0 1 2 ..., 8 9 8]
# This shows us that the first data point in the set was tagged as a 0 and the last one was tagged as an 8.
print(digits.target)


# 5.
# To visualize the data images, we need to use Matplotlib. Let’s visualize the image at index 100:

# plt.gray() 
 
# plt.matshow(digits.images[100])
 
# plt.show()
# The image should look like:
fig = plt.figure(figsize=(6, 6))
 
# Adjust the subplots 
 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
 
# For each of the 64 images
 
for i in range(64):
 
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
 
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
 
    # Display an image at the i-th position
 
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
 
    # Label the image with the target value
 
    ax.text(0, 7, str(digits.target[i]))
 
plt.show()
plt.gray() 
 
plt.matshow(digits.images[100])
 
plt.show()


# Is it a 4? Let’s print out the target label at index 100 to find out!
print(digits.target[100])
# print(digits.target[100])
# Open the hint to see how you can visualize more than one image.


# Hint
# To take a look at 64 sample images. Copy and paste the code below:

# # Figure size (width, height)
 
# fig = plt.figure(figsize=(6, 6))
 
# # Adjust the subplots 
 
# fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
 
# # For each of the 64 images
 
# for i in range(64):
 
#     # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
 
#     ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
 
#     # Display an image at the i-th position
 
#     ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
 
#     # Label the image with the target value
 
#     ax.text(0, 7, str(digits.target[i]))
 
# plt.show()
# K-Means Clustering:
# 6.
# Now we understand what we are working with. Let’s cluster the 1797 different digit images into groups.

# Import KMeans from sklearn.cluster.
from sklearn.cluster import KMeans

# Hint
# from sklearn.cluster import KMeans
# 7.
# What should be the k, the number of clusters, here?

# Use the KMeans() method to build a model that finds k clusters.


# Hint
# Because there are 10 digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9), there should be 10 clusters.

# So k, the number of clusters, is 10:

# model = KMeans(n_clusters=10, random_state=42)
# The random_state will ensure that every time you run your code, the model is built in the same way. 
#This can be any number. We used random_state = 42.

model = KMeans(n_clusters = 10, random_state=42)



# 8.
# Use the .fit() method to fit the digits.data to the model.

model.fit(digits.data)
# Hint
# model.fit(digits.data)
# Visualizing after K-Means:
# 9.
# Let’s visualize all the centroids! Because data samples live in a 64-dimensional space,
# the centroids have values so they can be images!

# First, add a figure of size 8x3 using .figure().

# Then, add a title using .suptitle().


# Hint
# fig = plt.figure(figsize=(8, 3))
 
# fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

fig = plt.figure(figsize=(8,3))
fig.suptitle('Cluster Center Images', fontsize=14, fontweight= 'bold')


# 10.
# Scikit-learn sometimes calls centroids “cluster centers”.

# Write a for loop to displays each of the cluster_centers_ like so:

# for i in range(10):
 
#   # Initialize subplots in a grid of 2X5, at i+1th position
#   ax = fig.add_subplot(2, 5, 1 + i)
 
#   # Display images
#   ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
# The cluster centers should be a list with 64 values (0-16). Here, we are making each of the cluster centers
# into an 8x8 2D array.





# 11.
# Outside of the for loop, use .show() to display the visualization.

# Did it work?

# These are the centroids of handwriting from thirty different people collected by Bogazici University (Istanbul, Turkey):

# Index 0 looks like 0
# Index 1 looks like 9
# Index 2 looks like 2
# Index 3 looks like 1
# Index 4 looks like 6
# Index 5 looks like 8
# Index 6 looks like 4
# Index 7 looks like 5
# Index 8 looks like 7
# Index 9 looks like 3
# Notice how the centroids that look like 1 and 8 look very similar and 1 and 4 also look very similar.


# Hint
# plt.show()
# 12.
# Optional:

# If you want to see another example that visualizes the data clusters and their centers using K-means,
#check out the sklearn‘s own example.

# K-means clustering example

# You will get a different K-means clustering map each time you run a new K-means model.


# Hint
# In this code, they use k-means++ to place the initial centroids.

# Testing Your Model:
# 13.
# Instead of feeding new arrays into the model, let’s do something cooler!

# Inside the right panel, go to test.html.


# Hint
# https://localhost/test.html

# 14.
# What year will robots take over the world?

# Use your mouse to write a digit in each of the boxes and click Get Array.


# Hint
# 2020?

# 15.
# Back in script.py, create a new variable named new_samples and copy and paste the 2D array into it.

# new_samples = np.array(      )

# Hint
# Copy and paste the entire code into the parentheses:

# new_samples = np.array(      )
# Make sure to even copy paste the outer square brackets.

# 16.
# Use the .predict() function to predict new labels for these four new digits. Store those predictions
# in a variable named new_labels.


# Hint
# new_labels = model.predict(new_samples)
 
# print(new_labels) 
# 17.
# But wait, because this is a clustering algorithm, we don’t know which label is which.

# By looking at the cluster centers, let’s map out each of the labels with the digits we think it represents:

# for i in range(len(new_labels)):
#   if new_labels[i] == 0:
#     print(0, end='')
#   elif new_labels[i] == 1:
#     print(9, end='')
#   elif new_labels[i] == 2:
#     print(2, end='')
#   elif new_labels[i] == 3:
#     print(1, end='')
#   elif new_labels[i] == 4:
#     print(6, end='')
#   elif new_labels[i] == 5:
#     print(8, end='')
#   elif new_labels[i] == 6:
#     print(4, end='')
#   elif new_labels[i] == 7:
#     print(5, end='')
#   elif new_labels[i] == 8:
#     print(7, end='')
#   elif new_labels[i] == 9:
#     print(3, end='')

# Hint
# We did print(x, end='') so that all the digits are printed on the same line.

# Index 0 looks like 0
# Index 1 looks like 9
# Index 2 looks like 2
# Index 3 looks like 1
# Index 4 looks like 6
# Index 5 looks like 8
# Index 6 looks like 4
# Index 7 looks like 5
# Index 8 looks like 7
# Index 9 looks like 3
# 18.
# Is the model recognizing your handwriting?

# Remember, this model is trained on handwritten digits of 30 Turkish people (from the 1990’s).







































