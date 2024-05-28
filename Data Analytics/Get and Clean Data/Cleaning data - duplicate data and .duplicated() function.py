# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 08:57:38 2023

@author: geron
"""

#  finding and clearing duplicates with the .duplicated() function to find and the .drop_duplicates() fucntionn to clear
#  the .drop_duplicates() only clears duplicates if its an exact match throughout all values in row.  If you want to be 
#  specific about what you drop you can add the subset=['column_name'] as a paramater to remove all rows that are duplicate
#  in that specific column stated

#fruits = fruits.drop_duplicates(subset=['item'])

import pandas as pd
from students import students

print(students)

duplicates = students.duplicated()
print(duplicates.value_counts())

students = students.drop_duplicates()

duplicates = students.duplicated()
print(duplicates.value_counts())








