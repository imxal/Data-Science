import numpy as np

first_numpy_array = np.array([1,2,3,4])
print(first_numpy_array)

array_with_zeros = np.zeros((3,3))
print(array_with_zeros)

array_with_ones = np.ones((2,2))
print(array_with_ones)

empty_array = np.empty((2,3))
print(empty_array)

arange_array = np.arange(12)
print(arange_array)

print(arange_array.reshape(3,4))

#linspace for linearly spaced data elements
"""takes 3 arguments->1st=first element=1
                   ->2nd=last element=6
                   ->3rd=total no.of equidistant elements=5"""

np_linspace = np.linspace(1,4, 5)
print(np_linspace)

oneD_array=np.arange(15)
print(oneD_array)

TwoD_array=oneD_array.reshape(5,3)
print(TwoD_array)

ThreeD_array=np.arange(27).reshape(3,3,3)
print(ThreeD_array)







