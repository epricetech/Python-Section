# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:21:57 2023

@author: geron
"""

# Set containers - from file Intro to Python sets has a combination of operations it can perform.  
#  These operations allows you to combine sets, find differences and intersections of set and more
#  These can be useful for filtering items, categorizing, combining ect ect
#  Main set operations are
# Unions, Intersections(and intersection updates), Differences(and difference updates), Symmetric Differences(symetric difference updates)

# Combining Sets - Unions
#  To merge either sets or frozen sets we can use the .union() method or the | operator.  Doing so will return a 
# a new set or frozen set containg all elements from both sets without duplicates

# example of combining sets with the union() method
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})
# Get the union using the .union() method
combined_tags = prepare_to_py.union(py_and_dry)
print(combined_tags)
# Output
# {'electric guitar', 'classic', 'heavy metal', 'rock and roll', 'rock', 'synth'}

# example of the | operator to combine sets
 # Get the union using the | operator
frozen_combined_tags = py_and_dry | prepare_to_py
print(frozen_combined_tags)
# ouput
#frozenset({'electric guitar', 'rock and roll', 'rock', 'synth', 'heavy metal', 'classic'})

# breakdown of the 2 examples
#Note that the return value in both methods takes the form of the left operand. In the first example since
 # prepare_to_py() called the union() function, so the result was a regular set. In the second example, 
 # since py_and_dry was the left operand, the end result was a frozenset.


# example of using the | operator and instructions for what is going on
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}
#Our goal now is to consolidate the tags into one dictionary for each category. To accomplish this we need to: 
#     Loop over song_data.items() (all the items in song_data)
# # On each iteration of the loop, create a set for each category of tags. This will require creating 
# two new sets, one for song_data and one for user_tag_data. In addition to creating the sets on each iteration, 
# create a new key inside of new_song_data for each category and set the value to be a union of the two new sets.
for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set | user_tag_set
print(new_song_data)


# Set Intersections
#  when you want to find items in multiple sets that have something in common.  Set container has a method called
# .intersection() which returns a new set or frozenset consiting of those elements.  You can also use the & operator
# Similar to the other operations, the type of the first operand (a set or frozenset on the left side of the
# operator or method) determines if a set or frozenset is returned when finding the intersection.

# example of an intersection
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
 
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})
 
# Find the intersection between them while providing the `frozenset` first.
frozen_intersected_tags = py_and_dry.intersection(prepare_to_py)
print(frozen_intersected_tags)
# output
#frozenset({'electric guitar', 'rock'})

# example of intersection using the & operator
# Find the intersection using the operator `&` and providing the normal set first
intersected_tags = prepare_to_py & py_and_dry
print(intersected_tags)
# output
# {'rock', 'electric guitar'}

#  You an also use .intersection_update() method which will not create a new set of intersections but update the
# original set to contain the results of the intersection

# example of using the & operator for intersection and looping through dictionary and nested loop
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
#We want to add a feature to our app which will recommend songs based on the most recent songs a user has listened to. One way we can do this is by using the intersection of the recent song tags. Let’s use the intersection of these tags to find which other songs are similar.
#First, create a variable called tags_int that stores the intersection between the tags for the user_recent_songs two recent songs 'Retro Words' and 'Lowkey Space'. Remember to convert each list into a set to perform the operation.
#We will be using these common tags as a basis for finding a recommended song in song_data.
tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])
#Now, let’s find the recommended songs based on the common tags we found in the previous step.
#Find all other songs in song_data which have these tags. Store the songs which have any matching tags into a dictionary called recommended_songs. Make sure that you do not add any songs which the user has listened to recently!
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val

print(recommended_songs)
# output
#{'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}


# Set Differences
#  This allows us to find unique elements in one set.  We can use the .difference() method or - operator
#  it will return a set or frozen set that contains only the elements from the first set which are not found in 2nd set
#  Similar to the other operations, the type of the first operand (a set or frozenset on the left side of the
# operator or method) determines if a set or frozenset is returned when finding the difference.

# example of set differences
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
 
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})
 
# Find the elements which are only in prepare_to_py
only_in_prepare_to_py = prepare_to_py.difference(py_and_dry)
print(only_in_prepare_to_py)
# output
# {'heavy metal', 'synth'}

# example using the - operator
# Find the elements which are only in py_and_dry
only_in_py_and_dry = py_and_dry - prepare_to_py
print(only_in_py_and_dry)
# output
#frozenset({'rock and roll', 'classic'})

# this operation also allows for the .difference_update() method which instead of creating a new set it updates orginal set

# example of differences - creating a dictionatry - looping through dictionary
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
#In order to try and increase the accuracy of your app’s song recommendations, we have decided to add some logic that will find the differences between liked and disliked songs. We will create another recommended dictionary of songs based on these differences.
#Create a new variable called tag_diff that is the set difference between the tags inside of the one song of user_liked_song and the one song of user_disliked_song. Don’t forget to convert the list of tags into a set to perform this operation!
tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])
#Now that you know the difference in tags between the liked song and disliked song, use those tags to find any songs from song_data which contain them.
#Make sure not to include the liked and disliked songs. Store the newly found songs into a dictionary called recommended_songs.
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
      if tag in tag_diff:
          if key not in user_liked_song and key not in user_disliked_song:
              recommended_songs[key] = val
print(recommended_songs)
# output
# {'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'], 'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional']}



# Symmetric difference
#  This is liek the opposite of the intersection operation.  Symmetric will return elements that are unique to each set
#  to perform we use the .symmetric_difference() method or the ^ operator
# example of symmetric differences using the .symmetric_difference() method
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
 
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})
 
# Find the elements which are exclusive to each song and not shared using the method
exclusive_tags = prepare_to_py.symmetric_difference(py_and_dry)
print(exclusive_tags)
# output
# {'heavy metal', 'synth', 'rock and roll', 'classic'}

# exaqmple of symmetric difference using the ^ operator
# Find the elements which are exclusive to each song and not shared using the operator
frozen_exclusive_tags = py_and_dry ^ prepare_to_py
print(frozen_exclusive_tags)
# output
# frozenset({'synth', 'rock and roll', 'heavy metal', 'classic'})

# we can also use the symmetric_difference_update() method that wont return a new set but update orginal set

#  Example of symmetric difference operation and instructions
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
#The users of our app would like to be able to see which tags are unique between them and their friends. This means that the tags which are not shared between the user and their friend are shown. In order to find this, we can use the symmetric difference.
#First, create a set called user_tags.
#Use a loop to populate the set to contain all of the tags from the songs in user_song_history.
user_tags = set()
for key, val in user_song_history.items():
    user_tags.update(set(val))
#Next, repeat the same logic in order to collect all of the tags from the friend_song_history and store it in a set called friend_tags.
friend_tags = set()
for key, val in friend_song_history.items():
    friend_tags.update(set(val))
#Finally, find the unique tags by getting the symmetric difference between user_tags and friend_tags.
#Store the result in a set called unique_tags and then print it!
unique_tags = user_tags ^ friend_tags
print(unique_tags)
# output
# {'intense', 'fast', 'happy', 'rap', 'moving', 'party', 'warm', 'pop', 'country', 'sad', 'emotional', 'romance', 'fiddle', 'dance', 'upbeat'}


# overall review breakdown
# Sets Review
# Great Job! You have learned about many different ways to work with set and frozenset containers! We looked at:

# Creating a set or frozenset:

# For set containers, we can use curly braces {}, the set() constructor, or set comprehension.
# For frozenset containers, we can only use the frozenset() constructor.
# Adding items to a set:

# We can add items to a set individually using the .add() method.
# We can add multiple items at once using the .update() method.
# Removing items from a set:

# The .remove() method is used to remove elements from a set.
# The .discard() method can also be used to remove elements from a set. It does not throw a KeyError if the 
# element is not found.
# Finding Elements:

# The in keyword can be used with set and frozenset containers to test if an element exists inside of them.
# Union:

# A union can be found using set or frozenset containers with the .union() method or | operator.
# Intersection:

# An intersection can be found using set or frozenset containers with the .intersection() method or & operator.
# Difference:

# The difference can be found using set or frozenset containers with the .difference() method or - operator.
# Symmetric Difference:

# The symmetric difference can be found using set or frozenset containers with the .symmetric_difference() 
# method or ^ operator.


# overall review example and instructions
# For these checkpoints, we will review the different operations which you can perform on set and frozenset containers.

# First, create a frozenset called my_tags which contains the elements:
#     'pop', 'electronic', 'relaxing', 'slow', and 'synth'.

# Checkpoint 2 Passed

# Stuck? Get a hint
# 2.
# Try finding the union of music_tags and my_tags, but make sure to return the result as a frozenset. 
# Store the result in a variable called frozen_tag_union.

# Checkpoint 3 Passed

# Stuck? Get a hint
# 3.
# Now store the intersection of music_tags and my_tags into a variable called regular_tag_intersect. 
# Make sure that it is stored as a normal set this time.

# Checkpoint 4 Passed

# Stuck? Get a hint
# 4.
# Now try finding the difference of my_tags with music_tags. Store this result in a variable called
#  frozen_tag_difference. The type of the result should be a frozenset.

# Checkpoint 5 Passed

# Stuck? Get a hint
# 5.
# Finally, get the symmetric difference of music_tags with my_tags and store it in a variable called 
# regular_tag_sd. The result should should be a set and not a frozenset.
music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Checkpoint 1
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Checkpoint 2
frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

# Checkpoint 3
regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

# Checkpoint 4
frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

# Checkpoint 5
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)









