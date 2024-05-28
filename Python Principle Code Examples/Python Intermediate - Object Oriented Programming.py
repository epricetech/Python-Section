# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 09:59:10 2023

@author: geron
"""

# Programming Paradigm - a way to classify different program languages and the unique features that they offered
# Most modern-day languages offer more than one specific paradigm we can program in
# The most popular paradigmn is Object Oriented Programming OOP which programs around classes and objects
# Example of the core aspects of OOP paradigm
class Dog:
  sound = "Woof"
 
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def bark(self):
    print(Dog.sound)
# the dog is the class with properties name and age and a method (bark)

# example of OOP core principles and structure
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()
#output
# My id is 1.
# My id is 2.


# Above is the basic core of OOP with class and method and properties but to go beyond you use the 4 pillars of OOP
# Four Pillars of OOP
# 1. Inheritance
# 2. Polymorphism
# 3. Abstraction
#4. Encapsulation

# OOP Inheritance
# allows you to create intricate structures within classes - allows you to reuse methods across multiple classes
# using a parent class.  We cn also create parent-child reltionships between entities
# example of concept with dog and cat class
class Dog:
 
  def bark(self):
    print('Woof!')
 
class Cat:
 
  def meow(self):
    print('Meow!')
# these are 2 classes that define 2 distinct animals and their method of communication - Now if we wanted to give
# both classes the ability to eat by calling a method called eat() - now we could write the method twice in both classes
# But this option might get hard if you have a ton of animal classes.  To do this easier we use inheritance
#  Since both cat and dog fall under the classificaiton of Animal we can create a parent class to represent
# properties and methods they can both share
# parent class of Animal
class Animal: 
  def eat(self): 
    print("Nom Nom Nom...eating food!")
# now to get dog and cat to inherit this parent class and method the structure will look like this
#class ParentClass:
  #class methods/properties...
# class ChildClass(ParentClass):
#   #class methods/properties...
#  how it is done on our example
class Dog(Animal):
  def bark(self):
    print('Bark!')
 
class Cat(Animal):
  def meow(self):
    print('Meow!')
# this will show how inheritance is in action
fluffy = Dog()
zoomie = Cat()
 
fluffy.eat() # Nom Nom Nom...eating food!
zoomie.eat() # Nom Nom Nom...eating food!

# example of inheritance of parent and child class
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  pass

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say.id()

# one issue when implementing inheritace a child class may want to change the behavior of a method from its parent class
# in python all we have to do is override a method definition.  An overriding method in a subclass is one that has
# the same definition as the parent class but contains different behavior.
class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
pet1 = Animal("Rex")
pet1.make_noise() # Rex says, Grrrr
# the animal class has one attribute, self.name and one method .make_noise() which will output a generic animal sound
#  if we define a subclass of animal we may want to make a different sound
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
pet2 = Cat("Maisy")
pet2.make_noise() # Maisy says, Meow!
#Now we’ve made a class for a more specific type of animal, Cat. It has all the attributes and methods of Animal. 
#However, if you call the .make_noise() method on this instance of Cat it will say “Maisy says, Meow!”
# change to example from above with a subclass added to admin class to override  behavior
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  def say_id(self):
    print("I am an Admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()


#When overriding methods we sometimes want to still access the behavior of the parent method.
#In order to do that we need a way to call the method of the parent class. Python gives us a way to do that using super()
# super() gives us a proxy object which we can invoke the method of an objects parent class also known as superclass
# we call the required function as a method on super()
class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound
 
  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))
 
class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!") 
 
pet_cat = Cat("Rachel")
pet_cat.make_noise() # Rachel says, Meow!
# breakdown In the above example, we have the class Animal and the subclass Cat. Animal has 2 attributes, name and 
# sound and one method, .make_noise(). The .make_noise() method outputs the name and sound of an instance.
# The Cat subclass has an .__init__() method which means the .__init__() method of its superclass,
#  Animal will not be called when creating an instance of Cat. The .__init__() method from the subclass 
#  is overriding the one from the superclass.
# To still invoke the .__init__() method of Animal, super().__init__(name, "Meow!") is called inside 
# the subclass .__init__() method. This additional logic allows us to add the "Meow" sound from within 
# the Cat class, but still use the .__init__() method of the Animal class.
# super() is used in subclasses to invoke a needed behavior from the superclass alongside the behavior
#  of a subclass method.

# example of parent child class overriding and using super()
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()


# Multiple Inheritance - When a subclass inherites from more than one superclass - onre form of multiple inheritance
# is when there are multiple levels of inheritance which means a class inherits members from its superclass and its
# super superclass
class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))
 
class Cat(Animal):
  pass
 
class Angry_Cat(Cat):
  pass
 
my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!
# in example Angry_cat inherits from cat and cat inherits from Animal.  Both Angry_cat and Cat have access to the 
# animal class name attribute and .say_hi() method.  Any feature added to Cat will also be available to Angry_cat
# Example of concept of using multiple inheritance and super
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Write your code below
class Manager(Admin):
  def say_id(self):
    print('I am in Charge')
    super().say_id()

e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()
# output
# I am in Charge
# My id is 4.
# I am an admin.


# Another form of multiple inhertance involves a subclass that inherits directly from 2 classes and can use
# the attributes and methods of both
class Animal:
  def __init__(self, name):
    self.name = name
 
class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))
 
class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))
 
class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)
 
my_pet = Hybrid("Fluffy")
my_pet.action() # Fluffy wags tail. Awwww
                # Fluffy bites. OUCH!
# in example the class Hybrid is a subclass of both Dog and Wolf which are also both subclasses of Animal class
# all 3 subclasses can use the features in Animal and Hybrid can use the features of Dog and Wolf.  But Dog and Wolf
# cant use each other features
# This form of multiple inheritance can be useful by adding functionality from a class that does not fit in with 
# the current design scheme of the current classes.

# Care must be taken when creating an inheritance structure like this, especially when using the super() method.
#  In the above example, calling super().action() inside the Hybrid class invokes the .action() method of the Dog class.
#  This is due to it being listed before Wolf in the Hybrid(Dog, Wolf) definition.

# The line Wolf.action(self) calls the Wolf class .action() method. The important thing to note here
#  is that self is passed as an argument. This ensures that the .action() method in Wolf receives the
#  Hybrid class instance to output the correct name.
# example
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Now let’s make sure the admins get their user data set up.
# Inside the .__init__() method of the Admin class:
# Call the .__init__() method of the User class
# Pass the Admin class instance, id and the string "Admin" as arguments to the .__init__() method call
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, 'Admin')
    

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()


# OOP Pillar - Polymorphism - ability to apply an identical operation onto different types of objects
#  Useful when an object type may not be known at the time.  This pillare can be applied multiple ways.  One
# form is similar to inheritance
class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Robot:
 
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")
# Have Animal class and subclasss of Cat and standalone class Robot.  Each class has a method called
# .make_noise() with different outputs.  The identical method name with different behaviors is a form of polymorphism
an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
  o.make_noise()
 
# OUTPUT
# "Bear says, Grrrr"
# "Maisy says, Meow!"
# "beep.boop...BEEEEP!!!"
# With the classes instantiated and added to a list, we are able to iterate through the list and call .make_noise(). 
#This is done without needing to know what type of class .make_noise() belongs to.

# example
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
#Define a variable meeting and set it equal to a list that contains an instance of each class, Employee(), Admin() and Manager()
meeting = [Employee(), Admin(), Manager()]
#With the different types of employees in the meeting, have them all say their ID.Using a for loop iterate through the list meeting Using your defined loop variable, call the .say_id() method on each instance in the list
for i in meeting:
  i.say_id()
# output
# My id is 1.
# My id is 2.
# I am an admin.
# My id is 3.
# I am an admin.
# I am in charge!


# Dunder Methods and Operator Overloading polymorphism
# this is when working with different object types like , int, str, list or + operator
# For an int and an int, + returns an int
2 + 4 == 6
# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"
# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]
# to implement the behavior we want we want to use the dunder methods
# We’ve explored a few already, the constructor __init__() and the string representation method __repr__().
#  The name dunder method is derived from the Double UNDERscores that surround the name of each method.
# Recall that the __repr__() method takes only one parameter, self, and must return a string value. 
# The returned value should be a string representation of the class, which can be seen by using print()
#  on an instance of the class
# defining a classes dunder methods is a way to perfom operator overloading
class Animal:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)
 
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"
# Has Animal class with a dunder method .__add__() - this defines the + operator behavior when used on objects of this
# class typel  The method returns a new Animal object with the names of the operand objects concatenated that is a3 in example
#  The line of code a3 = a1 + a2 invokes the .__add__() method of the left operand, a1, with the right operand a2 
# passed as an argument. The name attributes of a1 and a2 are concatenated using the .__add__() parameters,
#  self and another_animal. The resulting string is used as the name of a new Animal object which is returned to 
#  become the value of a3.

# overall example
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
#There is now a Meeting class with an attendees list attribute and an .__add__() dunder method that adds Employee instances to the attendees list. Before we try and add employees to a meeting, we want to make sure we can know how many employees are in a meeting.
#Inside the Meeting class:
#Overload the len() operation by defining a __len__() dunder method Inside the __len__() definition, return the length of the attribute attendees
class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
#2.Now add three employees to a meeting:
#Using the Meeting instance m1, add each of the employee instances e1, e2, and e3. Use one line for each employee instance.Output the length of meeting instance m1 You should see the output from each employee being added and then the length of the meeting, 3.
m1 + e1
m1 + e2
m1 + e3
print(len(m1))
# output
# ID 1 added.
# ID 2 added.
# ID 3 added.
# 3


#  OOP Pillar - Abstraction - when programs get to big and classes start to share functionality or lose sight of the
# purposes of the classes inheritance struction.  We ca use abstraction as an solution
#  Abstraction helps withthe design of code by defining necessary behaviors to be used in the class structure
#  this helps avoid leaving outor overlapping class functionality as class hierarchies get larger
# example of concept
from abc import ABC, abstractmethod
 
class Animal(ABC):
  def __init__(self, name):
    self.name = name
 
  @abstractmethod
  def make_noise(self):
    pass
 
class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))
 
kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"
# above we have Cat and Dog classes that inherity from Animal.Animal class now inherits from an impored class ABC
# which stants for Abstract Base Class - This is the first step to making  Animal an abstract class that cannont
# be instantaited.  The 2ns step is using the imported deconator @abstractmethod on the empty method .make_noise()
#now if we did this we would get an error
an_animal = Animal("Scruffy")
# TypeError: Can't instantiate abstract class Animal with abstract method make_noise
# The abstraction process defines what an Animal is but does not allow the creation of one
# the .__init__() method still requires a name since all animals have a name
# The .make_noise() method exists since all animals make a noise, but the method is not implemented since each
# animal makes a different noise.  Each subclass of Animal is now required to define their own .make_noise() method
# or an error will occur that is why you see make_noise method is in each class instead of inhearitance
# example of concept
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass
#Take a look at the code in script.py. The abstract class AbstractEmployee is defined. It has all the logic that has previously existed in the Employee class, except that the .say_id() method is not implemented and has the @abstractmethod decorator.
#The Employee class currently has no implementation.
#Run the code and observe that e1.say_id() is causing an AttributeError since the Employee class has no implementation.
# Write your code below - to fix error
#Nice work! But wait, there’s still an error!
#TypeError: Can't instantiate abstract class Employee with abstract methods say_id
#The .say_id() method in the AbstractEmployee class uses the @abstractmethod decorator. This means any class that inherits from AbstractEmployee must implement a .say_id() method.
#Inside the Employee class replace the pass statement, then:
#Define a say_id() method that outputs a message with self.id
#When complete you should see the output in the console.
class Employee(AbstractEmployee):
    def say_id(self):
      print("My id is {}".format(self.id))

e1 = Employee()
e1.say_id()


# OOP Pillar - Encapsulation - process of making methods and data hidden inside the object they relate too.  This is
# done by what is called access modifiers like Public, Protected, Private
# Public members can be accessed from anywhere, protected can only be accessed from coe within the same module and 
#private members can  only be accessed from code within the class that these are defined in.  Defualt is public
# Common convention to use a single underscore self._x to indicate that a member is protected.  
# Accessing a protected member outside of the module will not cause an error, it is added by developers to inform
# other developers that they should be careful when accessing this member in such a manner.
# to declare a member as private we used 2 leading underscores self.__c   This is more than a convention in python 
# because of a mechanism called name mangling.  Members that are preceded with two underscores have their names 
# modified in the background to obj._Classname__x. While they can still be publicly accessed, the purpose of this 
# mechanism is to prevent clashing member names of any inheriting classes that might define a member of the same name.
# One important difference is that dunder method names are not mangled. and dunder is treated differently than private member
# example of concept
class Employee():
    def __init__(self):
        self.id = None
# The Employee class contains one attribute id. An instance variable e is defined and then passed to the function dir() which is output to the console.
#dir() is a built-in Python function that returns a list of all class members, including dunder methods.
#When you run the code, you will see a list of class members with id as the last element.
        # Write your code below
#Now add an attribute that uses the single underscore naming convention.Inside the Employee class .__init__() method:Define the single underscore variable_id and set it equal to whatever you want When you run the code you can see _id as the second to last element in the output list.  
# Now define a variable using the double-underscore.
#Inside the Employee class .__init__() method:
#Define the double underscore variable __id and set it equal to whatever you want
#When you run the code you can see a new variable _Employee__id as the first element in the output list. This is the result of name-mangling the variable self.__id.

        self._id = 1042
        self.__id = 9877

e = Employee()
print(dir(e))
#output
#['_Employee__id', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'id']


# Getters, Setters, Deleters functions
#  one way to implement encapsulation where the state of class attributes can be handled within the class.
#  These are useful in making sure that the data being handled is appropriate for the defined class funtionality
class Animal:
  def __init__(self, name):
    self._name = name
    self._age = None
 
  def get_age(self):
    return self._age
 
  def set_age(self, new_age):
    if isinstance(new_age, int):
      self._age = new_age
    else:
      raise TypeError
 
  def delete_age(self):
    print("_age Deleted")
    del self._age
# Animal class has an single underscore attribute of _age - This motates it is inteded to be used only within the module
# There are 3 methods related to age each with a different purpose.  These define the getter, setter, and deleter
# of the spcific property.  First method related to age is a getter and returns self.age.  The setter is below that
# it includes logic that ensures that the value passed to new_age is an integer.  If so self.age = new_age if not
# raised an error.  The deleter is below setter.  It outputs a confirmation message and uses the del keyword to 
# delete the self._age attribute
a = Animal("Rufus")
print(a.get_age()) # None
 
a.set_age(10)
print(a.get_age()) # 10
 
a.set_age("Ten") # Raises a TypeError
 
a.delete_age() # "_age Deleted"
print(a.get_age()) # Raises a AttributeError
# Above we see a.get_age() gets the _age value, a.set_age(10) sets the value and a.delete_age() deletes the
 # attribute entirely. A TypeError occurs with a.set_age("Ten") because the defined logic in the setter is looking 
 # only for an integer. An AttributeError occurs with a.get_age() after the attribute was deleted.

class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name
#Above we see a.get_age() gets the _age value, a.set_age(10) sets the value and a.delete_age() deletes the attribute entirely. A TypeError occurs with a.set_age("Ten") because the defined logic in the setter is looking only for an integer. An AttributeError occurs with a.get_age() after the attribute was deleted.
  # Write your code below
  def get_name(self):
    return self._name
#Add a setter method.
#nside the Employee class:
#Define a setter method set_name that has an additional parameter for the name string and sets the class attribute _name.
  def set_name(self,new_name):
    self._name = new_name
#Lastly, Add a deleter method.
#Inside the Employee class:
#Define a deleter method del_name that deletes the attribute.
  def del_name(self):
    del self._name
e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())


# review of principles
# We discussed the four pillars of object-oriented programming as they apply to the Python programming language.

# Inheritance
# Python allows classes to inherit on multiple levels. Meaning a class can inherit from a base class as well as a 

# derived class. Python also supports multiple inheritance, where one class can inherit from any number of other classes.
#  This allows us to describe complex relationships between objects with minimal repeated code.

# Polymorphism
# Polymorphism is a concept that allows functions and objects to behave in different ways depending on context. 
# There is the polymorphism of functions like len() or the addition operator +, which can act differently depending 
# on the provided data.

# Abstraction
# Python supports the concept of abstraction by allowing objects with methods that have the same name, to be called 
# in a general manner. Further, Python provides the Abstract Base Class (ABC) for us to create a more clearly defined
#  interface.

# Encapsulation
# Python’s approach to encapsulation is unique compared to most other object-oriented programming languages. 
# In Python, all members of an object are publicly accessible but there are conventions to indicate to developers 
# that a member is intended to be protected or private.

# review example of all principles
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

class User:
  def __init__(self):
    self._username = None

  @property
  def username(self):
    return self._username

  @username.setter
  def username(self, new_name):
    self._username = new_name

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("{} added.".format(employee.username))
    self.attendees.append(employee.username)

  def __len__(self):
    return len(self.attendees)

class Employee(AbstractEmployee, User):
    def __init__(self, username):
      super().__init__()
      User.__init__(self)
      self.username = username

    def say_id(self):
      print("My id is {}".format(self.id))
 
    def say_username(self):
      print("My username is {}".format(self.username))


# @property Decorator for getters, setters and deleters
# recall that getters and setters are useful tools for encapsulation( a way to prevent data from direct modificatin)
#  We can define a private attribute and then use getters and setters to expose a public means of reading and 
# modifying a class attribute value. Further, getters and setter methods allow us to create complex behavior such as
#  limiting access under certain conditions or imposing restrictions on allowable ranges of values for an attribute.
#Let’s start by looking at an example class called Box with one attribute called weight. In this case, 
#weight will be a private attribute with a getter and a setter (getWeight() and setWeight()).
class Box:
  def __init__(self, weight):
    self.__weight = weight
 
  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight
# Notice two things:
#We want to follow best practices by denoting weight as a private attribute using __ (dunder) notation.
# This, however, does not make an attribute private, and we can still manipulate it directly.
#We are also posing some restrictions on our setter so that the weight of an instance of the Box class 
#can only be set to values greater than zero. We can see this if we try to manipulate an instance:
box = Box(10)
box.setWeight(-5) 
print(box.getWeight())
box.setWeight(5)
print(box.getWeight())
# That our box weight was unchanged on the first call:
# 10 
# 5
#Notice that we need to call the methods instead of directly interacting with the weight attribute. 
# What if we could have the best of both worlds? That is, a way to directly interact with the weight attribute 
# but still benefit from the complex behavior of methods such as the weight restriction. This is where the built-in 
# function property() comes in.
#The Python built-in property() function accepts four optional arguments: fget, fset, fdel, and doc. 
# The first three represent getter, setter, and deleter methods, respectively, and the last one is a docstring
#  for the attribute.
class Box:
  def __init__(self, weight):
    self.__weight = weight
 
  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight
 
  def delWeight(self):
    del self.__weight
 
  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
#Notice we have added one additional method to our class called delWeight() to serve as a deleter for the property. 
# While it is not strictly required, we will add it to show the full potential of the property() function. 
# We then call the property() function and pass the getter, setter, and deleter in as arguments. 
# This will immediately allow us to use the following syntax for our class:
box = Box(10)
print(box.weight) #this calls .getWeight()
box.weight = 5 #this called .setWeight()
del box.weight #this calls .delWeight()
box.weight = -5 #box.__weight is unchanged 
#With this change, our program gains some immediate benefits:
# We can now use the weight attribute as if it was public. We no longer have to call the setters, getters, 
# and deleter methods directly and thus giving our program a simpler syntax.
# Even though we no longer call the methods directly, we still can maintain constraints such as the weight 
# limit in setWeight(). It’s the best of both worlds!
# If we had a huge codebase that used our methods multiple times in multiple places, a single change to the
#  method name would seriously mess up our program since we would have to change it everywhere! We no longer 
#  have this issue using the property() method since we never call it directly.

#way to define getters, setters, and deleters is by using the @property decorator. 
# This decorator is syntactic sugar for using the property() function and helps our code look much cleaner. 
# Let’s take a look:

class Box:
 def __init__(self, weight):
   self.__weight = weight
 
 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight
 
 
 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight
 
 @weight.deleter
 def weight(self):
   del self.__weight
# Let’s break this down:

# First, we have renamed all of our methods to simply be weight().
# Then we denoted our getter with a @property. This marks the property to be used as a prefix for decorating the
#  setter and deleter methods.
# Lastly, we use @weight.setter and @weight.deleter to define our setter and deleter methods, respectively.
# This is the equivalent of doing:
#weight = property(getWeight, setWeight, delWeight,  "Docstring for the 'weight' property")
#And thus giving us the same syntactical advantage as before:
box = Box(10)
box.weight = 5
del box.weight













