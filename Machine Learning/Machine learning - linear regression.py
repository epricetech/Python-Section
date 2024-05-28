# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:22:10 2023

@author: geron
"""
#  to find clope and intercept formula is y = mx + b  m is the slope and b is the intercept where it hits the y axits
import codecademylib3_seaborn
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

plt.plot(months, revenue, "o")

plt.title("Sandra's Lemonade Stand")

plt.xlabel("Months")
plt.ylabel("Revenue ($)")

plt.show()

# What do you think the revenue in month 13 would be?
month_13 = 200


import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 12
#intercept:
b = 53

y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months,y)
plt.show()


##  LOSS - when we assign a slop and interecept to fit a set of bpoints we define what the best fit is
#   For each data point we calculate loss , a number that measures how bad the model or line prediction was
#  to figure out we square the distance from the point to the line.  We square the distance so points above and below
#  the line both contribute to total loss.

#What is the sum of squared error between the points described by x_values and y_values and the line described by m and b?
# y_values_of_points = [1, -4, -7, -6]
# y_values_of_line = [1, -3, -6, -8]
# Yes! To find the loss, square the distance from each point to the line, and add these together (0² + 1² + 1² + (-2)²)
# We have three points, (1, 5), (2, 1), and (3, 3). We are trying to find a line that produces lowest loss.

# We have provided you the list of x-values, x, and y-values, y, for these points.

# Find the y-values that the line with weights m1 and b1 would predict for the x-values given. 
#Store these in a list called y_predicted1.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# Find the y values that the line with weights m2 and b2 would predict for the x-values given. 
#Store these in a list called y_predicted2.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Create a variable called total_loss1 and set it equal to zero.

# Then, find the sum of the squared distance between the actual y-values of the points and the
# y_predicted1 values by looping through the list:

# Calculating the difference between y and y_predicted1
# Squaring the difference
# Adding it to total_loss1
# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Create a variable called total_loss2 and set it equal to zero.

# Find the sum of the squared distance between the actual y-values of the points and the 
#y_predicted2 values by looping through the list:

# Calculating the difference between y and y_predicted2
# Squaring the difference
# Adding it to total_loss2
# Checkpoint 5 Passed

# Stuck? Get a hint
# 5.
# Print out total_loss1 and total_loss2. Out of these two lines, which would you use to model the points?

# Create a variable called better_fit and assign it to 1 if line 1 fits the data better and 2 
#if line 2 fits the data better.
x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [m1*x_val + b1 for x_val in x]
y_predicted2 = [m2*x_val + b2 for x_val in x]

total_loss1 = 0
total_loss2 = 0

for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i])**2
  total_loss2 += (y[i] - y_predicted2[i])**2


print(total_loss1, total_loss2)
better_fit = 2




#  Gradient Descent for intercept - as we look to minimize loss we take each paramater we are changing and move it in 
#  the direction that minimizes loss.  this is gradient descent

#  exsmple the intercept for aline is 10.  a point 10 on the curve the slope is downward.  Therefore if we increase the 
#  intercept we be lowing the loss.  
#  to find formula
##we find the sum of y_value - (m*x_value + b) for all the y_values and x_values we have##
##and then we multiply the sum by a factor of -2/N. N is the number of points we have.

#example
# Define a function called get_gradient_at_b() that takes in a set of x values, x, a set of y values, y, a slope m, and an intercept value b.

# For now, have it return b, unchanged.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# In the get_gradient_at_b() function, we want to go through all of the x values and all of the y values and compute (y - (m*x+b)) for each of them.

# Create a variable called diff that has the sum of all of these values.

# Instead of returning b from the get_gradient_at_b() function, return diff.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Still in the get_gradient_at_b() function, define a variable called b_gradient and set it equal to the -2/N multiplied by diff.

# Note: N is the number of points, i.e. the length of the x list or the y list.

# Instead of returning diff, return b_gradient.

def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(0, len(x)):
      y_val = y[i]
      x_val = x[i]
      diff += (y_val - ((m * x_val) + b))

    b_gradient = -2/N * diff
    return b_gradient



#  Gradient Descent for Slope - 
# To find the m gradient:

# we find the sum of x_value * (y_value - (m*x_value + b)) for all the y_values and x_values we have
# and then we multiply the sum by a factor of -2/N. N is the number of points we have.


 #  Example
#  Define a function called get_gradient_at_m() that takes in a set of x values, x, a set of y values, y, a slope m, and an intercept value b.

# For now, have it return m.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# In this function, we want to go through all of the x values and all of the y values and compute x*(y - (m*x+b)) for each of them.

# Create a variable called diff that has the sum of all of these values, and return it from the function.

# Checkpoint 3 Passed
# 3.
# Define a variable called m_gradient and set it equal to the -2/N multiplied by diff.

# Instead of returning diff, return m_gradient.

def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val*(y_val - ((m * x_val) + b))
    m_gradient = -2/N * diff
    return m_gradient


#  Putting it together the m and b gradient to minimalize loss - be careful not to overshoot the minumum error
#  We can scale the size of the step by multiplying the gradient by a learning rate
##  new_b = current_b - (learning_rate * b_gradient)
# where current_b is our guess for what the b value is, b_gradient is the gradient of the loss curve at our current guess, 
# and learning_rate is proportional to the size of the step we want to take.

# Define a function called step_gradient() that takes in x, y, b_current, and m_current.

# This function will find the gradients at b_current and m_current, and then return new b and m values that have been moved in that direction.

# For now, just return the pair (b_current, m_current).

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# Inside step_gradient(), find the gradient at b_current and the gradient at m_current using the functions 
# defined before (get_gradient_at_b and get_gradient_at_m).

# Store these gradients in variables called b_gradient and m_gradient, and return these from the function
#  instead of b_current and m_current.

# Return them as a list.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Let’s try to move the parameter values in the direction of the gradient at a rate of 0.01.

# Create variables called b and m:

# b should be b_current - (0.01 * b_gradient)
# m should be m_current - (0.01 * m_gradient)
# Return the pair b and m from the function.

# Checkpoint 4 Passed
# 4.
# We have provided Sandra’s lemonade data once more. We have a guess for what we think the b and m might be.

# Call your function to perform one step of gradient descent. Store the results in the variables b and m.

# Great! We have a way to step to new b and m values! Next, we will call this function a bunch, in order 
# to move those values towards lower and lower loss.



def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

# Define your step_gradient function here
def step_gradient(x,y,b_current,m_current):
  b_gradient = get_gradient_at_b(x,y,b_current,m_current)
  m_gradient = get_gradient_at_m(x,y,b_current,m_current)
  b = b_current - (0.01 * b_gradient)
  m = m_current - (0.01 * m_gradient)
  return [b,m]




months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b, m = step_gradient(months,revenue,b,m)

print(b, m)



#  CONVERGENCE - How do we know when to stop changing the parameters for m and b?
#  we define a convergence - this is when the loss stops changing or changes very slowly when parapeters are changed.  
#  the values are where m and b stop chaning much


##  LEARNING RATE - a small learning rate will take a long time to converge and might run out of cycles where a large
#  learning rate might skip over best value and never converge 
#  Key is to find learning rate large enough that gradient descent converges witht he efficiency you need

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from data import bs, bs_000000001, bs_01


# bs_000000001: 1400 iterations of gradient descent on b with a learning rate of 0.000000001
# bs_01: 100 iterations of gradient descent on b with a learning rate of 0.01
# iterations = range(1400)
iterations = range(100)

plt.plot(iterations, bs_01)
plt.xlabel("Iterations")
plt.ylabel("b value")
plt.show()

# This learning rate is far too small! The b value is still changing with each iteration, and has not reached a plateau. 
# Whereas our other learning rate reached an answer at 1400 iterations (or before!), this one barely reached 0.00035 as a
#  guess for b, which we know is far from the value of 48.5 that the other learning rate converged to.

# This learning rate is far too large! The b value changed way too much with each iteration, and quickly blew up to 1e192.
#  That’s a 1 with 192 zeros after it. Whereas our other learning rate reached an answer at 1400 iterations, this one melted 
#  our processors at 100 iterations, because the b value had become way too large.



##  PUt it Together 2 - all steps till reach convergence

# We have all of the functions we have defined throughout the lesson.

# Now, let’s create a function called gradient_descent() that takes in x, y, learning_rate, and a num_iterations.

# For now, return [-1,-1].

# Checkpoint 2 Passed
# 2.
# In the function gradient_descent(), create variables b and m and set them both to zero for our initial guess.

# Return b and m from the function.

# Checkpoint 3 Passed
# 3.
# Update your step_gradient() function to take in the parameter learning_rate (as the last parameter) and replace the 0.01s in the calculations of b_gradient and m_gradient with learning_rate.

# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Let’s go back and finish the gradient_descent() function.

# Create a loop that runs num_iterations times. At each step, it should:

# Call step_gradient() with b, m, x, y, and learning_rate
# Update the values of b and m with the values step_gradient() returns.
# Checkpoint 5 Passed
# 5.
# Outside of the function, uncomment the line that calls gradient_descent on months and revenue, with a learning rate of 0.01 and 1000 iterations.

# It stores the results in variables called b and m.

# Checkpoint 6 Passed
# 6.
# Uncomment the lines that will plot the result to the browser.


import codecademylib3_seaborn
import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y,learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#Your gradient_descent function here:  
def gradient_descent(x,y,learning_rate,num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(b,m,x,y,learning_rate)
  return [b,m]



months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()



#  Example on real data - when done it doesnt really look right
# We have imported your gradient_descent() function. Call it with parameters:

# X
# y
# num_iterations of 1000
# learning_rate of 0.0001
# Store the result in variables called b and m.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Create a list called y_predictions. Set it to be every element of X multiplied by m and added to b.

# The easiest way to do this would be a list comprehension:

# new_y = [element*slope + intercept for element in y]
# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Plot X vs y_predictions on the same plot as the scatterplot.

# Does the line look right?


import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

plt.plot(X, y, 'o')
#plot your line here:
b, m = gradient_descent(X,y,num_iterations=1000,learning_rate=0.0001)
plt.show()

y_predictions = [m*x+b for x in X]

plt.plot(X,y_predictions)
plt.show()



###  all above built a linear regression algorithm from scratch
##  skikit-learn from sklern library does it all for you using LinearRegression() function
# he num_iterations and the learning_rate that you learned about in your own implementation have default values within 
# scikit-learn, so you don’t need to worry about setting them specifically!
from sklearn.linear_model import LinearRegression


line_fitter = LinearRegression()
line_fitter.fit(X, y)
# The .fit() method gives the model two variables that are useful to us:

# the line_fitter.coef_, which contains the slope
# the line_fitter.intercept_, which contains the intercept
# We can also use the .predict() function to pass in x-values and receive the y-values that this line would predict:

y_predicted = line_fitter.predict(X)

# We have imported a dataset of soup sales data vs temperature.

# Run the code to see the scatterplot. Can you envision the line that would fit this data?

# Checkpoint 2 Passed
# 2.
# Create an sklearn linear regression model and call it line_fitter.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Fit the line_fitter object to temperature and sales.

# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Create a list called sales_predict that is the predicted sales values that line_fitter would generate from the temperature list.

# Checkpoint 5 Passed

# Stuck? Get a hint
# 5.
# Plot sales_predict against temperature as a line, on the same plot as the scatterplot.

import codecademylib3_seaborn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression()
line_fitter.fit(temperature,sales)
sales_predict = line_fitter.predict(temperature)

plt.plot(temperature,sales_predict)
plt.plot(temperature, sales, 'o')
plt.show()










