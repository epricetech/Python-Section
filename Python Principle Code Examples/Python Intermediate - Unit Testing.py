# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 08:02:47 2023

@author: geron
"""

# Unit Testing - Not only are their syntax errors and exceptions but there are also could be mistakes in the programs
# logic and structure.  Testing will allow you to find the bugs quickly to resolve.
# testing can be divided into 2 categories
# 1. Manual Testing - a physical person interacts with the software much like a user woruld.  Also we are doing 
# manual testing every time we run our code and observe the results
# 2. Automated Testing - Tests are performed with code.  

# The Assert Statement - which performs a simple tests on your code
#  An assert statement can be used to test that a condition is met.  If the condition evaluates to False
# and AssertionError is raised with an option error message
# General syntax of assert statement
# assert <condition>, 'Message if condition is not met'
# example of assert statement on a function.  There is a bug in the function
def times_ten(number):
    return number * 100
 
result = times_ten(20)
assert result == 200, 'Expected times_ten(20) to return 200, instead got ' + str(result)
# Here, we want to test if our times_ten() function works as intended. We use the assert statement to 
# evaluate the expression result == 200 since we expect that our function would return 200 given an input of 20. 
# Since this is not the case, this expression evaluates to False (there is a bug in times_ten - it actually multiplies
# by 100!), we get the following exception:
# #output
# AssertionError: Expected times_ten(20) to return 200, instead got 2000

# example of assert statement checking if desitination is in destinations
destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below: 
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)
# output
# Welcome to Small World Airlines!
# What is the airport code of your travel destination?
# Traceback (most recent call last):
#   File "destinations.py", line 12, in <module>
#     assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
# AssertionError: Sorry, Small World currently does not fly to this destination!


# unit tests - when the program is broken down to specific parts.  Example would be testing a door.  the handle
# the hinge, the lock ect.  Each one those specific aspects is a unit.  We can test a single unit of a program
# such as function, loop or variable.  a unit test validates a single behavior
#  Let’s say we wanted to test a single function (a single unit). To test a single function, we might create 
# several test cases. A test case validates that a specific set of inputs produces an expected output for the 
# unit we are trying to test. Let’s examine a test case for our times_ten() function from the previous exercise:
# The unit we want to test
def times_ten(number):
    return number * 100
 
# A unit test function with a single test case
def test_multiply_ten_by_zero():
    assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'
# Great, now we have a simple test case that validates that times_ten() is behaving as expected for a valid input of 0!
#  We can improve our testing coverage of this function by adding some more test cases with different inputs. 
#  A common approach is to create test cases for specific edge case inputs as well as reasonable ones.
#  Here is an example of testing two extreme inputs:

def test_multiply_ten_by_one_million():
    assert times_ten(1000000) == 10000000, 'Expected times_ten(1000000) to return 10000000'
 
def test_multiply_ten_by_negative_number():
    assert times_ten(-10) == -100, 'Expected times_ten(-10) to return -100'
# above example Now we have several test cases for a wide variety of inputs: a large number, a negative number, and zero

# example of runing some tests and finding an error in the get_nearest_exit fucntion for any row higher than 30
def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'
def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

test_row_1()
test_row_20()
test_row_40()


# Python unittest Framework
# now with the previous examples they work because of the size of the program, however we had to write 3 tests and
# call those 3 tests to see the results.  There was no way to group the tests together and if one test failed
# the AssertioError would prevent any remaining tests from running.  
#  Python has a framework called unittest that solves these issues.  You must import unittest before starting
# The unittest module provides us with a Test Runner which is a component that collects and executes tests and then
#  provides results.  The framework also provides many other tools for testing like setup,teardown,skipping and more
#  To set up unittest steps
# first we must create a class which inherits from unittest.TestCase
import unittest 
class TestTimesTen(unittest.TestCase):
    pass
# this class with serve as the main storage for our unit test functions.  Once class is created we need to change our
# test functions so that they are methods of the class.  The unittest module requires that test funtions begin
# with the word 'test' - example of creation
import unittest
 
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        pass
 
    def test_multiply_ten_by_one_million(self):
        pass
 
    def test_multiply_ten_by_negative_number(self):
        pass
# lastly we need to change the assert statement to use the assertEqual method of unittest.TestCase
#  This requires a special method instead of the standard assert statement
#  example 
import unittest
 
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')
 
    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')
 
    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')

# example of all code put together in final format for testing
# Importing unittest framework
import unittest
 
# Function that gets tested
def times_ten(number):
    return number * 100
 
# Test class
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')
 
    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')
 
    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')
 
# Run the tests
unittest.main()
# output
# FF.
# ======================================================================
# FAIL: test_multiply_ten_by_negative_number (__main__.TestTimesTen)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "scratch.py", line 16, in test_multiply_ten_by_negative_number
#     self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')
# AssertionError: -1000 != -100 : Expected add_times_ten(-10) to return -100

# ======================================================================
# FAIL: test_multiply_ten_by_one_million (__main__.TestTimesTen)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "scratch.py", line 13, in test_multiply_ten_by_one_million
#     self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')
# AssertionError: 100000000 != 10000000 : Expected times_ten(1000000) to return 10000000

# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# FAILED (failures=2)
# In the test output, we can see that two of the tests failed (test_multiply_ten_by_one_million 
#and test_multiply_ten_by_negative_number).

# example of adding all tests under a class using unittest
# Checkpoint 1
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    # Checkpoint 6
    location = 'back'
  return location

# Checkpoint 2
class NearestExitTests(unittest.TestCase):
  # Checkpoint 3
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
    
  # Checkpoint 3
  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
    
  # Checkpoint 3
  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

# Checkpoint 4
unittest.main()
# output
# #...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK

# Assert Method - Equality Methods
# this section is expansion of the assert method in the TestCase class
# Three commonly used assert methods for testing equality and membership
# 1. assertEqual() - method that takes 2 values as arguments and checks that they are equal.  if not the test fails
# Basic syntax
self.assertEqual(value1, value2)
# 2.  assertin() - method takes 2 arguments.  It checks that the first argument is found in the 2nd argument
# which should be a container.  if not found in container the test fails
#basic syntax
self.assertIn(value, container)
# 3.  assertTrue() - method takes a single argument and checks that the argument evaluates to True.  If not true test fails
# Basic Syntax
self.assertTrue(value)

# comparision between these methods and using a simple assert statement
# Method	Equivalent
# self.assertEqual(2, 5)  -	assert 2 == 5
# self.assertIn(5, [1, 2, 3]) -	assert 5 in [1, 2, 3]
# self.assertTrue(0) -	assert bool(0) is True

# overall example of assertTrue and assertIn methods
def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'
def get_licensed_movies():
    print('Retrieving the list of licensed movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies
def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is inactive')
    return False
# Checkpoint 1
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    # Checkpoint 2
    self.assertIn(daily_movie, licensed_movies)


  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    # Checkpoint 3
    self.assertTrue(wifi_enabled)

unittest.main()
# output
# Retrieving the movie set to play on today's flight...
# Retrieving the list of licensed movies from the database...
# Checking WiFi signal...
# WiFi is inactive
# .F
# ======================================================================
# FAIL: test_wifi_status (__main__.EntertainmentSystemTests)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 17, in test_wifi_status
#     self.assertTrue(wifi_enabled)
# AssertionError: False is not true

# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# FAILED (failures=1)
# this test fails because burrently wifi is disabled


#  assert methods - quantitative methods
#  two common assert methods that test conditions related to numbers and quantitative comparisions
# 1.  assertLess() - method takes 2 arguments and checks that the first argument is less than the 2nd one. if not test fails
# general syntax
self.assertLess(value1, value2)
# 2.  assertAlmostEqual() - method takes 2 arguments and checks that their difference, when rounded to 7 decimal places is 0
#  in other words if they are almost equal.  if the values are not close enough to equality the test will fail
# basic syntax
self.assertAlmostEqual(value1, value2)
# comparision between these methods and a simple assert statement
# Method -	Equivalent
# self.assertLess(2, 5) -	assert 2 < 5
# self.assertAlmostEqual(.22, .225) -	assert round(.22 - .225, 7) == 0

# example of quantitative methods
def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'
def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies
def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is active')
    return True
def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 40
def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999
mport unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Checkpoint 1
  #Call entertainment.get_maximum_display_brightness() and store the return value in a variable called brightness.
#Next, call self.assertAlmostEqual() to make sure that brightness is almost equal to 400.
  def test_maximum_display_brightness(self):
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)

  # Checkpoint 2
  #Call entertainment.get_device_temp() and store the return value in a variable called device_temp.
#Then call self.assertLess() to make sure that device_temp is less than 35.
  def test_device_temperature(self):
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)
unittest.main()
# output
# Reading the temperature of the entertainment system device...
# Calculating maximum display brightness in nits...
# Retrieving the movie set to play on today's flight...
# Retrieving the list of licenses movies from the database...
# Checking WiFi signal...
# WiFi is active
# F...
# ======================================================================
# FAIL: test_device_temperature (__main__.EntertainmentSystemTests)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 27, in test_device_temperature
#     self.assertLess(device_temp, 35)
# AssertionError: 40 not less than 35

# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# FAILED (failures=1)
# test fails because current temp is 40


# Assert methods - Exception and Warning Methods
# these are methods that work on exceptions and methods - covered in intro to exception errors
# 1. asserRaises() - method take an exception type as its first argumment, a function reference as 2nd argument
# and an arbitrary number of arguments as the rest.  It calls the function and checks if an exception is raised as result
#  the test passes if exception is raised, is an error if another exception is raised or failes if not exception raised
#  this can be used with custom exceptions as well
# Basic syntax
self.assertRaises(specificException, function, functionArguments...)
# 2.  assertWarns() - method takes a warning type as its first argument, a function reference as 2nd argument
# and an arbitrary number of arguments as the rest.  It calls the function and checks that the warning occurs
#  the test passes if a warning is triggered and fails if not
# basic syntax
self.assertWarns(specificWarningException, function, functionArguments...)

# exaple of assert methods for exception and warning methods
import warnings

class PowerError(Exception):
    pass

class WaterLevelWarning(Warning):
    pass

def power_outage_detected(outage_detected):
    if outage_detected:
        raise PowerError('A power outage has been detected somewhere in the system')
    else:
        print('All systems receiving power')

def water_levels_check(liters):
    if liters < 200:
        warnings.warn('Water levels have fallen below 200 liters', WaterLevelWarning)
    else:
        print('Water levels are adequate')
import unittest
import alerts

# Write your code here:
#In our SystemAlertTests class, create a test method called test_power_outage_alert().
#Inside the new method, use self.assertRaises() to check that an alerts.PowerError is raised whenever alerts.power_outage_detected is called with an argument of True.
#This test should pass since we are passing a value of True and the exception is raised.
class SystemAlertTests(unittest.TestCase):
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)

#In our SystemAlertTests class, create a test method called test_water_levels_warning().
#Inside the new method, use self.assertWarns() to check that an alerts.WaterLevelWarning is raised whenever alerts.water_levels_check is called with an argument of 150 liters.
#This test should pass since we are passing a value less than 200 and a warning occurs.
  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)
unittest.main()



# Parameterizing Tests
#  Test parameterization is a toolset for tests with only minor differences - allows to do a single test on large amount
#  of coverage of different inputs.  We utilize the subTest contect manager
# example of structure
import unittest
 
# The function we want to test
def times_ten(number):
    return number * 100
 
# Our test class
class TestTimesTen(unittest.TestCase):
 
    # A test method
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest():
                expected_result = num * 10
                message = 'Expected times_ten(' + str(num) + ') to return ' + str(expected_result)
                self.assertEqual(times_ten(num), expected_result, message)
# Here, in our test method test_times_ten(), instead of writing individual test cases for each input 
# of 0, 10, and 1000000, we can test a collection of inputs by using a loop followed by a with statement 
# and our subTest context manager.

# By using subTest, each iteration of our loop is treated as an individual test. Python will run the code inside 
# of the context manager on each iteration, and if one fails, it will return the failure as a separate test case failure.

# Just like before, we are using the assertEqual() method to check the expected result, and 
# we are expecting (due to an error in times_ten()) that the cases of using an input of -10 and 1000000 will fail.

# Here is the new output:

# ======================================================================
# FAIL: test_times_ten (__main__.TestTimesTen) (<subtest>)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "scratch.py", line 12, in test_times_ten
#     self.assertEqual(times_ten(num), expected_result, message)
# AssertionError: 100000000 != 10000000 : Expected times_ten(1000000) to return 10000000

# ======================================================================
# FAIL: test_times_ten (__main__.TestTimesTen) (<subtest>)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "scratch.py", line 12, in test_times_ten
#     self.assertEqual(times_ten(num), expected_result, message)
# AssertionError: -1000 != -100 : Expected times_ten(-10) to return -100

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=2)

#  to expand our test coverage we can simply modify the list that our loop iterates over.
#  optinoally we can give our subtests better readability by making a small change in code for the first argument of
#  self.subTest()  Example of meaning and how to change above example
# ... more code above..
 
for num in [0, 1000000, -10]:
  with self.subTest(num):
 
# ... more code below ....
# This makes our test clearer, because our test error message goes from:

# FAIL: test_times_ten (__main__.TestTimesTen) (<subtest>)
# to:

# FAIL: test_times_ten (__main__.TestTimesTen) [1000000]

# example of  Parameterizing Tests using the subTest() method
def get_daily_movies():
    print('Retrieving the movie set to play on today\'s flight...')
    return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']
def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    # Checkpoint 1
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()

    # Checkpoint 2
    for movie in daily_movies:
      print(movie)
      # Checkpoint 3 & 4
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)
#indent our self.assertIn() call to be inside the for loop and change the first argument in self.assertIn() 
# from daily_movie to movie to represent the individual movies on each iteration of the loop.

# #Note: Creating this structure might be okay at first glance (and may even make you wonder why we need the 
# context manager), but if we run our test, we will see that the test will fail in the middle of our movies
#     collection and won’t check the rest (it stops at Black Widow and not Spiral)! This is because like many
#     testing frameworks, unittest will fail and stop on the first failure it encounters.
# #Lastly, under our print statement of movie but before our assertIn() call, insert a self.subTest() to wrap
#  our test method. To make sure we can distinguish test cases between each movie, pass a single argument of 
#  movie into self.subTest().

# #Don’t forget to preface the context manager with a with statement and indent our self.assertIn() statement. 
# Now, we can observe testing multiple movies and if they are licensed or not.

unittest.main()
# output
# Retrieving the movie set to play on today's flight...
# Retrieving the list of licenses movies from the database...
# Parasite
# Nomadland
# Roma
# Black Widow
# Spiral
# E
# ======================================================================
# ERROR: test_movie_license (__main__.EntertainmentSystemTests)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests.py", line 14, in test_movie_license
#     self.assertIn(daily_movie, licensed_movies)
# NameError: name 'daily_movie' is not defined

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (errors=1)


# Test Fixtures
#  Tests need to occure in a known state.  If conditions of test runs are not controlled results can contain
#  false negatives(invalid faild results) or false positives(invalid passed results)
#  Test fixture is a mechanism for ensuring proper test setup putting tests in a known state and test teardown
# meaning restoring the state prior to the test running.  
# example of a devices bluetooth module.  If it fails you have to power cycle and return to a working state
#  this example adds a test fixture to power cycle the device before and after each test
def power_cycle_device():
  print('Power cycling bluetooth device...')
 
class BluetoothDeviceTests(unittest.TestCase):
  def setUp(self):
    power_cycle_device()
 
  def test_feature_a(self):
    print('Testing Feature A')
 
  def test_feature_b(self):
    print('Testing Feature B')
 
  def tearDown(self):
    power_cycle_device()
# The unittest framework automatically identifies setup and teardown methods based on their names.
#  A method named setUp runs before each test case in the class. Similarly, a method named tearDown gets 
#  called after each test case. Now, we can guarantee that our Bluetooth module is in a working state before 
#  and after every test. Here is the output when these tests are run:

# Power cycling bluetooth device...
# Testing Feature A
# Power cycling bluetooth device...
# .Power cycling bluetooth device...
# Testing Feature B
# Power cycling bluetooth device...
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
 
# OK

# example same as above with changing the powercycle to only happen after all tests in the class are run
def power_cycle_device():
    print('Power cycling bluetooth device...')
 
class BluetoothDeviceTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    power_cycle_device()
 
  def test_feature_a(self):
    print('Testing Feature A')
 
  def test_feature_b(self):
    print('Testing Feature B')
 
  @classmethod
  def tearDownClass(cls):
    power_cycle_device()
#  we replaced out setUp method with the setUpClass method and added the @classmethod decorator.  We changed the argument
# from self to cls because this is a class method.  Also replaced the tearDown method with the tearDownClass class method
# output
# Power cycling bluetooth device...
# Testing Feature A
# Testing Feature B
# Power cycling bluetooth device...
 
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
 
# OK
# In addition to calling functions, we can also use setup methods to instantiate objects and or gather any other 
#data needed. Anything stored in our class will be available throughout our test functions.


# example of test fixtures
# #We want to make sure the kiosk is powered on before we run any tests. This is a great time to setup some test fixtures!

# Create a setUpClass() method which takes a single argument (cls) and calls kiosk.power_on_kiosk(). 
# Add the @classmethod decorator on top of it!

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# We don’t want to leave the kiosk powered on after all tests are run.

# Create a tearDownClass() method which takes a single argument (cls) and calls kiosk.power_off_kiosk(). 
# Add the @classmethod decorator on top of it!

# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# We also want to make sure that customers are on the welcome page before each test runs. 
# Create a method called setUp(). Inside of the method, call kiosk.return_to_welcome_page().
def power_on_kiosk():
    print('Powering on the check-in kiosk...')
def return_to_welcome_page():
    print('Returning check-in kiosk to Welcome Page')
def power_off_kiosk():
    print('Powering off the check-in kiosk...')
import unittest
import kiosk

class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Write your code below:
  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()
  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()
  def setUp(self):
    kiosk.return_to_welcome_page()
unittest.main()
# output
# Powering on the check-in kiosk...
# Returning check-in kiosk to Welcome Page
# Testing the check-in process based on flight number
# Returning check-in kiosk to Welcome Page
# Testing the check-in process based on passport
# Powering off the check-in kiosk...
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK


# skipping Tests
#  For when we want tests that should only run in a particular context.  Example we have a test that only runds
# on windows but not linux or maxOS
#  Two different ways to skip tests in unittest
# 1. @unittest skip decorator
# 2. skipTest() method

#  Skip decorator option - 2 decorator options both shown in example
import sys
 
class LinuxTests(unittest.TestCase):
 
    @unittest.skipUnless(sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_linux_feature(self):
        print("This test should only run on Linux")
 
    @unittest.skipIf(not sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_other_linux_feature(self):
        print("This test should only run on Linux")
# output
# ss
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
 
# OK (skipped=2)
# Breakdown
# the skipUnless option skips the test if the condition evaluates to False
# the skipIf option skips the test if the condition evaluates to True.  

# skipTest method
import sys
 
class LinuxTests(unittest.TestCase):
 
    def test_linux_feature(self):
        if not sys.platform.startswith("linux"):
            self.skipTest("Test only runs on Linux")
# ouput if ran on MacOS
# s
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
 
# OK (skipped=1)
# above we call the self.skipTest() from within the test function itself.  It takes a single string message as its
# argument and always causes the test to be skipped when called.


# example of skipTest and decorators
def regional_jet():
    print('This is a regional jet...')
    return True
def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'
def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies
def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is active')
    return True
def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 33.2
def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999

import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):
  # Checkpoint 1
  @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  # Checkpoint 2
  @unittest.skipUnless(entertainment.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Checkpoint 3
  def test_device_temperature(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  # Checkpoint 3
  def test_maximum_display_brightness(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()
# output

# Output:
# This is a regional jet...
# This is a regional jet...
# This is a regional jet...
# This is a regional jet...
# ssss
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# OK (skipped=4)


# expected Failures
# sometimes we know a test will fail.  In this case we wouldnt want an expected failue to cloud our test results.
#  instead of skipping the test we can mark the test as expected failure.  Expected failures are counted as passed tests
# we use expectedFailure decorator - example
class FeatureTests(unittest.TestCase):
 
    @unittest.expectedFailure
    def test_broken_feature(self):
        raise Exception("This test is going to fail")
# the expectedFailure takes no aruments.  
# output
# x
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
 
# OK (expected failures=1)


# example of expected failure
class FormError(Exception):
    pass

def issue_survey():
    print('Opening customer survey')
    raise FormError('An error occurred when opening customer survey form!')

def log_customer_complaint():
    print('Opening customer complaint form')
    print('Logged customer complaint')
    return 'Success'
import unittest
import feedback

class CustomerFeedbackTests(unittest.TestCase):

  # Write your code below:
  @unittest.expectedFailure
  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')

  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()
#ouptpur
# Opening customer complaint form
# Logged customer complaint
# Opening customer survey
# .x
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK (expected failures=1)



























