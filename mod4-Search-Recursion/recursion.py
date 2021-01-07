"""
Let's say that I give you a list of numbers.
"""
my_list = [1,2,3,4,5]
"""
I ask you to write a function that returns the sum of all the numbers in the list.

With an iterative approach, you would need a variable to keep track of the sum, a loop that adds each item in the list to the sum, and to return the sum after the loop ends.
"""

def sum_list(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum
"""
This iterative function depends on the ability to loop through each item in the list. Another way to iterate through a collection is with recursion. It's a little harder to understand at first, but the resulting code is often cleaner, simpler, and easier to understand.

How many numbers can you sum without having to rely on the loop construct? The answer is two.  How can we think of our problem as a collection of sums of only two numbers?

I'll put it another way. If you had the following, and I asked you to use parentheses to split the problem into sums of two numbers, how would you do it?

You start by separating the problem into two subproblems:
"""

1 + 2 + 3 + 4 + 5
(1 + (2 + 3 + 4 + 5))
"""
Now we continue doing so until we can no longer divide the problem into two subproblems:
"""

1 + 2 + 3 + 4 + 5
(1 + (2 + 3 + 4 + 5))
(1 + (2 + (3 + 4 + 5)))
(1 + (2 + (3 + (4 + 5))))
(1 + (2 + (3 + (4 + (5)))))
"""
Let's see if we can use this example to write a recursive function to sum a list of numbers.

The first thing we need to consider for our recursive function is how to know when to stop adding parentheses.

When we add the first set, we ask — what is the sum of the first item and the sum of the rest of the items?
But, as we continue dividing the problem into subproblems, we "run out" of the "rest of items." Once we no longer have a list of items longer than one, we cannot break the list into the first item and the rest of the items. So if someone asks us to sum one number, we know that the result is equal to that number. This "running out" is the base case for our recursive function.

Note: We usually place the base case of a recursive function in the first few lines of the function, though it doesn't have to be there.

Let's start writing out our function in pseudocode:

sum_list(items)
    if the length of items is one
        return the one item in the list

But what if someone asks us to sum more than one item? We must sum the first number and the sum of the rest of the items in the list.

Let's add this to our pseudocode:

sum_list(items)
    if the length of items is one
        return the one item in the list
    otherwise
        return the first item from the list + sum_list(the rest of the items)

Now let's convert our pseudocode into actual Python code:
"""

def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

"""
The first line of our pseudocode function prints the value of n. Then, we check the base case — is n equal to 0 — and, if it is, we return and stop recursing. Our pseudocode's final return is our recursive case, where we decrement the previous call's n value and call the function itself with that decremented value (the recursive case).

Let's turn it into actual Python code and then look at a visualization of the call stack when we call this function.
"""

def print_to_zero(n):
    print(n)
    if n == 0: # base case
        return
    return print_to_zero(n - 1) # recursive case
"""
Three rules of recursion
Let's use our sum_list function to see if we can make more generalized observations about recursion.

The three rules for a recursive function are:

Must have a base case
Must change its state to move towards the base case
Must call itself
1. Must have a base case
The first rule for recursion is that a recursive algorithm must have a base case.

What is a base case? It allows the algorithm to stop recursing. With our sum_list function, what allows the algorithm to stop recursing?

It's the first line: if len(items) == 1:. Notice how if this condition is true, it returns a value and doesn't make a recursive call to itself. We are saying to stop recursing if the list to sum has only one item.
"""
def sum_list(items):
    if len(items) == 1: # Base Case
        return items[0]
    else:
        return items[0] + sum_list(items[1:])
"""
2. Must change its state to move towards the base case
The second rule is that the algorithm must change its state to move towards the base case.

How does our function do that? With each subsequent recursion, the list passed into sum_list is one item smaller. For example, on the first recursion, items is [2,3,4,5], and on the subsequent recursion, items is [3,4,5].
"""

def sum_list(items):
    if len(items) == 1: # Base Case
        return items[0]
    else:
        return items[0] + sum_list(items[1:]) # items[1:] has one less item

"""
It's obvious then that regardless of the list's length, we will reach the base case where the list we are summing has only one item.

3. Must call itself
The third rule is that the algorithm must call itself. We are doing this on the final line of the function.
"""

def sum_list(items):
    if len(items) == 1: # Base Case
        return items[0]
    else:
        return items[0] + sum_list(items[1:])  
        # (items[1:] changes state to move towards base case)
        # Calls sum_list recursively(calls itself)

"""
When should I use recursion?
Now that we've considered one recursive algorithm and discussed the three recursion rules, we should think about when it is appropriate to use recursion.

When you are out in the world solving real-world problems, the problem itself doesn't say, "Hey! You should use recursion to solve me!" It's your job as the problem-solver to decide if using recursion makes sense.

So, what clues or hints might you find within a problem that could lead you to use recursion?

Compute the nth term
List the first or last n terms
Generate all permutations
Another way to think about it is to use the three rules. Is there a clear base case or stopping point that you are working towards (Rule 1)? Is there a straightforward way that the state of the data changes with each iteration that brings it closer to the base case (Rule 2)?

"""

"""
Let's look at another typical example of learning recursion–computing factorials.

A factorial (n!) is computed by taking n * (n-1) * (n-2) * ... 1.

For example, 4! is computed by doing the following:

4 * (4 - 1) * (4 - 2) * (4 - 3)

4 * 3 * 2 * 1

24

When does computing factorials come in handy? They are required when figuring combinations; how many ways can we arrange these many items? Or how many orders can there be with this list? Also, they are useful for determining ways of choosing a certain number of items from a collection. For example, if you have 100 different menu items, how many possible 5-item orders could you make?

Okay, let's get back to our 4! example. Let's look again at the computation and see if we can make some connections to our three rules for recursion.

4! = 4 * (4 - 1) * (4 - 2) * (4 - 3)

First, how did we know to stop writing? Why didn't we keep going?

4! = 4 * (4 - 1) * (4 - 2) * (4 - 3) * (4 - 4) * (4 - 5) * (4 - 6) * ...

Well, before, when talking about the general case, we wrote factorial like this:

n! = n * (n - 1) * (n - 2) * ... 1

What is the last item in the procedure, or how did we know to stop? When the item is 1. Could this serve as the base case for our recursive factorial function? Let's try it out!

We start by writing pseudocode.

recursive_factorial(n)
    if n equals 1
        return 1
Okay, so now we have a base case (Rule 1). But what about changing the state to move towards the base case (Rule 2)?

Let's look again at 4!.

4! = 4 * (4 - 1) * (4 - 2) * (4 - 3)

Notice that just like we can write 4! as 4 * (4 - 1) * ... 1, we can write (4 - 1)! as (4 - 1) * (4 - 2) * ... 1. So the inverse would also be true; we can write (4 - 1) * (4 - 2) * ... 1 as (4 - 1)!. Which means we can write 4! as 4 * (4 - 1)!.

Okay, we can't miss what we just discovered. Our discovery means that we can express factorial in terms of itself. For any n! we can solve it by breaking it into smaller sub-problems that also require factorial (Rule 3). And Rule 2 is satisfied because we make each subsequent call to factorial on a smaller n.

recursive_factorial(n)
    if n equals 1
        return 1
    otherwise
        return n * recursive_factorial(n - 1)
Now we need to convert our pseudocode into actual Python code. Luckily, in Python, this is usually a trivial change.
"""

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

n = [8, 32, 9, 43, 1, 0, 29]
# --------------- Challenge ------------------------
"""
Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.
What would be the base case(s) we'd have to consider for implementing this function?
"""
def recursive_search(n, target):
#     if len(n) == 1:
#         return print(n[0])
#         return True
#     else:
#         return print(n[0] + recursive_search(n[1:]))
#     return False
    for i in range (len(n)):
        cur_num = n[i]
        if cur_num == target:
            return i
    return -1


print(recursive_search, 1)
# target = 1