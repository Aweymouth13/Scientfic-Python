"""
###HW for week 3 and 4
KTX887
Aaron Weymouth
https://app.noteable.io/f/3f1af83b-486a-4122-9257-2dd002f52dd8/Week-3-Assignments.ipynb

"""

#import libs
import numpy as np


#Exercise 1
print('--' * 10)
print('Exercise 1')

#given two arrays, perform operations on them
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([79,89,99])

print('array 1 : \n', arr1)
print('array 2 : \n', arr2)

#replacing each column of arr1 with arr2
arr1[:,0] = arr2
arr1[:,1] = arr2
arr1[:,2] = arr2
print('array 1 with array 2 replacing each column : \n', arr1)

#reset array1
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])

#replaces each row of arr1 with arr2
arr1[0,:] = arr2
arr1[1,:] = arr2
arr1[2,:] = arr2
print('array 1 with array 2 replacing each row : \n', arr1)

#resetting array1
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])

#replaces 2nd and 3rd column of arr1 with arr2
arr1[:, 1:3] = arr2[1:]
print('array 1 with array 2 replacing 2nd and 3rd column : \n', arr1)


#Exercise 2
print('--' * 10)
print('Exercise 2')

#given an array, use np.tile, reshape, determinate of different arrays

#initial array
a=np.array([10,20,30,40,50])

#tile to repeate entire array 5 times
np.tile(a, 5)
print('the array repeated 5 times : \n', np.tile(a, 5))

#reshape into 2d matrix using i
b = np.tile(a,5).reshape(len(a),-1)
print('the array reshaped into 2d matrix : \n', b)

#create a square matrix for det
c = np.tile(a,5).reshape(len(a),-1)
det = np.linalg.det(c)
print('the determinant of the square matrix : \n', det)


#part 2: take determinate of given matrix
a=np.array([[1,2.333,-4],[-4,-3,-.001],[-.2,5.3,9.99]])
det_a = np.linalg.det(a)
print('the determinant of the given matrix : \n', det_a)

#part 3:

#flatten array from part 2
a_flat = a.flatten()
print('the flattened array : \n', a_flat)

#tile a_flat * 9
a_tile = np.tile(a_flat,9)
print('the array tiled 9 times : \n', a_tile)

#reshape into square matrix
a_reshaped = a_tile.reshape(len(a_flat), -1)
print('the reshaped array in 2d matrix : \n', a_reshaped)

#take det
det_a_reshaped = np.linalg.det(a_reshaped)
print('the determinate of the reshaped array: \n', det_a_reshaped)



#Exercise 3
print('--' * 10)
print('Exercise 3')

#given a system of linear equations, solve the system with np.linalg.solv, and nop.linalg.inv and np.dot, verify solution

#create coefficient matrix
A = np.array([[8, 6, -10], [-4, -8, 10], [16, 16, 0]])
B = np.array([2, 5, -3])

#solve using np.linalg.solve
a_values = np.linalg.solve(A, B)
print('solution using np.linalg.solve: ', np.around(a_values, 2))


#solve using np.linalg.inv + np.dot, if we dot a inverse with b, we get the same solution
A_inv = np.linalg.inv(A)
a_values_dot = np.dot(A_inv, B)
print('solution using np.linalg.inv + np.dot: ', np.around(a_values_dot, 2))

#asked to verify solutions, all close checks if all elements are close to each other (boolian)
verify_solve = np.allclose(np.dot(A, a_values), B)
verify_inv = np.allclose(np.dot(A, a_values_dot), B)

print(f'verification using np.linalg.solve method: {verify_solve}')
print(f'verification using np.linalg.inv + np.dot method: {verify_inv}')

#shows elements with subsitutions
print('Original equations:')
print('8a0 + 6a1 - 10a2 = 2')
print('-4a0 - 8a1 + 10a2 = 5')
print('16a0 + 16a1 = -3')

print('\nSubstituting values from np.linalg.solve method:')
print(f'8({a_values[0]:.2f}) + 6({a_values[1]:.2f}) - 10({a_values[2]:.2f}) = 2')
print(f'-4({a_values[0]:.2f}) - 8({a_values[1]:.2f}) + 10({a_values[2]:.2f}) = 5')
print(f'16({a_values[0]:.2f}) + 16({a_values[1]:.2f}) = -3')

print('\nEvaluating the equations:')
print(f'{8*a_values[0] + 6*a_values[1] - 10*a_values[2]:.2f} = 2')
print(f'{-4*a_values[0] - 8*a_values[1] + 10*a_values[2]:.2f} = 5')
print(f'{16*a_values[0] + 16*a_values[1]:.2f} = -3')

