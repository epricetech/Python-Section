# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:19:08 2023

@author: geron
"""

#  Logisitic Regression - predicts the probability, ranging from 0 to 1 of a datapoint belonging to a specific
# category or class - these probabilities can be used to assign, or classify observations to the more probable group
#  #  if we only have 2 groups that is called binary classification - example spam or not spam

## example of how many kids passed or failed exam  1 = passed and 0 is failes based on hours studied
#  the graph shows points points along the hours studied axis at 0 and 1.  Easily shows if you studied you passed
import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt
codecademyU = pd.read_csv('codecademyU.csv')

# Scatter plot of exam passage vs number of hours studied
plt.scatter(x = 'hours_studied', y = 'passed_exam', data = codecademyU, color='black')
plt.ylabel('passed/failed')
plt.xlabel('hours studied')

plt.show()


#  linear regression approach
#  formual  y = b0 + b1x1 + b2x2 and so on and so forth
#  b0 is the intercept of the regression line
#  b1 b2 b3 ect are the coefficents
#  x1 x2 x3 ect are the predictors or also called features.  
#  for a logistic regression the y value is either 1 or 0 
#  this approach of linear model doesnt always fit the data well.  and doesnt fix classification problem


#  example code of a logistic scatter plot and a linear regression model line - the variables slacker average and studious
#  are based on where that line crosses the scatterplot


import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
codecademyU = pd.read_csv('codecademyU.csv')

# Define slacker, average, and studious below
slacker = -.2
average = 0.5
studious = 1.75

# Fit a linear model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(codecademyU[['hours_studied']],codecademyU[['passed_exam']])

# Get predictions from the linear model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
predictions = model.predict(sample_x)

# Plot the data
plt.scatter(x = 'hours_studied', y = 'passed_exam', data = codecademyU, color='black', s=100)

# Plot the line
plt.plot(sample_x, predictions, color='red', linewidth=3)

# Customization for readability
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.axhline(y=0, color='k', linestyle='--')
plt.axhline(y=1, color='k', linestyle='--')

# Label plot and set limits
plt.ylabel('outcome (1=passed, 0=failed)', fontsize = 15)
plt.xlabel('hours studied', fontsize = 15)
plt.xlim(-16.65, 33.35)
plt.ylim(-.3, 1.8)

# Show the plot
plt.tight_layout()
plt.show()



#  Logistic Regression is the solution
#  to build a logistic model we apply a logit link function to the left hand side of our linear regression function
#  logistic formulat  ln(y/1-y) = b0 + b1x1 + b2x2 and so on and so forth  -  this keeps the line between the 2 clssifications
#  of the value being either 1 or 0
#  example code
mport codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
codecademyU = pd.read_csv('codecademyU.csv')

# Define five_hour_studier below
five_hour_studier = 0.0
# Fit the logistic regression model
hours_studied = codecademyU[['hours_studied']]
passed_exam = codecademyU[['passed_exam']]
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(hours_studied,passed_exam)

# Plug sample data into fitted model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict_proba(sample_x)[:,1]

# Plot exam data
plt.scatter(hours_studied, passed_exam, color='black', s=100)

# Plot logistic curve
plt.plot(sample_x, probability, color='red', linewidth=3)

# Customization for readability
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.axhline(y=0, color='k', linestyle='--')
plt.axhline(y=1, color='k', linestyle='--')

# Label plot and set limits
plt.ylabel('probability passed', fontsize = 30)
plt.xlabel('hours studied', fontsize = 30)
plt.xlim(-1, 25)
plt.tight_layout()

# Show the plot
plt.show()



##  Log-Odds -  it is the left side of the logistic regression formula.  odds can only be a positive number
## ln = p(event occuring) / 1 - p(event occuring)
#  Example odds of passing = 0.7 / 1-0.7 = 2.33     the 1-0.7 can also be .30

import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Calculate odds_of_rain
odds_of_rain = 0.4 / 0.6


# Calculate log_odds_of_rain

log_odds_of_rain = np.log(odds_of_rain)

# Calculate odds_on_time
odds_on_time = 0.9 / 0.1


# Calculate log_odds_on_time
log_odds_on_time = np.log(odds_on_time)




##  Sigmoid Function - inverse of the logit function - sigmoid produces the s-shaped curve in the graph
#  example want to find out whether a vistor to a  website will make a purchase and we will use number of minutes as a predictor
#  first fit the model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(purchase, min_on_site)
# then use the right hand side of equation  to make predictions for eachof our datapoiints
log_odds = model.intercept_ + model.coef_ * min_on_site 
print(log_odds)
# output is - these are log odds
# [[-3.28394203]
#  [-1.46465328]
#  [-0.02039445]
#  [ 1.22317391]
#  [ 2.18476234]]

#  then we turn log odds into a probability simultaneously for all data points
np.exp(log_odds)/(1+ np.exp(log_odds))
#  output is 
# array([[0.0361262 ],
#        [0.18775665],
#        [0.49490156],
#        [0.77262162],
#        [0.89887279]])


#  a full example of sigmoid function
# Import libraries and data
import pandas as pd
import numpy as np
codecademyU = pd.read_csv('codecademyU.csv')

# Fit the logistic regression model
hours_studied = codecademyU[['hours_studied']]
passed_exam = codecademyU[['passed_exam']]
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(hours_studied,passed_exam)

# Save intercept and coef
intercept = model.intercept_
coef = model.coef_

# Calculate log_odds here
log_odds = intercept + coef * hours_studied
print(log_odds)

# Calculate pred_probability_passing here
pred_probability_passing = np.exp(log_odds)/(1+np.exp(log_odds))
print(pred_probability_passing)



#  Fitting a model in sklern - using the LogisticRegression() function in sklerrn
#  create model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
#  fit model
model.fit(features, labels)


# The coefficients can be interpreted as follows:

# Large positive coefficient: a one unit increase in that feature is associated with a large increase in the log odds 
# (and therefore probability) of a datapoint belonging to the positive class (the outcome group labeled as 1)
# Large negative coefficient: a one unit increase in that feature is associated with a large decrease in the log 
# odds/probability of belonging to the positive class.
# Coefficient of 0: The feature is not associated with the outcome.

#  example  - fitting a model and finding the intercept and coef
# Import pandas and the data
import pandas as pd
codecademyU = pd.read_csv('codecademyU_2.csv')

# Separate out X and y
X = codecademyU[['hours_studied', 'practice_test']]
y = codecademyU.passed_exam

# Transform X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)

# Create and fit the logistic regression model here:
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train,y_train)

# Print the intercept and coefficients here:
print(cc_lr.intercept_)
print(cc_lr.coef_)



# Predictions in sklearn using the .predict() fucntion - lets us see what group they are in either 1 or 0
#  We can also use the .predict_proba() method to predict probability of group membership 
print(model.predict(features))
# Sample output: [0 1 1 0 0]
#  the predict_proba returns the probability of class membership for both possible groups. 
print(model.predict_proba(features)[:,1])
# Sample output: [0.32 0.75  0.55 0.20 0.44]  - if greated than .5 then it is a 1 which is called the threshold


#  example
# Import pandas and the data
import pandas as pd
codecademyU = pd.read_csv('codecademyU_2.csv')

# Separate out X and y
X = codecademyU[['hours_studied', 'practice_test']]
y = codecademyU.passed_exam

# Transform X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)

# Create and fit the logistic regression model here:
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train,y_train)

# Print out the predicted outcomes for the test data
print(cc_lr.predict(X_test))

# Print out the predicted probabilities for the test data
print(cc_lr.predict_proba(X_test)[:,1])
# Print out the true outcomes for the test data
print(y_test)
#  output
# [0 1 0 1 1]
# [0.32065927 0.7931881  0.05547483 0.57747928 0.87070434]
# 7     0
# 15    1
# 0     0
# 11    0
# 17    1
# Name: passed_exam, dtype: int64



#  classification thresholding - once we have used logistic regression to predict the probability of group membership
#  we then need to make a decision about what class a datapoint belongs too - this is classification thresholding
#  default for sklearn is 0.5 and if the datapoint is equal or greater then it belongs to the positive class
#  We can change the threshold.  the lower you go the more sensitive your model predictions are.  

#  in this example the 4th result the .5777 probability is misclassified.  Change alternative threshold higher to put it
# in the right class without effecting the others
# Pick an alternative threshold here:
alternative_threshold = 0.6
# Import pandas and the data
import pandas as pd
codecademyU = pd.read_csv('codecademyU_2.csv')

# Separate out X and y
X = codecademyU[['hours_studied', 'practice_test']]
y = codecademyU.passed_exam

# Transform X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)

# Create and fit the logistic regression model here:
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train,y_train)

# Print out the predicted outcomes for the test data
print(cc_lr.predict(X_test))

# Print out the predicted probabilities for the test data
print(cc_lr.predict_proba(X_test)[:,1])

# Print out the true outcomes for the test data
print(y_test)

# output
# [0 1 0 1 1]
# [0.32065927 0.7931881  0.05547483 0.57747928 0.87070434]
# 7     0
# 15    1
# 0     0
# 11    0
# 17    1
# Name: passed_exam, dtype: int64



#  Confusion Matrix - A way to evaluate our model - Confusion matrix shows us the numbers of
# 1. True positives
# 2. false positives
# 3 true negatives
# 4  false negatives
#example
#  suposed these were the results of or logistic regression model
y_true = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
y_pred = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
#  we create a confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_true, y_pred))
# output
# array([[3, 2],
#        [1, 4]])
# which tells us there are 3 true negatives - 1 false negative - 4 true positives and 2 fals positives
#  ideally we want the numbers on the main diagonal (in this case 3 and 4) with are true negatives and true positives to 
#  be as large as possible

#  example
# Import pandas and the data
import pandas as pd
codecademyU = pd.read_csv('codecademyU_2.csv')

# Separate out X and y
X = codecademyU[['hours_studied', 'practice_test']]
y = codecademyU.passed_exam

# Transform X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)

# Create and fit the logistic regression model here:
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train,y_train)

# Save and print the predicted outcomes
y_pred = cc_lr.predict(X_test)
print('predicted classes: ', y_pred)

# Print out the true outcomes for the test data
print('true classes: ', y_test)

# Print out the confusion matrix here
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

# Output:
# predicted classes:  [0 1 0 1 1]
# true classes:  7     0
# 15    1
# 0     0
# 11    0
# 17    1
# Name: passed_exam, dtype: int64
# [[2 1]
#  [0 2]]


#  Accuracy, Recall, Precision, F1 Score
#  once we have our confusion matrix we can use 4 values to summarize the matrix
#  for the formulas the tp and tn and fp and fn stand for true positive true negative false positive false negative
# 1. Accuracy = (TP + TN) / (TP +FP + TN + FN)
# 2. Precision = TP / (TP + FP)
# 3. Recall = TP / (TP + FN)
# 4. F1 Score - weighted average of precision and recall  f1 = 2 * precision * recall / precision + recall
#  examples of all 4
# accuracy:
from sklearn.metrics import accuracy_score
print(accuracy_score(y_true, y_pred))
# output: 0.7
 
# precision:
from sklearn.metrics import precision_score
print(precision_score(y_true, y_pred))
# output: 0.67
 
# recall: 
from sklearn.metrics import recall_score
print(recall_score(y_true, y_pred))
# output: 0.8
 
# F1 score
from sklearn.metrics import f1_score
print(f1_score(y_true, y_pred))
# output: 0.73


#  example
# Import pandas and the data
import pandas as pd
codecademyU = pd.read_csv('codecademyU_2.csv')

# Separate out X and y
X = codecademyU[['hours_studied', 'practice_test']]
y = codecademyU.passed_exam

# Transform X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 51)

# Create and fit the logistic regression model here:
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train,y_train)

# Save and print the predicted outcomes
y_pred = cc_lr.predict(X_test)
print('predicted classes: ', y_pred)

# Print out the true outcomes for the test data
print('true classes: ', y_test)

# Print out the confusion matrix
from sklearn.metrics import confusion_matrix
print('confusion matrix: ')
print(confusion_matrix(y_test, y_pred))

# Print accuracy here:
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))

# Print F1 score here:
from sklearn.metrics import f1_score
print(f1_score(y_test, y_pred))

# Output
# predicted classes:  [0 1 1 0 0]
# true classes:  1     0
# 12    0
# 15    1
# 2     0
# 7     0
# Name: passed_exam, dtype: int64
# confusion matrix: 
# [[3 1]
#  [0 1]]
# 0.8
# 0.6666666666666666



#  more examples  - to look at assumptions of logistic regression
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler #not currently used
from scipy.stats import zscore #not needed but built in
#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})

print(df.head())

#imports/load data
predictor_var = ['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']
df.head()

#1.Print distinct diagnosis values and frequency in dataset
print(df.diagnosis.value_counts())

#2. Test if the number of unique IDs is equal to sample size, i.e. no repeated patients
unique_ids = df.id.nunique()==df.id.count()
print(unique_ids)

#3. At a maximum, there should be no more than the smallest class size divided by 10 number of features.
max_features = min(df.diagnosis.value_counts()/10)
print(max_features)


#4. Uncomment the code to see which features have extreme outliers:
sns.boxplot(data=np.log(df[predictor_var]+.01).apply(zscore))
plt.xticks(rotation=45);
plt.show()
plt.close()

#5. Uncomment the code to remove the samples with extreme fractal_dimensions_mean values:
q_hi  = df["fractal_dimension_mean"].quantile(0.99)
df_filtered = df[(df["fractal_dimension_mean"] < q_hi)]

#6. Run the boxplot again but with the filtered dataframe:
sns.boxplot(data=np.log(df_filtered[predictor_var]+.01).apply(zscore))
plt.xticks(rotation=45);
plt.show()
plt.close()



#  Assumptions of logistic regression
#  to test assumptions visually we can use Seaborns regplot with the paramater logistic=True and 
#  the x value as our feature of interest
#  if the condition is met the fit model will resemble a sigmoidal curve.  
#  Multicollinerity - meaning features should not be highly correlated.  Multicollinearity can cause the coefficents
#  and p values to be inaccurate.  

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 'perimeter_mean','area_mean', 'smoothness_mean', 'compactness_mean','concavity_mean', 'symmetry_mean', 'fractal_dimension_mean']
x = df[predictor_var]

#Compare the curves
sns.regplot(x= 'radius_mean', y= 'diagnosis', data= df, logistic= True,)
plt.show()
plt.close()
sns.regplot(x= 'fractal_dimension_mean', y= 'diagnosis', data= df, logistic= True)
plt.show()
plt.close()

#1 Uncomment the heatmap and identify the two features that are highly correlated with radius_mean.
plt.figure(figsize = (10,7))
sns.heatmap(x.corr(), annot=True)
plt.show()

#2. Identify the other highly correlated pair. Define an array called correlated_pair containing the two features you've identified.

correlated_pair = ['compactness_mean', 'concavity_mean']



#  scikit-learn module for logisic regression - will check our assumptions
#  first we set the Hyperparameters of our model which we refine later.
#  evaluation metrics - accuracy, precision, recall and f1score


import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean',]
outcome_var='diagnosis'
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=0, test_size=0.3)

#1. Fit a Logsitic Regression model with the specified hyperparameters
log_reg = LogisticRegression(penalty='none', fit_intercept=True)
print(log_reg.get_params())

#2. Fit the model to training data and obtain cofficient and intercept
log_reg.fit(x_train, y_train)
coefficients = log_reg.coef_
intercept = log_reg.intercept_

print('coefficeints: ', coefficients)
print('intercept: ', intercept)


#3. Calculate the accuracy, precision, recall, and f1-score on the testing data
y_pred = log_reg.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Test set accuracy:\t{accuracy}')
print(f'Test set precision:\t{precision}')
print(f'Test set recall:\t{recall}')
print(f'Test set f1-score:\t{f1}')

#4. Remove the comments from the following code block to print the confusion matrix
test_conf_matrix = pd.DataFrame(
   confusion_matrix(y_test, y_pred), 
 index=['actual no', 'actual yes'], 
  columns=['predicted no', 'predicted yes']
)
print(test_conf_matrix)

#output
# {'C': 1.0, 'class_weight': None, 'dual': False, 'fit_intercept': True, 'intercept_scaling': 1, 'l1_ratio': None, 'max_iter': 100, 'multi_class': 'auto', 'n_jobs': None, 'penalty': 'none', 'random_state': None, 'solver': 'lbfgs', 'tol': 0.0001, 'verbose': 0, 'warm_start': False}
# coefficeints:  [[ 1.07991529  0.28744917 30.96010078 29.97251648]]
# intercept:  [-30.15566409]
# Test set accuracy:	0.9064327485380117
# Test set precision:	0.8507462686567164
# Test set recall:	0.9047619047619048
# Test set f1-score:	0.8769230769230769
#             predicted no  predicted yes
# actual no             98             10
# actual yes             6             57




#  Prediction Tresholds

import pandas as pd
import numpy as np

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean',]
outcome_var='diagnosis'
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=0, test_size=0.3)


log_reg = LogisticRegression(penalty='none', fit_intercept=True,tol=0.0000001,solver='newton-cg')
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
y_pred_prob = log_reg.predict_proba(x_test)



#Using the predicted probabilities to get the predicted class
y_pred_class = (y_pred_prob[:,1]>0.5)*1.0
#1 Check if it's the same as y_pred
diff = np.array_equal(y_pred_class,y_pred)
print(diff)

## 2. Print the confusion matrix
print("Confusion Matrix: Threshold 50%")
cm_50 = confusion_matrix( y_test, y_pred_class)
print(cm_50)

##3 Confusion matrices for thresholds of 0.25 and 0.75
print("Confusion Matrix: Threshold 25%")
cm_25 = confusion_matrix(y_test, (y_pred_prob[:,1]>0.25)*1.0)
print(cm_25)

print("Confusion Matrix: Threshold 75%")
cm_75 = confusion_matrix(y_test, (y_pred_prob[:,1]>0.75)*1.0)
print(cm_75)

#4. Choosing the right threshold for a question

#Array of thresholds
thresh = np.linspace(0,1,100)
false_negatives = []

for t in thresh:
  cm = confusion_matrix(y_test, (y_pred_prob[:,1]>t)*1.0)
  false_negatives.append(cm[1][0])
thresh_choice = thresh[np.argmax(np.array(false_negatives)>=2)]
print(thresh_choice)




#  ROC Curve and AUC
#  when you change the threshold incrementally from 0 to 1 for each of these thresholds the TPR true positive rate
#  and the FPR false positive rate can be calculated and plotted.  The resulting curve these poins form is
#  known as the ROC or receiver operating characteristic and measures the probabilities
#  TPR = TP / TP + FN - is on the y axis   FPR = FP / TN + FP - is on the x-axis
#  AUC or area under the curve gives us a single metric for separability.  Tells us how well our model can distinguish 
#  between the 2 classes.  A AUC score close to 1 is near perfect where as 0.5 is close to random guessing

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean',]
outcome_var='diagnosis'
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=0, test_size=0.3)

log_reg = LogisticRegression(penalty='none', fit_intercept=True,tol=0.0000001,solver='newton-cg')
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
y_pred_prob = log_reg.predict_proba(x_test)
###################################################################
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, thresholds = roc_curve(y_test,y_pred_prob[:,1])
plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         label='ROC curve')
idx = list(range(len(thresholds)))[1::4]
for i in idx:
    plt.text(fpr[i], tpr[i], thresholds[i].round(2))

clf = DummyClassifier(strategy='most_frequent', random_state=0)
clf.fit(x_train, y_train)
roc_auc = roc_auc_score(y_test, clf.predict_proba(x_test)[:,1] )
fpr, tpr, thresholds = roc_curve(y_test, clf.predict_proba(x_test)[:,1])
plt.plot(fpr, tpr, color='navy',linestyle='--', label='Dummy Classifier (most frequent) \n (area = %0.2f)' % roc_auc)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.grid()
plt.legend(loc="lower right")
plt.show()

#1. Run the code

#2. Find ROC_AUC score and print it
roc_auc = roc_auc_score(y_test,y_pred_prob[:,1])
print(f'ROC AUC score: [roc_auc]')



#  class Imbalance - the key is to try and keep class distribution to a 50/50 split or can create bias
#  Positive Rate - Can be used to tell how balanced classes are - positivity rate is the rate of occurences for 
#  the positive class.  
#  Stratification - is when the data is sorted into subgroups to ensure a nearly equal class distribution in your
#  train and test sets.  - to help with imbalance especially when you split into train and test groups.  
#  after using stratification the train and test sets should have similar positivity rate.  
#  Undersampling/Oversampling - we can undersample the majority class or oversample the minority class. 
#For oversampling, repeated samples (with replacement) are taken from the minority class until the size is 
#equal to that of the majority class. This causes the same data to be used multiple times, giving a higher 
#weight to these samples. Alternatively, undersampling leaves out some of the majority class data to have the 
#same number of samples as the minority class, leaving fewer data to build the model. 
# Balance the Class Weight - paramater class_weight='balanced' will help with class imbalance.  This applies
# a weight inversely proportional to the class frequency.  Can increease the accuracy for smaller classes


from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve('y_test' , 'y_pred_prob'[:,1])
plt.plot('fpr', 'tpr')

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean']
outcome_var='diagnosis'

x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=6, test_size=0.3)

print('Train positivity rate: ')
print(sum(y_train)/y_train.shape[0])
print('Test positivity rate: ')
print(sum(y_test)/y_test.shape[0])

log_reg = LogisticRegression(penalty='none', max_iter=1000, fit_intercept=True, tol=0.000001)
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

recall = recall_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print('Recall and Accuracy scores')
print(recall, accuracy)

## 1. Stratified Sampling
x_train_str, x_test_str, y_train_str, y_test_str = train_test_split(df[predictor_var], df[outcome_var], random_state=6, test_size=0.3, stratify=df[outcome_var])

### 2. Stratified positivity rates
print('Stratified train positivity rate: ')
str_train_positivity_rate = sum(y_train_str)/y_train_str.shape[0]
print(str_train_positivity_rate)
print('Stratified test positivity rate: ')
str_test_positivity_rate = sum(y_test_str)/y_test_str.shape[0]
print(str_test_positivity_rate)


### 3. Model predictions after Stratified sampling 
log_reg.fit(x_train_str,y_train_str)
y_pred = log_reg.predict(x_test_str)
recall_str = recall_score(y_test_str,y_pred)
accuracy_str = accuracy_score(y_test_str,y_pred)

print('Stratified Sampling: Recall and Accuracy scores')
print(recall_str, accuracy_str)


### 4. Balanced Class Weights
log_reg_bal = LogisticRegression(penalty='none', max_iter=1000, fit_intercept=True, tol=0.000001, class_weight='balanced')

### 5. Model Predictions after balancing Class Weights
log_reg_bal.fit(x_train,y_train)
y_pred = log_reg_bal.predict(x_test)
recall_bal = recall_score(y_test,y_pred)
accuracy_bal = accuracy_score(y_test, y_pred)
print('Balanced Class Weights: Recall and Accuracy scores')
print(recall_bal)
print(accuracy_bal)

#output
# Train positivity rate: 
# 0.34673366834170855
# Test positivity rate: 
# 0.4327485380116959
# Recall and Accuracy scores
# 0.8783783783783784 0.9181286549707602
# Stratified train positivity rate: 
# 0.37185929648241206
# Stratified test positivity rate: 
# 0.3742690058479532
# Stratified Sampling: Recall and Accuracy scores
# 0.875 0.9239766081871345
# Balanced Class Weights: Recall and Accuracy scores
# 0.9054054054054054
# 0.9239766081871345








































