# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:59:22 2023

@author: geron
"""


#splitting column by character  -  example is splitting data formatted like user_Kenya and admin_US

# Create the 'str_split' column
df['str_split'] = df.type.str.split('_')
 
# Create the 'usertype' column
df['usertype'] = df.str_split.str.get(0)
 
# Create the 'country' column
df['country'] = df.str_split.str.get(1)



import pandas as pd
from students import students

print(students)
#create a series object
name_split = students['full_name'].str.split(" ")

students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)

print(students.head())