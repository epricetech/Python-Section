# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:06:07 2023

@author: geron
"""

#  2 sample t-test using ehs scipy function ttest_ind()it takes the alues for each group as inputs and returns
# the t-stat and p-value   - if the pvalue is less than 0.05 then there is significant difference
#  this test is between a quantitive variable Time spent on website and binary categorical variable or or new color scheme

from scipy.stats import ttest_ind
tstat, pval = ttest_ind(times_version1, times_version2)


import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3
from scipy.stats import ttest_ind
data = pd.read_csv('version_time.csv')

#separate out times for  two versions
old = data.time_minutes[data.version=='old']
new = data.time_minutes[data.version=='new']

#run the t-test here:
tstat, pval = ttest_ind(old,new)

#determine significance
significant = True

#plot overlapping histograms
plt.hist(old, alpha=.8, label='old')
plt.hist(new, alpha=.8, label='new')
plt.legend()
plt.show()


## when we want an association between a quantitive variable and a non binary categorical variable - non binary means more than 
## 2 categories    -   This is running 3 seperate t tests
from scipy.stats import ttest_ind
import codecademylib3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run t-tests
_b_tval, a_b_pval = ttest_ind(a,b)
a_c_tval, a_c_pval = ttest_ind(a,c)
b_c_tval, b_c_pval = ttest_ind(b,c)
print("A to B comparison:", a_b_pval)
print("A to C comparison:", a_c_pval)
print("B to C comparison:", b_c_pval)

# determine significance
a_b_significant = True 
a_c_significant = True
b_c_significant = False

# create plot
sns.boxplot(data=veryants, x='Store', y='Sale')
plt.show()



##  instead of running a bunch of t-tests we can use ANOVA - analysis of variance  - tests the null hypotheses that all
## groups have the same population mean(example the true average price of a sale is the same at all locaitons)
#  in python we use f_oneway() function to perform ANOVA and has 2 outputs.  The f stat and the p-value
from scipy.stats import f_oneway
fstat, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists)


from scipy.stats import f_oneway
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run ANOVA
fstat, pval = f_oneway(a,b,c)
print(pval)
# determine significance
#  p value of .00015355 does show significant differnce in sales
significant = True



#  Tukey Range Test -  pairwise_turkeyhsd() function  When we want to compare t-test results example
#  want to know video game scores for math, writing and psych majors.  W have a dataset data with 2 columns score and major
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey_results = pairwise_tukeyhsd(data.score, data.major, 0.05)
print(tukey_results)


from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')

# run tukey's test
tukey_results = pairwise_tukeyhsd(veryants.Sale, veryants.Store, 0.05)
print(tukey_results)

# determine significance
a_b_significant = True
a_c_significant = False
b_c_significant = False


# Assuptions of T-tests ANOVA and Tukey
# 1.  Obersvations shoel be independent and random
# 2. The standard deviation of the groups should be equal.  
#  3 data should be normally distributedish
# 4. Groups create by categorical varialbe must be independent.  

import codecademylib3
import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv")
dist_2 = np.genfromtxt("2.csv")

#calculate ratio of standard deviations:
ratio = np.std(dist_1)/np.std(dist_2)
print(ratio)

#check normality assumption
normal_assumption = True

#plot histograms of each distribution
plt.hist(dist_1, alpha = .8, normed = True, label = 'dist 1')
plt.hist(dist_2, alpha = .8, normed = True, label = 'dist 2')
plt.legend()
plt.show()


#  Chi-Square Test - to see wheather the outcomes of 2 categorical variables are associated
#  we use the chi2_contingency() function and crosstab()
#create table:
import pandas as pd
table = pd.crosstab(variable_1, variable_2)
 
#run the test:
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(table)


import pandas as pd
from scipy.stats import chi2_contingency

# read in and print data
ants = pd.read_csv("ants_grade.csv")
print(ants.head())

# create contingency table
table = pd.crosstab(ants.Grade, ants.Ant)
print(table)

# run Chi-Square test and print p-value
chi2, pval, dof, expected = chi2_contingency(table)

# determine significance
significant = False

#  Assumptions of chi-square test
# 1. Observations should be independent and random
# 2. Categories of both variables must be mutually exclusive
# 3.  The groups should be independent.  




















