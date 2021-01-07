"""
We want to write a simple program to conduct a linear search on a collection of data. Let's write a function that takes a list (arr) and an integer (target) as its input and returns the integer idx where the target is found. If the target does not exist in the arr, then the function should return -1.
A linear search goes through each index, one by one, left to right, until we have reached the target value.
"""
def linear_search(arr, target):
    # loop through each item in the input array
    for idx in range(len(arr)):
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

"""
Rewrite the implementation of linear search below so that the algorithm searches from the end of the list to the beginning.
"""
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5

def linear_search(arr, target):
    # loop through each item in the input array
    for idx in reversed(range(len(arr))):
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

print(linear_search(arr, target))