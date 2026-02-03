#  Given an array arr[]. Your task is to find the minimum and maximum elements 
# in the array. 
# Examples: 
# Input: arr[] = [1, 4, 3, 5, 8, 6] 
# Output: [1, 8] 
# Explanation: minimum and maximum elements of array are 1 and 8. 
def find_min_max(arr):
    # Initialize min and max with the first element
    minimum = arr[0]
    maximum = arr[0]
    
    # Traverse the array
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return [minimum, maximum]

# Example usage:
arr = [1, 4, 3, 5, 8, 6]
result = find_min_max(arr)
print(result)