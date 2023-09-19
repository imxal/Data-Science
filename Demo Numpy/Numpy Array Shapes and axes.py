import numpy as np
# np.array(24)
# np.array([1,2,3,4])
# print(np.array([[1,1,1],[1,2,1]]))
# print(np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]]))
# numpy_arr = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
# print(numpy_arr.shape)
# print(numpy_arr.ndim)


numpy_arr = np.array([x for x in range(1,10)])
print(numpy_arr)
print(numpy_arr.reshape(3,3))
numpy_arr = np.array([x for x in range(1,13)])
print(numpy_arr.reshape(2,2,3))
print(numpy_arr.reshape(3,2,2))
print(numpy_arr.reshape(2,2,-1))

numpy_arr=numpy_arr.reshape(3,2,2)
print(numpy_arr)
print(numpy_arr.reshape(-1))









