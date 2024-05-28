# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:10:12 2023

@author: geron
"""

# lambda functions also called anonymous function is a one-line shorthand for functions
# example of code written normal and lambda way
def add_two(my_input):
  return my_input + 2
# Or this way for same results
add_two = lambda my_input: my_input + 2
print(add_two(3))
print(add_two(100))
print(add_two(-2))
# Let’s break this syntax down:
# The function is stored in a variable called add_two.
# The lambda keyword declares that this is a lambda function (similar to how we use def to declare a normal function).
# my_input is a parameter used to hold the value passed to add_two.
# In the lambda function version, we are returning my_input + 2 without the use of a return keyword
#  (the normal Python function explicitly uses the keyword return).

# more complex lambda function using an if statment
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
# grade is the paramater for the check_if_a_grade function and the if statment is what we are returning



# High order functions
# all functions are classified as first class objects and have 4 important characteristics
# 1. First class objects can be stored as variables
# 2. First class objects can be passed as arguments to a function
# 3. First Class objects can be returned by a function
# 4. First Class objects can be stored in data structures like lists and dictionaries
# Here, we assign a function to a variable - basic examples of first class objects functions
uppercase = str.upper 
# And then call it 
big_pie = uppercase("pumpkinpie")
# Here we store two functions in a list
string_manipulation_functions = [str.upper, str.lower] 

# Higher order functions operate on other functions via arguments or via return values.  Meanins Higher order functions 
# do one or both of the follwing
# 1. Accept a function as an argument
# 2. Have a return value that is a function

# Functions as Arguments
# This example is taking a function called total_bill() that takes another function as an argument - func is the other function
def total_bill(func, value):
  total = func(value)
  return total

# not lets have add_tax function and pass it to our higher order total_bill function
def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total
 
total_bill(add_tax, 100)
# output is 106.0
# next example to reuse our higher order function to add gratuity instead of tax
def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total
 
total_bill(add_tip, 100)
# output is 120.0
# now these examples can be just done by calling the function and setting a value but the true power comes
#when we want to keep a consistent manipulation no matter what function is passed in. We can see this if we
 # modify our total_bill() function so it adds formatting to the total amount owed in a consistent and friendly way, 
 # regardless of which function is passed in:
def total_bill(func, value):
  total = func(value)
  return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

print(total_bill(add_tax, 100))
print(total_bill(add_tip, 100))
# output
# 'The total amount owed is $106.00. Thank you! :)'
# 'The total amount owed is $120.00. Thank you! :)'

# functions as arguments - iteration
# using the total bill example from above but instead of doing a single bill we wanted to add tax or tip to each bill
# based on the type of sale it is.  We could write seperate loops for each.  If we did that it would look like this
# this would be for adding tax
bills = [115, 120, 42]
new_bills = []
for i in range(len(bills)):
  total = add_tax(bills[i])
  new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")
 
print(new_bills)
# output
# ['Total amount owed is $121.90. Thank you! :)',
#  'Total amount owed is $127.20. Thank you! :)',
#  'Total amount owed is $44.52. Thank you! :)']
# now we could do the same thing for the tip loop but the better option would be a higher order function to apply
# add_tax or add_tip to each balance in our list.  

#Lets first define a higher-order function, total_bills(), that takes a function and a list as arguments, 
# applies the function to each element in the list, standardizes the format of the result and adds a friendly 
# message, appends the output to a new list, and finally returns the updated new list:
def total_bills(func, list):
  # This list will store all the new bill values
  new_bills = []
 
  # This loop will iterate through our bills
  for i in range(len(list)):
 
    # Here we apply the function to each element of the list!
    total = func(list[i])
    new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")
 
  return new_bills
#Next, let’s use the add_tax() function that we wrote before with our new total_bills() higher-order function:
bills = [115, 120, 42]
bills_w_tax = total_bills(add_tax, bills)
print(bills_w_tax)
#output
# ['Total amount owed is $121.90. Thank you! :)',
#  'Total amount owed is $127.20. Thank you! :)',
#  'Total amount owed is $44.52. Thank you! :)']
#And if we needed to add a tip instead of tax, we could simply swap out the function argument:
bills_w_tip = total_bills(add_tip, bills)
print(bills_w_tip)
# output
# ['Total amount owed is $138.00. Thank you! :)',
#  'Total amount owed is $144.00. Thank you! :)',
#  'Total amount owed is $50.40. Thank you! :)']
#As these examples show, being able to pass functions in as arguments can be pretty handy, 
#especially when we want to apply a function multiple times


# Functions as return values
# example of a higher order function make_box_volume_function() that will calculate the volumes of boxes when they
# have the same height
def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,        
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length*width*height
 
    return volume
box_volume_height15 = make_box_volume_function(15)
print(box_volume_height15(3,2))
# output is 90
#And if we had slightly shorter boxes:
box_volume_height10 = make_box_volume_function(10)
print(box_volume_height10(3,2))
# output is 60

# In the example, we wrote a higher-order function, make_box_volume_function(), that takes a height as an 
# argument and returns a new function that calculates the volume of any box with that height when it is passed 
# the length and width of the box. As we can see, higher-order functions with functions as return values are just
#  as reusable as higher-order functions with functions as arguments and, therefore, also reduce repetition and 
#  the chances for mistakes to creep into code. 



# Built in Higher order functions
# 3 distinct built in higher order functions
# 1. map()
# 2. filter()
# 3. reduce()

# map() built in higher order function
# Syntax example
returned_map_object = map(function, iterable)
# if we set iterable to a list of [3,6,9]
# the output would be function(3), function(6), function(9)
# When called, map() applies the passed function to each and every element in the iterable and returns a map object.
#  The returned map object holds the results from applying the mapping function to each element in the passed iterable. 
#  We will usually convert the map into a list to enable viewing and further use.
# example if we wanted to double every value in a list of numbers
def double(x):
 return x*2
int_list = [3, 6, 9]
doubled = map(double, int_list)
print(doubled)
# output
# <map object at 0x0000018D5381C490>
# In our example:
# We defined a function called double() that takes in a value and returns the value doubled. This function can be
#  used anywhere in our program—not only with map().
# We also defined an iterable (int_list) that we wanted to apply the function to.
# We then passed the function reference double as the function argument and int_list as the iterable to map()
# The map() function proceeded to apply double() onto each element in int_list.
# When we printed the result, we could see that the output of the map() function was a specific type of object 
# called a map object.
# if we wanted to see the actual results of the mapping we need to use the built in list() function
print(list(doubled))
# output
# [6,12,18]

# we can also use lambda functions with map() - in above example if we dont plan on reusing the double() function
# we can rewrite it as a lambda function instead of defining a double function
doubled = map(lambda input: input*2, int_list)
print(list(doubled))
# output 
# [6,12,18]

# example of map and lambda function
grade_list = [3.5, 3.7, 2.6, 95, 87]
# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list)
# convert grades_100scale to a list and save it as updated_grade_list 
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)


# filter() built in higher object function
# takes a function and an iterable as agruments.  Goal is to filter values out of an iterable
#Filter() does this by applying a passed filtering function to each element in the passed iterable.  It returns
# either a true or false value.  Filter will only those elements of the passed iterable that the filter returns True
# example with collection of names and returns only names that start with M or m
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
print(list(M_names))
# output
#['margarita', 'Masako', 'Maki']
# in example filter takes the lamba function paramater and the list names as iterable
# goes through each element in names and sees if the function return is true.  if it is it keeps value
# example of filter based on type of element
books = [["Burgess", 1985], ["Orwell", "Nineteen Eighty-four"], ["Murakami", "1Q85"], ["Orwell", 1984], ["Burgess", "Nineteen Eighty-five"], ["Murakami", 1985]]
# assign the result of your filter function to the variable  string_titles
string_titles = filter(lambda value: type(value[1]) == str, books)
# convert your filter object to a list stored in the variable string_titles_list
string_titles_list = list(string_titles)
# print the list string_titles_list
print(string_titles_list)


# reduce() built in higher object function
# Has two distinct differences from map and filter
#  the reduce() function must be imported from the functools module to use it where map and filter are always available
# from functools import reduce
#  last difference is reduce() returns a single value and to get this value reduce() cumulatively applies
# a passed function to each sequential pair of elements in an iterable
# example of reduce() to multiply together all values in a list
from functools import reduce
int_list = [3, 6, 9, 12]
reduced_int_list = reduce(lambda x,y: x*y, int_list)
print(reduced_int_list)
# output
# 1944
# In this example:
# The reduce() function takes 2 arguments: a lambda function and a list of integers.
# The lambda function takes 2 numbers, x and y and multiplies them together.
# The reduce() function applies the lambda function to the first two elements in the list, 3 and 6, 
# to get a product of 18.
# Next, 18 was multiplied by the following element in the list, 9, to get 162.
# Continuing on, 162 was multiplied by the next element, 12, to get 1944.
# This last, final value—1944—is what was returned by reduce().
# This process was essentially the same as multiplying 3*6*9*12.

# another example of reduce()
letters = ['r', 'e', 'd', 'u', 'c', 'e']
# remember to import the reduce function
from functools import reduce
word = reduce(lambda x,y: x+y, letters)
# store the result of your reduce function in the variable word
print(word)
# Output
# reduce



# Decorators - special functions that work with other functions

# 1. Functions are objects
# # 2. Functions within functions - nested functions
# 3. Returning functions from functions
# example
def get_math_function(operation): # + or -
    def add(n1,n2):
        return n1 + n2
    def sub(n1,n2):
        return n1- n2
    if operation == '+':
        return add
    elif operation == '-':
        return sub
add_function = get_math_function('+')
sub_function = get_math_function('-')
print( add_function(4,6) )
print( sub_function(12,6) )
# 4. Decorating a function - the title_decorator function with the wrapper function is considered the decorating the print my name function
def title_decorator(print_name_function):
    def wrapper():
        print('Professor:')
        print_name_function()
    return wrapper
def print_my_name():
    print("Eric")
# this line is passing a function print m name into title_decorator function
decorated_function = title_decorator(print_my_name)
decorated_function()
# what this example did is took the print name function put it into title decorator function which then ran the wrapper
# function and returned both the print my name and wrapper fucntion
# 5. Decorators with python - same as above but a siplified version
def title_decorator(print_name_function):
    def wrapper():
        print('Professor:')
        print_name_function()
    return wrapper
@title_decorator # this line is in essance the last 2 lines of the previous example python does it for you
def print_my_name():
    print("Eric")
# now if we had multiple functions you have to decorate each one
@title_decorator
def print_joes_name():
    print("Joe")
print_my_name()
print_joes_name()

# 6. Decorators w/ parameters
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):  # the args and kwargs will pass in any agrument you use when you call the function
        print('Professor:')
        print_name_function(*args, **kwargs)
    return wrapper
@title_decorator
def print_my_name(name):
    print(name)
print_my_name('Shelby')



















