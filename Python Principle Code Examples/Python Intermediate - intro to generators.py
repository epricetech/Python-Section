# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 08:27:04 2023

@author: geron
"""

# Generator - allows for the creation of iterators without having to implement __iter__() and __next__() methods
#  two types of generators in python
# 1. General functions
# 2. General Expressions
#  Both of these return a generator object that can be looped over simial to a list, but the contents of the 
# generator object are not stored in memory allowing for complex and even infinte iteration of data
# generator functions must return an iterator but instead of using return like a regular function it uses yield
# Yield VS Return when working with Gernator functions vs regular functions
# awith yield any code written after a yeild experession will execute on the next iteration of the iterator. Code
# written after a return statement will not execute thus a major difference
# another difference is that the yield expression will suspend the execution of the function and preserve any local
# variables that exist within the function.  With rreturn statement it will terminate the function immediately and return
# return the result(s) to the caller.
#  like all objects the iterator object returned by a generator function can be stored in a variable
# example of yield expression used within a generator function
def course_generator():
  yield 'Computer Science'
  yield 'Art'
  yield 'Business'
# this function will return an iterator that contains those 3 string values.  on each iteration of the iterator
# each yield will return its corresponding course value
courses = course_generator()
for course in courses:
    print(course)
# output
# Computer Science
# Art
# Business

# another example of yield 
def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()
for classes in class_standings:
  print(classes)
#output
# Freshman
# Sophomore
# Junior
# Senior


# next() and StopIteration for Generator functions
# Generator functions return an iterator objext that contains tranversable values.  To get to the next value
# from a generator object we use the next() function which will cause the generator function to resume its
# execution until the next yield expression is found.  And keep going til no yield expressions are found and
# StopIteration is raised.  also yield can occur inside of a loop
# example we have a dictionary with student and student id.  We want to hold raffle where student id is a multiple of 3
# wins prize A and studentid whos multiple of 5 wins prize B ext
def prize_generator():
  student_info = {
    "Joan Stark": 355,
    "Billy Mars": 45,
    "Tori Rivers": 18,
    "Kyle Newman": 25
  }
 
  for student in student_info:
    name = student
    id = student_info[name]
    if id % 3 == 0 and id % 5 == 0:
      yield student + " gets prize C"
    elif id % 3 == 0:
      yield student + " gets prize A"
    elif id % 5 == 0:
      yield student + " gets prize B"
# breakdown Since this is a generator function, the local variable dictionary, student_info is preserved while the 
# function executes with each next() call. We can see this by creating a variable prizes that calls the 
# prize_generator() function and then calling next() on it. Let’s have a look:
prizes = prize_generator()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))
#output
# Joan Stark gets prize B
# Billy Mars gets prize C
# Tori Rivers gets prize A
# Kyle Newman gets prize B
# if we were to call another next() function we would get a StopIteration exception since dictionary has been exhausted

# example and insturctions
def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
 # Write your code below:
#Finish the function by adding a for loop that traverses through the student_standings list and yields 500 for each 'Freshman' value.
  for standing in student_standings:
    if standing == 'Freshman':
      yield 500

# Outside the function, retrieve the iterator object by calling student_standing_generator() and set it to a variable called standing_values.
standing_values = student_standing_generator()
#Print out the values within the returned standing_values generator using the Python built-in function next().
#Two values of 500 should be retrieved since our student_standings list contained two 'Freshman' values.

print(next(standing_values))
print(next(standing_values))
print(next(standing_values))
# last print statement creates StopIteration exception


# Generator Expressions
#  These allow for a single ine definition and creation of an iterator which replaces can replace the full examples above
# gernator expressions syntax is simialar to a list with various differences
# Generator Expressions	- List Comprehensions
# Returns a newly defined iterator -	Returns a new list
# Uses parentheses -	Uses brackets
# example of the 2.  A list and a generator expression - difference is the brackes and parentheses
# List comprehension
a_list = [i*i for i in range(4)]
# Generator comprehension
a_generator = (i*i for i in range(4))
#  now the a_generator is a generator object and cannot be accessed directly like a list so to retrieve the values
# we must traverse them to retrieve - aka loop
#Since our generator expression returns an iterator object, we can loop through to obtain the values within it:
for i in a_generator:
    print(i)
#output
# 0
# 1
# 4
# 9

# example and instructions
def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Write your code below:
#Given the defined generator function cs_generator(), retrieve a generator object by calling cs_generator() and 
# set it to a variable called cs_courses. Print out the values within the iterator using a for loop.
cs_courses = cs_generator()
for course in cs_courses:
  print(course)

#After the for loop, create an iterator using a generator expression and put it in a variable called cs_generator_exp.
 # The iterator should produce the same output as cs_generator().
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))
#Print out the values of the cs_generator_exp iterator object using a for loop. The output should match the for
 # loop print output of iterating over cs_courses.
for course in cs_generator_exp:
  print(course)


# Generator Methods - send() - special methods to maniplulte generators
#  the .send() method allos us to send a value to a generator using the yield expression.  If you assing yield
# to a variable the argument passed to the .send() method will be assigned to that variable.  Calling .send()
# will also cause the generator to perform an iteration
# example of the send method and breakdown
def count_generator():
  while True:
    n = yield
    print(n)
 
my_generator = count_generator()
next(my_generator) # 1st Iteration Output: 
next(my_generator) # 2nd Iteration Output: None
my_generator.send(3) # 3rd Iteration Output: 3
next(my_generator) # 4th Iteration Output: None
# above the generator definition contains n = yield which will assign the value in yield to N which will be None
# unless a value is passed using .send()
# The last 4 lines are 4 iterations.  3 using the next() and one using .send()
# The 1st iteration creates no output since the execution stops at n = yield which is before print(n).
# The 2nd iteration assigns None to n through the n = yield expression. None is printed.
# The 3rd iteration is caused by my_generator.send(3). The value 3 is passed through yield and assigned to n. 3 is printed.
# The last, and 4th, iteration, assigns None to n. None is printed.

# the .send() method can control the value of the generator when a second variable is introduced.  One variable 
# holds the iteration value and the other holds the value passed through yield
# example and breakdown
def generator():
  count = 0
  while True:
    n = yield count
    if n is not None:
      count = n
    count += 1
 
my_generator = generator()
print(next(my_generator)) # Output: 0
print(next(my_generator)) # Output: 1
print(my_generator.send(3)) # Output: 4
print(next(my_generator)) # Output: 5
# above the generator function defines count = 0 as the iteration value.  N is used to hold the value provided
# by yield.  The updated line n = yield count has 2 behaviors
# 1. At the start of each iteration the value provided by yield is assigned to n. This value will be None when next() 
#causes an iteration or it will be equal to the value passed using .send()
# 2. At the end of each iteration, the value stored in count is returned by the generator.
#If n is not None the value stored in n can be assigned to the iterator variable, count. This allows the iterator 
# to only change the value of count when the .send() method is called.

# example and insructions
MAX_STUDENTS = 50
#You are a teacher with a roster of 50 students. You have created a generator, get_student_ids(), that outputs each student’s id which you then use for assignment grading.
#Things to note about the code in the workspace:
#MAX_STUDENTS is set to 50 and is used in the while loop condition to cutoff the iteration.
#student_id is initialized to 1 and is incremented at the bottom of the while loop.
#The generator currently uses yield to return student_id at the end of each iteration.
#A for loop at the bottom of the code iterates through the generator object student_id_generator and outputs each id.
#Run the code to see all 50 ids printed.
def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
#When you are interrupted while grading, you need to pick up where you left off! This requires you to start the id generation at a number higher than 1. One way to solve this problem is to change the generator to support the .send() method. Inside get_student_ids():Change the yield expression so the value from yield is assigned to n.
#Just below the yield expression check that n is not equal to None. If they are not equal, assign the value of n to student_id.
#Still inside the if statement, stop student_id from incrementing by skipping the rest of the iteration.
#When you run the code, you should see no change.
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  # Write your code below
#To start the iteration at a different id, you want to send the generator a new value during the first iteration.
#Inside the for loop and before print(i):
#Check if i is equal to the first id number, 1.
#If so, set i to the return value of the student_id_generator.send() method.
#Set the argument for the .send() method so the output starts at 25.
  if i == 1:
    i = student_id_generator.send(25)
  print(i)


#  Generator Methods - throw()
# throw() provides the ability to throw an exception inside the generator from the caller point.  Can be useful
# if we need to end the generator once it reaches a certain value or condition
# example of throw
def generator():
  i = 0
  while True:
    yield i
    i += 1
 
my_generator = generator()
for item in my_generator:
    if item == 3:
        my_generator.throw(ValueError, "Bad value given")
        
# example of throw and instructions of what we are trying to do
def student_counter():
  for i in range(1,5001):
    yield i
# We only want to retrieve information on the first 100 students. Use the throw() method to throw a ValueError of “Invalid student ID” if the iterated student ID goes over 100. Insert your code before the print(student_id) line.
student_generator = student_counter()
for student_id in student_generator:
  if student_id > 100:
    student_generator.throw(ValueError, "Invalid student ID")
  print(student_id)


# Generator Method - close()
# .close() method is used to terminate a generator early.  Once the .close() method is called the generator is 
# finished just like the end of a for loop.  Any further iterations attempts will raise an StopIteration exception
# example and breakdown
def generator():
  i = 0
  while True:
    yield i
    i += 1
 
my_generator = generator()
next(my_generator)
next(my_generator)
my_generator.close()
next(my_generator) # raises StopGenerator exception
# above my/-generator() holds an infinite generator object.  After a couple of next(my_generator) calls
# the my_generator.close() is called.  When we try another next() method oafter it will give the StopIteration exception
# The .close() method works by raising a GeneratorExit exceptiion inside the generator function.  
#  the exception is usually ignored but can be handled by using try and except
# example and breakdown
def generator():
  i = 0
  while True:
    try:
      yield i
    except GeneratorExit:
      print("Early exit, BYE!")
      break
    i += 1
 
my_generator = generator()
for item in my_generator:
  print(item)
  if item == 1:
    my_generator.close()
#output
# 0
# 1
# Early exit, BYE!
# Putting the yield expression in a try block we can handle the GeneratorExit exception. In this case, we simply 
# print out a message. Because we interrupted the automatic behavior of the .close() method, we must also use a 
# break to exit the loop or else a RuntimeError will occur.

# example and instrucaiton
#We have a collection of 5,000 students. We only want to retrieve information on the first 100 students. 
# Use the close() method to terminate the generator after 100 students.

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  # Write your code below:
  if student_id >= 100:
    student_generator.close()


# connecting Generators
#  very similar to the chain() method in itertools.  In order to connect generators we use the yield from statement
# example and breakdown
def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'
 
def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'
 
 
def all_courses():
    yield from cs_courses()
    yield from art_courses()
 
combined_generator = all_courses()
# We have a generator function called cs_courses() that yields two results, 'Computer Science' and
#  'Artificial Intelligence'.
# We have another generator function called art_courses() that will yield two separate results,
#  'Intro to Art' and 'Selecting Mediums'.
# Our all_courses() generator function will yield results from both cs_courses() and art_courses() 
# to create one combined generator with all four string values representing the courses.
# If we iterate through each value within combined_generator using print() and next(), we can see that yield from 
# retrieves each individual yield item at a time in the order that the yields are called within the generator functions.
print(next(combined_generator))
print(next(combined_generator))
print(next(combined_generator))
print(next(combined_generator))
# output
# Computer Science
# Artificial Intelligence
# Intro to Art
# Selecting Mediums

# example and instructions
def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
# Write your code below
#We have a generator function called science students(x) that yields science major students with student IDs 1 to x. We have another generator function, non_science_students(x,y), that yields non-science major students with student IDs x-y. We want to retrieve student ids in the following order:
#Science students with IDs 1-5
#Non-science students with IDs 10-15
#Non-science students with IDs 25-30
#Use a connected generator function called combined_students that uses yield from statements to achieve this.
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10,15)
  yield from non_science_students(25,30)
# Checkpoint 2
#Call the combined_students() combined generator function and set it to a variable named student_generator. Print out the results using a for loop.
student_generator = combined_students()
for i in student_generator:
  print (i)


# Generator Pipelines - allows us to use multiple generators to perform a series of operations all whichin one 
# expression.  To pipeline generators the output of one generator function can be the input of another generator function
#  the resulting generator can then be used as input for another generator function and so on and so forth
#  The pipeline are also known as nested generators
# example and breakdown
def number_generator():
  i = 0
  while True:
    yield i
    i += 1
 
def even_number_generator(numbers):
  for n in numbers:
    if n % 2 == 0:
      yield n
 
even_numbers = even_number_generator(number_generator())
 
for e in even_numbers:
  print(e)
  if e == 100:
    break
#t he infinite generator number_generator() that yields numbers incrementing by 1
# The infinite generator even_number_generator() which takes a generator as a parameter, iterates through that
#  generator and only yields even numbers.
# The even_numbers variable which holds an even_number_generator() object with number_generator() as its argument.
# When we iterate over even_numbers only even numbers are output. The even_number_generator() iterates over all 
# numbers using number_generator(). When an even number occurs, that number is returned by even_number_generator().
# example and instructions
def course_generator():
    yield ('Computer Science', 5)
    # Checkpoint 1
    yield ('Art', 10)
    yield ('Business', 15)
#We have three courses:Computer Science which has 5 students Art which has 10 students Business which has 15 students First, complete the generator function called course_generator that can yield tuples of (Course name, Number students) for the above courses and the corresponding number of students. The first tuple for Computer Science has been provided.
# Checkpoint 2
#We need to add 5 students to each course. Create a generator function called add_five_students that takes in an input variable called courses. This courses object contains tuples of (Course name, Number of students). The add_five_students generator function should loop through the courses input object.
#On each iteration, it should yield a tuple containing the course name and number of students plus 5. The resulting generator that is yielded should have the following values:
#Computer Science with 10 students
#Art with 15 students
#Business with 20 students.
def add_five_students(courses):
    for course, num_students in courses:
        yield (course, num_students + 5)

# Checkpoint 3
#se a pipeline generator (nested generator) to get the resulting generator that has the 5 added students to each course. Set it to a variable called increased_courses.
#Print out each course tuple in the resulting increased_courses generator using a for loop.
increased_courses = add_five_students(course_generator())
for course in increased_courses:
    print(course)
# output
#     ('Computer Science', 10)
# ('Art', 15)
# ('Business', 20)


# another example and instructions
# Create a generator function called graduation_countdown() that will countdown the number of days left before
#  student graduation. It should take in as input days and yield one less day on each next() call, so the last value
#  yielded is 0. Use a while loop for yielding and decrementing the day.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# Create an equivalent generator expression called countdown_generator for the graduation_countdown generator function.
#  It should generate the days in a descending order starting from the provided days value. Place the code after 
#  the days = 25 line.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Modify the graduation_countdown() generator function to accept values sent using send(). Use a local variable 
# called days_left to store sent values. Use an if/else statement to check for sent values.

# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Call the graduation_countdown() function and set it to a variable called grad_days.

# Iterate through grad_days generator to print the number of days left with a string of “Days Left: x” where x 
# represents the countdown value.

# On the 15th day of the graduation countdown, the school president announces that graduation will be moved up 5 days.
#  Send a value of 10 to the grad_days generator when the 15th day in the countdown is reached.

# Checkpoint 5 Passed

# Stuck? Get a hint
# 5.
# It’s our lucky day! The school president announces that graduation will now occur on the 3rd day left of the countdown. 
# Modify the for loop so that when the countdown day is 3, the generator will close. Insert the condition
#  check and close() before the “Days Left” printout.

# Checkpoint 6 Passed

# Stuck? Get a hint
# 6.
# We have three honors achievements to assign to students that are defined within the summa(), magna(), and 
# cum_laude() generator functions. Each honor is assigned based on a given GPA range listed below. Given a
#  list of input GPAs, create a generator function called honors_generator that takes in 1 input argument 
#  named gpas that represents the list of GPAs from the variable gpas. The function should use yield from 
#  on each input GPA to determine the honors assignment.

# Honors Assignment	GPA
# Summa Cum Laude	> 3.9
# Magna Cum Laude	> 3.7
# Cum Laude	> 3.5
# Checkpoint 7 Passed

# Stuck? Get a hint
# 7.
# Call the connected generator function honors_generator with the gpas list and set it to a variable called honors.
#  Loop through the honors generator and print out each honor_label value to see which honors labels will be generated
#  given the gpas list.
def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude' 

def cum_laude():
    yield 'Cum Laude'

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()


def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1


days = 25
countdown_generator = (day for day in range(days, -1,-1))
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: " + str(day))


days = 25
gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)























