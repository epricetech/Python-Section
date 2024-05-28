# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:09:12 2023

@author: geron
"""

# names and namespaces
# every time you create a variable and assign a value that information is stored in pythons namespaces for each data type
#  when you call a variable python will look in the namespace for the data
#  There are 4 distinct namespaces in python
# 1. Built-in - highest level of namespaces - this is for the built-in names we can use in python like print() and str() ext
# 2. Global - These are non nested names. it is created when we run our main program and lives until program terminates
#  To see whats in the global namespace you can use globals() built in function 
# 3. Local - only exists inside ofa tunction and remains till function terminates - can be called using locals() function
# 4. Enclosing - special type of local namespace - they are created specifically when we work with nested functions
# and only exist when function is executing - can use enclosing() to see and locals()
print(dir(__builtins__))  #this will print all the built in namespaces currently working
print(globals()) # this will print all the global names in the namespace
print(locals()) # this will print all the local names in the namespace
print(enclosing())
# example of all 3
global_variable = 'global'
print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
print(globals())

# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1 / num2
  print(locals())

# Write Checkpoint 3 here:
def multiply(num1, num2):
  product = num1 * num2
  print(locals())

print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:
divide(3,4)

print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:
multiply(4,50)

print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals())

# Output:
#  -- Local and global Namespaces with empty script -- 

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4e8b14ac50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'script.py', '__cached__': None, 'global_variable': 'global'}
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4e8b14ac50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'script.py', '__cached__': None, 'global_variable': 'global'}
 
#  -- Local Namespace for divide -- 

# {'result': 0.75, 'num2': 4, 'num1': 3}
 
#  -- Local Namespace for multiply -- 

# {'product': 200, 'num2': 50, 'num1': 4}
 
#  -- Local Namespace final -- 

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4e8b14ac50>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'script.py', '__cached__': None, 'global_variable': 'global', 'divide': <function divide at 0x7f4e8b171e18>, 'multiply': <function multiply at 0x7f4e8af6bd08>}



# example of enclosing namespace
global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
 
  def inner_function():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    # Add locals() below
    print(locals())
  inner_function()
 
outer_function()
#output
#{'inner_nested_function': <function outer_function.<locals>.inner_function.<locals>.inner_nested_function at 0x7f80d313de18>, 'inner_value': 'inner'}

