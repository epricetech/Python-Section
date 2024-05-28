# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:49:10 2023

@author: geron
"""

def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []

  for value in lst:
    normalized_num = (value - minimum) / (maximum - minimum)
    normalized.append(normalized_num)

  return normalized

print(min_max_normalize([0, 25, 50, 75, 100]))
# should print [0.0, 0.25, 0.5, 0.75, 1.0]
print(min_max_normalize([10, 12, 14]))
# should print [0.0, 0.5, 1.0]


def standardize(lst, mean, std_dev):
  standardized = []

  for value in lst:   
    standardized_num = (value - mean) / (std_dev)    
    standardized.append(standardized_num)

  return standardized

print(standardize([1, 2,, 3, 4, 5], 3.0, 1.41))
# should print [-1.418, -0.709, 0.0, 0.709, 1.418]
print(standardize([10, 15, 20], 15.0, 4.08))
# should print [-1.225, 0.0, 1.225]