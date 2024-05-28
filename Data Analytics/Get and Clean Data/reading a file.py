# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:16:21 2023

@author: geron
"""

#Open Files - to open files you use with open(txt file name) as objectname:  
#Then assign it to a variable using the .read()  variable = objectname.read()


with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)



with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)



# you can also use the readlines() which will give you back a specific line on text or every line - use a for loop for this

with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)


# the readline() option only goes through a certain portion of the text file

with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)



with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)
  






