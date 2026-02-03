"""
You are given two arrays a[] and b[], return the Union of both the arrays in any 
order. 
The Union of two arrays is a collection of all distinct elements present in either of 
the arrays. If an element appears more than once in one or both arrays, it should be 
included only once in the result. 
"""
# given arrays a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
def union_arrays(a, b): 
# making an empty list to store the union of both arrays
    union_array = [] 
    
    for element in a:
# adding elements of array a to union_array if not already present
        if element not in union_array:
            union_array.append(element)
 # same for array b   
    for element in b:
        if element not in union_array:
            union_array.append(element)

    return union_array

# testing the function with given arrays
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
result = union_arrays(a, b)
# printing the union of both arrays in sorted order
print(sorted(result))  