"""
1. Create a "numbers" list that contains two different integer values and two different floating point values.

2. Create a "strings" list that contains three different strings.

3. Print the 4th number of your numbers list and the 1st string of your strings list.

4. Iterate through your strings list and print each string.
"""

num_list = [1, 3, 4.5, 7.9]

string_list = ["Lambda is not the same as it once was", "said", "all current students."]

print(num_list[3], string_list[0])

for lists in num_list, string_list:
    print(lists)