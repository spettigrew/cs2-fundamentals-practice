"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module 
that start with the letters "is".
"""                 
# YOUR CODE HERE
import math

# m = sorted(math)
# def sort_list(word):
    #lambda takes an argument and returns the length of that. Uses it to determine everything.
    # word.sort(key = len)
math_function = [words for words in dir(math) if words.startswith('is')]

print(math_function)