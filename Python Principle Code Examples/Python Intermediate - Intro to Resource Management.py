# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:23:44 2023

@author: geron
"""

#  When talking about resource management with computers it is referring to the usage of memory, storage and power
#  If we dont manage these aspects it can lead to running out of memory, space or even crashes device
#  One way to manage these aspects is through the use of Context Managers
#  A Context Manager is an object that takes care of assigning and releasing resources like files, connections, database ect
#  example of a with statement which is an example of a context manager
with open("file_name.txt", "w") as file:
   file.write("How you gonna win when you ain't right within?")
# Here is what is happening in our small script:
# The with statement calls the built-in open() function on "file_name.txt" with a mode of "w" which represents write mode.
# The as clause assigns the object opened (the file) to a target variable called file, which can be accessed 
# inside of the context manager.
# file.write() writes a sentence to "file_name.txt"

# example of the same thing without the with statement
file = open("file_name.txt", "w")
try:
   file.write("How you gonna win when you ain't right within?")
finally:
   file.close()
# in this above option we would have to use the open() and .close() method on all the files we are working on.
#  but using the site statment it serves as a context manager where files are automatically closed after script
#  completion and we dont have to worry about forgetting to close a resource.  
#  example of using the try and finally vs the with context manager statement
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()
# with statement for conext manager
with open('file_name.txt', 'r') as open_file:
  print(open_file.read())
  

# Class Based Context Managers
# The Class based is one approch of creating context managers.  It requires explicitly defining and implements the 
#  two methods inside of a class
# 1.  An __enter__ method 
# The __enter__ method allows for the setup of context managers. This method commonly takes care of opening 
# resources (like files). This method also begins what is known as the runtime context - the period of time in 
# which a script runs. In our previous examples, it was the time in which the code passed into the with statement 
# code block was executed (basically everything under the with statement).
# 2. An __exit__ method
# The __exit__ ensures the breakdown of the context manager. This method commonly takes care of closing open 
# resources that are no longer in use.

# example of these 2 methods
class ContextManager:
  def __init__(self):
    print('Initializing class...')
 
  def __enter__(self):
    print('Entering context...')
 
  def __exit__(self, *exc):
    print('Exiting context...')
# here we define a new class and implemented the required 2 methods.  by defining these 2 methods we are implementing the
# context management protocol.  This allows us to immediately invoke the class using the with statement
with ContextManager() as cm:
  print('Code inside with statement')
#  Above we invoke the ContextManager class with a with statment
# output would be
# Initializing class...
# Entering context...
# Code inside with statement
# Exiting context...
#  The above context manager class is being executed in the following sequence
# 1. __ init__ method
# 2. __enter__ method
# 3. The code with the with statment
# 4. __exit__ method


# example of context manager with with statement and insturctions of what is going on
# Write your code below: 
#Let’s create a context manager that will work with files filled with creative poems. While we won’t directly 
#work with a file in this exercise, make sure to note the order of method execution in a context manager. 
#Don’t worry, we’ll work with an actual file soon! For now, we are just going to get comfortable with the basics.
#Create a class called PoemFiles. For now, give it a single pass statement so it won’t create an error when run.
#Next, remove the pass statement and create an __init__ method inside of the PoemFiles class that prints 
#'Creating Poems!
class PoemFiles:
  def __init__(self):
    print('Creating Poems!')
#Let’s implement the __enter__ method. Have the method print 'Opening poem file'.
  def __enter__(self):
    print('Opening poem file')    
#Lastly, create an __exit__ method that prints 'Closing poem file'.
  def __exit__(self, *exc):
    print('Closing Poem file')
##Awesome! Now we have our very own context manager! Let’s see it in action by calling it with a with statement.
#Have the with statement save the invoked class to a variable called manager and have it print a famous line from 
#the poet Emily Dickinson: 'Hope is the thing with feathers'.
with PoemFiles() as manager:
  print('hope is the thing with feathers')
  
  
# Example of class based context manager when working with files
class WorkWithFile:
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
 
  def __exit__(self, *exc):
    self.opened_file.close()
# Break down of above code
# 1.  __init__ method which is standard accross most classes - 3 paramaters
# self: This is standard for any class we work with and allows us to work with methods and properties we assign to an 
# instance of a class.

# file: Since we are working with files, we need to be able to take in a file argument when we call the class with 
# a with statement.

# mode: Lastly, we need to provide the file a mode. This allows us to manage what our context manager will actually 
# be doing, such as reading, writing, or both!
# Both file and mode arguments allow us to accomplish the following syntax:
# with WorkWithFile('file.txt', 'r')

# 2. __enter__ method - this is where we deal with opening the file we want
# Since any new instance of our context manager will have a file and mode property, we can pass them into the open() 
# function to open a specific file with a specific mode. Then, we save it as a variable called self.opened_file, 
# and return it.

# By returning self.opened_file, the file will be passed into the variable we define when we call it with the with 
# statement. So for example:

# with WorkWithFile('file.txt', 'r') as file
# Will assign the open file 'file.txt' to the variable called file that follows the as clause and thus allowing 
# us to use it in the with statement code block (which we will look at shortly).

# 3.  __exit__ method - which will close the file we work on and still take the *exc argument
# Now that we created our context manager, we can now use it in a with statement like so:

# with WorkWithFile("file.txt", "r") as file:
#   print(file.read())


# example and instructions of what we are doing
# Let’s build our poem context manager from earlier again! This time we will allow it to work on files. 
# By the end of these exercises, we will have a custom context manager that has written to a file!

# Create a class called PoemFiles and give it a __init__ method that defines a self, poem_file, and mode parameter.

# Inside the method, print 'Starting up a poem context manager'

# Checkpoint 2 Passed
# 2.
# Next, let’s built the properties of the class via __init__. Remember this is so we can pass a file name 
# and a mode when we call the context manager with the with statement.

# Inside of the __init_ method and under the print statement, assign two properties to the class:

# file that is equal to the poem_file parameter
# mode that is equal to the mode parameter
# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Next, let’s work on the __enter__ method to set up what happens when we want to start working on a file.

# Create an __enter__ method. Have the method print 'Opening poem file'.

# Checkpoint 4 Passed
# 4.
# In the __enter__ method, we will need to open the file we want to work on and return it! This way, it will be
#  assigned to the variable we declare when we work with the with statement.

# Inside __enter__ method give the class a new property called opened_poem_file and assign it to a call 
# of the open() function that takes two arguments:

# self.file: our classes file property
# self.mode: our classes mode property
# Lastly, return the opened_poem_file property!

# Checkpoint 5 Passed

# Stuck? Get a hint
# 5.
# Lastly, we need to create an __exit__ method.

# Write a __exit__ method that defines a self parameter and a *exc parameter. Make the method print 'Closing poem file'.

# Checkpoint 6 Passed
# 6.
# We need to make sure we close our file in the __exit__ method so we properly manage our resources.

# In the __exit__ method, under the print statement, call the .close() built-in function on the
#  opened_poem_file property of the class.

# Checkpoint 7 Passed

# Stuck? Get a hint
# 7.
# Uncomment the with statement and run the code. Check out poem.txt to see if the poem has been added!

# Note: in reality, we wouldn’t have to create a context manager that opens a file because there’s 
# already an open() built-in function that you can run with a with statement that will open and close a file. 
# However, open() has its limitations, and knowing this base structure will allow us to create our own custom and
#  more advanced context managers that can do much more than open()!
class PoemFiles:

  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
  
  def __exit__(self, *exc):
    print('Closing poem file')
    self.opened_poem_file.close()


with PoemFiles('poem.txt', 'w') as open_poem_file:
   open_poem_file.write('Hope is the thing with feathers')



#  Handeling Exceptions - regarding the exc paramater in the __exit__ method
#The __exit__ method is responsible for dealing with any exceptions.  It can implement how to close the file and
# any other operations we want to perform if an exception occures.  
# example
#def __exit__(self):
# output
#__exit__() takes 1 positional argument but 4 were given.
#Normally the __exit__ method needs 4 arguments but we can use * operator to tell the method will pass a variable
# number of arguments.  It is a good way to put the error on hold.
#  __exit__ method and the 3 required arguments that can be named anything.  in addition to the self argument
# 1. An exception type - which indicates the class of exception IE AttributeError class, or NameError class
# 2. An exception value - the actual value of the error
# 3.  A Traceback - a report detailing the sequences of steps that cause the error and all the details need to fix error
# example of __exit__ method with the 4 arguments
class OpenFile:
 
 def __init__(self, file, mode):
   self.file = file
   self.mode = mode
 
 def __enter__(self):
   self.opened_file = open(self.file, self.mode)
   return self.opened_file
 
 def __exit__(self, exc_type, exc_val, traceback):
   print(exc_type)
   print(exc_val)
   print(traceback)
   self.opened_file.close()
# in this example above we add a script that prints the exception values so if we run our with statement with a failure
#  it would output the following 
with OpenFile("file.txt", "r") as file:
  # .see() is not a real method
  print(file.see())
# output
# <class 'AttributeError'>
# '_io.TextIOWrapper' object has no attribute 'see'
# <traceback object at 0x7f08dcfb5040>
# Traceback (most recent call last):
#   File "script.py", line 14, in <module>
#     print(file.see())
# AttributeError: '_io.TextIOWrapper' object has no attribute 'see'

# now if we didnt have the .see() error from above the output of the __exit__ method would have printed
# None
# None
# None


# example - the first with statment errors with an attribute error because uppercasewords() method doesnt exist
class PoemFiles:

  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
#Let’s return to our trusty PoemFiles context manager. Unfortunately, it’s missing an __exit__ method. Now that we have seen how to set up the method to capture exception data, let’s build it out.
#Create an __exit__ method, and add the 4 necessary arguments: self, exc_type, exc_value, traceback. Have the method use 3 different print statements to print each exception argument. This will help us visualize the exceptions when we run into them!
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()

# First
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# Second
with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print("---- Exception data below ----")
  

# An exception that occurs in a context manager can be handled in two ways:
# If we want to throw an error when an error occurs, we can either:
# Return False after the .close() method
# Do nothing
# If we want to suppress the error, we can:
# Return True after the .close() method

# example of the 2 ways to handle the exceptions
class OpenFile:
 
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
 
  def __exit__(self, exc_type, exc_val, traceback):
    print(exc_type, exc_val, traceback)
    print("The exception has been handled")
    self.file.close()
    return True
# only difference from the example above is that we added a return true statment with will implement the suppression of an error
# to see it in action with 2 with statements.  one will throw an exception and other will not
with OpenFile("file.txt", "r") as file:
  # .see() is not a real method
  print(file.see())
 
with OpenFile("file.txt", "r") as file:
  print(file.read())
# output
# <class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'see' <traceback object at 0x7fedf822d180>
# The exception has been handled
# None None None

# #If we did not return True, the second (and all proceeding) with statements would not have run since an 
# exception would be hit.

# example of working with a TypeError
class OpenFile:
 
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
 
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
 
  def __exit__(self, exc_type, exc_val, traceback):
    self.file.close()
    if isinstance(exc_val, TypeError):
      # Handle TypeError here...
      print("The exception has been handled")
      return True
# the if statement that compares exc_val to a sepcific exception we are trying to catch.  Anything we want to happen
# for this specific exception can occur in the conditional code block.  Next we return True to make sure we
# surpress the excption from arising and stoping the rest of the code

#  Example 
class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Write your code below: 
    self.opened_poem_file.close()
    if isinstance(exc_value, AttributeError):
      return True

with PoemFiles('poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")


  
# Contextlib
#  Built in python module for creating context managers
#  contextlib allows for the creation of a context manager with the use of a generator funation
#  a function that uses yield instead of return.  and the contextlib decorator @contextmanager
#  instead of creaing a class and defining __enter__ and __exit methods we can use this function
#  First step is to import the module and decorator
from contextlib import contextmanager
# then we use the @contextmanager decorator to wrap a single generator function
 
@contextmanager
def open_file_contextlib(file, mode):
  opened_file = open(file, mode)
  try:
      yield opened_file
  finally:
       opened_file.close()
# We are doing a few things here:

# We have written a generator function called open_file_contextlib with the expectation that it will take in 
# two arguments, a file and a mode.
# We then use the built-in open() function to open the file (that we received as an argument) and save it to a 
# variable called opened_file.
# The function then will attempt (via a try statement) to yield the opened file and complete whatever code we 
# pass when we use it in conjunction with the with statement. More on this in a bit!
# Lastly the resource (file) will be closed once all the code is done being executed.

# once we have created the function and denoted it as a context manager with the decorator we can use our with statement
with open_file_contextlib('file.txt', 'w') as opened_file:
 opened_file.write('We just made a context manager using contexlib')


# example and instructions of what is going on
# Write your code below:
from contextlib import contextmanager
#Now, let’s create a generator function called poem_files that has two parameters file and mode. The function should do two things:
#Print 'Opening File'
#Open the file using open() with the file and mode parameters, and save the result to a variable called open_poem_file.
#Don’t forget to decorate it with the @contextmanager decorator.
@contextmanager
def poem_files(file,mode):
  print('Opening File')
  open_poem_file = open(file,mode)
#Next, we will have to create the try/finally structure. Inside of the function write the try clause, and inside of it use the yield keyword to yield the open_poem_file variable.
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
  print('Inside yield')
  opened_file.write('Rose is beautiful, Just like you.')
  

# dealing with the exceptions using the contextlib and @contextmanager decorator
#  For the decorator method errors are most commonly dealt with an except block between the try and finally block
#   there are 2 main ways to deal with errors
# 1. Throw and error and stop the execution of the entire program by excluding an except block
# 2. to catch error and continue the execuction of the program you add the except block
# Example of adding the except block for handling errors
from contextlib import contextmanager
 
@contextmanager
def open_file_contextlib(file, mode):
  open_file = open(file, mode)
 
  try:
   yield open_file
 
 # Exception Handling
  except Exception as exception:
   print('We hit an error: ' + str(exception))
 
  finally:
   open_file.close()
 
with open_file_contextlib('file.txt', 'w') as opened_file:
 opened_file.sign('We just made a context manager using contexlib')

# in this example When this context manager is called in the with statement above, it will hit the exception 
# block because .sign() is not a file method. The output would look like this:
# output
# We hit an error: '_io.TextIOWrapper' object has no attribute 'sign'


# Nested Context Managers
#  When needing to work with multiple resourses (files) at once context managers can be nested together in a with
# statement to manage multiple resources at the same time.
#  Here is an with statement that deales with 2 files
with open('teacher.txt', 'w') as teacher, open('student.txt', 'r') as student:
 teacher.write(student.read())
# descritption of what is happening above
# The with statement is being called once but invoking two context managers. This is a single-line nested with statement.
# Each context manager is separated by a comma and has its own target variable.
# Our teacher.txt file is being opened in write mode because it will be written into and our student.txt is 
# opened in read mode because we are attempting to copy the text into the teacher’s file
# The resulting teacher.txt file will now include everything that was in the student.txt file.
# Here we have chosen to use the open() built-in function rather than a custom context manager. 
# It is entirely possible to use our own in place of the open() function.

# another way of writing nested context manager which isnt much different than above but is clearer about the nesting
with open("teacher.txt", "w") as teacher:
   with open("student.txt", "r") as student:
     teacher.write(student.read())

# example of nested context managers
from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File', file)
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File', file)
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File', file)
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File', file)
    open_card_file.close()

# Checkpoint 1
with poem_files('poem.txt', 'r') as poem:
   with card_files('card.txt', 'w') as card:
     print(poem, card)
     # Checkpoint 2
     card.write(poem.read())

















