import numpy as np

a=np.array([[1,2],[3,4]]) #2x2 matrix 1, 2 for row =0 and 3,4 for row =1
b=np.array([[1,2]]) #a row vector
b2=np.array([[1],[2]]) #a column vector
 
#
print(np.dot(a,b2))
 

print(np.dot(b,a))

print(np.matmul(a,b2))

#column vector 3 elements long
c=np.array([[1],[2],[3]])
#row vector 2 elements long
d=np.array([[1,2]])
#outter product
print(np.matmul(c,d))