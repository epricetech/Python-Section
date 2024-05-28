# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:18:51 2023

@author: geron
"""

#you can save specific values within the column to a variable to make easy to analize
# scores_GP = students.G3[students.school == 'GP']
# scores_MS = students.G3[students.school == 'MS']


import pandas as pd


students = pd.read_csv('students.csv')

#print the first five rows of students:
print(students.head(5))

#separate out scores for students who live in urban and rural locations:

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']



#finding differences in mean and medial pending on column values - the np.mean and np.median is a special function

# mean_GP = np.mean(scores_GP)
# mean_MS = np.mean(scores_MS)
# print(mean_GP) #output: 10.49
# print(mean_MS) #output: 9.85
# print(mean_GP - mean_MS) #Output: 0.64

# median_GP = np.median(scores_GP)
# median_MS = np.median(scores_MS)
# print(median_GP) #Output: 11.0
# print(median_MS) #Output: 10.0
# print(median_GP-median_MS) #Output: 1.0


import numpy as np
import pandas as pd
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#calculate means for each group:
scores_urban_mean = np.mean(scores_urban)
scores_rural_mean = np.mean(scores_rural)

#print mean scores:
print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)

#calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

#print mean difference
print('Mean difference:')
print(mean_diff)

#calculate medians for each group:
scores_urban_median = np.median(scores_urban)
scores_rural_median = np.median(scores_rural)

#print median scores
print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

#calculate median difference
median_diff = scores_urban_median - scores_rural_median

#print median difference
print('Median difference:')
print(median_diff)



#with vizualization you can selct more than just X for the plot.  You can also choose a y axis.  Exampl
# sns.boxplot(data = df, x = 'school', y = 'G3')
# plt.show()

#same for histogram
# plt.hist(scores_GP , color="blue", label="GP", normed=True, alpha=0.5)
# plt.hist(scores_MS , color="red", label="MS", normed=True, alpha=0.5)
# plt.legend()
# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#create the overlapping histograms here:
plt.hist(scores_urban, color='blue', normed = True, alpha = 0.5, label='urban')
plt.hist(scores_rural, color='red', normed = True, alpha = 0.5, label='rural')
plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


titanic = pd.read_csv('titanic.csv')

Survived = titanic.Fare[titanic.Survived == 1]
Dies = titanic.Fare[titanic.Survived == 0]

survive_mean = np.mean(Survived)
died_mean = np.mean(Dies)

diff_mean = survive_mean-died_mean

print(diff_mean)

survive_med= np.median(Survived)
died_med = np.median(Dies)

diff_med = survive_med-died_med

print(diff_med)

sns.boxplot(data = titanic, x = 'Survived', y = 'Fare')
plt.show()




