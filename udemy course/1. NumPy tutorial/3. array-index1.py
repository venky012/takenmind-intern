import numpy as np
arr = np.arange(0,12)
print (arr)
print ()
print (arr[0:5])
print ()
print (arr[2:6])
print ()
arr[0:5] = 20
print (arr)
print ()
# Interesting thing & Important

arr2 = arr[0:6]

arr2[:] = 29 #all elements are modified

print (arr2)
print ()
print (arr)
print ()
# creating new array copy

arrcopy = arr.copy()    #for copying the array
print (arrcopy)

