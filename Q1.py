"""
Given an integer array arr[] and an integer k, your task is to find and return
the kth smallest element in the given array.
"""
# given array [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k =4
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
# creating a list to store elements of arr (no change in original array)
temp = []
for i in arr:
#copying elements of arr to temp 
        temp.append(i)
#sorting the array using sort() function
temp.sort()

#returning the kth smallest element by accessing the (k-1)th index
print(temp[k-1]) 