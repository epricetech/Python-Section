# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 08:37:02 2023

@author: geron
"""


# The parameters you provide are:

# frame: the DataFrame you want to melt
# id_vars: the column(s) of the old DataFrame to preserve
# value_vars: the column(s) of the old DataFrame that you want to turn into variables
# value_name: what to call the column of the new DataFrame that stores the values
# var_name: what to call the column of the new DataFrame that stores the variables
# The default names may work in certain situations, but it’s best to always have data that is self-explanatory. 
# Thus, we often use .columns() to rename the columns after melting:




df = pd.melt(frame=df, id_vars="Account", value_vars=["Checking","Savings"], value_name="Amount", var_name="Account Type")
df.columns(["Account", "Account Type", "Amount"])



#  this example takes old columns fractions and probabilities and changes it to exam and score

import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.columns)
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.head())
print(students.columns)
print(students.exam.value_counts())






