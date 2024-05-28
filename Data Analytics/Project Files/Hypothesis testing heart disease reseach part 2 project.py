# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:42:45 2023

@author: geron
"""


#The data has been saved as a dataframe named heart in script.py. It contains the following variables:

#age: age in years
#sex: sex assigned at birth; 'male' or 'female'
#trestbps: resting blood pressure in mm Hg
#chol: serum cholesterol in mg/dl
#cp: chest pain type ('typical angina', 'atypical angina', 'non-anginal pain', or 'asymptomatic')
#exang: whether the patient experiences exercise-induced angina (1: yes; 0: no)
#fbs: whether the patient’s fasting blood sugar is >120 mg/dl (1: yes; 0: no)
#thalach: maximum heart rate achieved in exercise test
#heart_disease: whether the patient is found to have heart disease ('presence': diagnosed with heart disease; 'absence': no heart disease)


# In order to investigate this question further, save the values for thalach among patients who were diagnosed with 
# heart disease as a variable named thalach_hd. Then save the values of thalach among patients who were not diagnosed 
# with heart disease as thalach_no_hd.


# Hint
# Here is the code for thalach_hd. Use similar syntax to create thalach_no_hd:

# thalach_hd = heart.thalach[heart.heart_disease == 'presence']
# 4.
# Calculate and print the difference in mean thalach for patients diagnosed with heart disease compared to patients 
# without heart disease. Then do the same for the median difference.


# Hint
# Here is code for the mean difference. Use similar syntax with the np.median() function to calculate the median difference.

# mean_diff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
# print('`thalach` mean Difference: ', mean_diff)
# 5.
# We’d like to find out if the average thalach of a heart disease patient is significantly different from the average 
# thalach for a person without heart disease.

# Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

# Null: The average thalach for a person with heart disease is equal to the average thalach for a person without heart disease.
# Alternative: The average thalach for a person with heart disease is NOT equal to the average thalach for a person
#  without heart disease.

# Hint
# This requires a two-sample t-test, which can be implemented using the ttest_ind() function from scipy.stats. 
# Import the function as follows:

# from scipy.stats import ttest_ind
# 6.
# Run the hypothesis test from task 5 and print out the p-value. Using a significance threshold of 0.05, 
# is there a significant difference in average thalach for people with heart disease compared to people with no heart disease?


# Hint
# The inputs to ttest_ind() are the values of thalach for each group (no heart disease and heart disease). 

# There are two outputs: the first output is the t-statistic and the second output is the p-value.

# If you run the hypothesis test correctly, you should get a p-value of 3.456964908430172e-14, 
# which is equivalent to 0.00000000000003457. This is less than 0.05, so we “reject the null hypothesis” and 
# conclude that there is a significant difference in thalach for people with heart disease compared to people 
# without heart disease.

# 7.
# Using the same process, investigate at least one other quantitative variable. Options include age, trestbps 
# (resting blood pressure), and chol (cholesterol). Are any of these variables also significantly associated 
# with heart disease?

# Note: before every new plot that you make, be sure to use plt.clf() to clear the previous plot first, so that
#  plots don’t get layered on top of each other. For example:

# first box plot:
sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.show()
 
# second box plot:
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()

Hint
Using a 0.05 significance threshold, both age (p = 8.955636917529706e-05) and trestbps (p = 0.008548268928594928) are significantly associated with heart disease. chol is not significantly associated with heart disease (p = 0.13914167020436527).

Chest Pain and Max Heart Rate
8.
Next, let’s investigate the relationship between thalach (maximum heart rate achieved during exercise) and the type of heart pain a person experiences. Create a set of side-by-side box plots of thalach for each chest pain type in the data. Make sure to use plt.clf() to clear the previous plots first!

Are there any chest pain types for which average thalach is significantly higher or lower (compared to other chest pain types)?


Hint
Fill in the following code:

plt.clf()
sns.boxplot(x = heart.___, y = heart.___)
plt.show()
9.
To investigate this further, save the values of thalach for patients who experienced each type of chest pain as thalach_typical, thalach_asymptom, thalach_nonangin, and thalach_atypical, respectively.


Hint
Below is the syntax to create thalach_typical. The other variables can be created using similar syntax (the other values of cp are 'asymptomatic', 'non-anginal pain', and 'atypical angina').

thalach_typical = heart.thalach[heart.cp == 'typical angina']
10.
Run a single hypothesis test to address the following null and alternative hypotheses:

Null: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people all have the same average thalach.
Alternative: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach.
Save the resulting p-value as pval and print it out. Using a significance threshold of 0.05, is there at least one pair of chest pain categories for which people in those categories have significantly different thalach?


Hint
This test addresses an association between two variables: a non-binary categorical variable (cp, with four possible options) and a quantitative variable (thalach). We could use six separate two-sample t-tests here, but since we’ve been asked to use a single hypothesis test, we should use an ANOVA.

To do this, we first need to import the f_oneway() function:

from scipy.stats import f_oneway
Then, we need to input the thalach values for each cp type (fill in the code below):

Fstat, pval = f_oneway(thalach_typical, ___, ___, ___)
print(pval)
11.
If you completed the previous step correctly, you should have concluded that there is at least one pair of chest pain types (cp) for which people with those pain types have significantly different average max heart rates during exercise (thalach).

Run another hypothesis test to determine which of those pairs are significantly different. Use an overall type I error rate of 0.05 for all six comparisons.


Hint
For this test, we need Tukey’s range test, which can be implemented with pairwise_tukeyhsd. First we need to import the function:

from statsmodels.stats.multicomp import pairwise_tukeyhsd
The inputs to this function are our two variables of interest: the max heart rate during exercise (thalach) and chest pain type (cp). Fill in the following code:

results = pairwise_tukeyhsd(endog = ___, groups = ___)
print(results)
For any pair where “Reject” is “True”, we conclude that people with those chest pain types have significantly different maximum heart rates during exercise. Note: you may need to expand the output window to see the full chart.

Maybe surprisingly, people who are 'asymptomatic' seem to have a lower maximum heart rate (associated with heart disease) than people who have other kinds of chest pain.

Heart Disease and Chest Pain
12.
Finally, let’s investigate the relationship between the kind of chest pain a person experiences and whether or not they have heart disease. Create a contingency table of cp and heart_disease and save it as Xtab, then print it out.


Hint
Fill in the following code:

Xtab = pd.crosstab(heart.___, heart.___)
print(Xtab)
Based on this table, it seems like people who are diagnosed with heart disease tend to be asymptomatic, while people with who are not diagnosed with heart disease tend to have different kinds of chest pain. This helps explain our findings on the relationship between chest pain and max heart rate above. However, we’d have to do more research to try to understand why this is the case. It seems a little counter-intuitive!

13.
Run a hypothesis test for the following null and alternative hypotheses:

Null: There is NOT an association between chest pain type and whether or not someone is diagnosed with heart disease.
Alternative: There is an association between chest pain type and whether or not someone is diagnosed with heart disease.
Save the p-value as pval and print it out. Using a significance threshold of 0.05, is there a significant association between chest pain type and whether or not someone is diagnosed with heart disease?


Hint
This test investigates an association between two categorical variables, so we need to use a Chi-Square test. First, we can import the chi2_contingency() function as follows:

from scipy.stats import chi2_contingency
Then we can use that function to run our test. The chi2_contingency() function has four outputs (the p-value is the second output). It takes one input that you’ll need to fill in below — the contingency table:

chi2, pval, dof, exp = chi2_contingency(___)
If you run the test correctly, you should calculate a p-value of 1.2517106007837527e-17, which is equivalent to 0.0000000000000000125. This is less than 0.05, so we can conclude that there is a significant association between these variables.

Further Exploration
14.
Congratulations! You’ve used a sample of data to understand how health related outcomes are associated with heart disease. Now that you’ve gotten your feet wet, there are a number of additional variables in this dataset that we haven’t looked at yet! If you want additional practice, use this space to continue your investigation. What other variables might be predictive of heart disease? Can you identify which hypothesis test to use for each variable?

As a reminder, the variables in this data are:

age: age in years
sex: sex assigned at birth; 'male' or 'female'
trestbps: resting blood pressure in mm Hg
chol: serum cholesterol in mg/dl
cp: chest pain type ('typical angina', 'atypical angina', 'non-anginal pain', or 'asymptomatic')
exang: whether the patient experiences exercise-induced angina (1: yes; 0: no)
fbs: whether the patient’s fasting blood sugar is >120 mg/dl (1: yes; 0: no)
thalach: maximum heart rate achieved in exercise test
heart_disease: whether the patient is found to have heart disease ('presence': diagnosed with heart disease; 'absence': no heart disease)



# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')

# inspect data
print(heart.head())

# box plot of `thalach` based on heart disease
sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.show()

# save `thalach` for hd patients and non-hd patients
thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

# calculate and print mean difference
mean_diff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
print('`thalach` mean Difference: ', mean_diff)

# calculate and print median difference
med_diff = np.median(thalach_no_hd) - np.median(thalach_hd)
print('`thalach` median Difference: ', med_diff)

# run two-sample t-test
from scipy.stats import ttest_ind
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print('p-value for `thalach` two-sample t-test: ', pval)

# investigating other quantitative variables
#age
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()
age_hd = heart.age[heart.heart_disease == 'presence']
age_no_hd = heart.age[heart.heart_disease == 'absence']
mean_diff = np.mean(age_hd) - np.mean(age_no_hd)
print('`age` mean Difference: ', mean_diff)
med_diff = np.median(age_hd) - np.median(age_no_hd)
print('`age` median Difference: ', med_diff)
tstat, pval = ttest_ind(age_hd, age_no_hd)
print('p-value for `age` two-sample t-test: ', pval)

#trestbps
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.trestbps)
plt.show()
trestbps_hd = heart.trestbps[heart.heart_disease == 'presence']
trestbps_no_hd = heart.trestbps[heart.heart_disease == 'absence']
mean_diff = np.mean(trestbps_hd) - np.mean(trestbps_no_hd)
print('`trestbps` mean Difference: ', mean_diff)
med_diff = np.median(trestbps_hd) - np.median(trestbps_no_hd)
print('`trestbps` median Difference: ', med_diff)
tstat, pval = ttest_ind(trestbps_hd, trestbps_no_hd)
print('p-value for `trestbps` two-sample t-test: ', pval)

#chol
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.chol)
plt.show()
chol_hd = heart.chol[heart.heart_disease == 'presence']
chol_no_hd = heart.chol[heart.heart_disease == 'absence']
mean_diff = np.mean(chol_hd) - np.mean(chol_no_hd)
print('`chol` mean Difference: ', mean_diff)
med_diff = np.median(chol_hd) - np.median(chol_no_hd)
print('`chol` median Difference: ', med_diff)
tstat, pval = ttest_ind(chol_hd, chol_no_hd)
print('p-value for `chol` two-sample t-test: ', pval)

# box plot of `thalach` based on `cp`
plt.clf()
sns.boxplot(x=heart.cp, y=heart.thalach)
plt.show()

# save `thalach` based on `cp`
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

# run ANOVA
from scipy.stats import f_oneway
Fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print('p-value for ANOVA: ', pval)

# run Tukey's range test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
output = pairwise_tukeyhsd(heart.thalach, heart.cp)
print(output)

# contingency table of heart disease vs cp
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

# run chi-square test
from scipy.stats import chi2_contingency
chi2, pval, dof, exp = chi2_contingency(Xtab)
print('p-value for chi-square test: ', pval)

