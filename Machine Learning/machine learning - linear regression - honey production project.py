# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:00:17 2023

@author: geron
"""

import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")


print(df.head(5))
#For now, we care about the total production of honey per year. Use the .groupby() method provided by pandas to get the mean of totalprod per year.
#Store this in a variable called prod_per_year.
prod_per_year = df.groupby('year').totalprod.mean().reset_index()

#Create a variable called X that is the column of years in this prod_per_year DataFrame.
#After creating X, we will need to reshape it to get it into the right format
X = prod_per_year['year']
X = X.values.reshape(-1,1)
#Create a variable called y that is the totalprod column in the prod_per_year dataset.
y = prod_per_year['totalprod']

#Using plt.scatter(), plot y vs X as a scatterplot. Display the plot using plt.show().Can you see a vaguely linear relationship between these variables?
plt.scatter(X,y)
plt.show()

#Create a linear regression model from scikit-learn and call it regr.  Use the LinearRegression() constructor from the linear_model module to do this.
regr = linear_model.LinearRegression()
#Fit the model to the data by using .fit(). You can feed X into your regr model by passing it in as a parameter of .fit().
#After you have fit the model, print out the slope of the line (stored in a list called regr.coef_) and the intercept of the line (regr.intercept_).
regr.fit(X,y)
print(regr.coef_[0])

#Create a list called y_predict that is the predictions your regr model would make on the X data.
y_predict = regr.predict(X)
#Plot y_predict vs X as a line, on top of your scatterplot using plt.plot().
plt.plot(X,y_predict)
plt.show()
#Our known dataset stops at the year 2013, so let’s create a NumPy array called X_future that is the range from 2013 to 2050
X_future = np.array(range(2013,2050))
X_future = X_future.reshape(-1, 1)
#You can think of reshape() as rotating this array. Rather than one big row of numbers, X_future is now a big column of numbers — there’s one number in each row.

#Create a list called future_predict that is the y-values that your regr model would predict for the values of X_future.
future_predict = regr.predict(X_future)

#Plot future_predict vs X_future on a different plot.
plt.plot(X_future,future_predict)
plt.show()