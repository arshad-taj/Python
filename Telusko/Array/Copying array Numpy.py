from numpy import *
from numpy import array

arr = array([1,2,3,4,5])

#adding 5 to each element using for loop
print('********* USING FOR LOOP ************')

for i in range(len(arr)):
    arr[i] = arr[i] + 5

print(arr)

#adding 5 to each element using numpy
print('**** adding 5 to each element using numpy ****')
arr = arr + 5

print (arr)
