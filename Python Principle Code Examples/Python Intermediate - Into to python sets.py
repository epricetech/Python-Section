# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:42:20 2023

@author: geron
"""

# Python sets - is a group of elements that are unordered and don not contain fuplicates.  Used for organizing items
# and performing set mathematics.  
# For example, we can imagine two different groups of items that have some similarities and differences. 
# Using set mathematics, we can find the matching items, differences, combine the sets based on different parameters, 
# and more! This is especially helpful when combing through very large datasets.
# Different types of sets.  One is called a Frozen set which is immutable and does not include methods that
# modify the frozenset in any way


# Creating a Set
#  Muliple ways to create a set.  A set object can be created by passing an iterable object into its constructor
# using curly braces or using a set comprehension
# syntax of these methods
# Creating a set with curly braces
music_genres = {'country', 'punk', 'rap', 'techno', 'pop', 'latin'}
 
# Creating a set from a list using set()
music_genres_2 = set(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])
#  creating a set from a list with duplicates produces a set with the duplicates removed
# example of this
# Creating a set from a list that contains duplicates
music_genres_3 = set(['country', 'punk', 'rap', 'pop', 'pop', 'pop'])
print(music_genres_3)
# output
# {'country', 'punk', 'pop', 'rap'}

# sets can contain any combination of data types as long as they are unique values - example
music_different = {70, 'music times', 'categories', True , 'country', 45.7}

# we can also create an empty set with one specific method - example
# Creating an empty set using the set() constructor
# Doing set = {} will define a dictionary rather than a set.  
empty_genres = set()

#  Similiar to list comprehensions, we can create sets using a set comprehension and a data set(such as a list) - example
items = ['country', 'punk', 'rap', 'techno', 'pop', 'latin']
 
music_genres = {category for category in items if category[0] == 'p'}
print(music_genres)
# output is a set containing all elements from items starting with the letter P
# {'punk', 'pop'}


# example of create a set from list and create a set comprehension
genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)
print(survey_genres)
#For this step, use a set comprehension to create a new set called survey_abbreviated which stores the first three letters of each genre found in the survey results without duplication.
survey_abbreviated = {genre[0:3] for genre in genre_results}
print(survey_abbreviated)
#output
# {'k-pop', 'rock', 'pop', 'rap', 'latin', 'classical', 'country'}
# {'cla', 'lat', 'k-p', 'pop', 'rap', 'roc', 'cou'}


# Creating a Frozenset
#  You can only create a frozenset using its constructor.  And cant modify the elements inside of it
# syntax example of creating a frozenset
# Creating a frozenset from a list
frozen_music_genres = frozenset(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])
# Example of creating an empty frozenset
empty_frozen_music_genres = frozenset()

# example of creating a frozen set from list
top_genres = ['rap', 'rock', 'pop']

# Write your code below!
frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)
# output

# Output:
# frozenset({'rock', 'rap', 'pop'})


# Adding to a Set
# There are 2 different ways to add elements to a set.
# Neither of these methods will add a duplicate item to the set.
# A frozenset cant have any itemes added to it so these methods wont work
#also when printed they are not printed in the same order in which they entered the set because sets are unordered
# 1. The .add() method can add a single element to the set
# example
# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}
# Add a new tag to the set and try to add a duplicate.
song_tags.add('guitar')
song_tags.add('country')
print(song_tags)
# output
# {'country', 'acoustic', 'guitar', 'folk'}

# 2. the .update() method can add multiple elements
# example
# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}
# Add more tags using a hashable object (such as a list of elements)
other_tags = ['live', 'blues', 'acoustic']
song_tags.update(other_tags)
print(song_tags)
# output
# {'acoustic', 'folk', 'country', 'live', 'blues'}

# overall example of create set, add to set 
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
#For the first step, create a new set called tag_set from the original song’s tags located in song_data.
tag_set = set(song_data['Retro Words'])
#xt add 3 user tag strings to tag_set
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)
# Finally, update song_data so that the value of the key, 'Retro Words' is equal to the updated tag set.
song_data = {'Retro Words': tag_set}
print(song_data)
# output
# {'Retro Words': {'exciting', 'warm', 'happy', 'electric', 'pop'}}


# Removing from a Set
#  Two methods for removing specific elements from a set and does not work on Frozensets
# 1. .remove() method searches for an element within the set and removes it if it exists, otherwise a KeyError is thrown
# Example of .remove() method
# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
# Remove an existing element
song_tags.remove('folk')
print(song_tags)
# Try removing a non-existent element
song_tags.remove('fiddle')
#output
# {'blues', 'acoustic', 'country', 'guitar', 'live'}
# Traceback (most recent call last):
# File "some_file_name.py", line 9, in <module>
#  song_tags.remove('fiddle')
# KeyError: 'fiddle'

# 2. .discard() method works the same way but doesnt throw an exception if element is not present
# example of the .discard() method
# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
# Try removing a non-existent element but with the discard method
song_tags.discard('guitar')
print(song_tags)
# Try removing a non-existent element but with the discard method
song_tags.discard('fiddle')
print(song_tags)
# output
# {'folk', 'acoustic', 'blues', 'live', 'country'}
# {'folk', 'acoustic', 'blues', 'live', 'country'}


# example of remove() method.  Pay close attention to the final 2 lines of code that replaces the value of the key 'retrowords'
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')
#For the last step, replace the value of the key, 'Retro Words' inside of song_data_users so that it is equal to the updated tag set.
song_data_users = {'Retro Words': tag_set}
print(song_data_users)
# output
#{'Retro Words': {'happy', 'pop', 'electric', 'warm'}}



# Finding Elements in a Set
#  Both set and frozenset items cannot be accessed by a specific index since they are both unordered and have no indices
#  We can use the in keyword to test if an element is in a set of frozen set
#  example of finding an element
# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
 
# Print the result of testing whether 'country' is in the set of tags or not
print('country' in song_tags)
# output
# True
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
frozen_tags = frozenset(song_tags)
print('rock' in frozen_tags)
# output
# False


# example and instructions of looping through list and adding it to another list and then append main list
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
#Create a list called bad_tags. Then, iterate through each element of tag_set, adding tags to bad_tags that don’t belong.
bad_tags = []
for tags in tag_set:
  if tags not in allowed_tags:
    bad_tags.append(tags)
#Using the collected bad_tags, write another loop to iterate over each of the tags in bad_tags, and remove the elements from tag_set so we have only the allowed tags.
for badtag in bad_tags:
  tag_set.remove(badtag)
print(tag_set)
#Finally, replace the value of the key, 'Retro Words' inside of song_data_users so that it is equal to the updated tag set.
song_data_users = {'Retro Words': tag_set}
print(song_data_users)
# output
# {'warm', 'happy', 'pop'}
# {'Retro Words': {'warm', 'happy', 'pop'}}








































