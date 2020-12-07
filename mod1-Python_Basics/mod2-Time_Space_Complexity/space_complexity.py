"""
Use Big O notation to classify the space complexity of the function below.

Space complexity - anything additional the function is adding to memory.
"""
def fibonacci(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i-2] + lst[i-1])
    
    return lst[n-1]

    # appending is storing a value in the list. O(n)



"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci_two(n):
    x, y, z = 0, 1, None
    
    if n == 0:
        return x
    if n == 1:
        return y
    
    for i in range(2, n):
        z = x + y
        x, y = y, z

    return z

    # space complexity remains the same, because we're only returning the value of z. O(1)
    # Time complexity is O(n) because the number of operations will increase as the list increases.


"""
Use Big O notation to classify the space complexity of the function below.
"""
def do_something(n):
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(i + j)
    
    return lst

    # append =  O(n)