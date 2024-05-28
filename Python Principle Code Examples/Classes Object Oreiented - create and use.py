# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:14:27 2023

@author: geron
"""

#  classes are consided a blueprint of objects.  Each class is like a prototype.  It contains all the deatils of the object
#  example is like a blueprint for a house.  It contains details about floors, doors, windows ect.  
#  from this blue print we can create many houses (objects) from a single class
#  In OOP - object oriented prgramming where class instances are created to implement design principles
#  such as inheritance and encapsulation
#  we define class by using the class method
#  we can use the pass statment as a placeholder to avoid errors
#  In a class body, you can define attributes and methods as needed. As you already learned,
# attributes are variables that hold the class data, while methods are functions that provide behavior 
# and typically act on the class data.
# The .__init__() method has a special meaning in Python classes. This method is known as the object initializer 
# because it defines and sets the initial values for your attributes.
# attributes for the init statement must contain self and any other that you need. 
#Class attributes are variables that are defined outside of all methods and have the same value for every instance 
# of the class. They also can be accessed via the class name rather than the instance name. Setting the variable 
# via the class name will change it for all instances. 
# example syntax
class Home:
  def __init__(self, rooms, stories):
    # Setting instance variables
    self.rooms = rooms
    self.stories = stories

# the repr method  - used to tell python what the string representation of the class should be - should have only self paramater
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

john = Employee('John')
print(john) # John

# example of using type function - will return the data type of the argument passed to it
a = 1
print(type(a)) # <class 'int'>
a = 1.1
print(type(a)) # <class 'float'>
a = 'b'
print(type(a)) # <class 'str'>
a = None
print(type(a)) # <class 'NoneType'>

# example of dir function - without any arguments returns a list of all attributes in scope
class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Hi, I'm " + self.name)

    print(dir())
# # ['Employee', '__builtins__', '__doc__',
# '__file__', '__name__', '__package__',
# 'new_employee']
print(dir(Employee))
# ['__doc__', '__init__', '__module__',
# 'print_name']


# example of attributes
class Bird:
  # Class attribute
  is_hungry = True
parakeet = Bird()
parrot = Bird()
print("Birds are hungry!")
print("Feeding birds...")
parakeet.is_hungry = False
parrot.is_hungry = False
print("Birds fed!")

# class instances Objects can be created or instantiated from classes. 
#These objects are known as class instances and are created by setting a variable equal to the class name
# followed by parentheses ():
my_home = Home()

# methods inside of class like functions
# example
class Bird:
  # Class attribute
  is_hungry = True
  def feed_bird(self, food):
    if(self.is_hungry):
      self.is_hungry = False
      print(f"Feeding with {food}. Bird fed!")
    else:
      print("Bird already ate.")
sparrow = Bird()
sparrow.feed_bird('seeds')
sparrow.feed_bird('oats')

# static method where you want to apply method to class itself - example comparing to ways of doing methods
class Home:
  name="Code Ninja"
  rooms = 4
  stories = 2

  @staticmethod
  def is_on_market(home):
    if(home.name == ""):
      return True
    else:
      return False

  @classmethod
  def paint_wall(self, color):
    return f"Painting wall with the color {color}."

home = Home()

print(Home.is_on_market(home))
# Output: False

# example of classes and methods
class Dog:
  dog_time_dilation = 7
 
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
 
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

# example of class with methods
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)
print(teaching_table_area)
print(round_room_area)


# methods with multiple arguments but one is the defualt self
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

# example of method and class
class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

# create object of a class
jessa = Person('Jessa', 'Female', 'Software Engineer')

# call methods
jessa.show()
jessa.work()

# example of class modifying and using class and methods
class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)


# overall example of class with different methods
# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name

s1 = Student("Harry", 12)

# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
# call instance methods
s1.show()

# example create class and assign values and methods
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score



roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)
pieter.add_grade(Grade(100))


# examples - the following examples are showing the veolution of a class and what you can do with it
# Define the DriveBot class here!
class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.direction = 0
    self.sensor_range = 0
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# adds robot logic by adding more methods in class
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
     # Add the methods here!
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)
# Use the methods here!
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

#  adds a 2nd robot and changed the contrustor which is the __init__ statement
class DriveBot:
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10
robot_2 = DriveBot(35, 75, 25)
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

#  controls multi robots at the same time
class DriveBot:
  # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10
robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!
DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True
print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

# identifying robots with an id value
class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10
robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)
print(robot_1.id)
print(robot_2.id)
print(robot_3.id)


# _init_() method to initialize a new created object
class Shouter:
  def __init__(self):
    print("HELLO?!")
shout1 = Shouter()
# prints "HELLO?!"
shout2 = Shouter()
# prints "HELLO?!"
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
 
      # then shout it out
      print(phrase.upper())
shout1 = Shouter("shout")
# prints "SHOUT"
shout2 = Shouter("shout")
# prints "SHOUT"
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

class Circle:
  pi = 3.14
  # Add constructor here:
  def __init__(self, diameter):
    print('New circle with diameter: {}'.format(diameter))
teaching_table = Circle(36)


# example class taht sets url for variables
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.url)
# prints "www.codecademy.com"
 
print(wikipedia.url)
# prints "www.wikipedia.org"


# uses the secure() argument to take the one required argument
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.secure())
# prints "https://www.codecademy.com"
 
print(wikipedia.secure())
# prints "https://www.wikipedia.org"


# example of class with attributes and objects
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:

    self.radius = diameter / 2
    
  def circumference(self):
      return 2 * self.pi * self.radius
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


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

# example
class NoCustomAttributes:
  pass
 
attributeless = NoCustomAttributes()
 
try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")
 
# prints "This text gets printed!"

hasattr(attributeless, "fake_attribute")
# returns False and can have 2 attributes
 
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value and can has a 3rd default value


can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, 'count'):
    print(str(type(element)) + ' has the count attribute!')
  else:
    print(str(type(element)) + ' does not have the count attribute :(')

# example of instance variables
class FakeDict:
  pass


fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = "Isabelle's Ices"














