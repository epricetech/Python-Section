# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 07:45:22 2023

@author: geron
"""

#  When you want to work with mulitple files and concatenate them into a single dataframe
#  you use the glob() function from python.   Must import with impor glob
#   example  will look for any files that start with file and has an ext of .csv
import glob
 
files = glob.glob("file*.csv")
 
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
 
df = pd.concat(df_list)
 
print(files)



import codecademylib3_seaborn
import pandas as pd
import glob
# this is the regex creating using glob
student_files = glob.glob('exams*.csv')
df_list = []
#  loops through the files and then appends the data into a new dataframe
for filename in student_files:
  data = pd.read_csv(filename)
  df_list.append(data)

students = pd.concat(df_list)
print(students)
print(len(students))






