# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:11:01 2023

@author: geron
"""

# Next, create a class which will contain all of your tests. The class can be named whatever you’d like, 
# but it should inherit from unittest.TestCase.


# Hint
# Remember that classes can inherit from other classes by including a set of parentheses with a parent class 
# following the class name, like this:

# class MyClass(ParentClass):
# 3.
# The features you need to test have been implemented in the surfshop.ShoppingCart class. In order to test 
# the inner workings of a class, you will need to create a new instance of the shopping cart. Don’t worry - 
# you will handle that in the next tasks! For now, it’s important that every test has a new ShoppingCart 
# object to work with so that way the test always starts on a clean slate.

# In your class, create a setup fixture that runs before every test. It should instantiate a new ShoppingCart
# object and assign it to an instance variable called self.cart. Your tests can then use self.cart to reference your
#  instance of the ShoppingCart class.


# Hint
# Inside of a TestCase class, you can define a method called setUp(). This method runs automatically before each test.
# Remember that new objects are instantiated by calling the class name followed by parentheses, as follows:
# surfshop.ShoppingCart
# 4.
# It’s time to create your first test! Let’s test the add_surfboards() method of the cart.

# The ShoppingCart.add_surfboards() method takes an integer as its only argument and updates the number of 
# surfboards in the cart. Define a test method that calls this function with an argument of 1 and checks 
# that 'Successfully added 1 surfboard to cart!' is returned.


# Hint
# Remember that:

# test methods must start with the word test
# the self.assertEqual() method can be used to verify that two strings are the same
# 5.
# Let’s test another input for the .add_surfboardsmethod. Create another test method which calls
#  ShoppingCart.add_surfboards(), but this time, passes an argument of 2. It should test that 
#  the return value is 'Successfully added 2 surfboards to cart!'

# 6.
# The shopping cart has a limit of 4 surfboards per customer. Create a test to check that a
#  surfshop.TooManyBoardsError (a custom exception) is raised when ShoppingCart.add_surfboards() is called 
#  with an argument of 5.


# Hint
# The self.assertRaises() method takes an exception as its first argument and a function as its second
# . Any additional arguments get passed into the function. The test fails if the exception is not raised. 
# Alternatively, you can pass the arguments directly into the function.

# 7.
# The shopping cart has a feature that applies rental discounts for locals called apply_locals_discount(). 
# When this function is called, it sets the self.locals_discount property to True.

# Create a test that calls ShoppingCart.apply_locals_discount() and then checks that ShoppingCart.locals_discount is True.


# Hint
# The self.assertTrue() method checks that the passed argument evaluates to True.

# Run and maintain your tests
# 8.
# It’s time to start running your tests! At the bottom of tests.py, call unittest.main().

# If you’ve implemented your tests correctly, they should all pass - except for one! It seems 
# that the ShoppingCart.apply_locals_discount() function is not working as expected. While you 
# wait for the development team to fix this bug, you don’t want it to cause our tests to fail. 
# Mark this test as an expected failure.


# Hint
# The @unittest.expectedFailure decorator can mark tests as expected to fail.

# 9.
# Sam, the owner of Sam’s Surf Shop, has just informed us that the shop is heading into the off
#  season and business has slowed down. The store’s shopping cart no longer needs to enforce the 
#  4 surfboards per customer rule - at least until business picks up again.

# Go back and modify the test you wrote in task 5 which checks for a surfshop.TooManySurfboardsError
#  so that it is skipped.


# Hint
# You can use the @unittest.skip decorator to skip a test.

# 10.
# Parameterize the test you wrote in task 4 so that it runs 3 times, passing 2, 3, and 4 as the 
# arguments to surfshop.add_surfboards(). This allows us to easily test a single function with a 
# variety of inputs. Remember to modify the expected return value with the correct number of surfboards.


# Hint
# You can use the unittest.subTest() decorator inside of a for loop to parameterize a test.

# Improve the software
# 11.
# Sam has noticed all of your hard work and the fact that your tests found a bug. You can now start 
# working on the actual shopping cart software!

# Take a look in surfshop.py. Recall that the ShoppingCart.apply_locals_discount is not setting the 
# ShoppingCart.locals_discount attribute to True, as it should be. Can you fix it?

# When you do, comment out the expected failure decorator and see if all the tests pass.

# 12.
# Next, make an improvement to the exception that gets thrown when too many surfboards are added to 
# the cart. Modify TooManySurfboardsError so that when raised, it has the message 
# 'Cart cannot have more than 4 surfboards in it!'.


# Hint
# The __str__ method of an exception class determines the exception message.

# 13.
# Congratulations on your first successful software testing project! In this project, you successfully:

# Implemented a suite of unit tests for existing software.
# Ran and modified the tests according to results.
# Improved the existing software.
# If you want to challenge yourself even further, take a look at the ShoppingCart.set_checkout_date() function. 
# This function takes a datetime.datetime object as an argument and raises a surfshop.CheckoutDateError if the
#  date is not in the future. Can you write a test that validates this behavior?














import datetime

class TooManyBoardsError(Exception):
    def __str__(self):
        msg = 'Cart cannot have more than 4 surfboards in it!'
        return msg

class CheckoutDateError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.rental_days = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date

    def apply_locals_discount(self):
        self.locals_discount = True

import unittest
import surfshop
import datetime

class SurfShopTests(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    # old version without parameterization
    # def test_add_surfboards(self):
    #     message = self.cart.add_surfboards(2)
    #     self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
    #     self.cart = surfshop.ShoppingCart()

    @unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    # commented out - test should not fail at the end of project
    # @unittest.expectedFailure
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_add_invalid_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)


unittest.main()


