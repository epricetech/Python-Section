# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:09:17 2023

@author: geron
"""
# method 1  - will just remove the rows with nan values
bill_df = bill_df.dropna()
bill_df = bill_df.dropna(subset=['num_guests'])
#Method 2 - this will let you fill the nan values with any aggregate value like mean, min, max ect
bill_df = bill_df.fillna(value={"bill":bill_df.bill.mean(), "num_guests":bill_df.num_guests.mean()})





import pandas as pd
from students import students

print(students)

score_mean = students.score.mean()
print(score_mean)
students = students.fillna(0)

score_mean_2 = students.score.mean()
print(score_mean)
