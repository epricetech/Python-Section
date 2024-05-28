# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:36:52 2023

@author: geron
"""

# there are many different data types in python
# boolean - true or false
# int - and integer
# string - string value
# float - a number with a decimal or to the power of 10 using the notation e
# tuple - similar to list but it is immutable - means cant be changed - written by using () and call using []
# Unpacking tuples - you can set the data in the tuple to variables in order
# Example name, age, occupation = tuple
# list - list of values using []
# range - using range() and setting a paramater
# mapping data - dictionary {}
# set data types - set, frozen set - they are unordered lists - used to figure out cross over connections venn diagram

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# Example	Data Type	Try it
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	Data Type	Try it
# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview


# example of creating a string and bool data type an using type() method to see the data type
my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

#example of string and in
a_string = "Cool String"
an_int = 12
print(type(a_string))
# prints "<class 'str'>"
print(type(an_int))
# prints "<class 'int'>"
# example of int
print(type(5))
# prints class int
# example of dicitonary
my_dict = {}
print(type(my_dict))
# prints class dict
#example of list
my_list = []
print(type(my_list))
# print class list

# floats
#A number with a decimal point is called a float. You can define floats
#with numbers after the decimal point or by just including a decimal point
#at the end:

float1 = 1.0
float2 = 10.
float3 = -5.5
#You can also define a float using scientific notation, with e indicating the power of 10:
# this evaluates to 150:
float4 = 1.5e2

#However, if the numbers do not divide evenly, the result of the division
#is truncated into an integer. In other words, the quotient is rounded
#down to a whole number. This can be surprising when you expect to
#receive a decimal and you receive a rounded-down integer:

quotient = 7/2
# the value of quotient is 3, even though the result of the division
#here is 3.5
To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:

quotient1 = 7./2
# the value of quotient1 is 3.5
quotient2 = 7/2.
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5
An alternative way is to use the float() method:

quotient1 = float(7)/2
# the value of quotient1 is 3.5
























