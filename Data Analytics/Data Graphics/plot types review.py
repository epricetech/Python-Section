# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:58:55 2023

@author: geron
"""
#  bar charts
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]
# past_years_averages - years - error
# Make your chart here
#First, create a figure of width 10 and height 8.
plt.figure(figsize=(10,8))
#Plot the blue bars, which have the heights listed in past_years_averages.
plt.bar(range(len(past_years_averages)),past_years_averages, yerr=error,capsize=5)
#Add error bars of cap size 5 and heights corresponding to the list error.

#Set the axis to go from -0.5 to 6.5 on the x-axis and 70 to 95 on the y-axis.
plt.axis([-0.5,6.5,70,95])
#Create an ax object using plt.subplot(). Use ax to set the x-axis ticks to be range(len(years)) and the x-axis labels to be the years list.
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

#Add the title "Final Exam Averages", x-axis label "Year", and y-axis label "Test average".
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test average')
plt.savefig('my_bar_chart.png')
plt.show()


#  side by side bars


from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here
#  middle_school_a  - middle_school_b  - unit_topics

#Using create_x, make the lists school_a_x and school_b_x which will determine where to put the bars for Middle School A and Middle School B along the x-axis.   - use function above instead of writing the code for list comprehnsion
school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)
plt.figure(figsize=(10,8))

ax = plt.subplot()
#Plot a set of bars representing middle_school_a and a set representing middle_school_b next to each other on the same graph.
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x,middle_school_b)

#Create a new list of x-values called middle_x, which are the values in the middle of school_a_x and school_b_x. This is where we will place the x-ticks. Look at the final graph to see this placement.  use list comprehension and zip for this code middle_x
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
#Set the x-ticks to be the middle_x list.
ax.set_xticks(middle_x)
#Set the x-tick labels to be the list unit_topics.
ax.set_xticklabels(unit_topics)
#Create a legend, as shown in the final graph, that labels the first set of bars Middle School A and the second set of bars Middle School B.
plt.legend(['Middle School A', 'Middle School B'])
#Create a title (“Test Averages on Different Units”), x-axis label (“Unit”), and y-axis label (“Test Average”).
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')


plt.savefig('my_side_by_side.png')
plt.show()




#  Stacked Bars

from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)
#  As, Bs, Cs, Ds, Fs, unit_topics
#The Bs bars will go on top of the As bars, but at what heights will the Cs, Ds, and Fs bars start?

#The bottom of the bars representing the Cs will be at the height of the As plus the Bs. We can do this in NumPy (a scientific computing package for Python) with the np.add function. c_bottom, the starting heights for the Cs, will be:

c_bottom = np.add(As, Bs)
#Underneath the definition of c_bottom, define d_bottom (where the Cs end), and f_bottom (where the Ds end).
c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom,Cs)
f_bottom = np.add(d_bottom,Ds)
plt.figure(figsize=(10,8))
#create your plot here
#Plot the As, Bs, Cs, Ds, and Fs. Give each one the appropriate bottom list that will stack them on top of each other.
plt.bar(x, As)
plt.bar(x, Bs, bottom=As)
plt.bar(x, Cs, bottom=c_bottom)
plt.bar(x, Ds, bottom=d_bottom)
plt.bar(x, Fs, bottom=f_bottom)

ax = plt.subplot()

ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
#Give the plot the title you see in the final graph, and the same x-axis label and y-axis label.
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')


plt.show()
plt.savefig('my_stacked_bar.png')



#  two histograms on a plot

import codecademylib3
from matplotlib import pyplot as plt

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]
#  exam_scores1  - exam_scores2
# Make your plot here
plt.figure(figsize=(10,8))

#Make a histogram of the exam_scores1, normalized, with 12 bins.
plt.hist(exam_scores1, bins=12, density=True, histtype='step', linewidth=2)
#Make a histogram of the exam_scores2, normalized, with 12 bins.
#Add histtype = 'step' to each plt.hist call, in order to make these histograms more visible.
#We can also make the lines thicker by setting the linewidth inside the calls to plt.hist.
#Let’s set the linewidth to be 2 for both histograms.
plt.hist(exam_scores2, bins=12, density=True, histtype='step', linewidth=2)
#Create a legend showing that the first set of data is "1st Yr Teaching" and the second set of data is "2nd Yr Teaching".
plt.legend(['1st Yr Teaching', '2nd Yr Teaching'])
#Add the title, x-axis label, and y-axis label that you see on the final graph.
plt.title('Final Exam Score Distribution')
plt.xlabel('Percentage')
plt.ylabel('Frequency')

plt.show()
plt.savefig('my_histogram.png')





#  pie Chart

import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]
# unit_topics  - num_hardest_reported
#Make your plot here
plt.figure(figsize=(10,8))

#Label the slices with the unit_topics list and put a percentage label on each slice, rounded to the nearest int.
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
#Set the axes to be 'equal'.
plt.axis('equal')
plt.title('Hardest Topics')



plt.show()
plt.savefig('my_pie_chart.png')



#  line with shade error

import codecademylib
from matplotlib import pyplot as plt

hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]
#  hours_reported -  exam_scores
# Create your figure here
plt.figure(figsize=(10,8))
plt.plot(exam_scores,hours_reported, linewidth=2)
#let’s assume the error on students’ reporting of their hours studying is 20%.
#Create a list hours_lower_bound, which has the elements of hours_reported minus 20%, and a list hours_upper_bound, which has the elements of hours_reported plus 20%.
#You can do this with a list comprehension that looks like:
#y_lower_bound = [element - (element * error_in_decimal) for element in original_list_of_y_values]
hours_lower_bound = [element - (element * 0.2) for element in hours_reported]
hours_upper_bound = [element + (element * 0.2) for element in hours_reported]
#Shade the area between hours_lower_bound and hours_upper_bound with an alpha of 0.2.
plt.fill_between(exam_scores,hours_lower_bound,hours_upper_bound,alpha=0.2)
plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')

plt.show()
plt.savefig('my_line_graph.png')








