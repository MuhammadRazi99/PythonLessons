import numpy as np
from numpy.core.fromnumeric import ndim
""" new_array=np.array([1,2,3,4,5])
print(new_array)
print(type(new_array))
print(np.__version__)
 """
# using tuple to create an array
""" another_arr=np.array((1,2,3,4))
print(another_arr)
 """
# 0-D array:
array0=np.array(23)
# print(array0)

# 1-D array:
array1=np.array([1,2,3,4,5])
# print(array1)

#2-D array:
array2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(array2)

# 3-D Array
array3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(array3)

# how to find the diminsion of the array
""" print(array0.ndim)
print(array1.ndim)
print(array2.ndim)
print(array3.ndim) """

# generating higher dimminsion arrays
array5=np.array([1,2,3,4,5],ndmin=5)
# print(array5)
# print(array5.ndim)

# accessing the element of the dimminsion
# print(array3[0,1,0])

# array slicing of 1-D array same as list slicing
# print(array1[1:4])

# array slicing of 2-D array
""" print(array2[1,1:4]) #gives the [1][1],[1][2],[1][3]
print(array2[0:2,2]) #gives the [0][2],[1][2]
print(array2[0:2,1:4]) #gives the {[0][1],[0][2],[0][3]},{[1][1],[1][2],[1][3]} """

# to check the array type of the array 
""" arrInt=np.array([1,2,3,4])
arrStr=np.array(["Nauman Bro","Ahmed","NAbeel","HAfiz","Muneeb Bhai"])
print(arrInt.dtype)
print(arrStr.dtype) """

# NumPy operations
# similarly with * / -
""" add=array2+2
print(add) """

# adding two arrays
# similarly with * / -
""" add=array2+array1
print(add)
mul=array2*array1
print(mul) """

# dot   product
""" a=np.array([1,2,3,4])
b=np.array([10,20,30,40])
print(np.dot(a,b)) """

# exp 
""" a=np.array([10,20,30,40])
print(np.exp(a)) """