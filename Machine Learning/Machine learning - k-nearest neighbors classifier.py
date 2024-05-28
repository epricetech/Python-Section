# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:01:37 2023

@author: geron
"""

# KNN or k-nearest neighbors is a classification algorithm.  Based on the idea that data points with similar attributes
#  tend to fall into similar categories-  helps classify unknown points
# This is the central idea behind the K-Nearest Neighbor algorithm. If you have a dataset of points where the class
#  of each point is known, you can take a new point with an unknown class, find it’s nearest neighbors, and classify it.


# Distance Between Points - 2D - There are different ways to define the distance of 2 points
distance([1, 2, 3], [5, 8, 9]) - #example of how to create 2 sets of points to find the distance
#1. Eucildean distance - to find we first calculate the squared distance between each dimension.  Then add up all the squared 
#  differneces and take the square root of results.  formula Distance =  square root of (a1-b1)^2 + (a2-b2)^2 + (a3-b3)^2 
#and so on for each point.  
#  2.  Manhattan Distance - similiar to euclidean instead we sum the absolute value of the difference bween each dimension
# The manhattan distance will always be greated or equal to the eucilean distance
#  equation is distance = |a1 - b1| + |a2 - b2| + |a3 - b3|
# 3. Hamming Distance - only looks for if the dimensions are exactly equal - add one for every dimension that has different
#  values.  Most used in spell checking algorithms.  Example the hamming distance between the word there and the type
#  of thete is 1.  Each letter is a dimension and each dimension has the same value except one
##  Python scipy library for these 3
# Euclidean distnace = .euclidean()
#  Manhattan Distance = .cityblock()
# hamming distance = .hamming()

#  examples of library functions for 3 distance algorithms
print(distance.euclidean([1,2], [4,0]))
print(distance.cityblock([1,2], [4,0]))
print(distance.hamming([5,4,9], [1,7,9]))



# Eucildean example
def euclidean_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += (pt1[i] - pt2[i]) ** 2
  return distance ** 0.5

print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))


#  Manhattan Example
def manhattan_distance(pt1,pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

print(manhattan_distance([1,2],[4,0]))
print(manhattan_distance([1,2], [4,0]))
print(manhattan_distance([5,4,3], [1,7,9]))


#  Hamming example
def hamming_distance(pt1,pt2):
  distance = 0
  for i in range(len(pt1)):
    if pt1[i] != pt2[i]:
      distance += 1
  return distance

print(hamming_distance([1,2], [1,100]))
print(hamming_distance([5,4,9], [1,7,9]))




#  example

star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

def distance(movie1,movie2):
  length_difference = (movie1[0] - movie2[0]) **2
  year_difference = (movie1[1] - movie2[1]) ** 2
  distance = (length_difference + year_difference) ** 0.5
  return distance


print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))



#  distance between points - 3D
#  example will work with any number of dimensions
star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))



# Data with Different Scales - Normalization - 3 steps - normalize data - find k nearest neighbors - classify the new point base
# base on those neighbors
#  When you have dimensions that have different weights and distances between them it can curropt your algorithms
#  example of movies release year, and budget -  2 movies can be seperated by 70 years and 700 million dollors
#  however these distance algorithms will treat that 700 mill difference as only 70 dollar difference.  Basically each year 
# will equal 1 dollar in the budget aspect.  The data is not normalized.  Goal is to get every value between 0 and 1 
#  using min max normalizationa and a few others.

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]


def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for value in lst:
    normalized_num = (value - minimum) / (maximum - minimum)
    normalized.append(normalized_num)
  return normalized

print(min_max_normalize(release_dates))


# finding the k nearest neighbors
#  not that we have normalized the data we can begin classifying unknown data.  Example to find 5 nearest neighbors
#  we need to compare this new unclassified value to every other in the dataset.  We use the distance formula over and over
#  goal is to end up with sorted list of distances and the associated with those distance

[
  [0.30, 'Superman II'],
  [0.31, 'Finding Nemo'],
  ...
  ...
  [0.38, 'Blazing Saddles']
]
 

from movies import movie_dataset, movie_labels

#print(movie_dataset['Bruce Almighty'])
#print(movie_labels['Bruce Almighty'])

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  return neighbors
  
print(classify([.4, .2, .9], movie_dataset, 5))


# example from above finding the k nearest neightbors and have them stored in a list
[
  [0.083, 'Lady Vengeance'],
  [0.236, 'Steamboy'],
  ...
  ...
  [0.331, 'Godzilla 2000']
]
#  count neighbors - classify the new point based on those neighbors

#  this example will classify weather a movie is good or bad based on its neighbors and distance

from movies import movie_dataset, movie_labels

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0

print(classify([.4, .2, .9], movie_dataset, movie_labels, 5))


#Example

from movies import movie_dataset, movie_labels, normalize_point

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0
print("Call Me By Your Name" in movie_dataset)
my_movie = [3500000, 132, 2017]

normalized_my_movie = normalize_point(my_movie)
print(normalized_my_movie)
print(classify(normalized_my_movie, movie_dataset, movie_labels, 5))

#  above code is k nearest neighbors algorithm capable of classifcation - but out classifications could be wrong
#  so we will need to split our data into a training set and a validation set

#  Training and Validation Sets
#  once created you will use every point in the validation set as input to the K nearest neighbor algorithm.  
#  basically they will take a value from the validation set, compare it to all the values in the training set, find the 
#  K nearest neighbors and make a prediction.  - After prediction we can peek at the real 
#answer(found in the validation lables) to see if our classifier got the answer correct
# If we do this for the entire validation set we can count the number of times it got ir right or wrong.  Using those
#  totals we can see our validation accuracy.  Validation accuracy depends on what K you use

 from movies import training_set, training_labels, validation_set, validation_labels

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0
print(validation_set['Bee Movie'])
print(validation_labels['Bee Movie'])

guess = classify(validation_set['Bee Movie'],training_set,training_labels,5)
print(guess)
if guess == validation_labels['Bee Movie']:
  print('Correct!')
else:
  Print('Wrong!')



#  Choosing K
#  validation accuracy changes as k changes - to start off you want k to be very small like starting at k=1
#  overfitting means when you rely to heavily on your training data and assume this data will behave the same way in real life
#  in k nearestest overfitting occurs when you dont condier enough neighbors.  
#  underfitting means when your k value is too large and cant detect small quirks in the training set.  

from movies import training_set, training_labels, validation_set, validation_labels

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0

def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
  num_correct = 0.0
  for title in validation_set:
    guess = classify(validation_set[title], training_set, training_labels, k)
    if guess == validation_labels[title]:
      num_correct += 1
  return num_correct / len(validation_set)

print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, 3))




#  usking Sklern for k nearest
#  skleanr library called KNeighborsClassifier and takes one paramater K
classifier = KNeighborsClassifier(n_neighbors = 3)
# then we need to train our classifier with .fit() which takes 2 paramaters.  First is a list of points and the 2nd 
#  is the labels associated with thos epoints.  
training_points = [
  [0.5, 0.2, 0.1],
  [0.9, 0.7, 0.3],
  [0.4, 0.5, 0.7]
]
 
training_labels = [0, 1, 1]
classifier.fit(training_points, training_labels)

#  Finally we use the .predict() method to take a list of points that you want to classify
unknown_points = [
  [0.2, 0.1, 0.7],
  [0.4, 0.7, 0.6],
  [0.5, 0.8, 0.1]
]
 
guesses = classifier.predict(unknown_points)


#Example
from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(movie_dataset, labels)

guess = classifier.predict([[.45,.2,.5], [.25,.8,.9], [.1,.1,.9]])
print(guess)



# #  REview
# Data with n features can be conceptualized as points lying in n-dimensional space.
# Data points can be compared by using the distance formula. Data points that are similar will have a 
# smaller distance between them.
# A point with an unknown class can be classified by finding the k nearest neighbors
# To verify the effectiveness of a classifier, data with known classes can be split into a training 
# set and a validation set. Validation error can then be calculated.
# Classifiers have parameters that can be tuned to increase their effectiveness. In the case of K-Nearest Neighbors,
#  k can be changed.
# A classifier can be trained improperly and suffer from overfitting or underfitting. In the case of K-Nearest Neighbors, 
# a low k often leads to overfitting and a large k often leads to underfitting.
# Python’s sklearn library can be used for many classification and machine learning algorithms.
















