import numpy as np
data = np.array([[1,8,3,3,4], [1,8,9,9,4], [1,8,3,3,4]])
new_array = [tuple(row) for row in data]
print ("type(new_array)=", type(new_array))
print ("type(new_array[0])=", type(new_array[0]), new_array[0])
print ("type(new_array[1])=", type(new_array[1]), new_array[1])
print ("type(new_array[2])=", type(new_array[2]), new_array[2])
uniques = np.unique(new_array)
print (uniques)

"""
https://docs.scipy.org/doc/numpy/reference/generated/numpy.unique.html
numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False)[source]
Find the unique elements of an array.

Returns the sorted unique elements of an array. 
There are three optional outputs in addition to the unique elements: 
the indices of the input array that give the unique values, 
the indices of the unique array that reconstruct the input array, 
and the number of times each unique value comes up in the input array.


"""