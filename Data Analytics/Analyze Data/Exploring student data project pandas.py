# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 08:11:16 2023

@author: geron
"""

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head(5))
# Print summary statistics for all columns
print(students.describe(include='all'))
# Calculate mean
print(students.math_grade.mean())
# Calculate median
print(students.math_grade.median())
# Calculate mode
#Note that, because of how this function is written, the mode is returned as a pandas series. In order to convert it to a single value, we can extract the first value in the series (eg., students.math_grade.mode()[0])
print(students.math_grade.mode()[0])
# Calculate range
range = students.math_grade.max() - students.math_grade.min()
print(range)
# Calculate standard deviation
print(students.math_grade.std())
# Calculate MAD
print(students.math_grade.mad())
# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
mothers = students.Mjob.value_counts()
print(mothers)
# Calculate proportion of students with mothers in each job category
mothers_job = students.Mjob.value_counts(normalize=True)
print(mothers_job)
# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()
plt.close()