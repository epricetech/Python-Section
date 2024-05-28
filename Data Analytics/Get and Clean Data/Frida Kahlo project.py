# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:31:49 2023

@author: geron
"""

paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
dates = [1939, 1933, 1946, 1940]
paintings = list(zip(paintings, dates))
print(paintings)

paintings.append('The Broken Column, 1944')
paintings.append('The Wounded Deer, 1946')
paintings.append('Me and My Doll, 1937')
print(paintings)

paintings.extend(['The Broken Column, 1944', 'The Wounded Deer, 1946', 'Me and My Doll, 1937'])
#print(paintings)

total_paintings = len(paintings)
print(total_paintings)

audio_tour_number = 1
for i in range(total_paintings):
  audio_tour_number += i



#havent been able to make work yet
master_list = list(zip(audio_tour_number, paintings))
print(master_list)