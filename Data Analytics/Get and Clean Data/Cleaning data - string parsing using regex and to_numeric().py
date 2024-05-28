# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:30:17 2023

@author: geron
"""

# this will take a price column formatted type as an string '$1' to just 1 and float type first line removes the $ and 
#  2nd line converts it to a numeric instead of string


fruit.price = fruit['price'].replace('[\$,]', '', regex=True)

fruit.price = pd.to_numeric(fruit.price)



import pandas as pd
from students import students
#  this removes the % from the column
students.score = students['score'].replace('[\%]', '',regex=True)

students.score = pd.to_numeric(students.score)


#  example data  'lunges - 30 reps'   - this combines spliting by character and regex to match a character for parsing
# this will extract the numbers
split_df = df['exerciseDescription'].str.split('(\d+)', expand=True)
# then we assign columns from this dataframe to the original dataframe
df.reps = pd.to_numeric(split_df[1])
df.exercise = split_df[0].replace('[\- ]', '', regex=True)




import pandas as pd
from students import students

print(students.grade.head(5))

students.grade = students.grade.str.split('(\d+)', expand=True)[1]
print(students.dtypes)

students.grade = pd.to_numeric(students.grade)

avg_grade = students.grade.mean()
print(avg_grade)






