# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:44:48 2023

@author: geron
"""

# hyperparamter tuning can be donw with different methods
#  Grid search is one method and works by testing a model on a predetermined list of hyperparamater values
#  you want to know if l1 or l2 is best to you on model  You can determine this by training your model X amount of times.  
#Once with each different comination of hyperparamters.  
# for a in [1, 2, 3, 4, 5, 6]:
#     set Hyperparameter 1 = a
 
#     for b in [1, 2, 3, 4]:
#         set Hyperparameter 2 = b
 
#         train the model with the specified hyperparameters
#         evaluate the results



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
 
# Load the data set
X = vert.drop('class', axis=1)
y = vert['class']
 
# Split the data set into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y)
 
# Create the logistic regression model
model = LogisticRegression(solver = 'liblinear', max_iter = 1000)

# We set solver to 'liblinear' so that we try different regularization techniques later on. LogisticRegression‘s 
# default solver is not compatible with L1 regularization, but 'liblinear' is compatible with both L1 and L2 regularization.
# We set max_iter to 1000 so that the solver will converge.

# The LogisticRegression model uses regularization. The penalty parameter determines whether it uses L1 or L2 
# regularization, and C determines the strength of regularization. We would like to do a grid search to test out 
# several different combinations of penalty and C to see which ones make the model perform the best.

# In order to use scikit-learn’s grid search, we have to make a list of all the values of parameter and C that we 
# want to try and put them inside a dictionary.

parameters = {'penalty': ['l1', 'l2'], 'C': [1, 10, 100]}


# It’s worth noting that the terminology we’re using can be confusing. Regularization strength is a 
# hyperparameter of the linear regression model, but C is a parameter of the LogisticRegression object. 
# Since we’re dealing with Python code, it’s fair to call this dictionary parameters.

# Once we’ve prepared the model and listed all the hyperparameter values that we want to test, we can 
# create a GridSearchCV model.

from sklearn.model_selection import GridSearchCV
 
clf = GridSearchCV(model, parameters)
# GridSearchCV takes two important parameters: the name of the model that we are testing (in this case, model) 
# and the name of the dictionary that we made earlier (parameters).

# Now we are ready to tune the hyperparameters. We do this by calling the .fit() on clf.

clf.fit(X_train, y_train)
# This is a good time to remind you that it’s very important to separate the training data, testing data, 
# and the cross-validation data. If you don’t you will overfit your hyperparameters.

# We’ve already used train_test_split to set aside a testing set. GridSearchCV will automatically 
# divide ‘X_train and y_traininto training and cross-validation data. By default, it does this by using a
#  technique called k-fold cross-validation. 
#  We won't delve into the details of that here, but you may rest assured thatGridSearchCV` 
#  will automatically take care of the cross-validation.


# Example
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Load the data set
cancer = load_breast_cancer()

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target)

# These are the hyperparameters that we will test.
# We'll try both 'l1' and 'l2' regularization.
# C is the inverse of regularization strength. Smaller C will result in stronger regularization.
parameters = {'penalty': ['l1','l2'], 'C':[0.1,1,10,100,1000]}

# The logistic regression model
# The 'liblinear' solver is compatible with both 'l1' and 'l1' penalties.
# Setting max_iter to 1000 ensures that the solver will converge for this particular data set.
lr = LogisticRegression(solver = 'liblinear', max_iter=1000)

# Create a GridSearchCV model
# This will train the model 'lr' with each possible combination of hyperparameters in 'parameters'
clf = GridSearchCV(lr,parameters)

# Fit the GridSearchCV model
clf.fit(X_train,y_train)



# evaluationg the results of GridSearchCV
# print(clf.best_estimator_)
# LogisticRegression(C=1, penalty='l1', solver='liblinear')
# In this example, we see that the model performed best when C=1 and penalty='l1'.

# GridSearchCV also generates a dictionary that contains information about the model. Let’s take a look at the 
# entries clf.cv_results_['params'] and clf.cv_results_['mean_test_score'].

# print(clf.cv_results_['params'])
# [{'C': 1, 'penalty': 'l1'}, {'C': 1, 'penalty': 'l2'}, {'C': 2, 'penalty': 'l1'}, {'C': 2, 'penalty': 'l2'},
#  {'C': 3, 'penalty': 'l1'}, {'C': 3, 'penalty': 'l2'}]
# print(clf.cv_results_['mean_test_score'])
# [0.98906967 0.9883424  0.98833975 0.98906967 0.98761248 0.98906967]
# This displays each hyperparameter combination and the associated scores. Here’s some code to format this in a 
# single Pandas DataFrame for easy readability.

# import pandas as pd
 
# df = pd.concat([pd.DataFrame(clf.cv_results_['params']), pd.DataFrame(clf.cv_results_['mean_test_score'], 
#                                                                       columns=['Score'])] ,axis=1)
 
# cv_table = df.pivot(index='C', columns='penalty')
 
# print(cv_table)
#             Score          
# penalty        l1        l2
# C                          
# 1        0.989070  0.988342
# 2        0.988340  0.989070
# 3        0.987612  0.989070




import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Load the data set
cancer = load_breast_cancer()

# Split the data into training and testing sets
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# The hyperparameters that we will test.
parameters = {'penalty': ['l1', 'l2'], 'C': [0.1, 1, 10, 100]}

# The logistic regression model
# The 'liblinear' solver is compatible with both 'l1' and 'l2' penalties.
# Setting max_iter to 1000 ensures that the solver will converge for this particular data set.
lr = LogisticRegression(solver = 'liblinear', max_iter = 1000)

# Create a GridSearchCV model
clf = GridSearchCV(lr, parameters)

# Fit the GridSearchCV model
clf.fit(cancer.data, cancer.target)

# Print the hyperparameters that performed the best.
print(clf.best_estimator_)

# Print every combination of hyperparameters that you tested.
print(clf.cv_results_['params'])

# Print the score of the model with each combination of hyperparameters.
print(clf.cv_results_['mean_test_score'])

# This Pandas DataFrame tabulates hyperparameter values and the associated scores.
df = pd.concat([pd.DataFrame(clf.cv_results_['params']), pd.DataFrame(clf.cv_results_['mean_test_score'], columns=['Accuracy'])] ,axis=1)

# This table displays the information more clearly.
cv_table = df.pivot(index = 'C', columns = 'penalty')
print(cv_table)

# Compute and print the accuracy of the model on test data
acc = clf.score(X_test, y_test)
print(acc)


# output 
# LogisticRegression(C=100, max_iter=1000, penalty='l1', solver='liblinear')
# [{'C': 0.1, 'penalty': 'l1'}, {'C': 0.1, 'penalty': 'l2'}, {'C': 1, 'penalty': 'l1'}, {'C': 1, 'penalty': 'l2'},
#  {'C': 10, 'penalty': 'l1'}, {'C': 10, 'penalty': 'l2'}, {'C': 100, 'penalty': 'l1'}, {'C': 100, 'penalty': 'l2'}]
# [0.9279615  0.94552088 0.95081509 0.95081509 0.95783263 0.95081509
#  0.96839    0.94907623]
#          Accuracy          
# penalty        l1        l2
# C                          
# 0.1      0.927961  0.945521
# 1.0      0.950815  0.950815
# 10.0     0.957833  0.950815
# 100.0    0.968390  0.949076
# 0.9790209790209791



# random search instead of using grid search
# for i in the range 0 to 24:
#     a = random number between 0 and 6=
#     set Hyperparameter 1 = a
 
#     b = random number between 0 and 4
#     set Hyperparameter 2 = b
 
#     train the model with the specified hyperparameters
#     evaluate the results


# With random search, we don’t have to make a list, but we still have to provide some information about how we want
#  to select random numbers. Do we want random numbers between 0 and 100? Between -10 and 10? Do we want the same chance 
#  of picking small numbers and picking large numbers?

# We can do this by specifying a probability distribution for each hyperparameter.

# from scipy.stats import uniform
 
# distributions = {'penalty': ['l1', 'l2'], 'C': uniform(loc=0, scale=100)}
# Let’s take a closer look at each distribution. The penalty hyperparameter of scikit-learn’s LogisticRegression model 
# has only two possible values: l1 and l2. We list them both. RandomizedSearchCV will treat this as a discrete uniform
#  distribution. This just means that every item in the list has an equal chance of being selected. In this case,
#  there’s a 50% chance of drawing l1 and a 50% chance of drawing l2.

# The hyperparameter C is the inverse of regularization strength. It can be any positive number, so we have to 
# specify a probability distribution that allows us to randomly select a positive number. The scipy library
#  has many probability distributions to choose from (you can see a list of them here). For this example,
#  we’re using the uniform distribution. This allows us to randomly select numbers between loc and loc+scale
#  (in this case, between 0 and 100).

# Once we’ve prepared the model and specified a distribution for each hyperparameter, we can create a 
# RandomizedSearchCV model.

# from sklearn.model_selection import RandomizedSearchCV
 
# clf = RandomizedSearchCV(lr, distributions, n_iter=8)
# RandomizedSearchCV takes three important parameters: the name of the model that we are testing (in this case, lr), 
# the name of the dictionary that we made earlier (distributions), and n_iter. n_iter determines how many hyperparameter
#  combinations we’ll test.

# Now we are ready to tune the hyperparameters. We do this by calling the .fit() on clf.

# clf.fit(cancer.data, cancer.target)

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

# Load the data set
cancer = load_breast_cancer()

# Split the data into training and testing sets
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# These are the hyperparameters that we will test.
# We'll try both 'l1' and 'l2' regularization.
# C is the inverse of regularization strength. Smaller C will result in stronger regularization.
distributions = {'penalty': ['l1', 'l2'], 'C': uniform(loc=0, scale=100)}

# The logistic regression model
lr = LogisticRegression(solver = 'liblinear', max_iter = 1000)

# Create a RandomizedSearchCV model
clf = RandomizedSearchCV(lr, distributions, n_iter=8)

# Fit the RandomizedSearchCV model
clf.fit(X_train, y_train)



# evalutation results of random search
# print(clf.best_estimator_)
# LogisticRegression(C=81.21687287754932, max_iter=1000, penalty='l1', solver='liblinear')
# In this example, we see that the model performed best with an l1 penalty and with C equal to about 81.

# RandomSearchCV also generates a dictionary that contains information about the model. 
# Let’s take a look at the entries clf.cv_results_['params'] and clf.cv_results_['mean_test_score'].

# print(clf.cv_results_['params'])
# [OrderedDict([('C', 54.88135039273247), ('penalty', 'l2')]), 
# OrderedDict([('C', 84.42657485810173), ('penalty', 'l2')]), 
# OrderedDict([('C', 54.48831829968969), ('penalty', 'l2')]), 
# OrderedDict([('C', 62.35636967859723), ('penalty', 'l1')]), 
# OrderedDict([('C', 43.75872112626925), ('penalty', 'l1')]), 
# OrderedDict([('C', 5.671297731744318), ('penalty', 'l1')]), 
# OrderedDict([('C', 38.34415188257777), ('penalty', 'l1')]), 
# OrderedDict([('C', 81.21687287754932), ('penalty', 'l1')])]
# print(clf.cv_results_['mean_test_score'])
# [0.95083062, 0.94730632, 0.95081509, 0.96660456, 0.96309579,
#        0.95607825, 0.96309579, 0.96663562]
# We can use pandas to display a summary of the results of random search.

# import pandas as pd
 
# df = pd.concat([pd.DataFrame(clf.cv_results_['params']), pd.DataFrame(clf.cv_results_['mean_test_score'], 
#                                                                       columns=['Accuracy'])] ,axis=1)
 
# print(df.sort_values('Accuracy', ascending = False))
#            C penalty  Accuracy
# 7  81.216873      l1  0.966636
# 3  62.356370      l1  0.966605
# 4  43.758721      l1  0.963096
# 6  38.344152      l1  0.963096
# 5   5.671298      l1  0.956078
# 0  54.881350      l2  0.950831
# 2  54.488318      l2  0.950815
# 1  84.426575      l2  0.947306


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from skopt import BayesSearchCV
from skopt.space import Categorical, Real
import pandas as pd

# Load the data set
cancer = load_breast_cancer()

# Split the data into training and testing sets
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# The logistic regression model
lr = LogisticRegression(solver = 'liblinear', max_iter = 1000)

# These are the hyperparameters that we will test.
# We'll try both 'l1' and 'l2' regularization.
# C is the inverse of regularization strength. Smaller C will result in stronger regularization.
search_spaces = {'penalty': Categorical(['l1', 'l2']), 'C': Real(0.01, 100, prior='uniform')}

# Create a BayesSearchCV model
clf = BayesSearchCV(lr, search_spaces=search_spaces, n_iter=10)

# Fit the BayesSearchCV model
clf.fit(X_train, y_train)

# Show which hyperparameters performed the best
print(clf.best_estimator_)

# Print the the parameters and mean test score
print(clf.cv_results_['params'])
print(clf.cv_results_['mean_test_score'])

# Create and print Pandas DataFrame
cv_table = pd.concat([pd.DataFrame(clf.cv_results_['params']), pd.DataFrame(clf.cv_results_['mean_test_score'], columns=['Accuracy'])], axis=1)
 
print(cv_table.sort_values('Accuracy', ascending = False))

# Assess the model's accuracy on the testing data
acc = clf.score(X_test, y_test)
print(acc)

# output
# LogisticRegression(C=57.094820533761094, max_iter=1000, penalty='l1',
#                    solver='liblinear')
# [OrderedDict([('C', 33.85514282052376), ('penalty', 'l1')]), OrderedDict([('C', 59.149442209267015), 
#                                                                           ('penalty', 'l2')]),
#  OrderedDict([('C', 57.094820533761094), ('penalty', 'l1')]), OrderedDict([('C', 37.71840982585621), 
#                                                                            ('penalty', 'l2')]), 
#  OrderedDict([('C', 53.73075166225133), ('penalty', 'l2')]), OrderedDict([('C', 3.099392913081886), 
#                                                                           ('penalty', 'l2')]),
#  OrderedDict([('C', 94.99930392327487), ('penalty', 'l2')]), OrderedDict([('C', 68.03547038978355), 
#                                                                           ('penalty', 'l2')]), 
#  OrderedDict([('C', 92.65681008344126), ('penalty', 'l2')]), OrderedDict([('C', 81.18443409237895), ('penalty', 'l1')])]
# [0.9601368  0.94837209 0.96016416 0.95307798 0.95540356 0.95543092
#  0.95307798 0.95540356 0.95305062 0.95545828]
#            C penalty  Accuracy
# 2  57.094821      l1  0.960164
# 0  33.855143      l1  0.960137
# 9  81.184434      l1  0.955458
# 5   3.099393      l2  0.955431
# 4  53.730752      l2  0.955404
# 7  68.035470      l2  0.955404
# 3  37.718410      l2  0.953078
# 6  94.999304      l2  0.953078
# 8  92.656810      l2  0.953051
# 1  59.149442      l2  0.948372
# 0.951048951048951





























