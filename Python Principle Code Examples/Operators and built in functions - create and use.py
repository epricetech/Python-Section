# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:39:19 2023

@author: geron
"""

# operators - what is use in doing any kinds of math equations in pythong
#  built in functions- prebuilt functions in python that accomplish a specific task


# Operators
# Arithmetic Operators
# Python has the following arithmetic operators:

# Addition, +, which returns the sum of two numbers.
# Subtraction, -, which returns the difference of two numbers.
# Multiplication, *, which returns the product of two numbers.
# Division, /, which returns the quotient of two numbers.
# Exponentiation, **, which returns the value of one number raised to the power of another.
# Modulus, %, which returns the remainder of one number divided by another.
# Floor division, //, which returns the integer quotient of two numbers.
# Assignment Operators
# Python includes the following assignment operators:

# The = operator assigns the value on the right to the variable on the left.
# The += operator updates a variable by incrementing its value and reassigning it.
# The -= operator updates a variable by decrementing its value and reassigning it.
# using += will add the variable on the left side to the right side
# and will replace the value of the left side varible.
# using -= will subract the variable on the right side from the left side
# The *= operator updates a variable by multiplying its value and reassigning it.
# The /= operator updates a variable by dividing its value and reassigning it.
# The %= operator updates a variable by calculating its modulus against another value and reassigning it.
# Comparison Operators
# Python has the following comparison operators:

# Equal, ==, for returning True if two values are equal.
# Not equal, !=, for returning True if two values are not equal.
# Less than, <, for returning True if left value less than right value.
# Less than or equal to, <=, for returning True if left value is less than or equal to right value.
# Greater than, >, for returning True if left value greater than right value.
# Greater than or equal to, >=, for returning True if left value greater than or equal to right value.
# “”” or ‘’’  Used when you need multiple line strings.




# and - or - not - operators - used to test a statement to see if it is true or not.  and means both need to be true and or
# means only one needs to be true and not evaluates to its inverse value. 
# True and True # Evaluates to True
# True and False # Evaluates to False
# False and False # Evaluates to False
# 1 == 1 and 1 < 2 # Evaluates to True
# 1 < 2 and 3 < 1 # Evaluates to False
# "Yes" and 100 # Evaluates to True
# True or True # Evaluates to True
# True or False # Evaluates to True
# False or False # Evaluates to False
# 1 < 2 or 3 < 1 # Evaluates to True
# 3 < 1 or 1 > 6 # Evaluates to False
# 1 == 1 or 1 < 2 # Evaluates to True
# not True # Evaluates to False
# not False # Evaluates to True
# 1 > 2 # Evaluates to False
# not 1 > 2 # Evaluates to True
# 1 == 1 # Evaluates to True
# not 1 == 1 # Evaluates to False


# built in functions
# example of min, max and round
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
rounded_price = round(tshirt_price, 1)
print(rounded_price)

# Len() - Used to find the length of the string value.  hello.py
# Example
# 	Print (len(variable))

# Str - int - float
# 	Used to convert the value to a specific format.  File hello.py
# Example:
# 	print (str(29))
# print (int('29'))
# print (float('10'))

# example of these options
print("Hello Worl")
print("Whats is your name?")  # asks for name
myName = input()
print("it is good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))  # len( function finds the length of the string value)
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")
print(str(29))
print(int("29"))
print(float("10"))
print("I am " + str(29) + " Years old.")
print("You will be " + str(int(myAge) + 1) + " in a year.")
print("You will be " + str(int("4") + 1) + "in a year.")
print("you will be " + str(5) + " in a year.")
print("You will be " + str(4 + 1) + " in a year.")
print("you will be " + "  5  " + " in a year.")
print("You will be 5" + " in a year.")
print("You will be 5 in a year.")
# Rational operators copare 2 values and evaluate down to a single boolean value
# ==  equal to
#  !=  no equal to
#  <less than  >  Greater than  <=  less than or equal too  >= greater than or equal too
#  3 boolean operators    and, or & not

# (4<5) and (5<6)


#  hasattr() and getattr() built in functions
# hasattr() will return true if an object has the given named attribute
# hasattr() Parameters
# The hasattr() method takes two parameters:

# object - object whose named attribute is to be checked
# name - name of the attribute to be searched
class Person:
    age = 23
    name = "Adam"

person = Person()

print("Person's age:", hasattr(person, "age"))
print("Person's salary:", hasattr(person, "salary"))
# Output:
# Person's age: True
# Person's salary: False

# getattr - returns the value of the named attribute of an object.  if not found it returns the defualt value 
# provided in the funciton
# getattr() Parameters
# getattr() method takes multiple parameters:

# object - object whose named attribute's value is to be returned
# name - string that contains the attribute's name
# default (Optional) - value that is returned when the named attribute is not found
class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

name = getattr(person, 'name')
print(name)

marks = getattr(person, 'marks')
print(marks)

# Output: Sheeran
#         88

# example of when named attribute is not found
class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
print('The sex is:', getattr(person, 'sex'))


# math equation info about floats and quotients
# to find the remainder of a math equation you will use the %
# Example is 1398 % 11 which will give the remainder of 1398/11

# using += will add the variable on the left side to the right side
# and will replace the value of the left side varible.
# using -= will subract the variable on the right side from the left side

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
#To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:

quotient1 = 7./2
# the value of quotient1 is 3.5
quotient2 = 7/2.
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5
#An alternative way is to use the float() method:

quotient1 = float(7)/2
# the value of quotient1 is 3.5



















