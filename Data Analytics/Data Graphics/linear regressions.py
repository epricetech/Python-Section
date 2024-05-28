# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:11:30 2023

@author: geron
"""

#  linear regression - modeling technique to understand relationship between quantitative vairable and one or more variables
#  example like is there a relationship between apt size and rent in NY

# creates a scatter plot and a linear line through scatter plot
# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('test_data.csv')

# Write equation for a line
y = 9.85 * students.hours_studied + 43

# Create the plot here: 
plt.scatter(students.hours_studied, students.score)

plt.plot(students.hours_studied, y)
plt.show()

# x is 10 and y is 45
# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('test_data.csv')

# Write equation for a line
predicted_score = 10 * students.hours_studied + 45

# Create the plot
plt.scatter(students.hours_studied, students.score)
plt.plot(students.hours_studied, predicted_score)
plt.show()


# linear regression in python uses OLS.from_formulat() function from the statsmodels.api
# if we have 2 columns weight and height this will predeict weight based on height.  
#  Weight is the outcome variable and height is the predictor.  
model = sm.OLS.from_formula('weight ~ height', data = body_measurements)
#  then we fith the model using .fit()
results=models.fit()
# then we can print full summary using print(results.suppary())
# weill only look at the coeffiecients
print(results.params)
#output  - tells the best fit intercept is -21.67 and the best fit slope is .50
# Intercept   -21.67
# height        0.50
# dtype: float64




# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Create the model here:
model = sm.OLS.from_formula('score ~ hours_studied', data=students)
# Fit the model here:
results = model.fit()
# Print the coefficients here:
print(results.params)
#output
# Intercept        43.016014
# hours_studied     9.848111
# dtype: float64



# using a regression model for prediction
model = sm.OLS.from_formula('weight ~ height', data = body_measurements)
results = model.fit()
print(results.params)
#output
# Intercept   -21.67
# height        0.50
# dtype: float64

# to make a prediction we meed to plug in the intercept and slope into our equation for a line for example above
#  equation   Weight = .5 * height - 21.67
#In python, we can calculate this by plugging in values or by accessing the intercept and slope from results.
#params using their indices (0 and 1, respectively):
print(0.50 * 160 - 21.67) 
# Output: 58.33
 
# OR:
 
print(results.params[1]*160 + results.params[0])
# Output: 58.33


#  can also use the .predict() method to do the same as last 2 formulas
newdata = {"height":[160]}
print(results.predict(newdata))
#output
# 0      58.33
# dtype: float64



# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Print the model params
print(results.params)
# Output:
# Intercept        43.016014
# hours_studied     9.848111
# Calculate and print `pred_3hr` here:
pred_3hr = results.params[1] * 3 + results.params[0]
print(pred_3hr)
# output
# dtype: float64
# 72.56034698735526

# Calculate and print `pred_5hr` here:
newdata = {'hours_studied': [5]}
pred_5hr = results.predict(newdata)
print(pred_5hr)
#output
# dtype: float64
# 0    92.256569
# dtype: float64



#  finding fitted values for linear regression
fitted_values = results.predict(body_measurements)
print(fitted_values.head())
#output
# 0    66.673077
# 1    59.100962
# 2    71.721154
# 3    70.711538
# 4    65.158654
# dtype: float64



# find the residuals for linear reression
residuals = body_measurements.weight - fitted_values
print(residuals.head())
# Output:

# 0   -2.673077
# 1   -1.100962
# 2    3.278846
# 3   -3.711538
# 4    2.841346
# dtype: float64



# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Calculate `fitted_values` here:
fitted_values = results.predict(students)

# Calculate `residuals` here:
residuals = students.score - fitted_values
# Print the first 5 residuals here:
print(residuals.head(5))

# #output  - positive means they scored higher than predicted and negative they scored lower
# 0     3.894086
# 1     8.806731
# 2   -12.236291
# 3     5.827009
# 4    10.096631
# dtype: float64



# steps after finding fitted and residuals
#  these steps are for normality and homoscedasticity
# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()
print(results.params)
# Calculate fitted values
fitted_values = results.predict(students)

# Calculate residuals
residuals = students.score - fitted_values

# Plot a histogram of the residuals here:
plt.hist(residuals)

plt.show()
plt.clf()

# Plot the residuals against the fitted vals here:
plt.scatter(fitted_values, residuals)

plt.show()


#  categorical predictors and linear regressions

# Calculate group means
print(data.groupby('play_bball').mean().height)
# Output:

# play_bball
# 0	169.016
# 1	183.644

# Create scatter plot
plt.scatter(data.play_bball, data.height)
 
# Add the line using calculated group means
plt.plot([0,1], [169.016, 183.644])
 
# Show the plot
plt.show()



# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('test_data.csv')

# Calculate group means
print(students.groupby('breakfast').mean().score)

# Create the scatter plot here:
plt.scatter(students.breakfast,students.score)
#output
# 0	61.66415094339621
# 1	73.7212765957447
# Add the additional line here:
plt.plot([0,1], [61.6, 73.2])

# Show the plot
plt.show()


# categorical predictors fit and interpretation
#  uses the statsmodels.api.ols.from_formula() the same way quantitative predictor

model = sm.OLS.from_formula('height ~ play_bball', data)
results = model.fit()
print(results.params)
# Output:

# Intercept     169.016
# play_bball     14.628
# dtype: float64

# Note that this will work if the play_bball variable is coded with 0s and 1s, but it will also work if it is 
# coded with Trues and Falses, or even if it is coded with strings like 'yes' and 'no' (in this case, the 
# coefficient label will look something like play_bball[T.yes] in the params output, indicating that 'yes' 
# corresponds to a 1).



# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Calculate and print group means
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)

# Fit the model and print the coefficients
model = sm.OLS.from_formula('score ~ breakfast', students)
results = model.fit()
print(results.params)

# Calculate and print the difference in group means
print(mean_score_breakfast - mean_score_no_breakfast)


# Output:
# Mean score (no breakfast):  61.664150943396216
# Mean score (breakfast):  73.72127659574468
# Intercept    61.664151
# breakfast    12.057126
# dtype: float64
# 12.057125652348468


















