# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:36:25 2023

@author: geron
"""

#  There are many differnt ways to work with files.  Most of them are built in functions to import
# numby and pandas are the biggest - pandas lets you read csv files and numby lets you use its methods on the data
import pandas as pd
import numpy as np
# you can also use other methods to read files
# syntax for python file object
#with open('somefile.txt') as file:

# Python Readline Method
# tis will extract the next line in the file if it exists
# with open('somefile.txt') as file:
    #print(file.readline())

# parsing JSON files to dictionary
# json format is used to store key value pairs - this modlue allows reading such data format and parshing to dictionary
# the json.load function takes a file object as an argument and returns the data in a dictionary format
# Use json.load with an opened file object to read the contents into a Python dictionary.
# Contents of file.json
# { 'userId': 10 }
import json
with open('file.json') as json_file:
    python_dict = json.load(json_file)
print(python_dict.get('userId'))
# Prints 10


# Python write to file
# when you use the open with it is for read only.  A second argument is needed to make it writable.  To use write you must 
# add a 'w' as second argument and then use the .write() function
# with open('somefile.txt', w) as file:
   # file.write('This is a new entry to the file')


# realines method
# you can choose to return a list of strings.  each representing a lingle line in the file
# with opeen('somefile') as file:
#print(file.readlines())


# Class csv.Dictwriter
# this allows for read and write of a csv file.  - though pandas is the better optin when doing data analysis
# the csv.DictWriter takes 2 arguments.  First is the file name and where it is being writen too and the 2nd
# paramter is fieldnames whish is a list of field names that the csv is going to handle

# An example of csv.DictWriter
# import csv

# with open('companies.csv', 'w') as
# csvfile:
# fieldnames = ['name', 'type']
# writer = csv.DictWriter(csvfile,
# fieldnames=fieldnames)
# writer.writeheader()
# writer.writerow({'name': 'Codecademy',
# 'type': 'Learning'})
# writer.writerow({'name': 'Google',
# 'type': 'Search'})

# """
# After running the above code,
# companies.csv will contain the following
# information:

# name,type
# Codecademy,Learning
# Google,Search
# """

# python read method - reutns the entire file as a string
# with open('file.txt') as file:
    # file_data = file.read()


# Making API request in Python -  The result is a response objectFirst step is to import requests.  
#Then use the get() command and last turn it into a string using the .text command or the .json command
# Syntax
# Variable = requests.get(webstie_address)
# EXAMPLE
# r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')
# EXAMPLE OF convert to string or json option
# # Access data as JSON string
# print(r.text)
 
# # Access decoded JSON data as Python object
# print(r.json())
































