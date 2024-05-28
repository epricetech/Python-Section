# -*- coding: utf-8 -*-
"""
Created on Mon May  8 12:01:17 2023

@author: geron
"""

## numPy is used for linear algebra.  We us the np.array() function and list or nested list arguments for arrays with more than
## one dimension

##  example
v = np.array([1,2,3,4,5,6])
##  2 dimensions and nested list

A = np.array([[1,2],[3,4]])

##  can create matrix using the np.column_stack() function
# Example
v = np.array([-2,-2,-2,-2])
u = np.array([0,0,0,0])
w = np.array([3,3,3,3])
 
A = np.column_stack((v, u, w))
print(A)

# to access the shape of a matrix or vector once its been created as an array we call the .shape attribute to array variable
A = np.array([[1,2],[3,4]])
print(A.shape)


#  To access individual elements in array we can index the array using []  
A = np.array([[1,2],[3,4]])
print(A[0,1])


#  also select a subset or entire dimension of array using a colon
A = np.array([[1,2],[3,4]])
print(A[:,1])




import numpy as np

# Given vectors
vector_1 = np.array([-2,-6,2,3])
vector_2 = np.array([4,1,-3,8])
vector_3 = np.array([5,-7,9,0])

matrix = np.column_stack((vector_1, vector_2, vector_3))
print(matrix)
print(matrix.shape)
print(matrix[:,2])



# linear algebra operations
# to mulitply vector or matrix by scalar
A = np.array([[1,2],[3,4]])
4 * A

#  the addition of 2 vectors or matrix
A = np.array([[1,2],[3,4]])
B = np.array([[-4,-3],[-2,-1]])
A + B


#  matrix multiplication using either np.natmul() functon or using the @ symbol as shorthand  
A = np.array([[1,2],[3,4]])
B = np.array([[-4,-3],[-2,-1]])
 
# one way to matrix multiply
np.matmul(A,B)
# another way to matrix multiply
A@B


import numpy as np

# Given
# 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])
# 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])
# 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])

# Calculate D = 4A - 2B
D = 4*A - 2*B
print(D)

# Calculate E = AC
E = A@C
print(E)

# Calculate F = CA
F = C@A
print(F)


# Special Matrices 
#  identity matrix constructed using the np.eye() function with takes an integer argument that determins the n x n size
#  of the square identity matrix
# 4x4 identity matrix
identity = np.eye(4)

# a matrix or vector of all zeros using the np.zeros() function which takes a tuple argument for the shape of array
# 5-element vector of zeros
zero_vector = np.zeros((5))

# 3x2 matrix of zeros
zero_matrix = np.zeros((3,2))



import numpy as np

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])

print(A@B)
print(np.matmul(B,A))
#  transpose both matrix
print(A.T)
print(B.T)


#  np.linalg.   with .norm() and .inv()  - norm or length magnitude and inverse for inv
v = np.array([2,-4,1])
v_norm = np.linalg.norm(v)

A = np.array([[1,2],[3,4]])
print(np.linalg.inv(A))


#  can solve for unknown variables using np.linalg.solve() with takes a and b paramaters
# each array in A is an equation from the above system of equations
A = np.array([[1,4,-1],[-1,-3,2],[2,-1,-2]])
# the solution to each equation
b = np.array([-1,2,-2])
# solve for x, y, and z
x,y,z = np.linalg.solve(A,b)




import numpy as np
# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z

# Given
'''
4x + z = 2
-y + 2z - 3x = 0
.5y - x - 1.5z = -4
'''
A = np.array([[4, 0, 1],[-3, -1, 2],[-1, 0.5, -1.5]])

b = np.array([2,0,-4])

x,y,z = np.linalg.solve(A,b)
print(x,y,z)


