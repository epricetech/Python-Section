# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 08:48:29 2023

@author: geron
"""

# unsupervised learning is used when we need to find patterns and structure to unlabled data - meaning when your data
# wont be sorted into categories or have labels or answer your question you use unsupervised learning to get that into
#  Clustering - finds structure in unlabeled data by identifying similar groups or clusters.  
#  example of clusterin
# 1. Recommendation engine - group products to personalize the user experience
# 2. Search engines - groups topics and search results
# 3. Market segmentation - group customers based on geography, demography and behaviors
# 4. image segmentation - medical imiagin or road scene segmntation on self driving cars
# 5. Text clusting - group similiar texts together based on word usage.


# K-Means clustering - Tries to address 2 questions
# 1. The K refers to the number of clusters or groups we expect to find in the dataset
# 2. The MEANS regers to the average distance of data to each cluster center also known as the centriod which we are trying
# to minimize.  
#  This is a iterative approch meaning
# 1. Place k random centroids for the initial clusters.
# 2. Assign data samples to the nearest centroid.
# 3. Calculate new centroids based on the above-assigned data samples.
# 4. Repeat Steps 2 and 3 until convergence.
# convergance occurs when points dont move between clusters and centroids stabilize.  This is called training.  
#  once complete we can take new unlabled datapoint and quickly assign to appropriate clusters - this is called inference


# The Iris data set is famous example of unlabed data.  it consits of measures of sepals and petals on 50 diffreent iris flowers
from sklearn import datasets
iris = datasets.load_iris()

#output looks like this
# [[ 5.1  3.5  1.4  0.2 ]
#  [ 4.9  3.   1.4  0.2 ]
#  [ 4.7  3.2  1.3  0.2 ]
#  [ 4.6  3.1  1.5  0.2 ]
#    . . .
#  [ 5.9  3.   5.1  1.8 ]]
# each row of data is a sample - each flower is one sample - we are interested in features like petal length or color

import codecademylib3_seaborn
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()

print(iris.data)
#The iris.target values give the ground truth for the Iris dataset. Ground truth, in this case, is the number corresponding to the flower that we are trying to learn.
print(iris.target)
#Let’s take a look at one single row of data and the corresponding target.
print(iris.data[0,:], iris.target[0])
#good idea to read the descriptions of the data
print(iris.DESCR)

# output
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]
#  [5.4 3.9 1.7 0.4]
#  [4.6 3.4 1.4 0.3]
#  [5.  3.4 1.5 0.2]
#  [4.4 2.9 1.4 0.2]
#  [4.9 3.1 1.5 0.1]
#  [5.4 3.7 1.5 0.2]
#  [4.8 3.4 1.6 0.2]
#  [4.8 3.  1.4 0.1]
#  [4.3 3.  1.1 0.1]
#  [5.8 4.  1.2 0.2]
#  [5.7 4.4 1.5 0.4]
#  [5.4 3.9 1.3 0.4]
#  [5.1 3.5 1.4 0.3]
#  [5.7 3.8 1.7 0.3]
#  [5.1 3.8 1.5 0.3]
#  [5.4 3.4 1.7 0.2]
#  [5.1 3.7 1.5 0.4]
#  [4.6 3.6 1.  0.2]
#  [5.1 3.3 1.7 0.5]
#  [4.8 3.4 1.9 0.2]
#  [5.  3.  1.6 0.2]
#  [5.  3.4 1.6 0.4]
#  [5.2 3.5 1.5 0.2]
#  [5.2 3.4 1.4 0.2]
#  [4.7 3.2 1.6 0.2]
#  [4.8 3.1 1.6 0.2]
#  [5.4 3.4 1.5 0.4]
#  [5.2 4.1 1.5 0.1]
#  [5.5 4.2 1.4 0.2]
#  [4.9 3.1 1.5 0.2]
#  [5.  3.2 1.2 0.2]
#  [5.5 3.5 1.3 0.2]
#  [4.9 3.6 1.4 0.1]
#  [4.4 3.  1.3 0.2]
#  [5.1 3.4 1.5 0.2]
#  [5.  3.5 1.3 0.3]
#  [4.5 2.3 1.3 0.3]
#  [4.4 3.2 1.3 0.2]
#  [5.  3.5 1.6 0.6]
#  [5.1 3.8 1.9 0.4]
#  [4.8 3.  1.4 0.3]
#  [5.1 3.8 1.6 0.2]
#  [4.6 3.2 1.4 0.2]
#  [5.3 3.7 1.5 0.2]
#  [5.  3.3 1.4 0.2]
#  [7.  3.2 4.7 1.4]
#  [6.4 3.2 4.5 1.5]
#  [6.9 3.1 4.9 1.5]
#  [5.5 2.3 4.  1.3]
#  [6.5 2.8 4.6 1.5]
#  [5.7 2.8 4.5 1.3]
#  [6.3 3.3 4.7 1.6]
#  [4.9 2.4 3.3 1. ]
#  [6.6 2.9 4.6 1.3]
#  [5.2 2.7 3.9 1.4]
#  [5.  2.  3.5 1. ]
#  [5.9 3.  4.2 1.5]
#  [6.  2.2 4.  1. ]
#  [6.1 2.9 4.7 1.4]
#  [5.6 2.9 3.6 1.3]
#  [6.7 3.1 4.4 1.4]
#  [5.6 3.  4.5 1.5]
#  [5.8 2.7 4.1 1. ]
#  [6.2 2.2 4.5 1.5]
#  [5.6 2.5 3.9 1.1]
#  [5.9 3.2 4.8 1.8]
#  [6.1 2.8 4.  1.3]
#  [6.3 2.5 4.9 1.5]
#  [6.1 2.8 4.7 1.2]
#  [6.4 2.9 4.3 1.3]
#  [6.6 3.  4.4 1.4]
#  [6.8 2.8 4.8 1.4]
#  [6.7 3.  5.  1.7]
#  [6.  2.9 4.5 1.5]
#  [5.7 2.6 3.5 1. ]
#  [5.5 2.4 3.8 1.1]
#  [5.5 2.4 3.7 1. ]
#  [5.8 2.7 3.9 1.2]
#  [6.  2.7 5.1 1.6]
#  [5.4 3.  4.5 1.5]
#  [6.  3.4 4.5 1.6]
#  [6.7 3.1 4.7 1.5]
#  [6.3 2.3 4.4 1.3]
#  [5.6 3.  4.1 1.3]
#  [5.5 2.5 4.  1.3]
#  [5.5 2.6 4.4 1.2]
#  [6.1 3.  4.6 1.4]
#  [5.8 2.6 4.  1.2]
#  [5.  2.3 3.3 1. ]
#  [5.6 2.7 4.2 1.3]
#  [5.7 3.  4.2 1.2]
#  [5.7 2.9 4.2 1.3]
#  [6.2 2.9 4.3 1.3]
#  [5.1 2.5 3.  1.1]
#  [5.7 2.8 4.1 1.3]
#  [6.3 3.3 6.  2.5]
#  [5.8 2.7 5.1 1.9]
#  [7.1 3.  5.9 2.1]
#  [6.3 2.9 5.6 1.8]
#  [6.5 3.  5.8 2.2]
#  [7.6 3.  6.6 2.1]
#  [4.9 2.5 4.5 1.7]
#  [7.3 2.9 6.3 1.8]
#  [6.7 2.5 5.8 1.8]
#  [7.2 3.6 6.1 2.5]
#  [6.5 3.2 5.1 2. ]
#  [6.4 2.7 5.3 1.9]
#  [6.8 3.  5.5 2.1]
#  [5.7 2.5 5.  2. ]
#  [5.8 2.8 5.1 2.4]
#  [6.4 3.2 5.3 2.3]
#  [6.5 3.  5.5 1.8]
#  [7.7 3.8 6.7 2.2]
#  [7.7 2.6 6.9 2.3]
#  [6.  2.2 5.  1.5]
#  [6.9 3.2 5.7 2.3]
#  [5.6 2.8 4.9 2. ]
#  [7.7 2.8 6.7 2. ]
#  [6.3 2.7 4.9 1.8]
#  [6.7 3.3 5.7 2.1]
#  [7.2 3.2 6.  1.8]
#  [6.2 2.8 4.8 1.8]
#  [6.1 3.  4.9 1.8]
#  [6.4 2.8 5.6 2.1]
#  [7.2 3.  5.8 1.6]
#  [7.4 2.8 6.1 1.9]
#  [7.9 3.8 6.4 2. ]
#  [6.4 2.8 5.6 2.2]
#  [6.3 2.8 5.1 1.5]
#  [6.1 2.6 5.6 1.4]
#  [7.7 3.  6.1 2.3]
#  [6.3 3.4 5.6 2.4]
#  [6.4 3.1 5.5 1.8]
#  [6.  3.  4.8 1.8]
#  [6.9 3.1 5.4 2.1]
#  [6.7 3.1 5.6 2.4]
#  [6.9 3.1 5.1 2.3]
#  [5.8 2.7 5.1 1.9]
#  [6.8 3.2 5.9 2.3]
#  [6.7 3.3 5.7 2.5]
#  [6.7 3.  5.2 2.3]
#  [6.3 2.5 5.  1.9]
#  [6.5 3.  5.2 2. ]
#  [6.2 3.4 5.4 2.3]
#  [5.9 3.  5.1 1.8]]
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]
# [5.1 3.5 1.4 0.2] 0
# .. _iris_dataset:

# Iris plants dataset
# --------------------

# **Data Set Characteristics:**

#     :Number of Instances: 150 (50 in each of three classes)
#     :Number of Attributes: 4 numeric, predictive attributes and the class
#     :Attribute Information:
#         - sepal length in cm
#         - sepal width in cm
#         - petal length in cm
#         - petal width in cm
#         - class:
#                 - Iris-Setosa
#                 - Iris-Versicolour
#                 - Iris-Virginica
                
#     :Summary Statistics:

#     ============== ==== ==== ======= ===== ====================
#                     Min  Max   Mean    SD   Class Correlation
#     ============== ==== ==== ======= ===== ====================
#     sepal length:   4.3  7.9   5.84   0.83    0.7826
#     sepal width:    2.0  4.4   3.05   0.43   -0.4194
#     petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
#     petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
#     ============== ==== ==== ======= ===== ====================

#     :Missing Attribute Values: None
#     :Class Distribution: 33.3% for each of 3 classes.
#     :Creator: R.A. Fisher
#     :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
#     :Date: July, 1988

# The famous Iris database, first used by Sir R.A. Fisher. The dataset is taken
# from Fisher's paper. Note that it's the same as in R, but not as in the UCI
# Machine Learning Repository, which has two wrong data points.

# This is perhaps the best known database to be found in the
# pattern recognition literature.  Fisher's paper is a classic in the field and
# is referenced frequently to this day.  (See Duda & Hart, for example.)  The
# data set contains 3 classes of 50 instances each, where each class refers to a
# type of iris plant.  One class is linearly separable from the other 2; the
# latter are NOT linearly separable from each other.

# .. topic:: References

#    - Fisher, R.A. "The use of multiple measurements in taxonomic problems"
#      Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to
#      Mathematical Statistics" (John Wiley, NY, 1950).
#    - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.
#      (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.
#    - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System
#      Structure and Classification Rule for Recognition in Partially Exposed
#      Environments".  IEEE Transactions on Pattern Analysis and Machine
#      Intelligence, Vol. PAMI-2, No. 1, 67-71.
#    - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions
#      on Information Theory, May 1972, 431-433.
#    - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II
#      conceptual clustering system finds 3 classes in the data.
#    - Many, many more ...



#  Visualize before K-means - Helps get a better sense of the data
#  #example
# The sepal length measurements are stored in column 0 of the matrix, and the petal length measurements are 
#stored in column 2 of the matrix.
#But how do we get these values?
#Suppose we only want to retrieve the values that are in column 0 of a matrix, 
#we can use the NumPy/pandas notation [:,0] like so:
#matrix[:,0]
# then do a scatter plot
# plt.scatter(x, y)
# plt.show()

import codecademylib3_seaborn
import matplotlib.pyplot as plt

from sklearn import datasets

iris = datasets.load_iris()

# Store iris.data
samples = iris.data
# Create x and y
x = samples[:,0]
y = samples[:,1]
# Plot x and y
plt.scatter(x,y, alpha = 0.5)
# Show the plot
plt.show()


# implementing k-means - step 1
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

# Number of clusters
k = 3
# Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x), max(x), size=k)
# Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y), max(y), size=k)
# Create centroids array
centroids = np.array(list(zip(centroids_x, centroids_y)))
print(centroids)
# Make a scatter plot of x, y
plt.scatter(x,y)
# Make a scatter plot of the centroids
plt.scatter(centroids_x, centroids_y)
# Display plot
plt.show()

#output\
# [[5.33148102 2.81861484]
#  [5.82490766 4.30046591]
#  [6.78288993 4.394987  ]]


# implementing k-means step 2 - Assign data samples to the nearest centroid.
#Now we have the three random centroids. Let’s assign data points to their nearest centroids.

# To do this we’re going to use a distance formula to write a distance() function.

# There are many different kinds of distance formulas. The one you’re probably most familiar with is 
# called Euclidean distance. To find the Euclidean distance between two points on a 2-d plane, make a 
# right triangle so that the hypotenuse connects the points. The distance between them is the length of the hypotenuse.

# Another common distance formula is the taxicab distance. The taxicab distance between two points on a 2-d
#  plane is the distance you would travel if you took the long way around the right triangle via the two shorter sides, 
#  just like a taxicab would have to do if it wanted to travel to the opposite corner of a city block.
#  After we write the distance() function, we are going to iterate through our data samples and compute the 
#distance from each data point to each of the 3 centroids.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

# Step 1: Place K random centroids

k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

# Step 2: Assign samples to nearest centroid

# Distance formula

def distance(a, b):
  one = (a[0] - b[0]) **2
  two = (a[1] - b[1]) **2
  distance = (one+two) ** 0.5
  return distance

# Cluster labels for each point (either 0, 1, or 2)

labels = np.zeros(len(samples))

# A function that assigns the nearest centroid to a sample

def assign_to_centroid(sample, centroids):
  k = len(centroids)
  distances = np.zeros(k)
  for i in range(k):
    distances[i] = distance(sample, centroids[i])
  closest_centroid = np.argmin(distances)
  return closest_centroid

# Assign the nearest centroid to each sample

for i in range(len(samples)):
  labels[i] = assign_to_centroid(samples[i], centroids)

# Print labels

print(labels)


# implementing k-mean step 3 - update centroids based on the above assigned data samples

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy

iris = datasets.load_iris()

samples = iris.data
samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

# Step 1: Place K random centroids

k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

# Step 2: Assign samples to nearest centroid

def distance(a, b):
  one = (a[0] - b[0]) **2
  two = (a[1] - b[1]) **2
  distance = (one+two) ** 0.5
  return distance

# Cluster labels for each point (either 0, 1, or 2)
labels = np.zeros(len(samples))

# Distances to each centroid
distances = np.zeros(k)

for i in range(len(samples)):
  distances[0] = distance(sepal_length_width[i], centroids[0])
  distances[1] = distance(sepal_length_width[i], centroids[1])
  distances[2] = distance(sepal_length_width[i], centroids[2])
  cluster = np.argmin(distances)
  labels[i] = cluster

# Step 3: Update centroids
centroids_old = deepcopy(centroids)

# 2 ways to create for loop to iterate through k
for i in range(k):
  points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
  centroids[i] = np.mean(points, axis=0)

# or
#for i in range(k):
 # points = []
  #for j in range(len(sepal_length_width)):
   # if labels[j] == i:
    #  points.append(sepal_length_width[j])

print(centroids_old)
print(centroids)


#output
# [[7.68797561 4.25350142]
#  [7.14065308 2.28411427]
#  [4.70977597 2.13144158]]
# [[6.63333333 3.96666667]
#  [6.53432836 2.9358209 ]
#  [5.18051948 3.09220779]]



# implementing k-means step 4 - repeat steps 2 and 3 until convergence
#We can do this using a while loop. And everything from Step 2 and 3 goes inside the loop.

# For the condition of the while loop, we need to create an array named errors.
# In each error index, we calculate the difference between the updated centroid (centroids) and 
# the old centroid (centroids_old).

# The loop ends when all three values in errors are 0.
#After that, add a while loop:

# while error.all() != 0:
# And move everything below (from Step 2 and 3) inside.

# And recalculate error again at the end of each iteration of the while loop.
#  You can put this line inside the ‘for’ loop that computes the new centroids:

# error[i] = distance(centroids[i], centroids_old[i])
# Checkpoint 3 Passed

# Hint
# while error.all() != 0:
 
#   # Step 2: Assign samples to nearest centroid
 
#   for i in range(len(samples)):
#     labels[i] = assign_to_centroid(samples[i], centroids)
 
#   # Step 3: Update centroids
 
#   centroids_old = deepcopy(centroids)
 
#   for i in range(k):
#     points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
#     centroids[i] = np.mean(points, axis=0)
#     error[i] = distance(centroids[i], centroids_old[i])
# 3.
# Awesome, now you have everything, let’s visualize it.

# After the while loop finishes, let’s create an array of colors:

# colors = ['r', 'g', 'b']
# Then, create a for loop that iterates k times.

# Inside the for loop (similar to what we did in the last exercise), create an array named points where we get all the data points that have the cluster label i.

# Then we are going to make a scatter plot of points[:, 0] vs points[:, 1] using the scatter() function:

# plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)
# Checkpoint 4 Passed

# Hint
# colors = ['r', 'g', 'b']
 
# for i in range(k):
#   points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
#   plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)
# 4.
# Then, paste the following code at the very end. Here, we are visualizing all the points in each of the labels a 
# different color.

# plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=150)
 
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')
 
# plt.show()


import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

# Step 1: Place K random centroids

k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

def distance(a, b):
  one = (a[0] - b[0]) ** 2
  two = (a[1] - b[1]) ** 2
  distance = (one + two) ** 0.5
  return distance

# A function that assigns the nearest centroid to a sample
def assign_to_centroid(sample, centroids):
  k = len(centroids)
  distances = np.zeros(k)
  for i in range(k):
    distances[i] = distance(sample, centroids[i])
  closest_centroid = np.argmin(distances)
  return closest_centroid

# To store the value of centroids when it updates
centroids_old = np.zeros(centroids.shape)

# Cluster labeles (either 0, 1, or 2)
labels = np.zeros(len(samples))

distances = np.zeros(3)

# Initialize error:
error = np.zeros(3)

for i in range(k):
  error[i] = distance(centroids[i], centroids_old[i])

# Repeat Steps 2 and 3 until convergence:

while error.all() != 0:

  # Step 2: Assign samples to nearest centroid

  for i in range(len(samples)):
    labels[i] = assign_to_centroid(samples[i], centroids)

  # Step 3: Update centroids

  centroids_old = deepcopy(centroids)

  for i in range(k):
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    centroids[i] = np.mean(points, axis=0)
    error[i] = distance(centroids[i], centroids_old[i])

colors = ['r', 'g', 'b']

for i in range(k):
  points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
  plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)

plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=150)

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

plt.show()



# implementing k-means with scikit-learn
from sklearn.cluster import KMeans
#For Step 1, use the KMeans() method to build a model that finds k clusters. To specify the number of clusters (k), 
#use the n_clusters keyword argument:
model = KMeans(n_clusters = k)
#For Steps 2 and 3, use the .fit() method to compute k-means clustering:
model.fit(X)
# $After k-means, we can now predict the closest cluster each sample in X belongs to. Use the .predict()
#  method to compute cluster centers and predict cluster index for each sample:
model.predict(X)

#  example
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets

# From sklearn.cluster, import Kmeans class
from sklearn.cluster import KMeans
iris = datasets.load_iris()

samples = iris.data

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters = 3)
# Use .fit() to fit the model to samples
model.fit(samples)
# Use .predict() to determine the labels of samples 
model.predict(samples)
# Print the labels
print(samples)



# k-means and new data
#Since you have created a model that computed k-means clustering, you can now feed new data samples into it and 
#obtain the cluster labels using the .predict() method.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

model = KMeans(n_clusters=3)

model.fit(samples)

# Store the new Iris measurements
new_samples = np.array([[5.7, 4.4, 1.5, 0.4],
   [6.5, 3. , 5.5, 0.4],
   [5.8, 2.7, 5.1, 1.9]])
# Predict labels for the new_samples
print(new_samples)

new_labels = model.predict(new_samples)
print(new_labels)

new_names = [iris.target_names[label] for label in new_labels]
print(new_names)

#output
# [[5.7 4.4 1.5 0.4]
#  [6.5 3.  5.5 0.4]
#  [5.8 2.7 5.1 1.9]]
# [1 0 0]
# ['versicolor', 'setosa', 'setosa']



#  visualize after k-means
# We have done the following using sklearn library:

# Load the embedded dataset
# Compute k-means on the dataset (where k is 3)
# Predict the labels of the data samples
# And the labels resulted in either 0, 1, or 2.

# Let’s finish it by making a scatter plot of the data again!

# This time, however, use the labels numbers as the colors.

# To edit colors of the scatter plot, we can set c = labels:

# plt.scatter(x, y, c=labels, alpha=0.5)
 
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')



import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

model = KMeans(n_clusters=3)

model.fit(samples)

labels = model.predict(samples)

print(labels)

# Make a scatter plot of x and y and using labels to define the colors

x = samples[:,0]
y = samples[:,1]

plt.scatter(x,y)
plt.show()


#  Evaluation of k-means and visualize 
# At this point, we have clustered the Iris data into 3 different groups (implemented using Python and using scikit-learn). 
# But do the clusters correspond to the actual species? Let’s find out!

# First, remember that the Iris dataset comes with target values:

# target = iris.target
# It looks like:

# [ 0 0 0 0 0 ... 2 2 2]
# According to the metadata:

# All the 0‘s are Iris-setosa
# All the 1‘s are Iris-versicolor
# All the 2‘s are Iris-virginica
# Let’s change these values into the corresponding species using the following code:

# species = [iris.target_names[t] for t in list(target)]
# Then we are going to use the Pandas library to perform a cross-tabulation.

# Cross-tabulations enable you to examine relationships within the data that might not be readily apparent 
# when analyzing total survey responses.

# The result should look something like:

# labels    setosa    versicolor    virginica
# 0             50             0            0
# 1              0             2           36
# 2              0            48           14
# (You might need to expand this narrative panel in order to the read the table better.)

# The first column has the cluster labels. The second to fourth columns have the Iris species that are clustered 
# into each of the labels.

# By looking at this, you can conclude that:

# Iris-setosa was clustered with 100% accuracy.
# Iris-versicolor was clustered with 96% accuracy.
# Iris-virginica didn’t do so well.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd

iris = datasets.load_iris()

samples = iris.data

target = iris.target

model = KMeans(n_clusters=3)

model.fit(samples)

labels = [iris.target_names[s] for s in model.predict(samples)]

# Code starts here:
species = [iris.target_names[t] for t in list(target)]
df = pd.DataFrame({'labels': labels, 'species': species})
print(df)

ct = pd.crosstab(df['labels'], df['species'])
print(ct)
#output
#          labels    species
# 0    versicolor     setosa
# 1    versicolor     setosa
# 2    versicolor     setosa
# 3    versicolor     setosa
# 4    versicolor     setosa
# ..          ...        ...
# 145   virginica  virginica
# 146      setosa  virginica
# 147   virginica  virginica
# 148   virginica  virginica
# 149      setosa  virginica

# [150 rows x 2 columns]
# species     setosa  versicolor  virginica
# labels                                   
# setosa           0          48         14
# versicolor      50           0          0
# virginica        0           2         36



#  finding the number of clusters when it is not known - you define what a good cluster is.  those are tight clusters 
#  meaning that the samples in each cluster are bunched together.  How spread out they are is measured by inertia
#  inertia is the distance from each sample to the centroid of its cluster.  Lower inertia and 
# the fewer the clusters the better the model has done
# Elbow method - Choosing an “elbow” in the inertia plot, when inertia begins to decrease more slowly,
# finds the optimal number of clusters.
print(model.inertia_)



import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

# Code Start here:
num_clusters = [1,2,3,4,5,6,7,8]
inertias = []
#Then, iterate through num_clusters and calculate k-means for each number of clusters.
#Add each of their inertias into the inertias list.
for k in num_clusters:
  model = KMeans(n_clusters=k)
  model.fit(samples)
  inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')
 
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
 
plt.show()
























