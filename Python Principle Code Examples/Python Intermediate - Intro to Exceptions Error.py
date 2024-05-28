# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:31:45 2023

@author: geron
"""

# in Python errors in code will occur.  It is important to know how to control errors and use them to your advantage
# Most common is the syntax error that we see all the time.  These errors are mistakes in the structure of the code
# they are caught during a special parsing stage before the program is executed.  They always prevent the entire program
# from running.  Basic syntax error output
#   File "script.py", line 1
#     def print_five
#                  ^
# SyntaxError: invalid syntax

# Exception Errors - occur with syntactically correct code.  Exceptions are runtime errors because they occur during
# program execution, only when the offending code (the part causing the error) is reached.  An example of an 
# exception error is a NameError - Basic syntax NameError 
# Traceback (most recent call last):
#   File "script.py", line 1, in <module>
#     print(five)
# NameError: name 'five' is not defined
# Syntax and exception errors make up the 2 core categories for any error we run into
# There are many different kinds of exception errors and Python has a tool for gaining insight into the various
# exception errors.  The Traceback is a summary that includes the exception type, a message, and the series of 
# function calls preceding the exception, along with file names and line numbers.  
# example of a traceback for a small program
# Imaginary file script.py
print(1/0)
# Traceback (most recent call last):
#   File "script.py", line 1, in <module>
#     print(1/0)
# ZeroDivisionError: division by zero
# the traceback above reading the bottom line we see exception type of ZeroDivisionError followd by a message
# we see the exception happened on line 1 of a file called script.py while calling the print command

# Built in Exceptions
#  NameError is one of many built in exception errors.  Others cover fields ranging from mathematical errors all 
# the way up to operating system errors.  
#  These exception errors are objects and most exceptions inherit directly from a class called Exception
#  However they are all derived directly or indirectly from the BaseExceptions class
#  We can examine the base classes using the __bases__ attribute on any specific exception
print(NameError.__bases__)
# output
# <class 'Exception'>
# we can even call __bases__ on the exception class to see origins
print(Exception.__bases__)
# output
#<class 'BaseException'>

# The full hierarchy of built-in exceptions is the following:

# BaseException
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError


# Raising Exceptions
# encountering exceptions isnt always an accident.  We can throw an exception at any time by using the raise keyword
#  We can raise an exception anytime we think a mistake has or will occur in our program.  This lets us stop program
# execution immediately and provide a useful error message instead of allowing mistakes to occur which might be hard 
# diagnose.  One way to use the raise keyword is by pairing it with a specifice exception class name.  We can either
# call the class by itself or call a constructor and provide a specific error message.
# example
raise NameError
# or 
raise NameError('Custom Message')
# Example of raising e TypeError for a function.
def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    # Alternatives: raise TypeError() or TypeError('Message')
    raise TypeError
# When an employee_status is not 'Authorized', the function open_register() will throw a TypeError and stop
# program execution.

# when no built in exception makes sense we can use a generic exception using the base Exception class and provide
# a single argument that serves as the error message.  
# example of raising Exception object with message
def open_register(employee_status):
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    raise Exception('Employee does not have access!')

# example of raise
# Checkpoint 1
instrument_catalog = {
    'Marimba': 1999,
    'Kora': 499,
    'Flute': 899
}

def print_instrument_price(instrument):
    # Checkpoint 2
    if instrument in instrument_catalog:
      print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    # Checkpoint 3
    else:
      raise KeyError(instrument + ' is not found in instrument catalog!')

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')
# output
# The price of a Marimba is 1999
# The price of a Flute is 899
# Traceback (most recent call last):
#   File "prices.py", line 18, in <module>
#     print_instrument_price('Piano')
#   File "prices.py", line 14, in print_instrument_price
#     raise KeyError(instrument + ' is not found in instrument catalog!')
# KeyError: 'Piano is not found in instrument catalog!'


# Try / Except Exceptions
# It is possible for a program to continue executing even after encountering an exception
#  This process is known as exception handling and uses try / except clauses
# flow chart for try / except
# Start - execute try clause - exception encountered - Yes - Execute except clause and then End or No - End
# Python will first attempt to execute code inside the try clause code block.
# If no exception is encountered in the code, the except clause is skipped and the program continues normally.
# If an exception does occur inside of the try code block, Python will immediately stop executing the code and
#  begin executing the code inside the except code block (sometimes called a handler).
# example
colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
}
 
for color in ('red', 'green', 'yellow'):
  try:
    print('The hex value of ' + color + ' is ' + colors[color])
  except:
    print('An exception occurred! Color does not exist.')
  print('Loop continues...')
# output
# The hex value of red is #FF0000
# Loop continues...
# An exception occurred! Color does not exist.
# Loop continues...
# The hex value of yellow is #FFFF00
# Loop continues...

# in above code the try block runs until it hit an exception.  The hex value for red was successfully printed
# before it tried to access the hex value for green which caused a KeyError since green is not in out coloros and 
# ran the code in the except block.  However, the exception was handled so Python continued executing our code and 
#went onto print the hex value of yellow.
# example of try and except
# Checkpoint 1
staff = {
  'Austin': {
      'floor managers': 1,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 0,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 2,
      'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  # Checkpoint 2
  try:
    print_staff_report(location, staff)
  # Checkpoint 3
  except:
    print('Could not print sales report for ' + location)
#We successfully printed the staff report for Austin, but we hit an exception (ZeroDivisionError) when trying 
# to print out the ratio for Melbourne since we attempted to divide 8 by 0.
# output
# Instrument World Austin has:
# 5 sales employees
# 1 floor managers
# The ratio of sales people to managers is 5.0

# Could not print sales report for Melbourne
# Instrument World Beijing has:
# 5 sales employees
# 2 floor managers
# The ratio of sales people to managers is 2.5


# Catching Specific Exceptions
# above examples handled any exception hit during the try clause - however it is better to be as specific as 
# possible with the exception we want to raise.  
#  We can catcha specific exception by listing it after the except keyword - Example
try:
    print(undefined_var)
except NameError:
    print('We hit a NameError')
# in this example the except block is only executed if a NameError is encountered in the try block rather than any
# exception.  if any other exception occurs it is unhandled and program terminates
#  When we specify exception types, Python also allows us to capture the exception object using the as keyword. 
# The exception object hosts information about the specific error that occurred. Examine our previous function but
#  now capturing the exception object as errorObject:
try:
    print(undefined_var)
except NameError as errorObject:
    print('We hit a NameError')
    print(errorObject)
# output
# We hit a NameError
# name 'undefined_var' is not defined
# the errorObject is an arbitrary name and we can use anything we want - example
try:
    print(undefined_var)
except NameError as e:
    print('We hit a NameError')
    print(e)

# example of being specific with exception type in try and except
staff = {
  'Austin': {
    'floor managers': 1,
    'sales associates': 5
  },
  'Melbourne': {
    'floor managers': 0,
    'sales associates': 8
  },
  'Beijing': {
    'floor managers': 2,
    'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
      print_staff_report(location, staff)
  # Write your code below:
  except ZeroDivisionError as e:
      print('Could not print sales report for ' + location)
      print(e)
# output
# Instrument World Austin has:
# 5 sales employees
# 1 floor managers
# The ratio of sales people to managers is 5.0

# Could not print sales report for Melbourne
# division by zero
# Instrument World Beijing has:
# 5 sales employees
# 2 floor managers
# The ratio of sales people to managers is 2.5


# Handling Multiple Exceptions
# We can list more than one exception type in a tuple with a single except clause
# example of syntax
try:
    # Some code to try!
except (NameError, ZeroDivisionError) as e:
    print('We hit an Exception!')
    print(e)
# in above example we expect to encounter either a NameError or ZeroDivisionError.  We can list any number of exceptions
# in this tuple format as long as it makes sense for the code in out try block. This is where we can see the benefit
 # of capturing our exception object (via the as clause) since it enables us to print (or operate on) the 
 # specific exception that is caught. 
# we can also pair multiple except clauses with a single try clause enabling specific exceptions to be handled differently
#  example
try:
    # Some code to try!
except NameError:
    print('We hit a NameError Exception!')
except KeyError:
    print('We hit a TypeError Exception!')
except Exception:
    print('We hit an exception that is not a NameError or TypeError!')
# in above program NameError or KeyError will trigger one of the first 2 exception handlers.  Any other exceptions will
# trigger the third handler.  Order of handlers are imporant and python will execute the first one that matches it type
# best practice is use the last except clause as a generic Exception as a backup if no other specific 
#exception gets caught.

# example
instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo'
discount = '20'

# Write your code below:
try:
  display_discounted_price(instrument, discount)
except KeyError:
  print('An invalid instrument was entered!')
except TypeError:
  print('Discount percentage must be a number!')
except Exception:
  print('Hit an exception other than KeyError or TypeError!')


# Else clause with try and except exception error handlers
#  The else clause allows us to run some code if we do not encounter an exception
# Flow chart 
## Start - execute try clause - exception encountered - Yes - Execute except clause and then End or No - execute else clause then end
# example of try except and else
# Checkpoint 1
customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Checkpoint 2
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print('Customer was not found in rewards program!')
  # Checkpoint 3
  else:
    print('Rewards account number is: ' + str(rewards_number))

# Checkpoint 4
customer = 'Mario'
display_rewards_account(customer)
# output
# Rewards account number is: 17849


# The Finally Clause
# This allows you to execute code regardless of whether an exception occurs
# flow chart
# Start - execute try clause - exception encountered - Yes - Execute except clause and then execute finally clause then End
# or No - execute else clause then execute finally clause then end
# example
try:
  check_password()
except ValueError:
  print('Wrong Password! Try again!')
else:
  login_user()
  # 20 other lines of imaginary code
finally:
  load_footer()
# The finally clause can be used independently without except or else
# example
try:
    check_password()
finally:
    load_footer()
    # Other code we always want to run 

# example of finally clause
import database

instrument = 'Kora'
database.connect_to_database()

try:
  database.display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
# Write your code below: 
finally:
  database.disconnect_from_database()


# user defined exceptions - alows us to create our own when built in options are not the best to use
# Core syntax
class CustomError(Exception):
    pass
# All we have to do to create a custom exception is to derive a subclass from the built-in Exception class.
#Example of concept
# Let’s imagine that Instrument World has an optional delivery service for instruments. If someone tries to schedule a
#  delivery but their address is too far, we want to raise a custom LocationTooFarError exception. 
#  This isn’t a type of exception that is built into Python, but rather one that is specific to our program and use case.
#  Here is what our program might look like utilizing this custom exception:
class LocationTooFarError(Exception):
   pass
 
def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarError
    else:
        print('Scheduling the delivery...')
# above we have a class LocationTooFarError that inherits from Exceptionclass.  By doing this we tell python
# e want to us the class as our own custom exception
#Now, if we call schedule_delivery(20), we get the following output:
# Traceback (most recent call last):
#   File "inventory.py", line 10, in <module>
#     schedule_delivery(20)
#   File "inventory.py", line 6, in schedule_delivery
#     raise LocationTooFarError
# __main__.LocationTooFarError

# example
inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}


#Write your code below (Checkpoint 2):
class InventoryError(Exception):
  pass


def submit_order(instrument, quantity):
  supply = inventory[instrument]
  if quantity > supply:
    raise InventoryError
  else:
  # Write your code below (Checkpoint 3 & 4): 
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
# output
# Traceback (most recent call last):
#   File "inventory.py", line 24, in <module>
#     submit_order(instrument, quantity)
#   File "inventory.py", line 16, in submit_order
#     raise InventoryError
# __main__.InventoryError


# Customizing User defined exceptions
# adding more functionality and messages to your user defined exception
# example of adding a message to our exception
class LocationTooFarError(Exception):
   def __init__(self, distance):
       self.distance = distance
 
   def __str__(self):
        return 'Location is not within 10 km: ' + str(self.distance)
# Let’s break this down:

# Our class definition doesn’t look much different from before. We have a class named LocationTooFarError that still 
# inherits from the built-in Exception class.
# We have added a constructor that is going to take in a distance argument when we instantiate our exception class.
#  Here, we have overridden the constructor of the Exception class to accept our own custom argument of distance. 
#  The reason for taking in a distance is to use it in our __str__ method that will return a custom error message 
#  when the exception is hit!
# The __str__ method provides our exception a custom message by returning a string with the distance property from 
# the constructor.
# example
def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarError(distance_from_store)
    else:
        print('Scheduling the delivery...')
# output
# Traceback (most recent call last):
#   File "inventory.py", line 14, in <module>
#     schedule_delivery(20)
#   File "inventory.py", line 11, in schedule_delivery
#     raise LocationTooFarError(distance_from_store)
# __main__.LocationTooFarError: Location is not within 10 km: 20

# example of user defined exception
class InventoryError(Exception):
  def __init__(self, supply):
    self.supply = supply

  def __str__(self):
    return 'Available supply is only ' + str(self.supply)

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  if quantity > supply:
    raise InventoryError(supply)
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
# output
# Traceback (most recent call last):
#   File "inventory.py", line 24, in <module>
#     submit_order(instrument, quantity)
#   File "inventory.py", line 17, in submit_order
#     raise InventoryError(supply)
# __main__.InventoryError: Available supply is only 3

















































