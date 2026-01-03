#by using numpy module
from numpy import *

#heterogenous array we can declare using numpy
# arr = array([10,20,3.9,40,'Aniket'])

# for x in arr:
#     print(x,end=" ")

#type casting
# arr = array([10,20,30],float)

# for x in arr:
#     print(x,end=" ")

# arr = linspace(10, 20, 11)
# for x in arr:
#     print(x,end=" ")
# print()

# arr = arange(10,20,2)
# for x in arr:
#     print(x,end = " ")

# arr = logspace(10,20,2)
# for x in arr:
#     print(x,end = " ")

# arr = zeros(10)
# for x in arr:
    # print(x,end = " ")

# arr = ones(10)
# for x in arr:
#     print(x,end = " ")

# arr = full(10,2)
# for x in arr:
#     print(x,end = " ")

#Multi-Dimensional Array
# arr = array(10)
# print(arr)

arr = array([10,20,30,60])
print(arr)

# two dim array
arr = array([[10,20,30],[40,50,60]])
print(arr)

# three dim array         dimension must be same
arr = array([[[1,2,4],[5,6,8]],[[8,9,8],[6,8,2]]])
print(arr)

#by using array module
#from array import *

# arr = array('i',[10,20,30,40,50,60])

# arr.insert(2,88)
# arr.append(77)

# copyarray = array(arr.typecode , (x for x in arr))
# arr[2] = 90
# arr.pop()
# arr.pop(4)
# arr.remove(40)

# for i in range(len(copyarray)):
#     print( copyarray[i], end = ", ")

#slicing
# arr2 = arr[1:5]
# for i in range(len(arr2)):
#     print(arr2[i], end = ", ")

# arr2 = arr[::-1]
# for i in range(len(arr2)):
#     print(arr2[i], end = ", ")

# arr = array('i', [])

# n = int(input("Enter Number of Elements :"))

# for i in range(0,n):
#     arr.append(int(input("Enter Element :")))

# for i in arr:
#     print(i,end=" ")

# arr = array('i', [10,20,30,40,50,60])

# n = arr.index(40)
# print(n)