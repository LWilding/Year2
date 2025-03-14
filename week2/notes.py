import numpy as np

# creating ndarrays using list of list
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]  #list of lists
arr2 = np.array(data2)
print(arr2.ndim)   #2
print(arr2.shape)  # (2,4)


# -Arithmatic with NumPy Arrays-

# Any arithmetic operations between equal-size arrays
# applies the operation element-wise:
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
#[[1. 2. 3.]
 #[4. 5. 6.]]

print(arr * arr)
#[[ 1.  4.  9.]
 #[16. 25. 36.]]

print(arr - arr)
#[[0. 0. 0.]
 #[0. 0. 0.]]

# Arithmetic operations with scalars propagate the scalar
# argument to each element in the array:
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
#[[1. 2. 3.]
# [4. 5. 6.]]

print(arr **2)
#[[ 1.  4.  9.]
# [16. 25. 36.]]

# Comparisons between arrays of the same size yield boolean
# arrays:
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2)
#[[ 0.  4.  1.]
 #[ 7.  2. 12.]]

print(arr2 > arr)
#[[False  True False]
# [ True False  True]]



