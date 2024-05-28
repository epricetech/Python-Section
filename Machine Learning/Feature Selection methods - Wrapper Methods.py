# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:10:39 2023

@author: geron
"""

#  Wrapper Method - Wehn you need to distinguish between important and unimportant features or even important
# combinations of features.  The wrapper method selects features by evaluating the performance of a machine learning model
# on a different subset of features.  These algorithms add or remove features one at a time based on how useful those features
#  are to the model.  advantage over filter methods is the wrapper method evalutes features based on their performance
# with a specific model and filter mthod cant.  Also wrapper methods can take into account relationships between features.
#  There are 5 Different Wrapper methods
# Sequential forward selection
# Sequential backward selection
# Sequential forward floating selection
# Sequential backward floating selection
# Recursive feature elimination


#  Before you can use wrapper method you need tospecifify a machine model like logistic regression model
#  We’ll prepare the data by splitting it into a pandas DataFrame X and a pandas Series y. 
# X will contain the observations of the independent variables, and y will contain the observations of the dependent variable.

#  example of how to do this
# Here’s an example of how to do this. The fire dataset below was taken from the UCI Machine Learning Repository 
# and cleaned for our analysis. Its features are Temperature, RH (relative humidity), Ws (wind speed), Rain,
#  DMC (Duff Moisture Code), and FWI (Fire Weather Index). The final column, Classes, contains a 1 if there is a
#  forest fire at a specific location on a given day and 0 if not.

import pandas as pd
 
# Load the data
fire = pd.read_csv("fire.csv")
# Split independent and dependent variables
X = fire.iloc[:,:-1]
y = fire.iloc[:,-1]

#We can create a logistic regression model and fit it to X and y with scikit-learn using the following code.
from sklearn.linear_model import LogisticRegression
 
# Create and fit the logistic regression model
lr = LogisticRegression()
lr.fit(X, y)

# Logistic regression models give a probability that an observation belongs to a category. 
# In the fire dataset, probabilities greater than 0.5 are considered predictions that there is a fire, 
# and probabilities less than 0.5 are considered predictions that there is no fire. In the health dataset, 
# probabilities greater than 0.5 are considered predictions that a patient has breast cancer.

# The accuracy of a logistic regression model is the percentage of correct predictions that it makes on a testing set. 
# In scikit-learn, you can check the accuracy of a model with the .score() method.

print(lr.score(X,y))

#  output
#  0.9836065573770492

#  example of logistic regression method to set up wrapper method
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the data
health = pd.read_csv("dataR2.csv")
# Split independent and dependent variables
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Fit the model
lr.fit(X,y)
# Print the accuracy of the model
print(lr.score(X,y))



#  Sequential Forward Selection - wrapper method
#  builds a feature set by starting with no features and then adding one feature at a time until a desired number of
#  features are reached.  It trains and tests the model using one feature at time.  Then keeps the features that perform the best
#  It is a greedy algorithm, instead of checking every possible feature set by brute force it adds whichever feature
#  gives the best immediate performance gain

# SFS class from python mixtend library to implement sequential forward selection and choose a subset of features you want
#  example of choosing 3 features
# Set up SFS parameters
sfs = SFS(lr,
           k_features=3, # number of features to select
           forward=True,
           floating=False,
           scoring='accuracy',
           cv=0)
# Fit SFS to our features X and outcome y   
sfs.fit(X, y)

# The first parameter is the name of the model that you’re using. In the previous exercise,
#  we called the logistic regression model lr.
# The parameter k_features determines how many features the algorithm will select.
# forward=True and floating=False ensure that we are using sequential forward selection.
# scoring determines how the algorithm will evaluate each feature subset. It’s often okay to
#  use the default value None because mlxtend will automatically use a metric that is suitable for
#  whatever scikit-learn model you are using. For this lesson, we’ll set it to 'accuracy'.
# cv allows you to do k-fold cross-validation. We’ll leave it at 0 for this lesson and only evaluate
#  performance on the training set.

import pandas as pd
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Sequential forward selection
sfs = SFS(lr, k_features=3, forward=True,floating=False,scoring='accuracy',cv=0)
# Fit the equential forward selection model
sfs.fit(X,y)


#  the .subsets_ attribute allows you to see info and what feature was chosen at each step.  Looks like this
# {1: {'feature_idx': (7,),
#   'cv_scores': array([0.93852459]),
#   'avg_score': 0.9385245901639344,
#   'feature_names': ('FWI',)},
#  2: {'feature_idx': (4, 7),
#   'cv_scores': array([0.97540984]),
#   'avg_score': 0.9754098360655737,
#   'feature_names': ('DMC', 'FWI')},
#  3: {'feature_idx': (1, 4, 7),
#   'cv_scores': array([0.9795082]),
#   'avg_score': 0.9795081967213115,
#   'feature_names': (' RH', 'DMC', 'FWI')}}
# The keys in this dictionary are the numbers of features at each step in the sequential forward selection algorithm. 
# The values in the dictionary are dictionaries with information about the feature set at each step. 'avg_score' 
# is the accuracy of the model with the specified number of features.

# In this particular example, the model had an accuracy of about 93.9% after the feature FWI was added. 
# The accuracy improved to about 97.5% after a second feature, DMC, was added. Once three features were added 
# the accuracy improved to about 98.0%.

# you can use the previous dictionary to get a tuple of chosed features or the accuracy of the model after any step
# Print a tuple of feature names after 5 features are added
print(sfs.subsets_[5]['feature_names'])
#  output
#  (' RH', ' Ws', 'Rain ', 'DMC', 'FWI')

# Print the accuracy of the model after 5 features are added
print(sfs.subsets_[5]['avg_score'])
# output
#0.9836065573770492

#the mlxtend library also makes it easy to visualize how the accuracy of a model changes as sequential forward 
# selection adds features. You can use the code plot_sfs(sfs.get_metric_dict()) to create a matplotlib figure
#  that plots the model’s performance as a function of the number of features used.

from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
 
# Plot the accuracy of the model as a function of the number of features
plot_sfs(sfs.get_metric_dict())
plt.show()


#  example
import pandas as pd
import codecademylib3
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Sequential forward selection
sfs = SFS(lr,
          k_features=3,
          forward=True,
          floating=False,
          scoring='accuracy',
          cv=0)
sfs.fit(X, y)

# Print the chosen feature names
print(sfs.subsets_[3]['feature_names'])
# Print the accuracy of the model after sequential forward selection
print(sfs.subsets_[3]['avg_score'])
# Plot the model accuracy
plot_sfs(sfs.get_metric_dict())
plt.show()

#  output
#  ('Age', 'Glucose', 'Insulin')
#  0.7672413793103449



# sequential Backward Selection with mlxtend - wrapper method
#  instead of starting with no features this option starts with all of the features and removes one at a time
#To implement sequential backward selection in mlxtend you can use the same SFS class you used for 
#sequential forward selection. The only difference is that you have to set the parameter forward to False

import pandas as pd
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Sequential backward selection
sbs = SFS(lr,
          k_features=3,
          forward=False,
          floating=False,
          scoring='accuracy',
          cv=0)

# Fit sbs to X and y
sbs.fit(X,y)

#  evaluating the result of sequential backward selection using model.subsets_
#  example
# {6: {'feature_idx': (0, 1, 2, 3, 4, 5),
#   'cv_scores': array([0.98360656]),
#   'avg_score': 0.9836065573770492,
#   'feature_names': ('Temperature', ' RH', ' Ws', 'Rain ', 'DMC', 'FWI')},
#  5: {'feature_idx': (1, 2, 3, 4, 5),
#   'cv_scores': array([0.98360656]),
#   'avg_score': 0.9836065573770492,
#   'feature_names': (' RH', ' Ws', 'Rain ', 'DMC', 'FWI')},
#  4: {'feature_idx': (2, 3, 4, 5),
#   'cv_scores': array([0.98360656]),
#   'avg_score': 0.9836065573770492,
#   'feature_names': (' Ws', 'Rain ', 'DMC', 'FWI')},
#  3: {'feature_idx': (2, 4, 5),
#   'cv_scores': array([0.9795082]),
#   'avg_score': 0.9795081967213115,
#   'feature_names': (' Ws', 'DMC', 'FWI')}}

#  you can also plot it the same way
# Plot the accuracy of the model as a function of the number of features
plot_sfs(sbs.get_metric_dict())
plt.show()


#  example
import pandas as pd
import codecademylib3
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Sequential backward selection
sbs = SFS(lr,
          k_features=3,
          forward=False,
          floating=False,
          scoring='accuracy',
          cv=0)
sbs.fit(X, y)

# Evaluate the result of sequential backward selection
print(sbs.subsets_[3]['feature_names'])
print(sbs.subsets_[3]['avg_score'])

# Plot the model accuracy
plot_sfs(sbs.get_metric_dict())
plt.show()

#output
# {'feature_idx': (0, 2, 7), 'cv_scores': array([0.74137931]), 'avg_score': 0.7413793103448276, 
#  'feature_names': ('Age', 'Glucose', 'Resistin')}



#  Sequential Forward and Backward Floating Selection

#  # Sequential Forward Floating is a variation of sequential forward selection.  Starts with zero features and adds
#  one feature at a time, but after each addition it checks to see if we can improve performance by removing a feature
# If performance can’t be improved, the floating algorithm will continue to the next step and add another feature.
# If performance can be improved, the algorithm will make the removal that improves performance the most 
# (unless removal of that feature would lead to an infinite loop of adding and removing the same feature over and over again).
# example lets ay the algorithm adds weight to the feature set of age and resting_heart_rate.  The floating algorithm
#  will test weather it can imporove performance by removing age or resting_heart_rate and will keep that feature out of
#  the set if it does imporove performance when removed.

#  Sequential backward floating - variation of sequential backward selection - where it states will all features and 
#  removes on feature at a time.  After each feature removal it will check to see if any feature additions will 
#  improve performace but wont add anything back that will create an infinte loop.  These floating options
#  are used more than their counterparts because they can detect more usefull relationships between variables

#  Sequential Frward and backward floating selection with mlxtend
#  Done by setting the floating parameter to True
# Sequential backward floating selection
sbfs = SFS(lr,
          k_features=5,
          forward=False,
          floating=True,
          scoring='accuracy',
          cv=0)
sbfs.fit(X, y)
print(sbfs.subsets_[5]['feature_names'])
# output
#(' RH', ' Ws', 'Rain ', 'DMC', 'FWI')


#  example
import pandas as pd
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Sequential forward floating selection
sffs = SFS(lr,
          k_features=3,
          forward=True,
          floating=True,
          scoring='accuracy',
          cv=0)
sffs.fit(X, y)

# Print a tuple with the names of the features chosen by sequential forward floating selection.
print(sffs.subsets_[3]['feature_names'])
# Sequential backward floating selection
sbfs = SFS(lr,
          k_features=3,
          forward=False,
          floating= True,
          scoring='accuracy',
          cv=0)
sbfs.fit(X, y)

# Print a tuple with the names of the features chosen by sequential backward floating selection.
print(sbfs.subsets_[3]['feature_names'])


# Output:
# ('Age', 'Glucose', 'Insulin')
# ('Age', 'Glucose', 'Resistin')



#  Recursive Feature Elimination - wrapper method
#  it starts by training a model with all available features.  It then ranks each feature according to an importance metric
# and removes the least important feature.  Then it trains the model on the smaller feature set and ranks those features 
# and removes the least important feature.  This process stops when the desired number of features is reached
#  The regression coefficient for age has the smallest absolute value, so it is ranked least important by recursive 
# feature elimination. It will be removed, and the remaining four features will be re-ranked after the model is 
# trained without age.
# It’s important to note that you might need to standardize data before doing recursive feature elimination. 
# In regression problems in particular, it’s necessary to standardize data so that the scale of features doesn’t 
# affect the size of the coefficients.
#  with sequential backward selection it removes features by training a model on a collection of subsets and proceeding
# with whatever subset performs the best where recurisive feature elimination only trains a model on one feature
# subset before deciding which feature to remove next.  Thus can be must faster than the squential backward selection


#  recursive Feature elimination with scikit-learn
#  We can standardize features using scikit-learn’s StandardScaler().

from sklearn.preprocessing import StandardScaler
 
X = StandardScaler().fit_transform(X)

# once standardized we can train the model usingRFE() method with estimator parameter and n_feature_to_select

from sklearn.feature_selection import RFE
 #  lr is our logistic regression model
# Recursive feature elimination
rfe = RFE(lr, n_features_to_select=2)
rfe.fit(X, y)


# example
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

# Load the data
health = pd.read_csv("dataR2.csv")
X = np.array(health.iloc[:,:-1])
y = np.array(health.iloc[:,-1])

# Standardize the data
X = StandardScaler().fit_transform(X)

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Recursive feature elimination
rfe=RFE(lr,n_features_to_select=3)
rfe.fit(X,y)


#  evaluationg the results of recursive feature elimination
#  we can look at rfe.ranking and rfe.support_  
#  rfe.ranking is an array that contains the rank of each feature
# example
# ['Temperature', 'RH', 'Ws', 'Rain', 'DMC', 'FWI']
print(rfe.ranking_)
# [2 5 4 1 3 1]
# a 1 at a certain index indicates that recursive feature elimination kept the feature at the same index.  The other numbers
# indicated at which step a feature was removed.  the 5 is the highest rank in the array at index 1 means that the 
# feature at index 1 was removed first.  the 4 at index 2 means the feature was removed in the next step and so on
# the rfe.support_ is an array with true and false values to indicate which features were chosen
#Example
print(rfe.support_)
# [False False False  True False  True]

# If you have a list of feature names, you can use a list comprehension and rfe.support_ to get a list of 
# chosen feature names.

# features is a list of feature names
# Get a list of features chosen by rfe
rfe_features = [f for (f, support) in zip(features, rfe.support_) if support]
 
print(rfe_features)
['Rain ', 'FWI']



#  example
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Create a list of feature names
feature_list = list(X.columns)

# Standardize the data
X = StandardScaler().fit_transform(X)

# Logistic regression
lr = LogisticRegression(max_iter=1000)

# Recursive feature elimination
rfe = RFE(estimator=lr, n_features_to_select=3)
rfe.fit(X, y)

# List of features chosen by recursive feature elimination
rfe_features = [f for (f, support) in zip(feature_list,rfe.support_) if support]
# Print the accuracy of the model with features chosen by recursive feature elimination
print(rfe.score(X,y))

# output
# 0.7327586206896551


#  REview
# Wrapper methods for feature selection are algorithms that select features by evaluating the performance of a machine 
# learning model on different subsets of features. Here are some advantages of wrapper methods.

# They can detect relationships between features that might be relevant to the machine learning model.
# Unlike filter methods, they are designed to choose features that are relevant to whatever machine learning 
# model you are using.
# We covered four different greedy wrapper methods and implemented them using mlextend in Python.

# Sequential forward selection adds one feature at a time.
# Sequential backward selection removes one feature at a time.
# Sequential forward floating selection adds (and sometimes removes) one feature at a time.
# Sequential backward floating selection removes (and sometimes adds) one feature at a time.
# We also covered recursive feature elimination, which ranks features by importance and removes the least important 
# feature at every step. We used the scikit-learn library to implement that algorithm and investigate the results.













