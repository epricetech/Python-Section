# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:13:00 2023

@author: geron
"""

import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here

print(financial_data.head())

#2 Notice that financial_data has three columns – Month, Revenue, and Expenses.
#Store each column in three separate variables called month, revenue, and expenses.
month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

# next plot month and revenue
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))

#Notice that there are two columns:
#Expense: indicates the expense category
#Proportion: indicates how much of the overall expenses a specific category takes up
#Store the Expense column in a variable called expense_categories and the Proportion column in a variable called proportions.
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

#Next, we want to create a pie chart of the different expense categories. Use plt.clf() again to clear the previous plot, 
#then create a pie chart using the plt.pie() method, passing in two arguments: proportions labels = expense_categories
#Give your pie chart a title using plt.title(), then use plt.show() at the end to show the plot.
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15,0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense')
plt.axis('Equal')
plt.tight_layout()
plt.show()

#  Above pie plot is the code for this part It seems that Salaries, Advertising, and Office Rent make up most of the expenses, while the rest of the categories make up a small percentage.
#Before you hand this pie chart back to management, you would like to update the pie chart so that all categories making up less than 5% of the overall expenses (Equipment, Utilities, Supplies, and Food) are collapsed into an “Other” category.
#Update the pie chart accordingly.
expense_cut = 'Salaries'

employees = pd.read_csv('employees.csv')
print(employees.head())

#Notice that there is a Productivity column, which indicates the productivity score assigned to that employee.
#Sort the employees data frame (in ascending order) by the Productivity column and store the result in a variable called sorted_productivity.
#To sort a data frame, you can do the following:
sorted_data = employees.sort_values(by=['Productivity'])
print(sorted_data)

#You should now see the employees with the lowest productivity scores at the top of the data frame.
#The company decides to let go of the 100 least productive employees.
#Store the first 100 rows of sorted_productivity in a new variable called employees_cut and print out the result.
#Unfortunately, this batch of employees won’t be so lucky.
employees_cut = sorted_data.head(100)
print(employees_cut)

#  now you want to compare income to productivity but
# these are at 2 different scales.  so we must do some 
#standardization - does not have a bounding range since there are outliers


#The COO (Chief Operating Officer) is debating whether to allow employees to continue to work from home post-pandemic.
#He first wants to take a look at roughly how long the average commute time is for employees at the company. He asks for your help to analyze this data.
#The employees data frame has a column called Commute Time that stores the commute time (in minutes) for each employee.
#Create a variable called commute_times that stores the Commute Time column.

commute_time = employees['Commute Time']
commute_time_log = np.log(commute_time)
print(commute_time.head())
print(commute_time.describe())

plt.clf()
plt.hist(commute_time_log)
plt.title("Employee Commute Times")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()

#The data seems to be skewed to the right. To make it more symmetrical, we might try applying a log transformation.
#Right under the commute_times variable, create a variable called commute_times_log that stores a log-transformed version of commute_times.
#To apply log-transform, you can use numpy’s log() function.




