# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:19:20 2023

@author: geron
"""

#  Regularization is a statistical technique the minimizes overfitting and is executed during the model fitting step
# it is also an embedded freature selection method because it is implmented while the parameters of the model are being
#  calculated.  Regularization makes sure the model is accurate with new data being added
#  2 concepts important to regulatization
#  1 - bias-variance tradefoff
#  2 - hyperparameter tuning

# Overfitting - When a model is able to represent a particular set of data points effectivly but is not able to fit
# new data well when this happens the model has one or more attributes
# 1. It fits the training data well but performs significantly worse on test data
# 2. It typically has more parameters than necessary, i.e., it has high model complexity
#3 It might be fitting for features that are multi-collinear (i.e., features that are highly negatively or positively correlated)
#4 It might be fitting the noise in the data and likely mistaking the noise for features
# we see overfitting by comparing the model performance on the training data versus test data
#  example For instance if the R-squared score is high for training data but the model performs poorly on test data, 
#it’s a strong indicator of overfitting. 


# example
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt

df = pd.read_csv("./student_math.csv")
print(df.head())

#setting target and predictor variables
y = df['Final_Grade']
X = df.drop(columns = ['Final_Grade'])

# 1. Number of features
num_features = len(X.columns)
print("Number of features: ",num_features)

#Performing a Train-Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Fitting a Linear Regression Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

#Training Error
pred_train = model.predict(X_train)
MSE_train = np.mean((pred_train - y_train)**2)
print("Training Error: ", MSE_train)

# 2. Testing Error
#We’re about to fit the data to a model with 42 parameters! (Intercept plus 41 coefficients, one for each predictor variable.) This might already make us apprehensive of the model potentially overfitting the data because:

#the model likely has a high degree of complexity
#we haven’t checked for collinearity between the features
#In order to assess whether we are overfitting, we’re going to fit the model. In the workspace, you’ll see that we’ve provided code to split the data into a training and test set, fit a regression on all 41 features, and calculated the mean squared error (MSE) on the training data.

#In the section below the comment ​​# 2. Testing Error, fill in the code to calculate the MSE for the test set. Save the result as MSE_test (currently set to None).
pred_test = model.predict(X_test)
MSE_test = np.mean((pred_test - y_test)**2)
print("Testing Error: ", MSE_test)


#Calculating the regression coefficients
predictors = X.columns
coef = pd.Series(model.coef_,predictors).sort_values()

# 3. Plotting the Coefficients

plt.figure(figsize = (15,10))
coef.plot(kind='bar', fontsize = 20)
plt.title ("Regression Coefficients", fontsize = 30)
plt.show()

#output
# [5 rows x 42 columns]
# Number of features:  41
# Training Error:  2.6268841802196263
# Testing Error:  4.987346573982339
#  seing the test error is almost double the train error would indicate overfitting


#  The loss function
#  this function is how we get the coefficients or parameters of a linerar regression model.  
#  Formula y = b0 + b1x1 + b2x2 + e  - linear regression
#  we solbe for the intercept b0 and the boeffients b1 and b2 by minimizing the mean squareed error.  
#  loss function is minimized by the method of OLS ordinary least squares and for larger datasets the gradient
#  descent algorithm is used to arrive at the minumum.  

import numpy as np
import codecademylib3
import matplotlib.pyplot as plt

from sklearn import datasets
data, y, coefficients = datasets.make_regression(n_samples = 100, n_features = 2, coef = True, random_state = 23)
x1 = data[:,0]
x2 = data[:,1]

# 1. Print the coefficients
print(coefficients)
#We’re going to write a pythonic function to output the value of the loss function at each data point for all 
#possible values of b1 and b2.
# 2. Loss Function
def loss_function(b1,b2,y,x1,x2):
    error = y - (b1*x1) - (b2*x2)
    loss = np.mean(error**2)
    return loss

# 3. Plot loss function for data
from plot_loss import plot_loss_function
b1 = np.linspace(-150, 150, 501)
b2 = np.linspace(-150, 150, 501)
contour_plot = plot_loss_function(b1,b2,y,x1,x2)
plt.show()

# #Each ellipse in this plot represents the points where the loss function has the same value. 
# The larger the ellipse, the higher the value of loss for all the points (b1,b2) that fall on the ellipse, 
# as we can see from the labels on the contours.
# #Following this logic, the center of this set of concentric ellipses should represent the minimum value of 
# the loss function and the value of the coefficients (b1,b2) at this point should be the solution of the regression
#  problem and represent the best fit for our data.
# 4. Plot the best fit coefficients
best_fit_b1 = coefficients[0]
best_fit_b2 = coefficients[1]
plt.scatter(best_fit_b1, best_fit_b2, s = 50, color = 'green')
plt.show()


# The Regularization Term  - New loss function = old loss function + A*(regularization term)
# regularization penalizes models for overfitting by adding a penalty term to the loss function.
# they rely on penalizing overfitting by controlling how large the coefficents can get.  The penalty term or regularization 
#  term is multiplied by a facort alpha and added to the old loss function  
# The 2 most common ways
# 1 - Lasso or L1 -  aka manhattan distance sum of the absolute values of the coefficients - l1 = |b1| + |b2|
# 2 - Ridge or L2 -  aka euclidean distancesum of the squares of the coefficients  - l2 = b2/1 + b2/2

#L1 Loss

# Minimizing this new loss function essentially means restricting the size of the regularization term while minimizing 
# the old loss function. Let’s say that our regularization term can take a maximum value, s:

# |b1| + |b2| <= s
# ​
#  ∣≤s
# This is equivalent to confining our coefficients to a surface around the origin bounded by 4 lines
#  : b1+b2 = s, b1-b2 = s, b2-b1 = s and -b1-b2 = s.

# The figure to the right replicates the elliptical contours for the loss function that we’d plotted earlier 
# in the lesson. If we plot these four lines as with b1 and b2 as X and Y axes respectively, we get the diamond 
# shaped blue shaded region that we’ve shown here. We have chosen a value of s = 50 for this figure - 
# this means that either coefficient can have a maximum value of 50. The choice of s is deeply tied to
#  the choice of alpha as they are inversely related.

# The value of (b1,b2) that satisfies the regularization constraint while minimizing the loss function 
# is denoted by the white dot. Notice that it is exactly at the tip of the diamond where it intersects 
# with a contour from our loss function. It also happens to fall exactly on the X axis, thus setting the value of b2 to 0!

# Why is this the point that minimizes the new loss function? Remember that the goal here is to minimize 
# the original loss function while meeting the regularization constraint. We still want to be as close to 
# the center of the contours (the original loss function minimum) as possible. The point that’s closest to the 
# center of the contours while simultaneously lying within the regularization surface boundary is the white dot!

# The word Lasso is actually an acronym for “Least Absolute Shrinkage and Selection Operator” - 
# it shrinks the absolute value of coefficients and selects parameters by way of setting some of the
#  coefficients to zero. If the coefficient of a regression model is set to zero, it means that we’ve
#  pretty much eliminated the feature associated with it. In models with a high number of features,
#  lasso regularization tends to set a significant fraction of its parameters to zero, thus acting as a
#  feature selection method.


import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import helpers


df = pd.read_csv("./student_math.csv")
y = df['Final_Grade']
X = df.drop(columns = ['Final_Grade'])
#We can implement Lasso for this dataset by importing the Lasso module within scikit-learn‘s class of ‘linear_models. 
# We’re choosing a value of s by setting alpha to 0.1 - the scikit-learn default is 1. We’ve written some code in 
# script.py to do a train-test split, implement regression with Lasso regularization and calculate the training error.
# 1. Train-test split and fitting an l1-regularized regression model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
lasso = Lasso(alpha = 0.1)
lasso.fit(X_train, y_train)

l1_pred_train = lasso.predict(X_train)
l1_mse_train = np.mean((l1_pred_train - y_train)**2)
print("Lasso (L1) Training Error: ", l1_mse_train)
#ollowing the syntax for training error, calculate the testing error using the following steps:

set the variable l1_pred_test equal to the result of applying the model to X_test
set the variable l1_mse_test equal to the Mean Squared Error of the test data
print l1_mse_test
# The training and test Mean Squared Errors obtained from implementing the regression without regularization
#  were 2.627 and 4.987 (rounded to three decimals!) respectively. 
# 2. Calculate testing error
l1_pred_test = lasso.predict(X_test)
l1_mse_test = np.mean((l1_pred_test - y_test)**2)
print(l1_mse_test)

#We see how our training error went up but our test error went down, which makes sense as our model is performing 
# slightly better on test data at the cost of performing slightly worse on training data
# Lasso has shrunk more than half our coefficients to zero! Additionally, while the value of all the 
# coefficients have shrunk, Lasso has increased the relative importance of some. An important thing to note
#  here is that we manually set the value of alpha to 0.1. The number of features that get eliminated due to
#  Lasso is definitely tied to the value of alpha
# 3. Plotting the Coefficients
predictors = X.columns
coef = pd.Series(lasso.coef_,predictors).sort_values()
plt.figure(figsize = (12,8))
plt.ylim(-1.0,1.0)
coef.plot(kind='bar', title='Regression Coefficients with Lasso (L1) Regularization')
plt.show()

# output
# Lasso (L1) Training Error:  3.0118464559476825
# 4.272174214435373


# L2 or ridge regularization - b2/1 + b2/2 <= s^2
# key difference to l1 is instead of a diamond shaped area the coefficents live within a circle of radius S
# The general goal is still similar though, we want to minimize the old loss while restricting the values of the 
# coefficients to the boundary of this circle. Once again we want our new coefficient values to be as close to the 
# unregularized best fit solution (i.e., the center of the contours) as possible while falling within the circle.

# The value of (b1,b2) that minimizes this new loss function almost never lies on either axes. The solution here is
#  not the pink dot that lies on the X axis like in L1, but rather the white dot that we have shown. The reason for 
#  this is as follows: The circle that contains the white and pink dots represents the smallest value of the old loss 
#  function that satisfies the regularization constraint, but while the pink dot makes the regularization term’s 
#  value s^2 exactly, the white dot makes it even smaller as it lies inside the circle!

# Unlike Lasso, our Ridge coefficients can never be exactly zero! L2 regularization is therefore not a feature 
# elimination method like L1. The coefficients of L2 get arbitrarily small but never zero. This is particularly
#  useful when we don’t want to get rid of features during modeling but nonetheless want their relative importances
#  emphasized.

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import helpers

df = pd.read_csv("./student_math.csv")
y = df['Final_Grade']
X = df.drop(columns = ['Final_Grade'])
#We’re setting s by way of setting alpha to 100 - the scikit-learn default is 1. (We’ll delve deeper into how to 
# choose the right alpha in the upcoming exercise!)
# We’re going to evaluate our training and test error and the error just as we did last time. 
# Following the syntax for training error, calculate the testing error using the following steps:
# set the variable l2_pred_test equal to the result of applying the model to X_test
# set the variable l2_mse_test equal to the Mean Squared Error of the test data
# 1. Train-test split and fitting an l2-regularized regression model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
ridge = Ridge(alpha = 100)
ridge.fit(X_train, y_train)

#Training error
l2_pred_train = ridge.predict(X_train)
l2_mse_train = np.mean((l2_pred_train - y_train)**2)
print("Ridge (L2) Training Error: ", l2_mse_train)
# #he training and test Mean Squared Errors obtained from implementing the regression without regularization were
#  2.627 and 4.987 (rounded to three decimals!) respectively. We see how our training error went up but our test
#  error went down, which makes sense as our model is performing slightly better on test data at the cost of 
#  performing slightly worse on training data.

# What do our coefficients look like post ridge regularization? Uncomment the code below # 3.
#  Plotting the Coefficients, add a plt.show() and press “Run”.

# We see how L2 regularization shrinks the coefficients as well, and while there are some 
# coefficients that are very small, no coefficient is set to zero. The amount by which the 
# feature coefficients get shrunk is related to the alpha we choose in implementing regularization.
#  We’re now ready to learn the things to consider in choosing alpha.
# 2. Calculate testing error
l2_pred_test = ridge.predict(X_test)
l2_mse_test = np.mean((l2_pred_test - y_test)**2)
#print("Ridge (L2) Testing Error: ", l2_mse_test)
print(l2_mse_test)

# 3. Plotting the Coefficients
predictors = X.columns
coef = pd.Series(ridge.coef_,predictors).sort_values()
plt.figure(figsize = (12,8))
plt.ylim(-1.0,1.0)
coef.plot(kind='bar', title='Regression Coefficients with Lasso (L1) Regularization')
plt.show()
# output
# Ridge (L2) Training Error:  2.8476069326177864
# 4.35738634031129


# Hyperparameter Tuning - alpha is what is known as hyperparameter - it is not learned during the model fitting steo
# the way model paramaters are.  Rather its chosen prior to fitting the model and is used to control the learning process
#  The choice of alpha is how we control for overfitting
#  The larger the alpha the smaller the size of the allowed coefficients.  In essence alpha is inversely proportional
# to s in the case of L1 or s^2 in the case of L2
#If s is very large (i.e., alpha is very small), the unregularized loss function minimum can easily fall within 
#this large boundary and thus make it similar to regression without regularization.
#If s is very small (i.e., alpha is very large), the regression coefficients become very small and the loss 
#value for the best fit becomes large making the regression over-regularized.


# Bias Variance Tradeoff - When we add the regularization term to our loss function we are in essence introducing a bias
#  the greater the alpha the smaller the coefficients and the more biased the model.
#  For very high values of alpha, while Ridge begins to make most of the coefficients very small,
#  Lasso ends up eliminating all but one feature!

# Recall that the reason we wanted to perform regularization was to prevent our model from overfitting the data. 
# Such a model is said to have high variance as it is likely fitting for random errors or noise within the data.
#  We introduced the bias term to minimize the variance, but if we’re not careful and allow it to get arbitrarily
#  large, we run the risk of underfitting the model!

# Ideally we want a machine learning model to have low bias and low variance, i.e., we want it to perform well 
# on training data as well as test data. However, trying to minimize bias and variance simultaneously is a bit 
# of a conundrum as lowering one raises the other! This dilemma in machine learning models is known as the
#  bias-variance tradeoff.

# Hyperparameter tuning helps us find a sweet spot in this tradeoff to ensure that neither bias nor variance get too high. 
# Typically, a portion of the data is set aside that is known as the “validation set” 
# or “holdout set” (over and above the usual test-train split) and this is used to perform hyperparameter tuning on. 



# Imagine the data is already centered and the intercept b0 is thus zero.
# The linear regression equation here is given by: y = b1*x1 + b2*x2 + error
import numpy as np
 
def loss_function(b1,b2,y,x1,x2):
  error  = y - b1*x1 - b2*x2
  loss = np.mean(error**2)
  return loss
 
def regularization_term(b1,b2):
  ridge_regularization_term = b1**2 + b2**2
  return ridge_regularization_term
 
def ridge_loss_function(b1,b2,y,x1,x2, alpha):
  modified_loss = loss_function(b1,b2,y,x1,x2) + alpha*regularization_term(b1,b2)
  return modified_loss




#Complete the following piece of code that implements L1 regularization on a dataset (X,y) and 
#calculates the mean-squared error of the fit on test data:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = Lasso(alpha = 0.1)
 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
 
mse = mean_squared_error(y_test, y_pred)









