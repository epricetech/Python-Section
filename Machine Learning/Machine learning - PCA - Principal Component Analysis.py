# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 07:40:19 2023

@author: geron
"""

# PCA - Principal Component analysis
#  PCA is a technique where we can reduce the number of features in a dataset without losing any of the informaiton we have
#  Key aspect is to understand the importance of the data and how variance in that data.  
#  good variance in the data will indicate that they should be included in the dataset 
#  We can look at CV or Coefficient of varance to calculate the CV for each column
import numpy as np
 
#define function to calculate cv
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
 
print(df.apply(cv))

import numpy as np
import pandas as pd

# Load in new pizza dataset
df = pd.read_csv('pizza_new.csv')
df.head()

# Calculate coefficient of variance for every feature
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
print(df.apply(cv))

# Rank order of importance from highest to lowest (in a list)
importance_rank = ['amt_flour','amt_cheese','amt_tomatoes','total_customers','revenue']

# output
# revenue            0.019833
# total_customers    0.267750
# amt_flour          7.655968
# amt_tomatoes       0.764099
# amt_cheese         1.102769
# dtype: float64


# steps behind PCA
#  Step 1 isolcate Data Matrix aka dataset.  this matrix holds all the features that we are interested in
# will have columns that hold information like features and other columns that we want to predict aka labels
#  Step 2 - calculate the Covariance matrix - calculating how much a feature changes with changes in every other feature.
#  this can be calculated using ehe .cov() method
#  Step 3 - Matrix factorization - goal is to find a pair of smaller matricies whoes product would equal our covariance matrix
#  Another way of thinking is we want to find smaller matrix that captures the majority of our information
#  Important part are Elgenvectores - which are vectors(mathematical concept that have direction and magnitude) that do not
# change direction when a transformation is applied to them.  These elganvecotrs gives ua a direction to rotate the dataset
# in n-dimensional space so we can look at the entire dataset forma simplified perspective.  
#  the elganvalues are related to the relative variation described by each principal component. 

# Principal components - are a linear combination of all the input features from the original dataset.  By using elganvecors
# we can rotate our dataset fron n-dimensional space to 2-dimensional space for easier understand and analysis.
#  To illustrate this point, let’s return to our pizza dataset. We can observe the correlation between our revenue and total_customers features.

# sns.scatterplot(x='total_customers',
#     y='revenue',
#     data=df)
#We can see a positive correlation between these two features, and could use that information to guide any analysis we
# perform. We can also do correlation plots for every combination of features, like so:
#sns.pairplot(df)

#Each individual combination of features will have its own correlation and variance,
 # both of which provide valuable information about that relationship. When comparing two
 # features at a time, these relationships are more understandable. If we wanted to, however, 
 # look at all of the feature relationships and information at once, it would be very difficult to decipher, 
 # as we cannot visualize data in a 5-dimensional space.


# to pur our dataset into 2-dimensional space
from sklearn.decomposition import PCA
 
pca = PCA(n_components=2)
pca_array = pca.fit_transform(df)

# output
# array([[-2572.64663126,   -37.43225524],
#        [ -104.21066949,    31.54952593],
#        [ -521.0563251 ,   -54.19045713],
#        ...,
#        [ 1429.58053669,    -5.98229122],
#        [-3550.23561932,    23.8935932 ],
#        [ -481.85213117,   -34.14891261]])


#As we can see, by running PCA on our original dataset, we were able to take our 5 features and reduce the dimensions
#  down to 2 principal components. With 2 dimensions, we can now plot the data on a single scatterplot:

# sns.scatterplot(pca_array[:,0], pca_array[:,1])


#  implementing PCA in python

import pandas as pd
import codecademylib3

# Read the csv data as a DataFrame
df = pd.read_csv('./Dry_Bean.csv')

# Remove null and na values
df.dropna()

# 1. Print the DataFrame head
print(df.head())

# 2. Extract the numerical columns
data_matrix = df.drop(columns='Class')

# Extract the classes
classes = df['Class']

print(data_matrix)


# we use np.linalg.elg which performs the calculation for eigenvalues and eigenvecotrs
#  to implemnt in pythong we use the following syntax
# we generate a correlation matrix using .corr()
# then we use np.linalg.elg() to perfom the compostiion on the correlation matricx which gives us 2 values the eigenvalue and elgenvector

correlation_matrix = data_matrix.corr()
eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix).

#  example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import codecademylib3


data_matrix = pd.read_csv('./data_matrix.csv')

# 1. Use the `.corr()` method on `data_matrix` to get the correlation matrix 
correlation_matrix = data_matrix.corr()

## Heatmap code:
red_blue = sns.diverging_palette(220, 20, as_cmap=True)
sns.heatmap(correlation_matrix, vmin = -1, vmax = 1, cmap=red_blue)
plt.show()

# 2. Perform eigendecomposition using `np.linalg.eig` 
eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)

# 3. Print out the eigenvectors and eigenvalues
print('eigenvectors: ')
print(eigenvectors)

print('eigenvalues: ')
print(eigenvalues)

#output
# eigenvectors: 
# [[ 2.82457959e-01  2.45882017e-01 -6.14466787e-02 -3.15461931e-02
#   -9.13256234e-02 -3.66390029e-01  1.25044861e-01  7.17479179e-02
#    3.50665669e-02 -3.90419516e-01 -1.77686475e-01  5.44842282e-02
#    4.62948862e-02  6.55727948e-01  2.31435926e-01  1.33190280e-01]
#  [ 3.10891123e-01  1.79302922e-01 -1.88525952e-02 -4.24678975e-02
#    8.18198663e-02 -1.02508210e-02  8.15296990e-02  3.17295058e-02
#   -1.57501171e-01  3.44383066e-01  1.99453621e-01 -7.50549982e-01
#    3.17920275e-01  8.13901114e-02  1.46143834e-02  1.26584690e-02]
#  [ 3.25823976e-01  1.00756516e-01 -8.46919067e-02 -6.79308126e-03
#   -4.42163116e-02 -1.49091929e-02  1.18162546e-01 -2.00947006e-01
#   -3.52366452e-01  1.01996482e-01  1.73639683e-01  2.73549960e-02
#   -6.85301970e-01 -1.86251185e-01  3.46019419e-01  1.74431582e-01]
#  [ 2.36199383e-01  3.43460651e-01  7.50039030e-03 -6.12997105e-02
#   -4.29258549e-03 -2.78820146e-02 -6.23528140e-02  9.47252766e-02
#    4.14230636e-01  4.81150315e-01  4.73720994e-03  4.13935449e-01
#    2.58014714e-01 -1.83095641e-01  3.31749326e-01  1.55445404e-01]
#  [ 2.29298328e-01 -3.30844185e-01 -1.69058011e-01  5.36461191e-02
#   -2.47566532e-02  7.59699103e-02  3.67891855e-01 -5.29805906e-01
#    1.21518443e-01  2.08046178e-01 -5.40202985e-01 -3.34425477e-03
#    8.74672429e-02  2.66661426e-02 -1.23575705e-01  1.02810025e-01]
#  [ 2.31526055e-01 -3.19433875e-01 -1.63042022e-01  1.18388551e-01
#   -6.03039593e-02 -1.90427992e-01 -5.11031662e-01  4.09120604e-01
#   -3.22591880e-01  2.41533155e-01 -4.11402535e-01  3.41133220e-02
#   -2.23275476e-02  4.59487129e-05  1.47926798e-02 -4.23063140e-02]
#  [ 2.83199889e-01  2.44630067e-01 -5.36490752e-02 -3.09595575e-02
#   -8.91133649e-02 -3.69215707e-01  1.21178732e-01  6.45192756e-02
#    2.58278807e-02 -3.94275552e-01 -1.79002314e-01 -7.73945617e-02
#    1.02365543e-01 -6.48621711e-01 -2.24752670e-01 -1.30973874e-01]
#  [ 2.97483844e-01  2.22802185e-01 -4.99135477e-02 -3.24273855e-02
#   -2.19534105e-02 -3.35147364e-02 -6.30912872e-04 -3.40422281e-02
#   -1.66940989e-02  2.53700143e-01  1.96001889e-01  2.74139585e-01
#   -1.98496927e-01  2.66409059e-01 -6.75588995e-01 -3.32487857e-01]
#  [-5.98079606e-02  2.20619259e-01 -8.52582080e-02  9.48254269e-01
#    1.97598918e-01  5.10553897e-04  4.45929047e-02 -1.47000878e-02
#    6.00988144e-03 -8.95631344e-04 -2.77069112e-03 -4.38701370e-05
#    4.62379038e-04 -5.65700266e-05 -4.74695172e-06 -1.17646774e-06]
#  [-1.43016314e-01  1.03322337e-01 -7.38670228e-01 -4.95457556e-02
#   -2.82194373e-01  3.25692613e-01  3.09528792e-01  3.72834092e-01
#   -1.24670321e-02 -6.14713024e-03  8.92367231e-04  3.39336586e-04
#    5.39707165e-04 -7.67128823e-03 -2.11537089e-03 -1.38727447e-03]
#  [-2.48164811e-01  2.14805282e-01 -1.63325487e-01  6.74824148e-02
#   -6.48700706e-01 -1.73439085e-01 -4.16624414e-01 -4.61145752e-01
#    9.44150591e-03  7.30163366e-02  3.45701555e-02 -1.20891182e-01
#    4.96397316e-02  1.46685284e-02  1.89361431e-03  2.37532216e-03]
#  [-2.38378001e-01  3.28914360e-01  1.49700768e-01 -8.71555716e-02
#    5.85957324e-02  1.23232305e-02 -3.24244642e-02  1.67809467e-01
#    3.93833779e-02  1.17265401e-01 -3.22502975e-01 -1.53253508e-01
#   -2.54641355e-01  2.02577285e-03 -3.72516048e-01  6.52515603e-01]
#  [-2.21318903e-01 -3.32548514e-01 -3.26229309e-02  7.23303405e-02
#   -1.12907779e-01 -6.33211910e-01  2.93567734e-01  1.91922106e-01
#    3.36948538e-01  2.71583838e-01  2.00505414e-01 -1.28472846e-01
#   -2.30735279e-01  4.01059407e-03 -1.12850106e-02 -5.46798042e-03]
#  [-3.14624593e-01  1.29419241e-01  1.20076675e-01 -4.65438196e-02
#   -2.64141427e-02 -2.59245737e-01  3.54310851e-01 -3.19852488e-02
#   -6.59508821e-01  2.12589947e-01 -3.73372481e-02  2.97904717e-01
#    3.19900059e-01 -1.85035834e-02  1.46683913e-02  5.54470201e-03]
#  [-2.38983301e-01  3.27521662e-01  1.49570241e-01 -9.56788529e-02
#    6.22269463e-02  4.74498435e-02  8.31848115e-02  4.52594153e-02
#    9.00540674e-02  1.65952214e-01 -4.68319821e-01 -1.89335830e-01
#   -2.82232572e-01  4.61837471e-02  2.34064698e-01 -6.01334520e-01]
#  [-1.98009429e-01  1.00061082e-01 -5.36903055e-01 -2.10119897e-01
#    6.40371689e-01 -2.80088867e-01 -2.40046279e-01 -2.66748910e-01
#    2.97986049e-03 -3.46314997e-03  2.84785031e-02  9.79933869e-03
#    2.73100957e-03 -4.29724598e-03  1.03771345e-02  6.16002705e-04]]
# eigenvalues: 
# [8.87463018e+00 4.22895571e+00 1.28105028e+00 8.18252847e-01
#  4.38286865e-01 1.83961749e-01 1.11624116e-01 5.20132000e-02
#  8.26026072e-03 1.45388993e-03 1.05418870e-03 2.93982938e-04
#  1.48794566e-04 1.00102669e-05 1.78479176e-06 2.14611338e-06]


#  after performing PCA we want to know how useful the new features are we can do this with a scree plot which shows
# the proportion of informaiton described by each principal component

# The proportion of information explained is equal to the relative size of each eigenvalue:
info_prop = eigenvalues / eigenvalues.sum()
print(info_prop)

# to create a scree plot
plt.plot(np.arange(1,len(info_prop)+1),
         info_prop, 
         'bo-')
plt.show()

# From this plot, we see that the first principal component explains about 50% of the variation in the data, 
# the second explains about 30%, and so on.

# Another way to view this is to see how many principal axes it takes to reach around 95% of the total amount of
#  information. Ideally, we’d like to retain as few features as possible while still reaching this threshold.

# To do this, we need to calculate the cumulative sum of the info_prop vector we created earlier:
cum_info_prop = np.cumsum(info_prop)
# then plot
plt.plot(np.arange(1,len(info_prop)+1),
         cum_info_prop, 
         'bo-')
plt.hlines(y=.95, xmin=0, xmax=15)
plt.vlines(x=4, ymin=0, ymax=1)
plt.show()
#From this plot, we see that four principal axes account for 95% of the variation in the data.


# example - first graph shows the first point in top left corner then moving down till it flat lines for most of the axis
#  graph 2 is the oppoistite  it starts in the middle left side and goes to the top and flat lines above the top for majority of axis

import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt

eigenvalues = pd.read_csv('eigenvalues.csv')['eigenvalues'].values

# 1. Find the proportion of information for each eigenvector, which is equal to the eigenvalues divided by the sum of all eigenvalues
info_prop = eigenvalues / eigenvalues.sum()

## Plot the principal axes vs the information proportions for each principal axis

plt.plot(np.arange(1,len(info_prop)+1),info_prop, 'bo-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Axes')
plt.xticks(np.arange(1,len(info_prop)+1))
plt.ylabel('Percent of Information Explained')
plt.show()
plt.clf()

# 2. Find the cumulative sum of the proportions
cum_info_prop = np.cumsum(info_prop)

## Plot the cumulative proportions array

plt.plot(cum_info_prop, 'bo-', linewidth=2)
plt.hlines(y=.95, xmin=0, xmax=15)
plt.vlines(x=3, ymin=0, ymax=1)
plt.title('Cumulative Information percentages')
plt.xlabel('Principal Axes')
plt.xticks(np.arange(1,len(info_prop)+1))
plt.ylabel('Cumulative Proportion of Variance Explained')
plt.show()


#  Implementing PCA using scikit-learn using sklearn.decomposition.PCA
# Step 1 - Standardize the data matrix - done by subtracting the mean and dividing by the standard deviation of each column vector
mean = data.mean(axis=0)
sttd = data.std(axis=0)
data_standardized = (data - mean) / sttd
# Next step - perform eigendecomposition by fitting the standardized data.  Done by using components_ attribute and 
# the proportional sizes of the eigenvalues using the explained_variance_ratio_ attribute
pca = PCA()
components = pca.fit(data_standardized).components_
components = pd.DataFrame(components).transpose()
components.index =  data_matrix.columns
print(components)
var_ratio = pca.explained_variance_ratio_
var_ratio = pd.DataFrame(var_ratio).transpose()
print(var_ratio)


# example
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import codecademylib3

data_matrix = pd.read_csv('./data_matrix.csv')

# 1. Standardize the data matrix
mean = data_matrix.mean(axis=0)
sttd = data_matrix.std(axis=0)
data_matrix_standardized = (data_matrix - mean) / sttd
print(data_matrix_standardized.head())

# 2. Find the principal components
pca = PCA()
components =  pca.fit(data_matrix_standardized).components_
components = pd.DataFrame(components).transpose()
components.index =  data_matrix.columns
print(components)

# 3. Calculate the variance/info ratios
var_ratio = pca.explained_variance_ratio_
var_ratio = pd.DataFrame(var_ratio).transpose()
print(var_ratio)

# Output
#       Area  Perimeter  ...  ShapeFactor3  ShapeFactor4
# 0 -0.840718  -1.143277  ...      1.925653      0.838340
# 1 -0.829157  -1.013887  ...      2.689603      0.771110
# 2 -0.807128  -1.078789  ...      1.841288      0.916721
# 3 -0.785712  -0.977179  ...      2.204169     -0.197978
# 4 -0.781210  -1.097344  ...      3.013352      0.939605

# [5 rows x 16 columns]
#                        0         1         2   ...        13        14        15
# Area             0.282458  0.245882 -0.061447  ... -0.655728  0.133190  0.231436
# Perimeter        0.310891  0.179303 -0.018853  ... -0.081390  0.012658  0.014614
# MajorAxisLength  0.325824  0.100757 -0.084692  ...  0.186251  0.174432  0.346019
# MinorAxisLength  0.236199  0.343461  0.007500  ...  0.183096  0.155445  0.331749
# AspectRation     0.229298 -0.330844 -0.169058  ... -0.026666  0.102810 -0.123576
# Eccentricity     0.231526 -0.319434 -0.163042  ... -0.000046 -0.042306  0.014793
# ConvexArea       0.283200  0.244630 -0.053649  ...  0.648622 -0.130974 -0.224753
# EquivDiameter    0.297484  0.222802 -0.049914  ... -0.266409 -0.332488 -0.675589
# Extent          -0.059808  0.220619 -0.085258  ...  0.000057 -0.000001 -0.000005
# Solidity        -0.143016  0.103322 -0.738670  ...  0.007671 -0.001387 -0.002115
# roundness       -0.248165  0.214805 -0.163325  ... -0.014669  0.002375  0.001894
# Compactness     -0.238378  0.328914  0.149701  ... -0.002026  0.652516 -0.372516
# ShapeFactor1    -0.221319 -0.332549 -0.032623  ... -0.004011 -0.005468 -0.011285
# ShapeFactor2    -0.314625  0.129419  0.120077  ...  0.018504  0.005545  0.014668
# ShapeFactor3    -0.238983  0.327522  0.149570  ... -0.046184 -0.601335  0.234065
# ShapeFactor4    -0.198009  0.100061 -0.536903  ...  0.004297  0.000616  0.010377

# [16 rows x 16 columns]
#          0        1         2   ...            13            14            15
# 0  0.554664  0.26431  0.080066  ...  6.256417e-07  1.341321e-07  1.115495e-07

# [1 rows x 16 columns]


# projecting the data onto the principal axis
#  once we have done PCA and eigenvecots we can use them to project the data onto the first few principal axis.  
#  we can do this by using sklearn.decomposition.PCA
from sklearn.decomposition import PCA
 
# only keep 3 PCs
pca = PCA(n_components = 3)
 
# transform the data using the first 3 PCs
data_pcomp = pca.fit_transform(data_standardized)
 
# transform into a dataframe
data_pcomp = pd.DataFrame(data_pcomp)
 
# rename columns
data_pcomp.columns = ['PC1', 'PC2', 'PC3']
 
# print the transformed data
print(data_pcomp.head())

# once transformed we can look at a scatter plot 
sns.lmplot(x='PC1', y='PC2', data=data_pcomp, hue='species', fit_reg=False)
plt.show()



# example
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

data_matrix_standardized = pd.read_csv('./data_matrix_standardized.csv')
classes = pd.read_csv('./classes.csv')['Class']

# 1. Transform the data into 4 new features using the first PCs
pca = PCA(n_components=4)
data_pcomp = pca.fit_transform(data_matrix_standardized)
data_pcomp = pd.DataFrame(data_pcomp)
data_pcomp.columns = ['PC1', 'PC2', 'PC3', 'PC4']
print(data_pcomp.head())

## 2. Plot the first two principal components colored by the bean classes

data_pcomp['bean_classes'] = classes
sns.lmplot(x='PC1', y='PC2', data=data_pcomp, hue='bean_classes', fit_reg=False)
plt.show()

#output
#        PC1       PC2       PC3       PC4
# 0 -4.981378  1.824630  0.748993 -0.390797
# 1 -5.436593  2.932257  2.182294 -0.431944
# 2 -4.757913  1.826817  0.514019 -0.125849
# 3 -4.300383  2.003587  3.554316  0.082961
# 4 -6.349107  4.088055  1.179156 -0.830327


#  PCA as features - prior we have found the principal axis and projectd data onto them - but we can take a subset for modeling
#  n this checkpoint, we will be using the first four principal components as our training data for a 
# Support Vector Classifier (SVC). We will compare this to a model fit with the entire dataset (16 features) 
# using the average likelihood score. Average likelihood is a model evaluation metric; the higher the average
#  likelihood, the better the fit.

#example
# Read through the code to make sure that you understand what’s happening. Here are the steps:

# Transform the original data by projecting it onto the first four principal axes. We chose four PCs because we 
# previously found that they contain 95% of the variance in the original data
# Split the data into 67% training and 33% testing sets
# Use the transformed training data to fit an SVM model
# Print out the average likelihood score for the testing data
# Re-split the original 16 standardized features into training and test sets
# Fit the same SVM model on the training set with all 16 features
# Print out the average likelihood score for the test data
# Notice that the score for the model using the first 4 principal components is higher than for the model 
# that was fit with the 16 original features. We only needed 1/4 of the data to get even better model performance!


import pandas as pd
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
 
 
data_matrix_standardized = pd.read_csv('./data_matrix_standardized.csv')
classes = pd.read_csv('./classes.csv')
 
# We will use the classes as y
y = classes.Class.astype('category').cat.codes
 
# Get principal components with 4 features and save as X
pca_1 = PCA(n_components=4) 
X = pca_1.fit_transform(data_matrix_standardized) 
 
# Split the data into 33% testing and the rest training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
 
# Create a Linear Support Vector Classifier
svc_1 = LinearSVC(random_state=0, tol=1e-5)
svc_1.fit(X_train, y_train) 
 
# Generate a score for the testing data
score_1 = svc_1.score(X_test, y_test)
print(f'Score for model with 4 PCA features: {score_1}')
 
# Split the original data intro 33% testing and the rest training
X_train, X_test, y_train, y_test = train_test_split(data_matrix_standardized, y, test_size=0.33, random_state=42)
 
# Create a Linear Support Vector Classifier
svc_2 = LinearSVC(random_state=0)
svc_2.fit(X_train, y_train)
 
# Generate a score for the testing data
score_2 = svc_2.score(X_test, y_test)
print(f'Score for model with original features: {score_2}')


#output
# Score for model with 4 PCA features: 0.4363312555654497
# Score for model with original features: 0.39158504007123773


# PCA for images
# Another way to show the inner workings of PCA is to use an image dataset. An image can be represented as a row
# in a data matrix, where each feature corresponds to the intensity of a pixel.


# example that is looking at images of faces the grouping them together
import numpy as np
from sklearn import datasets
import codecademylib3
import matplotlib.pyplot as plt


# Download the data from sklearn's datasets
faces = datasets.fetch_olivetti_faces()['data']

# 1. Standardize the images using the mean and standard deviation
faces_mean = faces.mean(axis=0)
faces_std = faces.std(axis=0)
faces_standardized = (faces - faces_mean) / faces_std


# 2. Find the number of features per image
n_images, n_features = faces_standardized.shape
side_length = int(np.sqrt(n_features))
print(f'Number of features(pixels) per image: {n_features}')
print(f'Square image side length: {side_length}')


# 3. Plot the images
# Create an empty 10x8 plot
fig = plt.figure(figsize=(10, 8))

# Observe the first 15 images.
for i in range(15):

    # Create subplot, remove x and y ticks, and add title
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.set_title(f'Image of Face: #{i}')

    # Get an image from a row based on the current value of i
    face_image = faces_standardized[i]

    # Reshape this image into side_length x side_length 
    face_image_reshaped = face_image.reshape(side_length, side_length)

    # Show the image
    ax.imshow(face_image_reshaped, cmap=plt.cm.bone)
plt.show()


# This can be useful in understanding how PCA works! We can visualize the eigenvectors by plotting them.
#  They actually have a name: eigenfaces. The eigenfaces are the building blocks for all the other faces in the data.

# We can also visualize the dimensionality reduction that occurs when we transform the original data using a smaller
#  number of principal components. In the code editor, we’ve provided you with code to:

# Plot the eigenfaces
# Plot the reconstructed faces using a smaller number of transformed features. To start, we’ve used
# 400 principal components — only 0.9% of the original number of features (pixels)!

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import codecademylib3
import matplotlib.pyplot as plt


faces_standardized = pd.read_csv('./faces_standardized.csv').values

# 1. Instantiate a PCA object and fit the standardized faces dataset
pca = PCA(n_components=40) 
pca.fit(faces_standardized)

# 2. Retrieve and plot eigenvectors (eigenfaces)
eigenfaces = pca.components_ 

fig = plt.figure(figsize=(10, 8))
fig.suptitle('Eigenvectors of Images (Eigenfaces)')
for i in range(15):
    # Create subplot, remove x and y ticks, and add title
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.set_title(f'Eigenface: #{i}')
    
    # Get an eigenvector from the current value of i
    eigenface = eigenfaces[i]

    # Reshape this image into 64x64 since the flattened shape was 4096
    eigenface_reshaped = eigenface.reshape(64, 64)

    # Show the image
    ax.imshow(eigenface_reshaped, cmap=plt.cm.bone)
plt.show()

# 3. Reconstruct images from the compressed principal components
# The principal components are usually calculated using `faces_standardized @ principal_axes` or the `.transform` method
principal_components = pca.transform(faces_standardized) 

# The `inverse_transform` method allows for reconstruction of images in the original size
faces_reconstructed = pca.inverse_transform(principal_components)

# Plot the reconstructed images 
fig = plt.figure(figsize=(10, 8))
fig.suptitle('Reconstructed Images from Principal Components')
for i in range(15):
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.set_title(f'Reconstructed: {i}')

    reconstructed_face = faces_reconstructed[i]
    reconstructed_face_reshaped = reconstructed_face.reshape(64, 64)
    ax.imshow(reconstructed_face_reshaped, cmap=plt.cm.bone)
plt.show()



# Review
# Implementation: scikit-learn provides a more in-depth set of methods and attributes that extend the number of ways to
#  perform PCA or display the percentage of variance for each principal axis.
# Dimensionality reduction: We visualized the data projected onto the principal axes, known as principal components.
# Image classification: We performed PCA on images of faces to visually understand how principal components still retain 
# nearly all the information in the original dataset.
# Improved algorithmic speed/accuracy: Using principal components as input to a classifier, we observed how we could 
# achieve equal or better results with lower dimensional data. Having lower dimensionality also speeds the training.

































