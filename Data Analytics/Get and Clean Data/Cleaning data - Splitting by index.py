# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:46:07 2023

@author: geron
"""


#  splitting a column into mulitple columns using the str function and index locations.  
#  example is a columna with birthday as mmddyy format and want seperate columns

# Create the 'month' column
df['month'] = df.birthday.str[0:2]
 
# Create the 'day' column
df['day'] = df.birthday.str[2:4]
 
# Create the 'year' column
df['year'] = df.birthday.str[4:]


import pandas as pd
from students import students

print(students)

print(students.columns)
print(students.gender_age.head())

students['gender'] = students.gender_age.str[0:1]
students['age'] = students.gender_age.str[1:3]

print(students.head())
#  this line resets df get rid of the column we just split
students = students[['full_name','exam','grade','score','gender','age']]



