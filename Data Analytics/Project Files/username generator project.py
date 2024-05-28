# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:44:45 2023

@author: geron
"""
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password



# def username_generator(first_name, last_name):
#   username = first_name[:3] + last_name[:4]
#   return username

# def password_generator(user_name):
#     password = ""
#     for i in range(0, len(user_name)):
#         password += user_name[i-1]
#     return password