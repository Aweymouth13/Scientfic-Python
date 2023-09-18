"""
###HW for week 3 and 4
KTX887
Aaron Weymouth
https://app.noteable.io/f/3f1af83b-486a-4122-9257-2dd002f52dd8/Week-3-Assignments.ipynb

"""

#import libs
import numpy as np
import svd_image
import matplotlib.pyplot as plt
from matplotlib.image import imread
from sklearn.decomposition import PCA



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

"""
START OF HW 4

"""
print('start of homework 4')
print('--' * 10)
print('Exercise 4')

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
det = np.linalg.det(A)
if det == 0:
    print("matrix can't be inverted, determinant is zero.")
else:
    print("matrix can be inverted.")

#we know we can't invert the matrix directly bc the determinate is zero, singular matrix

#svd
U, S, VT = np.linalg.svd(A)
print('U:\n', U)
print('S:\n', S)
print('V:\n', VT)

#the max value of S is
print('the max value of S is: ', np.max(S))

#machine error ~1E-15
rcond = S.max() * 1E-15 #arbitrary, near machine precision

print('singular values', S)
print('rcond', rcond)

#actual v. effective rank
actual_rank = np.linalg.matrix_rank(A)
effective_rank = np.sum(S > rcond) # number of singular values larger than rcond

print('actual rank', actual_rank)
print('effective rank', effective_rank)

#the actual and effective ranks are the same, if we want them different
#we will need to choose a value that is larger than the second largest singular value



#Exercise 5
print('--' * 10)
print('Exercise 5')

#91x91 rand matrix, compute rank, recompute by SVD, truncate, recompose ...

aaa=np.random.rand(91,91)
print('the rank of the matrix is: ', np.linalg.matrix_rank(aaa))

#svd
U, S, VT = np.linalg.svd(aaa)

#truncate terms in S rcond<1E-2
rcond = 1e-2
effective_rank = np.sum(S > rcond)

#recompose
S_trunc = np.diag(S[:effective_rank])
U_trunc = U[:, :effective_rank]
VT_trunc = VT[:effective_rank, :]
aaa_recomposed = np.dot(U_trunc, np.dot(S_trunc, VT_trunc))

print('the effective rank is: ', effective_rank)

print('--' * 10)
print('Exercise 6')

#after reading function will automatically plot if plotme=True
svd_image.denoise_image()
#150 chosen by the slope of the curve plotted
svd_image.denoise_image(k=150)




#added custom functions to play with different variations of K
#enter file name

file_name = 'photo2.jpeg'
svd_image.plot_reconstructed_images(file_name)



print('-' * 10)
print('Exercise 7')

#use linspace to create matrix, then eigendecomp

#linspace
matrix = np.linspace(40,60,9).reshape(3,3)

#eigen decomp
evects, evals = np.linalg.eig(matrix)

#rank
rank = np.linalg.matrix_rank(matrix)

print('the eigenvalues are: ', evals)
print('the eigenvectors are: ', evects)
print('the rank of the matrix is: ', rank)

#simplest way is to check if the matrix has a linear combonoation of another row
#R3 is a scalar multiple of R1 therefore rank 2

print('-' * 10)
print('Exercise 8')

#find patter and create matrix, reshape, eigenvectors, and eigenvalues, then confirm.

#given array pattern start at 4^2 and end at 6^2 9 values for spacing
z = np.linspace(16,36,9)
print('the OG matrix is: ', z)

#reshape into 3x3 matrix
A = z.reshape(3,3)

#eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)

#diag matrix using eigenvalues
Lamb_duh = np.diag(eigenvalues)
print('the diagonal matrix is: ', Lamb_duh)

#reconstruction/confirm
A_reconstructed = np.dot(eigenvectors, np.dot(Lamb_duh, np.linalg.inv(eigenvectors)))
Lamb_duh_reconstructed = np.dot(np.linalg.inv(eigenvectors), np.dot(A, eigenvectors))

#check if matricies are equal
bool_equal_A = np.allclose(A, A_reconstructed)
bool_equal_lamb_duh = np.allclose(Lamb_duh, Lamb_duh_reconstructed)

print('the reconstructed matrix A is equal to the original matrix A: ', bool_equal_A)
print('the reconstructed matrix Lambda is equal to the original matrix Lambda: ', bool_equal_lamb_duh)


#will attempt unassigned exercise, if doesn't work will fix 
#when assigned next week, do not understand pcademo3 function
#will just plot w/ matplotlib

print('-' * 10)
print('Exercise 9: for funzies')

#data from class
rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T

#pca with 2 components first
pca = PCA(n_components=2)
pca.fit(X)

#principle comp
components = pca.components_

#mean
mean = pca.mean_

#plot w/ matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.5)
plt.quiver(mean[0], mean[1], components[0, 0], components[0, 1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(mean[0], mean[1], components[1, 0], components[1, 1], angles='xy', scale_units='xy', scale=1, color='g')
plt.axis('equal')
plt.title('PCA with 2 Components')
#plt.show()


#PCA 1 comp
pca_1 = PCA(n_components=1)
pca_1.fit(X)

#principle comp
components_1 = pca_1.components_

#mean
mean_1 = pca_1.mean_

#1D projection
X_proj = pca_1.transform(X)

#inverse back to OG space
X_inv = pca_1.inverse_transform(X_proj)

#plot w/ matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.5, label='Original Data')
plt.scatter(X_inv[:, 0], X_inv[:, 1], alpha=0.5, label='Projection onto 1st Principal Component')
plt.quiver(mean_1[0], mean_1[1], components_1[0, 0], components_1[0, 1], angles='xy', scale_units='xy', scale=1, color='r')
plt.axis('equal')
plt.title('PCA with 1 Component')
plt.legend()
#plt.show()
