# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:17:06 2023

@author: geron
"""

# Scopes defines which namespaces the program will look into and in what order - 
#While multiple namespaces usually exist at once, this does not mean we can access all of them in different parts of our program
# 4 levels of scope
# 1. Built in Scope
# 2. Global Scope - names in global namespace will be in global scope automaticall can be access but not modified
# In addition, the global statement can be used even if the name has not been defined in the global namespace. 
# Using the global statement would create the new variable in the global namespace.
# 3. Enclosing Scope - there also exist special rules that apply for accessing nested values.
 # These rules make up the enclosing scope (also known as nonlocal scope
 #Enclosing scope allows any value defined in an enclosing function to be accessed in nested functions below it
# 4. Local Scope - Whenever we decide to call a function, a new local scope will be generated. Each subsequent 
# function call will generate a new local scope. Since the local scope is the deepest level of the four scopes, names
#  in a local scope cannot be accessed or modified by any code called in outer scopes. As a rule of thumb, any names
#  created in a local namespace are usually also locally scoped.

# local scope example
# def favorite_color(): 
#   color = 'Red'
# print(color) 
# #In this case, the name of color is scoped locally to the function favorite_color(). Since the statement print(color) 
# # is called outside of the function, it has no access to the local scope (and thus the local namespace) inside of
# #  favorite_color() and returns an error.
# # this code fixes the scope to be locally
# def favorite_color(): 
#   color = 'Red'
#   print(color) 
# favorite_color()

# example of enclosing scope
def outer_function():
  enclosing_value = 'Enclosing Value'
 
  def nested_function():
    nested_value = 'Nested Value'
 
    def second_nested():
       print(enclosing_value)
       print(nested_value)
       second_nested() 
 
  nested_function()
 
outer_function()
# 2 important aspects of example above
# The flow of scope access only flows upwards. This means that the deepest level has access to every enclosing 
# namespace above it, but not the other way around. For example, if we tried to access nested_value from one 
# level above where it was defined:
# mmutable objects, such as strings or numbers, can be accessed in nested functions, but cannot be modified.
#  Let’s try to change enclosing_value to see this restriction in action:
# example of enclosing scope
def calc_paint_amount(width, height):


  square_feet = width * height
  # Write your code below!
  def calc_gallons():
      return square_feet / 400
  return calc_gallons()
print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))


# we can modify names fomr the enclosing scopy by using the nonlocal statement
#Given the following enclosing and nested function, there is a variable defined in the enclosing scope, 
#which is not modifiable from within the nested function.
def enclosing_function():
  var = "value"
 
  def nested_function():
    var = "new_value"
 
  nested_function()
 
  print(var)
 
enclosing_function()

#as the value of var was not modified by the nested function. After using the nonlocal statement, 
#the variable is now modifiable from the local scope.
def enclosing_function():
  var = "value"
 
  def nested_function():
    nonlocal var
    var = "new_value"
 
  nested_function()
  print(var)
 
enclosing_function()

# another example for modify
walls = [(20, 9), (25, 9), (20, 9), (25, 9)]

def calc_paint_amount(wall_measurements):

  square_feet = 0

  def calc_square_feet():
    nonlocal square_feet
    for width, height in wall_measurements:
      square_feet += width * height

  def calc_gallons():
    return square_feet / 400

  calc_square_feet()

  return calc_gallons()
print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))


# modifying global scope using the global statement
global_var = 10
 
def some_function():
  global global_var
  global_var = 20
 
some_function()
 
print(global_var)

# example
def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)


# the LEGB Rule for scope resolution
# scope resolution describes a search procedure for a name in various namespaces.  LEGB stands for local, enclosing, global
# and builtin - 
# To see this rule in action, let’s take a look at two specific scenarios where Python is searching for a name. 
# The first scenario is a nested function that wants to print a variable called age:

age = 27 
 
def func(): 
 
  def inner_func():
    print(age)
  inner_func()
 
func()
# Would output:

# 27
# So what exactly happened here in terms of scope resolution? It went a bit like this:

# First, Python looked in the local (The L of LEGB) scope that existed inside of inner_func(). 
# This is the lowest level of the LEGB rule and thus where Python starts the search for a name that

#  is trying to be called (in this case via a print()). Python then realized the name of age isn’t in the 
#  local namespace and continues the search to the upper levels of scope.

# The second level Python examined is the enclosing scope (The E of LEGB) of func(). Unfortunately, again the 
# name of age doesn’t exist in the enclosing namespace, and Python moves upwards to higher scopes.

# Next, Python arrives at the global scope and finds the name of age in the global namespace. The search is 
# finished, and the result is returned.

# This process of scope resolution is crucial to understanding how programs are able to access names in
#  different scopes. Keep in mind the order that Python searches always start at the lowest level (the local level) 
#  and always flows upward to the higher scopes.

# The second scenario to examine is seeing what happens when we have two of the same name in different namespaces.

# Let’s examine the same script but with a slight modification that creates a second name called age 
# in a different namespace. Here is what it looks like:

age = 27 
 
def func(): 
  age = 42
 
  def inner_func():
    print(age)
 
  inner_func() 
 
func()
# Here the output will be 42 because Python could find a name (age) in the enclosing scope and did 
# not continue to search for the value up into the global scope. If Python cannot find a name in any 
# of the four scopes it searches, it will return a NameError exception.
color = 'green'

def change_color(new_color):
  global color
  # Checkpoint #2
  to_update = new_color
  
  def disp_color():
    print('The original color was: ' + color)

  disp_color()
  # Checkpoint #3
  color = to_update
  print('The new color is: ' + color)

change_color('blue')







