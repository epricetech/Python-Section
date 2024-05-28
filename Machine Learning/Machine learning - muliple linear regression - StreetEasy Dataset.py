# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:09:02 2023

@author: geron
"""

# It has the following columns:

# rental_id: rental ID
# rent: price of rent in dollars
# bedrooms: number of bedrooms
# bathrooms: number of bathrooms
# size_sqft: size in square feet
# min_to_subway: distance from subway station in minutes
# floor: floor number
# building_age_yrs: building’s age in years
# no_fee: does it have a broker fee? (0 for fee, 1 for no fee)
# has_roofdeck: does it have a roof deck? (0 for no, 1 for yes)
# has_washer_dryer: does it have washer/dryer in unit? (0/1)
# has_doorman: does it have a doorman? (0/1)
# has_elevator: does it have an elevator? (0/1)
# has_dishwasher: does it have a dishwasher (0/1)
# has_patio: does it have a patio? (0/1)
# has_gym: does the building have a gym? (0/1)
# neighborhood: (ex: Greenpoint)
# borough: (ex: Brooklyn)

#  3 datasets csv files - queens, brooklyn,manhattan  downoaded csv files but this is converting an url into the df

import codecademylib3_seaborn
import pandas as pd

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/queens.csv")

df = pd.DataFrame(streeteasy)

print(df.head())


#  Training Set VS Test Set
# 1.Training set - the data used to fith the model
# 2. Test Set - The data partitioned away at the very start of the experiment (to provide an unbiased evalution of the model)
#  in general putting 80% of your data in the training set and 20% of your data in the test set

#  Example suppose you have some values in x and some in y
from sklearn.model_selection import train_test_split
 x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

# here are the parameters:

# train_size: the proportion of the dataset to include in the train split (between 0.0 and 1.0)
# test_size: the proportion of the dataset to include in the test split (between 0.0 and 1.0)
# random_state: the seed used by the random number generator [optional]

import codecademylib3_seaborn
import pandas as pd

# import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

from sklearn.model_selection import train_test_split

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
 
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, test_size=0.2,random_state=6)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


###  Above creates out tests amd training sets now below steps will do the multiple linear regreassion in scikit-learn
#  The steps are identical to that of a simple linear regreassion
#  first you use  
from sklern.linear_model import LinearRegression
#  then create you model with  
model = LinearRegression()
#  Then create your x_train and y_train to fit   
model.fit(x_train,y_train)
##  then use predict() to pass in the x values and return the y_values 
y_predicted = model.predict(x_test)
# takes values calculated by `.fit()` and the `x` values, plugs them into the multiple linear regression equation, 
#and calculates the predicted y values. 


#  Full example of creating dataset, making dependent and mulitple independent variables - creating tha training and test set

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split


streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

# Add the code here:
from sklearn.linear_model import LinearRegression
mir = LinearRegression()
mir.fit(x_train,y_train)
y_predict = mir.predict(x_test)


##  not to visualize these splits using matplotlib and scatter()
# Create a scatter plot
# plt.scatter(x, y, alpha=0.4)
 # # Create x-axis label and y-axis label
# plt.xlabel("the x-axis label")
# plt.ylabel("the y-axis label")
# # Create a title
# plt.title("title!")
# # Show the plot
# plt.show()

#  example 
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

lm = LinearRegression()

model=lm.fit(x_train, y_train)

y_predict = lm.predict(x_test)


plt.scatter(y_test,y_predict)
plt.xlabel('Rent Prices')
plt.ylabel('Predicted Prices')
plt.title('Rental Prices')
plt.show()

##  with the multiple linear regression formula
##  y = b + m1x1 + m2x2 + m3x3 and so of for each independent variable
#  b = the intercept that you want to find and m refers to the coefficients  
#  we use LinearRegression and .fit() which gives the model 2 variables that are useful
#  1.  .coef_ - contains the coeffiecients - helpful to see what independent variables carries the most weight
#  2.  .intercept - which contains the intercept


#  example of .coef_
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

mlr = LinearRegression()

model = mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

# Input code here:

print(mlr.coef_)



#  Correlations - Interpreting graphs and seeing which coeefficents have positive and negative effects on the dependent
# variable
#  example manhatten model has 14 independent variables which also means it has 14 coeffiecents.
#  Independted Variables have 3 possible relationships to the dependent variaable
# 1.  a positive linear relationship - means as the x value increases so does the y value - generally seen in an upward trend
# 2.  a negative linear relationship - means as the x value increases the y value decreases - seen in a downward trend
# 3.  no relationship.    


import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

# Input code here:
plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4)
plt.scatter(df[['min_to_subway']],df[['rent']], alpha=0.4)


plt.show()



#  Evaluating the models accuracy
#  One Technique is Residual Analysis
#  the residual e is the difference between the actual value y and the predicted value y
#   e = y - y_predict
#  LinearRegression() comes with a .score() method that returns the coefficient of the determination r^2 of the prediction
#  formual  1 - u/v  - where u is the resicual sum of squares
((y - y_predict) ** 2).sum()
#  and v is the total sum of squares
((y - y.mean()) ** 2).sum()

#  example of .score
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

mlr = LinearRegression()

model=mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

# Input code here:
print(model.score(x_train, y_train))

print(model.score(x_test, y_test))

















