"""
Given an array arr[]. The task is to find the largest element and return it.
"""
# given array arr[] = [1, 8, 7, 56, 90] 
arr = [1, 8, 7, 56, 90]
# initializing largest element as first element of array
largest = arr[0]

for i in range(1, len(arr)):
# comparing each element with largest
    if arr[i] > largest:
# updating largest if current element is greater
        largest = arr[i]
print(largest)
