"""
Example One
"""
my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = my_list1
# How would you verify that my_list1 and my_list2 have the same identity?   -Check memory placement number by using id
print(my_list1)

my_list1.append(7)
# Check if my_list1 and my_list2 still have the same identity.
# If they do, why is that?  - yes. because lists are mutable
print(my_list1)



"""
Example Two
"""
my_text1 = "Lambda School"
my_text2 = my_text1
# How would you verify that my_text1 and my_text2 have the same identity?   -check the id of print(id(my_text1))
print(my_text1)

my_text1 += " is awesome!"
# Check if my_text1 and my_text2 still have the same identity?
print(my_text1)
print(id(my_text1))
# If they do not, why is that?   -yes. because lists are mutable

# Now check if my_text1 and my_text2 have the same value?
print(id(my_text1))
# Do they? Explain why or why not. yes. because 2 was reassignd to 1



"""
Example Three   - lists [], tuples ()
"""
# Initialize a list and assign to produce
produce = ["Apple", "Banana", "Carrot"]
print(produce)
# Initialize a tuple and include a reference to the produce list in the tuple
store = ("Bill's Grocery", produce)
print(id(store))
print(id(produce))
# Add a new item to the produce list
produce.append("Dragonfruit")
print(id(store))
print(produce)

# Did you notice that the identity of store remained the same?
# But I thought if you changed a mutable object, a new object would
# be created in memory? Why did that not occur here?
# A new object has been created, but still holds the same place in memory, so it will not be assigned a new place in memory.