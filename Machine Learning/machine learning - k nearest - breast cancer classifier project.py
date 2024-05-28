# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:06:36 2023

@author: geron
"""

# Explore the data
# 1.
# Let’s begin by importing the breast cancer data from sklearn. We want to import the function load_breast_cancer from 
# sklearn.datasets.

# Once we’ve imported the dataset, let’s load the data into a variable called breast_cancer_data. Do this by setting
#  breast_cancer_data equal to the function load_breast_cancer().


# Hint
# To load the data, use the following code:

# from sklearn.datasets import load_breast_cancer
# Then set breast_cancer_data equal to load_breast_cancer().

# 2.
# Before jumping into creating our classifier, let’s take a look at the data. Begin by printing breast_cancer_data.data[0].
#  That’s the first datapoint in our set. But what do all of those numbers represent? 
#  Let’s also print breast_cancer_data.feature_names.


# Hint
# To see all of the data, do the following:

# print(breast_cancer_data.data).

# 3.
# We now have a sense of what the data looks like, but what are we trying to classify?
#  Let’s print both breast_cancer_data.target and breast_cancer_data.target_names.

# Was the very first data point tagged as malignant or benign?


# Hint
# breast_cancer_data.target gives you the labels of every data point. 
# The very first data point in the set had a label of 0. By looking at the target_names, 
# we know that 0 corresponds to malignant.

# Splitting the data into Training and Validation Sets
# 4.
# We have our data, but now it needs to be split into training and validation sets. Luckily, 
# sklearn has a function that does that for us. Begin by importing the train_test_split function from sklearn.model_selection.


# Hint
# Look at how you imported the load_breast_cancer function. This should be the same 
# thing except you should import train_test_split from sklearn.model_selection.

# 5.
# Call the train_test_split function. It takes several parameters:

# The data you want to split (for us breast_cancer_data.data)
# The labels associated with that data (for us, breast_cancer_data.target).
# The test_size. This is what percentage of your data you want to be in your testing set. Let’s use test_size = 0.2
# random_state. This will ensure that every time you run your code, the data is split in the same way. 
# This can be any number. We used random_state = 100.

# Hint
# The third and fourth parameters need the name of the parameter. For example look at the code below.

# train_test_split(____, _____, test_size = 0.2, random_state = 100)
# Use that code, but fill in the data and labels for the first two parameters.

# 6.
# Right now we’re not storing the return value of train_test_split. train_test_split returns four 
# values in the following order:

# The training set
# The validation set
# The training labels
# The validation labels
# Store those values in variables named training_data, validation_data, training_labels, and validation_labels.


# Hint
# Your code should look like this:

# training_data, _____ , training_labels, _____ = train_test_split(breast_cancer_data.data, 
#                                                                  breast_cancer_data.target, test_size = 0.2, 
#                                                                  random_state = 100)
 
# What should the second and fourth variables be?

# 7.
# Let’s confirm that worked correctly. Print out the length of training_data and training_labels. 
# They should be the same size - one label for every piece of data!


# Hint
# print(len(training_data))

# Running the classifier
# 8.
# Now that we’ve created training and validation sets, we can create a KNeighborsClassifier and test its accuracy.
#  Begin by importing KNeighborsClassifier from sklearn.neighbors.


# Hint
# This should be similar to your other import statements.

# 9.
# Create a KNeighborsClassifier where n_neighbors = 3. Name the classifier classifier.


# Hint
# classifier = KNeighborsClassifier(n_neighbors = 3)
# 10.
# Train your classifier using the fit function. This function takes two parameters: the training set and the training labels.


# Hint
# classifier.fit(training_data, ____)
# The training labels should be the second parameter.

# 11.
# Now that the classifier has been trained, let’s find how accurate it is on the validation set. 
# Call the classifier’s score function. score takes two parameters: the validation set and the validation labels. 
# Print the result!


# Hint
# print(classifier.score(____, validation_labels))
# The first parameter of score should be the validation set.

# 12.
# The classifier does pretty well when k = 3. But maybe there’s a better k! Put the previous 3 lines of code 
# inside a for loop. The loop should have a variable named k that starts at 1 and increases to 100.
#  Rather than n_neighbors always being 3, it should be this new variable k.

# You should now see 100 different validation accuracies print out. Which k seems the best?


# Hint
# Your for loop should look like this:

# for k in range(1, 101):
#   #Create classifier
#   #Train classifier
#   #Report accuracy
# Make sure when you’re creating the classifier, you use n_neighbors = k.

# Graphing the results
# 13.
# We now have the validation accuracy for 100 different ks. Rather than just printing it out, 
# let’s make a graph using matplotlib. Begin by importing matplotlib.pyplot as plt.


# Hint
# This import statement looks a bit different because we’re importing multiple functions from matplotlib.pyplot. 
# The import statement should look like this:

# import matplotlib.pyplot as plt
# 14.
# The x-axis should be the values of k that we tested. This should be a list of numbers between 1 and 100. 
# You can use the range function to make this list. Store it in a variable named k_list.


# Hint
# range(1,5) will give you a list [1, 2, 3, 4]. Create a list of numbers of 1 through 100 (including 100).

# 15.
# The y-axis of our graph should be the validation accuracy. Instead of printing the validation accuracies, 
# we want to add them to a list. Outside of the for loop, create an empty list named accuracies. Inside the for loop, 
# instead of printing each accuracy, append it to accuracies.


# Hint
# Add the validation accuracy to the list like this. The parameters of score should be the same as before.

# accuracies.append(classifier.score(____,____))
# 16.
# We can now plot our data! Call plt.plot(). The first parameter should be k_list and the second parameter 
# should be accuracies.

# After plotting the graph, show it using plt.show().


# Hint
# plt.plot(k_list, accuracies)
# plt.show()
# 17.
# Let’s add some labels and a title. Set the x-axis label to "k" using plt.xlabel().
#  Set the y-axis label to "Validation Accuracy". Set the title to "Breast Cancer Classifier Accuracy".


# Hint
# The three functions you will want to use are plt.xlabel(), plt.ylabel(), and plt.title(). 
# All three take a String as a parameter.

# 18.
# Great work! If you want to play around with this more, try changing the random_state parameter 
# when making the training set and validation set. This will change which points are in the training set and which are in the validation set.

# Ideally, the graph will look the same no matter how you split up the training set and test set. 
# This data set is fairly small, so there is slightly more variance than usual.



import codecademylib3_seaborn

from sklearn.datasets import load_breast_cancer
breast_cancer_data = load_breast_cancer()
# 2
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)

# 3  0 = malignant and 1 = benign
print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

# 4 and 5
from sklearn.model_selection import train_test_split
train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2,random_state=100)

# 6
training_data, validation_data,training_labels,validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state=100)

#7  - results were 455 and 455 showing balanced
print(len(training_data))
print(len(training_labels))

# 8 
from sklearn.neighbors import KNeighborsClassifier

# 9
#classifier = KNeighborsClassifier(n_neighbors=3)

#10
#classifier.fit(training_data, training_labels)

#11  - results 0.947368421052631
#print(classifier.score(validation_set, validation_labels))
accuracies = []

#12 - takes previous 3 steps and creates a loop
for k in range(1, 101):
  classifier = KNeighborsClassifier(n_neighbors=k)
  classifier.fit(training_data, training_labels)
  accuracies.append(classifier.score(validation_data,validation_labels))
  #print(classifier.score(validation_data,validation_labels))

#13
import matplotlib.pyplot as plt

#14
k_list = range(1,101)

#15 - see above #12 also updated for loop with .append
print(accuracies)

#16
plt.plot(k_list,accuracies)


#17
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()

































