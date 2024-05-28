# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 12:10:21 2023

@author: geron
"""

# #It’s the first day of summer and you have a new incoming class of elementary students to prepare for in the coming months!

# First, look at the code in roster.py. You have been provided a roster of students for the 10 children in your class.
#  Each child’s record contains name, age, height (in inches), favorite classroom subject, and favorite animal to help 
#  you get to know them better.

# We’ve learned that an iterable is simply a Python object that can be traversed. This list of dictionaries is your
# first iterable. Navigate to script.py and import the student_roster list from roster.py. Create an iterator for 
# the student_roster list and print out each student’s information using next().


# Hint
# The built-in function next() can retrieve the next value in an iterator. The print (variable) statement can be
#  used to print out the output of a variable.

# 2.
# Now that we know a little more about the students in our classroom, let’s start organizing the classroom!
#  First, we should create a custom class that will allow us to manage our classroom and students.

# You’ve been provided a file called classroom_organizer.py. Start defining out your custom ClassroomOrganizer class.

# First, we should import the student_roster list from the roster.py file so that we can utilize it within our 
# custom class. Another module we will need later on will be the itertools module. Let’s import these both into
#  the classroom_organizer.py file now.


# Hint
# To import modules, use the syntax:

# import module_name
# 3.
# Next, we want to create a simple way to run through morning roll call, by ordering all students by first
#  name alphabetically. When you iterate on your ClassroomOrganizer object, it should return each student’s 
#  name one at a time on each next() call or for loop iteration.

# Define the iterator protocol for our ClassroomOrganizer class that can achieve this. Once defined, 
# use either next() calls or a for loop on the ClassroomOrganizer object to print out the next student on the roll call.


# Hint
# A class member to store the index of which student within self.stored_names has been returned should be defined.

# Itertools
# 4.
# Next, we need to organize our classroom and decide where our students will be sitting. We have 5 tables
#  in our classroom that can seat 2 students each. We’d like to see what combination of students we can 
#  put at each table.

# Using the itertools module, define a method within ClassroomOrganizer that will retrieve a final list
#  of all tuple combinations of 2 students that can be seated at each table.

# From script.py, print out the result to see all the possible combinations.


# Hint
# The combinations() itertool will accomplish this. The result can then be converted to a list afterwards.

# The script.py file will also need to import the ClassroomOrganizer class.

# 5.
# You are offering an afterschool program for those students whose favorite subjects are Math and Science.

# Your tables can fit 4 students at them. Retrieve a list of all 4 combinations of students whose favorite 
# subjects are Math and Science.

# The get_students_with_subject() method can be used to retrieve iterables for each of the subjects.

# From script.py, print the final list of combinations.


# Hint
# The chain() itertool can combine the Math and Science iterables into one. The combinations() itertool can 
# then get all combinations of 4 using the chained iterable result.

# The script.py file will also need to import the itertools module.

# Finishing Up
# 6.
# Congrats, you were able to set up and organize your student roster, classroom, and school programs!

# Through this project, you were able to reinforce what iterables and iterators are, how to write custom 
# classes that can be made into iterables, and how to use various Python itertools to manipulate iterables.

# You may use the remaining dictionary info within the student roster list (favorite animal, height, age) to 
# practice more with itertools or custom iterators.




student_roster = [
  {
    "name": "Karina M",
    "age": 8,
    "height": 48,
    "favorite_subject": "Math",
    "favorite_animal": "Dog"
  },
  {
    "name": "Yori K",
    "age": 7,
    "height": 50,
    "favorite_subject": "Art",
    "favorite_animal": "Cat"
  },
  {
    "name": "Alex C",
    "age": 7,
    "height": 47,
    "favorite_subject": "Science",
    "favorite_animal": "Cow"
  },
  {
    "name": "Esmeralda R",
    "age": 8,
    "height": 52,
    "favorite_subject": "History",
    "favorite_animal": "Rabbit"
  },
  {
    "name": "Sandy P",
    "age": 7,
    "height": 49,
    "favorite_subject": "Recess",
    "favorite_animal": "Guinea Pig"
  },
  {
    "name": "Matthew Q",
    "age": 7,
    "height": 46,
    "favorite_subject": "Music",
    "favorite_animal": "Walrus"
  },
  {
    "name": "Trudy B",
    "age": 8,
    "height": 45,
    "favorite_subject": "Science",
    "favorite_animal": "Ladybug"
  },
  {
    "name": "Benny D",
    "age": 7,
    "height": 51,
    "favorite_subject": "Math",
    "favorite_animal": "Ant"
  },
  {
    "name": "Helena L",
    "age": 7,
    "height": 53,
    "favorite_subject": "Art",
    "favorite_animal": "Butterfly"
  },
  {
    "name": "Marisol R",
    "age": 8,
    "height": 50,
    "favorite_subject": "Math",
    "favorite_animal": "Lion"
  }
]


# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    each_student = self.sorted_names[self.index]
    self.index += 1
    if self.index >= 10:
      raise StopIteration
    return each_student

  def _sort_alphabetically(self, students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def two_students_combos(self):
    two_combos = []
    twos = itertools.combinations(self.sorted_names, 2)
    for two in twos:
      two_combos.append(two)    
    return two_combos

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def get_student_name_animal(self):
    fav_animals = []
    for student in student_roster:
      fav_animals.append((student["name"], student["favorite_animal"]))
    return fav_animals
    
          
  def get_students_with_info(self):
    name_age_height = []
    for student in student_roster:
      name_age_height.append((student['name'], student["age"], student["height"]))
    return name_age_height


#task 1
#from roster import student_roster
import itertools
#task 2
#from classroom_organizer import ClassroomOrganizer 

new_student = ClassroomOrganizer()
student_roster_iterator = iter(student_roster)
print("task 1")
print("The full student roster (dictionary):")
for each_student in range(len(student_roster)):
  print(next(student_roster_iterator))

print()
print("task 3")
print("Each student by 'first' name one at a time, alphabetically:")

for each_name in new_student.sorted_names: 
  print(each_name[:-1])

print()
print("The student names, alphabetically as a list:")
print(new_student.sorted_names)
print()
print("Each student by first name and last initial one at a time:")
for each_student in new_student.sorted_names:
  print(each_student)

print()
print("task 4 - Two students combos possible")
two_students = new_student.two_students_combos()
print(two_students)
#tables_five = itertools.combinations(two_students, 5)
#for table in tables_five:
#  print(list(table)) 


print()
#print(new_student.get_students_with_subject("Math"))
#print(new_student.get_students_with_subject("Science"))
print("task 5: favorite subject is Math or Science")
math_science_list = list(itertools.chain(new_student.get_students_with_subject("Math"), new_student.get_students_with_subject("Science")))
print(math_science_list)
print()
print("task 5: combos of tables of four.")
math_science_fours = list(itertools.combinations(math_science_list, 4))
print(math_science_fours)

print()
print("task 6:")
print("Each student and their favorite animal")
for item in sorted(new_student.get_student_name_animal()):
  print("{} - {}".format(item[0], item[1]))

print()
print("task 6: student name, age, height")
for item in sorted(new_student.get_students_with_info()):
  print('{}: {} years, {}"'.format(item[0], item[1], item[2]))

