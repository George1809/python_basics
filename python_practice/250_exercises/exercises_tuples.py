print("Hello tuples")

'''Exercise 69 - Tuples
Given the code below, use the correct method on line 3 in order to find out the number of elements in my_tup.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

number = len(my_tup)

print(number)

'''Exercise 70 - Tuples
Given the code below, use the correct method on line 3 in order to find out the index of Slovakia in my_tup.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

index = my_tup.index("Slovakia")

print(index)

'''
Exercise 71 - Tuples
Given the code below, write code in order to perform tuple assignment on line 3 and obtain the results below.'''

my_tup = ("Romania", "Poland", "Estonia")

#ro = my_tup[0]
#po = my_tup[1]
#es = my_tup[2]

(ro, po, es) = my_tup

print(ro + ", " + po + ", " + es) #returns 'Romania, Poland, Estonia'


'''Exercise 72 - Tuples
Given the code below, use the correct method on line 3 in order to find out the last element of my_tup in alphabetical order.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

#last = sorted(my_tup)
last = max(my_tup)

print(last) #should return Slovenia


'''Exercise 73 - Tuples
Given the code below, use the correct method on line 3 in order to find out the number of occurrences of Estonia in my_tup.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

number = my_tup.count("Estonia")

print(number)

'''Exercise 74 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the first two of them, using a negative index.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[-5:]

print(my_slice)

'''Exercise 75 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the last three of them, using a negative index.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:-3]

print(my_slice)

'''Exercise 76 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the first three of them, using a positive index.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[3:]

print(my_slice)


'''Exercise 77 - Tuples
Given the code below, use the correct slice on line 3 in order to return all the elements of my_tup, except the last two of them, using a positive index.'''

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

my_slice = my_tup[:5]

print(my_slice)