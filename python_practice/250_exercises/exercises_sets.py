print("Hello sets")

'''Exercise 61 - Sets
Given the code below, use the correct function on line 3 in order to convert my_list to a set.'''

my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = set(my_list)

print(type(my_set))

'''Exercise 62 - Sets
Given the code below, use the correct function on line 3 in order to convert my_list to a frozen set.'''

my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]

my_set = frozenset(my_list)

print(type(my_set))

'''
Exercise 63 - Sets
Given the code below, use the correct code on line 3 in order to verify if element 10 is in my_set.'''

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

check = 10 in my_set

print(check)

'''Exercise 64 - Sets
Given the code below, use the correct method on line 3 in order to add the element 19 to my_set.'''

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.add(19)

print(my_set)

'''Exercise 65 - Sets
Given the code below, use the correct method on line 3 in order to delete the element 9 from my_set.'''

my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}

my_set.remove(9)

print(my_set)

'''Exercise 66 - Sets
Given the code below, use the correct method on line 4 in order to find out the common elements of my_set1 and my_set2.'''

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

common = my_set.intersection(my_set2)

print(sorted(list(common)))

'''Exercise 67 - Sets
Given the code below, use the correct method on line 4 in order to join the elements of my_set1 and my_set2.'''

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

join = my_set1.union(my_set2)

print(sorted(list(join)))

'''Exercise 68 - Sets
Given the code below, use the correct method on line 4 in order to find out the elements of my_set2 that are not members of my_set1.'''

my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}

diff = my_set1.difference(my_set2)

print(sorted(list(diff)))