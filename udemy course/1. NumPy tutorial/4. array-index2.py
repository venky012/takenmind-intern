import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (arr2d)
print ()
print (arr2d[0][0])
print ()

#slices of 2d array

slice1 = arr2d[0:3,0:2]
print (slice1)
print ()

arr2d[:2,1:] = 15
print (arr2d)
print ()

#using loops to index
arr_len = arr2d.shape[0]
print(arr_len)
print()
for i in range(arr_len):
    arr2d[i] = i;
print (arr2d);
print ()

#one more way of accessing the rows
print (arr2d[[0,2]])
print ()

print (arr2d[[1,0]])