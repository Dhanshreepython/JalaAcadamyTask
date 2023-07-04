# 1. Write a function to add integer values of an array

mylist = []
for i in range(6):
    mylist.append(i)
print(mylist)


# 2. Write a function to calculate the average value of an array of integers
def average( a , n ):
    sum = 0
    for i in range(n):
        sum += a[i]    
    return sum/n
arr = [10, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print(average(arr, n))


# 3. Write a program to find the index of an array element.

import numpy as np 
arr = np.array([2, 5, 6, 3, 9, 8, 2, 2, 5])
 
print("All index value of 2 is: ", np.where(arr == 2)[0])
 
print("First index value of 5 is: ",np.where(arr == 5)[0][0])


# 4. Write a function to test if array contains a specific value

animals = ['Dog', 'Cat', 'Bird', 'Fish']
def animal():
    for animal in animals:
        if animal == 'Bird':
            print('Chirp!')
animal()


# 5. Write a function to remove a specific element from an array
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)


cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)


# 6. Write a function to copy an array to another array

arr1 = [1, 2, 3, 4, 5];         
arr2 = [None] * len(arr1);         
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i];     
     
print("Elements of original array: ");    
for i in range(0, len(arr1)):    
   print(arr1[i]),    
     
print();    
     
print("Elements of new array: ");    
for i in range(0, len(arr2)):    
   print(arr2[i]),  

# 7. Write a function to insert an element at a specific position in the array
arr = [1, 2, 3, 4, 5]
num=int(input("Enter a number to insert in array : "))
index=int(input("Enter a index to insert value : "))
if index >= len(arr):
    print("please enter index smaller than",len(arr))
else:
    # insering element ‘num’ at ‘index’ position
    arr.insert(index, num)  
print("Array after inserting",num,"=",arr)


# 8. Write a function to find the minimum and maximum value of an 

arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
  if arr[i] < mini: mini = arr[i] 
  
if arr[i] > maxi: maxi = arr[i]

print (mini)
print (maxi)


# 9. Write a function to reverse an array of integer values
def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1
# Driver function to test above function
A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)

# 10. Write a function to find the duplicate values of an array

def find(array):
    duplicate_element_array = []

    for i in array:
        if array.count(i) > 1 and i not in duplicate_element_array:
            duplicate_element_array.append(i)

    print("Duplicate element in an array : ", end="")
    for i in sorted(duplicate_element_array):
        print(i, end=" ")
array = [-1, 8, 1, 8, -1, 5, 1, -3]
print("Array= ", array)
find(array)


# 11. Write a program to find the common values between two arrays
a = [1, 2, 3, 4, 5]
b = [5, 2, 6, 3, 9]

result = [i for i in a if i in b]

print("The common elements are:", result)


# 12. Write a method to remove duplicate elements from an array
lst = [1, 5, 3, 6, 3, 5, 6,  1] 
print ("The original array is: ",lst) 
result = []

for i in lst: 
   if i not in result: 
      result.append(i) 
print ("The array after removing dupulicates elements: ", result)


# 13. Write a method to find the second largest number in an array
# Python program to find second largest number in array

def secondSmallest(arr, N):
    arr.sort(reverse=True)
    return arr[1]
arr = [30, 15, 75, 7, 94, 45, 64, 22, 61]
N = len(arr)
print("The second smallest number in an array: ",
    secondSmallest(arr, N))


# 15. Write a method to find number of even number and odd numbers in an array

n = int(input("Enter size of array: "))
arr = []
print("Enter array elements: ")
for i in range(0,n):
    temp = int(input())
    arr.append(temp)
even = 0
odd = 0
for i in range(0, n):
   if arr[i]%2==0 :
    even += 1
   else:
    odd += 1
print("Number of even elements: ",even )
print("Number of odd elements: ",odd)



# 16. Write a function to get the difference of largest and smallest value
def solve(nums):
   if len(nums) <= 4:
      return 0
   nums.sort()
   ans = float("inf")
   for i in range(4):
      mi = nums[i]
      ma = nums[-(3-i+1)]
      ans = min(ma-mi,ans)
   return ans
nums = [3,7,2,12,16]
print(solve(nums))



