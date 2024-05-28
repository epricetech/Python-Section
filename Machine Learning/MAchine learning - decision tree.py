# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:10:03 2023

@author: geron
"""

#  sklern has a library for decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt


#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

#Loading the dataset
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])

## 1a. Take a look at the dataset
print(df.head())

## 1b. Setting the target and predictor variables
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']

## 1c. Examine the new features
print(X.columns)
print(len(X.columns))

## 2a. Performing the train-test split
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)

## 2b.Fitting the decision tree classifier
dt = DecisionTreeClassifier(max_depth=3, ccp_alpha=0.01,criterion='gini')
dt.fit(x_train, y_train)

## 3.Plotting the Tree
plt.figure(figsize=(20,12))
tree.plot_tree(dt, feature_names = x_train.columns, max_depth=5, class_names = ['unacc', 'acc'], label='all', filled=True)
plt.tight_layout()
plt.show()

#Two important concepts to note here are the following:

# The root node is identified as the top of the tree. This is notated already with the number of samples 
# and the numbers in each class (i.e. unacceptable vs. acceptable) that was used to build the tree.

# Splits occur with True to the left, False to the right. Note the right split is a leaf node i.e.,
#  there are no more branches. Any decision ending here results in the majority class. (The majority class here is unacc.)


# The root node is identified as the top of the tree. This is notated already with the number of samples 
# and the numbers in each class (i.e. unacceptable vs. acceptable) that was used to build the tree.
#  We’ve created a variable frac_acc to print the fraction of acceptable cars the tree was trained on. 
#  Calculate this from the root node of the tree.

# Checkpoint 2 Passed

# Hint
# According to the root node, the total number of samples is 1382. The number of cars that are in the class acc is 412. 
# Thus the fraction of acceptable cars would be:

# frac_acc = 412/1382
# 2.
# The first split occurs off the root node based on the boolean safety_low <=0.5. As this is a dummy variable, 
# a value of 1 indicates safety='low', 0 indicates safety<>'low'. Splits occur with True to the left, False to the right. 
# Note the right split is a leaf node (i.e. there are no more branches), so any decision ending here results 
# in the majority class. What is the predicted class of any vehicle with LOW safety?

# (We’ve created a variable low_safety_class to fill in the answer in the code editor.)

# Checkpoint 3 Passed

# Hint
# When safety_low is > 0.5, we see that the tree splits off to a leaf on the right resulting in the car 
# belonging to the unacc class. (This intuitively makes sense because we expect a car with a low safety 
#                                indicator to be less acceptable!)

# 3.
# Identify the final outcome of the decision tree for the sample with buying_vhigh=1, persons_2= 0, safety_low =0. 
# We’ve defined a variable called sample_class to fill in the correct answer.

# Checkpoint 4 Passed

# Hint
# Let’s traverse the tree from the root node. We have safety_low = 0, so we move to the left child node. 
# We have persons_2 = 0, which means we move down one more node to the left.
#  Now we have buying_vhigh = 1 which means we move down one level but to the right now, leaving us in class = unacc.

https://static-assets.codecademy.com/skillpaths/ml-fundamentals/decision_trees/decision_tree_cars.png


#  Gini impurity - formula to find impurity of a set of data points.  1 - (p2/1 + p2/2) = 1 - (p2/1 + (1 - p1)^2)

# Using the same decision tree from the previous exercise, notice that each node is labeled with a gini=, 
# which is the Gini impurity for the samples at that node. For the root node, calculate the Gini impurity 
# using the formula and confirm this matches the value listed on the node.

# Checkpoint 2 Passed

# Hint
# Observe that in the root node, there are 1382 samples with 412 acc and 970 unacc car classes, i.e.,
#  p1 is 412/1382 and p2 is 970/1382 here!

# 2.
# Confirm the Gini impurity for the bottom left node. Since this is a non-root node (either a leaf or a split node), 
# the Gini impurity is only calculated for the samples passing through this node, not the entire dataset – 
# hence the number of samples is 449, not 1382.


# Hint
# Use the same formula as above, but observe that the bottom left node has 449 samples with 96 acc and 353 unacc cars. 
# (So p1 = 96/449 and so on.)


gini_root = 1 - ((412/1382)**2 + (970/1382)**2)
print(f'Gini impurity root node : {gini_root}')


gini_bottom_left = 1 - ( (96/449)**2 + (353/449)**2 )
print(f'Gini impurity bottom left node : {gini_bottom_left}')


#  Decision tree information gain - our goal is to hve a low gini impurity in the leaves of the tree, but must figure
# our which features to split on in order to achieve this.  For find we calculate the information gain of
#  splitting the data on a certain feature.  Information gain measures the difference in the impurity of the data before 
#  and after the split

#1. Information gain at a pure node (i.e., node with no more branches!)
r = 0.5 #ratio of new split, could be anything
gini_pure_node = 0
gini_info_gain = r*gini_pure_node  + (1-r)*gini_pure_node 
print(f'Gini information gain pure node split safety_low >= .5 : {gini_info_gain}')

#2. Information gain at the 'persons_2' split
r_persons_2 = 604/912 #read ratio of the split from the tree!
gini_left_split = 0.434
gini_right_split = 0
gini_info_gain_persons_2 = r_persons_2*gini_left_split + r_persons_2*gini_right_split
print(f'Gini information gain node persons_2 : {gini_info_gain_persons_2}')




## The usual libraries, loading the dataset and performing the train-test split
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)

## Functions to calculate gini impurity and information gain

def gini(data):
    """calculate the Gini Impurity
    """
    data = pd.Series(data)
    return 1 - sum(data.value_counts(normalize=True)**2)
   
def info_gain(left, right, current_impurity):
    """Information Gain associated with creating a node/split data.
    Input: left, right are data in left branch, right banch, respectively
    current_impurity is the data impurity before splitting into left, right branches
    """
    # weight for gini score of the left branch
    w = float(len(left)) / (len(left) + len(right))
    return current_impurity - w * gini(left) - (1 - w) * gini(right)


# Create two DataFrames left and right that represent the y_train values that correspond to x_train['persons_2'] 
# being 0 and 1 respectively. Calculate the length of these DataFrames, store them as len_left and len_right, and print them.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# We’re now going to calculate the gini impurities corresponding to the overall training data and the left and right split.
#  To do so:

# Uncomment the line pertaining to calculating the gini impurity in the overall training data.
# For the gini value of the left node, create a variable gini_left and use the gini function to calculate the value.
# For the gini value of the right node, create a variable gini_right and use the gini function to calculate the value.
# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Before proceeding to calculate the information gain at this split, let’s consolidate what we’ve calculated in the previous checkpoints:

# There are 917 cars with a persons_2 value of 0 and 465 cars with persons_2 value of 1.
# The overall gini impurity of the training data is 0.4185. The gini impurity for the left split was 0.4949 
# and the gini impurity of the right split is 0.
# This means that the weighted impurity of this split is:

# 917/1382 (0.4949) + 465/1382 (0) = 0.3284
# The information gain for tree whose root node is persons_2 should be

# 0.4185 - 0.3284 =  0.0901
# Use the info_gain function to calculate the information gain corresponding to this split and store it as 
# info_gain_persons_2. Print it to check if it is indeed the expected value!

# Checkpoint 4 Passed

# Hint
# The inputs to the info_gain function as we’ve defined it are left, right and current_impurity. 
# current_impurity refers to the gini impurity of the root node.

# 4.
# We’ve now verified that splitting at a root node of persons_2 gives us a lesser information 
# gain than splitting at safety_low (0.0901 in comparison to 0.0918!). Verify the information gain 
# is the highest at the root node using the function info_gain and looping through ALL the features. 
# Uncomment the lines that pertain to this calculation to verify if the tree we’ve been working with so 
# far has the best possible root node!



#### -----------------------------------
## 1. Calculate sample sizes for a split on `persons_2`

left = y_train[x_train['persons_2']==0]
right = y_train[x_train['persons_2']==1]
len_left = len(left)
len_right = len(right)
print ('No. of cars with persons_2 == 0:', len_left)
print ('No. of cars with persons_2 == 1:', len_right)

## 2. Calculate gini impurities
gi = gini(y_train)
gini_left = gini(left)
gini_right = gini(right)

print('Left split gini impurity:', gini_left)
print('Right split gini impurity:', gini_right)

## 3.Information gain when using feature `persons_2`
info_gain_persons_2 = info_gain(left, right, gi)
print(f'Information gain for persons_2:', info_gain_persons_2)

## 4. Which feature split maximizes information gain?
info_gain_list = []
for i in x_train.columns:
    left = y_train[x_train[i]==0]
    right = y_train[x_train[i]==1]
    info_gain_list.append([i, info_gain(left, right, gi)])

info_gain_table = pd.DataFrame(info_gain_list).sort_values(1,ascending=False)
print(info_gain_table.iloc[0,:][0])
print(f'Greatest impurity gain at:{info_gain_table.iloc[0,:]}')
print(info_gain_table)




#  how a decision tree is built - Recursion
#  once we can find the best feature to split the dataset, we can repeat this proces again and again to create the 
#  full tree.  This is the recursive algorithm.  
#  in summary We start with every data point from the training set, find the best feature to split the data,
 # split the data based on that feature, and then recursively repeat the process again on each subset that was created 
 # from the split.  We’ll stop the recursion when we can no longer find a feature that results in any information gain. 
 #In other words, we want to create a leaf of the tree when we can’t find a way to split the data that makes purer subsets.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

def gini(data):
    """calculate the Gini Impurity
    """
    data = pd.Series(data)
    return 1 - sum(data.value_counts(normalize=True)**2)
   
def info_gain(left, right, current_impurity):
    """Information Gain associated with creating a node/split data.
    Input: left, right are data in left branch, right banch, respectively
    current_impurity is the data impurity before splitting into left, right branches
    """
    # weight for gini score of the left branch
    w = float(len(left)) / (len(left) + len(right))
    return current_impurity - w * gini(left) - (1 - w) * gini(right)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)

y_train_sub = y_train[x_train['safety_low']==0]
x_train_sub = x_train[x_train['safety_low']==0]

gi = gini(y_train_sub)
print(f'Gini impurity at root: {gi}')

info_gain_list = []
for i in x_train.columns:
    left = y_train_sub[x_train_sub[i]==0]
    right = y_train_sub[x_train_sub[i]==1]
    info_gain_list.append([i, info_gain(left, right, gi)])

info_gain_table = pd.DataFrame(info_gain_list).sort_values(1,ascending=False)
print(f'Greatest impurity gain at:{info_gain_table.iloc[0,:]}')




#  train and predict using scikit-learn 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)

## 1. Create a decision tree and print the parameters
dtree = DecisionTreeClassifier()
print(f'Decision Tree parameters: {dtree.get_params()}')

## 2. Fit decision tree on training set and print the depth of the tree
dtree.fit(x_train, y_train)
print(f'Decision tree depth: {dtree.get_depth()}')

## 3. Predict on test data and accuracy of model on test set
y_pred = dtree.predict(x_test)

print(f'Test set accuracy: {dtree.score(x_test,y_test)}') # or accuracy_score(y_test, y_pred)

# output
# Decision Tree parameters: {'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'gini', 'max_depth': None, 
#                            'max_features': None, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 
#                            'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 
#                            'min_weight_fraction_leaf': 0.0, 'presort': 'deprecated', 'random_state': None, 
#                            'splitter': 'best'}
# Decision tree depth: 11
# Test set accuracy: 0.9826589595375722




# visualize decision tree - with matplotlib and tree_plot 

import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

## Loading the data and setting target and predictor variables
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']

## Train-test split and fitting the tree
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.3)
dtree = DecisionTreeClassifier(max_depth=3)
dtree.fit(x_train, y_train)

## Visualizing the tree
plt.figure(figsize=(27,12))
tree.plot_tree(dtree)
plt.tight_layout()
plt.show()

## Text-based visualization of the tree (View this in the Output terminal!)
print(tree.export_text(dtree))

#  output
# |--- feature_19 <= 0.50
# |   |--- feature_12 <= 0.50
# |   |   |--- feature_7 <= 0.50
# |   |   |   |--- class: True
# |   |   |--- feature_7 >  0.50
# |   |   |   |--- class: False
# |   |--- feature_12 >  0.50
# |   |   |--- class: False
# |--- feature_19 >  0.50
# |   |--- class: False


#  review

import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep']=='unacc') #1 is acceptable, 0 if not acceptable
X = pd.get_dummies(df.iloc[:,0:6])
y = df['accep']

x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.3)

## 1. Two decision trees
dtree1 = DecisionTreeClassifier()
dtree2 = DecisionTreeClassifier(max_depth = 7)

## Fit first decision tree
dtree1.fit(x_train, y_train)
dtree1_depth = dtree1.get_depth()
print(f'First Decision Tree depth: {dtree1_depth}')

## Fit second decision tree
dtree2.fit(x_train, y_train)
dtree2_depth = dtree2.get_depth()
print(f'Second Decision Tree depth: {dtree2_depth}')

## 2. Calculate accuracy scores on test data for both trees

dtree1_score = dtree1.score(x_test, y_test)
print(f'Test set accuracy tree no max depth: {dtree1_score}')# or accuracy_score(y_test, y_pred)

dtree2_score = dtree2.score(x_test, y_test)
print(f'Test set accuracy tree max depth 7: {dtree2_score}')# or accuracy_score(y_test, y_pred)













