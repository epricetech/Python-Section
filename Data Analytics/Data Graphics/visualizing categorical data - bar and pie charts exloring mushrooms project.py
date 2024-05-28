# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 08:16:57 2023

@author: geron
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
#There are 23 variables in this dataset (one for each column). Graphing each one individually would be tedious; luckily, you will use loops.

#If you look at plot.py, you will see an attribute called columns. This attribute returns the name of each variable in mushroom_data.csv.

#Create a loop that traverses each column in the columns list.
#Print each column in columns while iterating through the loop. This is to check that your for loop is working correctly.
# list of all column headers
for index in range(0,len(df['Bruises'])):
    df['Bruises'][index] = str(df['Bruises'][index])
columns = df.columns.tolist()
columns = df.columns.tolist()
# this loop will create a bar graph for each column
for column in columns:
  # to add order argument  you must use the value_counts().index function
  sns.countplot(x=column, data=df, order=df[column].value_counts().index) 
# rotates the value labels slightly so they don’t overlap also slightly increases font size
  plt.xticks(rotation=30, fontsize=10)
# increases the variable label font size slightly to increase #readability
  plt.xlabel(column, fontsize=12)
  plt.title(column + 'Value Counts')
  plt.show()
  plt.clf()
 #print(column)

#You can now plot your data using the .countplot() method from the seaborn library. Follow these steps:
#Call .countplot() in the for loop
#Use column and the df pandas DataFrame to graph the value counts of each variable in mushroom_data.csv.
#Please wait until the next task to use plt.show(). Since you are creating 23 plots in the browser, you will need an additional line of code.
#Hint
#Recall that to graph a csv column using the .countplot() method, you can use a pandas DataFrame as shown in the code block:
#sns.countplot(pandas_df["column name"])
#Since you are using a for loop to graph each variable automatically, use column (notice the lack of quotes here!) in place of "column name" and replace pandas_df with the df DataFrame in plot.py.












