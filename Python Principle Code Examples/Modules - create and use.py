# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 08:15:20 2023

@author: geron
"""

# modules are pre built functions that are called modules that you can import into your code
# example of modules are the math and random
# you call a module with an import statement which must have import name of module
# example of importing the random module
import random
for i in range(5):
    print(random.randint(1, 10))

# there are 3 ways you can import modules 
# First way
import module
module.function()
# # Second way
from module import function
function()
# # Third way - not the best option as it can lead to cluttered local namspace 
from module import *
function()

# alias - you can also set an alias for module using as keyword
# Aliasing matplotlib.pyplot as plt
from matplotlib import pyplot as plt
plt.plot(x, y)
# Aliasing calendar as c
import calendar as c
print(c.month_name[1])


# data and time module - it allows you to set date, time, or both
# you can use the datatime module
#  and then use the date()   time()  or datetime() function
import datetime
feb_16_2019 = datetime.date(year=2019,month=2, day=16)
feb_16_2019 = datetime.date(2019, 2, 16)
print(feb_16_2019) #2019-02-16
time_13_48min_5sec = datetime.time(hour=13, minute=48,second=5)
time_13_48min_5sec = datetime.time(13, 48,5)
print(time_13_48min_5sec) #13:48:05
timestamp= datetime.datetime(year=2019,month=2, day=16, hour=13, minute=48,second=5)
timestamp = datetime.datetime(2019, 2, 16,13, 48, 5)
print (timestamp) #2019-01-02 13:48:05

# example of datetime module and various functions you can use
from datetime import datetime
# year - month - day - hour - minute - second - timezone(not shown)
birthday = datetime(1977, 9, 8, 6, 25, 12)
print(birthday.year)
print(birthday.day)
print(birthday.second)
print(birthday.hour)
print(birthday.weekday())  # 0 represents monday and so on
print(datetime.now())# Data
# you can also subract these datetimes
print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now() - datetime(2018, 1, 1))

# example of using the strptime function parsing the data
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date.month)
print(parsed_date.year)

# example of using the strftime function to render a date as a string
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)

# example of the decimal module with returns an answer with a certain decimal point
from decimal import Decimal
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')
cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996

# Import Decimal below:
from decimal import Decimal
# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)
four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)


# ranint() and random.choice() function from random module
# randint provides a uniform random selection from a range of integers and the 
# choice() provides a uniform selection of a random element from a sequence
# Returns a random integer N in a given range, such that start <= N <= end
# random.randint(start, end)
r1 = random.randint(0, 10)
print(r1) <= 10 # Random integer where 0 <= r1
# Prints a random element from a sequence
seq = ["a", "b", "c", "d", "e"]
r2 = random.choice(seq)
print(r2) # Random element in the sequence


# you can also import another file using import filename
# file1 content
# def f1_function():
# return "Hello World"
# file2
# import file1
# # Now we can use f1_function, because we
# imported file1
# f1_function()



































