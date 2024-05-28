# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:17:18 2023

@author: geron
"""

#  typically k-nearest is used for classification - however it can perform regression
#  Very similiar to how you do classification but has one final step.  
#  Example is the movie dataset.  instead of seeing if a movie is good or bad based on the k-nearest neighbors we
#  are going to have the regressor average their imdb ratings.  
#  example if we have 3 k-nearest values of 5.0,9.2,6.8 then we could predict that the new unknown movies will have a 
# rating of 7.0 which is the average of the k-nearest neighbors

from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
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
  #We’ve included the majority of the K-Nearest Neighbor algorithm in the predict() function. Right now, 
#   the variable neighbors stores a list of [distance, title] pairs.

# Loop through every neighbor and find its rating in movie_ratings. Add those ratings together
#  and return that sum divided by the total number of neighbors.
  sum = 0
  for neighbor in neighbors:
    title = neighbor[1]
    sum += movie_ratings[title]
  return sum/len(neighbors)

print(movie_dataset['Life of Pi'])
print(movie_ratings['Life of Pi'])

print(predict([0.016, 0.300, 1.022], movie_dataset,movie_ratings,5))




#  weighted Regressions - before we just found the average of the k-nearest neightbors but we can compute a weighted
#  average based on how close each neighbor is.  We find this by using a distance formula
#  Movie	Rating	Distance to movie X
# A	5.0	3.2
# B	6.8	11.5
# C	9.0	1.1

# If we find the mean, the predicted rating for X would be 6.93. 
# However, movie X is most similar to movie C, so movie C’s rating should be more important when computing the average. 
# Using a weighted average, we can find movie X’s rating:

# Formula (5.0/3.2 + 6.8/11.5 + 9.0/1.1) / 1/3.2 + 1/11.5 + 1/1.1 = 7.9
# The numerator is the sum of every rating divided by their respective distances. 
# The denominator is the sum of one over every distance. Even though the ratings are the same as before, 
# the weighted average has now gone up to 7.9.


from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
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
  numerator = 0
  denominator = 0
  for neighbor in neighbors:
    rating = movie_ratings[neighbor[1]]
    distance_to_neighbor = neighbor[0]
    numerator += rating / distance_to_neighbor
    denominator += 1 / distance_to_neighbor
  return numerator / denominator

print(predict([0.016, 0.300, 1.022], movie_dataset, movie_ratings, 5))



# k-nearest neighbor regressor in scikit-learn using the KNeighborsRegressor()
# inside we must create the regressor with n_neighbors = 3, and a 2nd parameter for weight weights = 'Value'
classifier = KNeighborsRegressor(n_neighbors = 3, weights = "distance")
#  next you need to fit the model to our training data using the .fit() method 2 parameters first list of points and 
#  second is list of values associated with those points.  
training_points = [
  [0.5, 0.2, 0.1],
  [0.9, 0.7, 0.3],
  [0.4, 0.5, 0.7]
]
 
training_labels = [5.0, 6.8, 9.0]
classifier.fit(training_points, training_labels)
#  finally we can use .predict() which takes a list of points and retuns a list of predictions for those points
unknown_points = [
  [0.2, 0.1, 0.7],
  [0.4, 0.7, 0.6],
  [0.5, 0.8, 0.1]
]
 
guesses = classifier.predict(unknown_points)

#  example
from movies import movie_dataset, movie_ratings
from sklearn.neighbors import KNeighborsRegressor

regressor = KNeighborsRegressor(n_neighbors = 5, weights = 'distance')

regressor.fit(movie_dataset, movie_ratings)

print(regressor.predict([[0.016,0.30,1.022], [0.0004092981,0.283,1.0112], [0.00687649,0.235,1.0112]]))


#  Review
# The K-Nearest Neighbor algorithm can be used for regression. Rather than returning a classification, it returns a number.
# By using a weighted average, data points that are extremely similar to the input point will have more of 
# a say in the final result.
# scikit-learn has an implementation of a K-Nearest Neighbor regressor named KNeighborsRegressor.




















