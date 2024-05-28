# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:02:37 2023

@author: geron
"""

# We need to create classes for primary and high schools. Because these classes share properties and methods,
#  each will inherit from a parent School class. Our parent and three child classes have the following properties,
#  getters, setters, and methods:

# School
# Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
# Getters: all properties have getters
# Setters: the numberOfStudents property has a setter
# Methods: A __repr__ method that displays information about the school.
# Primary
# Includes everything in the School class, plus one additional property
# Properties: pickupPolicy (string, like "Pickup after 3pm")
# Middle
# Does not include any additional properties or methods
# High
# Includes everything in the School class, plus one additional property
# Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])

# instructions
# Create the School Class
# 1.
# Let’s start by making a parent class for Primary, Middle, and High classes.

# Create an empty class named School.


# Stuck? Get a hint
# 2.
# Inside the School class, create a constructor that accepts three parameters in addition to self. 
# The names of these parameters should match the properties listed in the narrative above.


# Hint
# A constructor is created using __init__(self, paramater1, parameter2, ...)

# 3.
# Inside the constructor, set the School properties equal to the values passed into the constructor. 
# Remember to use the self keyword when setting these properties.


# Hint
# For example, we used self.name = name to create a property named self.name and set it equal to the value 
# passed into the constructor.

# 4.
# Create getters for the name, level, and numberOfStudents properties. Each getter should return the value 
# saved to the property.


# Hint
# For example, here is our getter for the name property:

# def getName(self):
#   return self.name
# 5.
# Create a setter for numberOfStudents. This method should take one parameter (in addition to self) and 
# set self.numberOfStudents equal to the value passed into the method.


# Hint
# We called our parameter newNumberOfStudents and set self.numberOfStudents = newNumberOfStudents.

# 6.
# Create a __repr__() method so when a School is printed, it displays relevant information about the object. 
# You can choose what you want displayed, but we printed:

# A {level} school named {name} with {numberOfStudents} students


# Hint
# Recall that the __repr__() method should return the string that you want to be displayed when you print an 
# object of the class.

# 7.
# At this point, it’s probably a good idea to test your code if you haven’t already. Try creating a School object, 
# use the getter and setter methods you created, and print that object


# Hint
# Our code looked like this:

# a = School("Codecademy", "high", 100)
# print(a)
# print(a.getName())
# print(a.getLevel())
# a.setNumberOfStudents(200)
# print(a.getNumberOfStudents())
# Create the PrimarySchool class
# 8.
# Next, we’ll build a PrimarySchool class that inherits from School. If you feel comfortable building the 
# PrimarySchool class on your own, give it a shot. If not, use the steps below to help you along the way.

# Whether you want to follow the steps or not, it’s important to note, the PrimarySchool class only has one 
# additional property, pickupPolicy.

# Create an empty PrimarySchool class that inherits from School.


# Hint
# The following code creates a class named A that inherits from B:

# class A(B):
 
# 9.
# Inside the PrimarySchool class, create a constructor that accepts three arguments in addition to self. 
# Think about which three properties we’ll need arguments for.


# Hint
# We need arguments for name, numberOfStudents, and pickupPolicy. The level of a PrimarySchool will automatically 
# be set to primary.

# 10.
# Call super().__init__() on the first line of the PrimarySchool‘s constructor. Pass it any arguments that the 
# parent constructor uses.

# Since this is the PrimarySchool class, pass 'primary' as the argument for the level parameter in the parent constructor.


# Hint
# The arguments for the call to the superclass’ constructor should look like name, "primary", numberOfStudents.

# 11.
# You’ve used two of the arguments you’ve passed to the PrimarySchool constructor. Now use the third argument
#  to set the value of a new property named self.pickupPolicy.


# Hint
# Because we named that argument pickupPolicy, we have self.pickupPolicy = pickupPolicy.

# 12.
# Since our PrimarySchool class inherits Schools‘s properties and getters, we only need to create one new getter
#  in the PrimarySchool class. Add this getter to the PrimarySchool class. Each getter should return the value saved 
#  to that property.


# Hint
# We want to create a getPickupPolicy() method that returns self.pickupPolicy.

# 13.
# Finally, we probably want the __repr__() method for a PrimarySchool to display information about the pickupPolicy
#  variable. Override the __repr__() method so when a PrimarySchool is printed, information about the pickup policy 
#  is displayed in addition to the other information about the school.

# You can call super().__repr__() to avoid repeating some code.


# Hint
# This is what our overridden __repr__() method looks like. Notice we call the parent class’ __repr__() method 
# so we don’t repeat work.

# def __repr__(self):
#   parentRepr = super().__repr__()
#   return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)
# 14.
# Create a PrimarySchool object and verify your new constructor, getter method, and __repr__() method work as expected.


# Hint
# Our test code looked like this:

# b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
# print(b.getPickupPolicy())
# print(b)
# Create the HighSchool class
# 15.
# In this task, you will create a HighSchool class that inherits from the School class. In addition to the properties,
#  getters, and methods in School, the HighSchool includes the following:

# Properties: sportsTeams (list of strings)
# Getters: A getter for the sportsTeams array. The getter should return the list of the sports teams.
# Override the __repr__() method to display information about sportsTeams.
# Take a look at the Hint for step-by-step instructions.


# Hint
# Follow these steps to complete the task:

# Create an empty HighSchool class that inherits from School.
# Create a constructor that accepts arguments for name, numberOfStudents, and sportsTeams.
# On the first line of the constructor, call super().__init__() and pass it name, 'high', and numberOfStudents
#  as arguments.
# On the next line, set the sportsTeams property using self.sportsTeams = sportsTeams
# Under the constructor, create a getter for sportsTeams.
# Override the __repr__() method to display information about sportsTeams.
# 16.
# Once again, let’s test our code to make sure it works correctly. Create a High School object and verify your 
# new constructor, getter method, and __repr__() method work as expected.



print('Hello world!')
class School:
  def __init__(self, name, level, number):
    self.name = name
    self.level = level
    self.number = number
    
  def get_name(self):
    return self.name
  
  def get_level(self):
    return self.level

  def get_number(self):
    return self.number
  
  def set_number(self, new_number):
    self.number = new_number

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.number} students.'

a = School("Codecademy", "high", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_number(200)
print(a.get_number())


class PrimarySchool(School):
  def __init__(self, name, number, pickup):
    super().__init__(name, 'primary', number)
    self.pickup = pickup

  def get_pickup(self):
    return self.pickup
    
  def __repr__(self):
    primaryRepr = super().__repr__()
    return primaryRepr + f'The pickup policy is {self.pickup}'
    
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickup())
print(b)

class HighSchool(School):
  def __init__(self, name, number, sports):
    super().__init__(name, 'high', number)
    self.sports = sports

  def get_sports(self):
    return self.sports

  def __repr__(self):
    highRepr = super().__repr__()
    return highRepr + f"You can play the following sports: {self.sports}."

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sports())
print(c)

# output
#A high school named Codecademy with 100 students.
# Codecademy
# high
# 200
# Pickup Allowed
# A primary school named Codecademy with 300 students.The pickup policy is Pickup Allowed
# ['Tennis', 'Basketball']
# A high school named Codecademy High with 500 students.You can play the following sports: ['Tennis', 'Basketball'].











































