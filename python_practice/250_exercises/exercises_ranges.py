print("Hello ranges")

'''Exercise 78 - Ranges
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range of consecutive integers from 0 to 9 inclusively. Use a single argument inside the parentheses of range()!'''

my_range = range(10)

print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range of consecutive integers from 0 to 9 inclusively. Use two arguments inside the parentheses of range()!'''

my_range = range(0,10)

print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


'''Exercise 80 - Ranges
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return a range of consecutive integers from 117 to 129 exclusively.'''

my_range = range(117,129)

print(list(my_range)) #[117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]

'''Exercise 81 - Ranges
Given the code below, use the correct argument(s) for the range() function on line 1 in order to return [10, 13, 16, 19] when converted to a list.'''

my_range = range(10,20,3)

print(list(my_range)) #[10, 13, 16, 19]

'''Exercise 82 - Ranges
Given the code below, add the correct step as the third argument of the range() function on line 1 in order to return [115, 120] when converted to a list.'''

my_range = range(115, 125, 5)

print(list(my_range)) #[115, 120]

'''Exercise 83 - Ranges
Given the code below, add the correct step as the third argument of the range() function on line 1 in order to return [-75, -60, -45, -30] when converted to a list.'''

my_range = range(-75, -25, 15)

print(list(my_range)) #[-75, -60, -45, -30]

'''
Exercise 84 - Ranges
Given the code below, add the correct step as the third argument of the range() function on line 1 in order to return [-25, 5, 35, 65, 95, 125] when converted to a list.'''

my_range = range(-25, 139, 30)

print(list(my_range)) #[-25, 5, 35, 65, 95, 125]

'''Exercise 85 - Ranges
Given the code below, write the correct range on line 1 in order to return [-10] when converted to a list.'''

my_range = range(-10,-9)

print(list(my_range)) #[-10]