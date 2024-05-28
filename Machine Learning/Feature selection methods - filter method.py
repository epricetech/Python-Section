# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:52:45 2023

@author: geron
"""

import pandas as pd
 
df = pd.DataFrame(data={
    'edu_goal': ['bachelors', 'bachelors', 'bachelors', 'masters', 'masters', 'masters', 'masters', 'phd', 'phd', 'phd'],
    'hours_study': [1, 2, 3, 3, 3, 4, 3, 4, 5, 5],
    'hours_TV': [4, 3, 4, 3, 2, 3, 2, 2, 1, 1],
    'hours_sleep': [10, 10, 8, 8, 6, 6, 8, 8, 10, 10],
    'height_cm': [155, 151, 160, 160, 156, 150, 164, 151, 158, 152],
    'grade_level': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    'exam_score': [71, 72, 78, 79, 85, 86, 92, 93, 99, 100]
})
 
print(df)

#  goal is to predict how each student will perform on the exam.  so target variable is exam_score and rest are features
# 10 x 6 features matrix
#We’ll prepare the data by separating the features matrix (X) and the target vector (y):
X = df.drop(columns=['exam_score'])
print(X)
# 10 x 1 target vector
y = df['exam_score']
print(y)


#  Variance Threshold - to remove any features that have little to no variation in their values.  
#  edu_goal is only feature not numeric - this will get rid of it.  
X_num = X.drop(columns=['edu_goal'])
 
print(X_num)

#  now we can used the VarianceThreshold from scikit-learn to help remove low-variance features from x_num.
#by defualt it drops all features with 0 variance but you can adjust with threshold paramater
# anf .fit_transform() method returns the filtered features as a numby array

from sklearn.feature_selection import VarianceThreshold
 
selector = VarianceThreshold(threshold=0)  # 0 is default
 
print(selector.fit_transform(X_num))


#VarianceThreshold offers another method called .get_support() that can return the indices of the selected features, 
#which we can use to manually subset our numeric features DataFrame:

# Specify `indices=True` to get indices of selected features
print(selector.get_support(indices=True))

# Use indices to get the corresponding column names of selected features
num_cols = list(X_num.columns[selector.get_support(indices=True)])
 
print(num_cols)

# Subset `X_num` to retain only selected features
X_num = X_num[num_cols]
 
print(X_num)


#  finally obtain our entire features datafram including the categorical column the edu_goal we removed earlier

X = X[['edu_goal'] + num_cols]
 
print(X)



#  Pearsons correlation - involves finding the correlation between variables - useful for measureing the linear
#  relationship between 2 numeric, continuous variables - a coefficient close to 1 represents a positive correlation,
#  a -1 represents a negative correlation and 0 represents no correlation.  
#  pearsons correlation coefficent cannot be calculated for categorical variables.  

#  to find which variables are correlated with one andother we can use the .corr() mehtong and the method paramater

import matplotlib.pyplot as plt
import seaborn as sns
 
corr_matrix = X_num.corr(method='pearson')  # 'pearson' is default
 
sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r')
plt.show()

# Let’s define high correlation as having a coefficient of greater than 0.7 or less than -0.7. 
#We can loop through the correlation matrix to identify the highly correlated variables:
# Loop over bottom diagonal of correlation matrix
for i in range(len(corr_matrix.columns)):
    for j in range(i):
 
        # Print variables with high correlation
        if abs(corr_matrix.iloc[i, j]) > 0.7:
            print(corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j])




#  correlation between feature and target
#  in peasons correlation its usefull to fit a linear model wich assumes a linear relationshi between target and predictor variables
#  if a feature is not very correlated with the target variable  like between -0.3 and 0.3then it may not 
#be very predictive and can potentiallybe filtered out.  
#  We can use the .corr() method to obtain the rorrelation between the target variable and the rest of the features.  
# Example first you need to creae a new dataframe containing the numeric features with the exam score column

X_y = X_num.copy()
X_y['exam_score'] = y
 
print(X_y)

#  then we generate the correlation matric and isolate the column corresponding to the trarget variable and see how strong
# the feature correlates with it
corr_matrix = X_y.corr()
 
# Isolate the column corresponding to `exam_score`
corr_target = corr_matrix[['exam_score']].drop(labels=['exam_score'])
 
sns.heatmap(corr_target, annot=True, fmt='.3', cmap='RdBu_r')
plt.show()



#  alternative approach for assessing the correlation between variables.  Instead of generating the full correlation matrix
#  we could use f_regression() funnction to find the F-stat for a model with each predictor on its own
#  the f-stat will be larger and the p-value will be smaller for predictors that are more highly correlated
from sklearn.feature_selection import f_regression
 
print(f_regression(X_num, y))


#  Mutual information - used to rank and select top features - it measures the dependency between 2 variables and can
#  detect more than just linear correlation.  Use the LabelEncoder() function


from sklearn.preprocessing import LabelEncoder
 
le = LabelEncoder()
 
# Create copy of `X` for encoded version
X_enc = X.copy()
X_enc['edu_goal'] = le.fit_transform(X['edu_goal'])
 
print(X_enc)


#  now we compute the mutual information between each feature and using mutual_info_regression()

from sklearn.feature_selection import mutual_info_regression
 
print(mutual_info_regression(X_enc, y, random_state=68))



#  in order to properly calculate the nutual information we need to tell the mutual_info_regression() which features
# are discrete by providing their index using discrete_features parameter


print(mutual_info_regression(X_enc, y, discrete_features=[0], random_state=68))


#  finally we have SelectKBest funcion to pick out the top k feautrs with the highest ranked scores.  


from sklearn.feature_selection import SelectKBest
from functools import partial
 
score_func = partial(mutual_info_regression, discrete_features=[0], random_state=68)
 
# Select top 3 features with the most mutual information
selection = SelectKBest(score_func=score_func, k=3)
 
print(selection.fit_transform(X_enc, y))


X = X[X.columns[selection.get_support(indices=True)]]
 
print(X)










