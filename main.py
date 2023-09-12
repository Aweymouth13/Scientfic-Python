import numpy as np

"""
Consider the matrix ...
np.array([[1,2,3],[4,5,6],[7,8,9]])
What happens when you try to invert this matrix directly? Why? How could you have
determined this outcome ahead of time?
Use SVD to decompose this matrix. Based on the singular values, where should you
truncate Σ (i.e. which rcond value)?
Given Σ what is the "effective" rank of the (decomposed) matrix?

"""

#matrix
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
#if we try to invert this matrix it won't work, det = 0
print('singluar matrix bc det is:\n', np.linalg.det(A))

#SVD
U, S, V = np.linalg.svd(A)
print('U:\n', U)
print('S:\n', S)
print('V:\n', V)
