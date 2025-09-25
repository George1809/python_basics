print("Hello others")


'''Exercise 241 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(1, 5) and return a list of its elements.'''


cph = []

for i in range(1,5):
    cph.append(i)

#cph = [i for i in range(1, 5)]


print(cph)


'''
Exercise 242 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(1, 15, 5) and return a list of its elements squared.'''

print("--------------")

cph = []

for j in range(1,15,5):
    cph.append(j ** 2)

#cph = [i ** 2 for i in range(1,15,5)]

print(cph)


'''
Exercise 243 - Other Concepts
Write a list comprehension on line 1 that will iterate over range(5, 25, 3) and return a list of its elements squared only for the elements that 
are less than or equal to 16.'''

print("--------------")

cph = []

for u in range(5, 25, 3) :
    if u <= 16:
        cph.append(u ** 2)

#cph = [u ** 2 for u in range(5, 25, 3)  if u <= 16]


print(cph)

'''
Exercise 244 - Other Concepts
Write a dictionary comprehension on line 1 that will iterate over range(9) and return a dictionary of key-value pairs where the value 
is equal to the key times 3.'''

print("--------------")



#cph = {v:v + v for v in range(9)}
cph = {v:v * 3 for v in range(9)}

print(cph)

'''
Exercise 245 - Other Concepts
Write a set comprehension on line 1 that will iterate over range(10, 19) and return a set of its elements divided by 2.5.'''

print("--------------")

# cph = {}

# for d in range(10,19):
#     cph.add(d / 2.5)

cph = {d / 2.5 for d in range(10,19)}

print(cph)

'''Exercise 246 - Other Concepts
Write a lambda function on line 1 that takes two parameters x and y and multiplies x with y.'''

print("--------------")

lam = lambda x, y:y * x 

print(lam(2, 5))


'''Exercise 247 - Other Concepts
Write a lambda function on line 1 that takes a list list1 as a parameter, and multiplies each element of range(1, 5) with each element of list1 
using a list comprehension.'''

print("--------------")

lam = lambda list1: [x * y for x in range(1, 5) for y in list1]

print(lam([1, 2]))


'''Exercise 248 - Other Concepts
Use the correct function from the itertools module on line 6, in between the parentheses of list(), in order to concatenate list1 and list2.'''

print("--------------")

import itertools

list1 = [1, 2, 3]
list2 = [4, 5]

result = list(itertools.chain(list1, list2))

print(result)


'''Exercise 249 - Other Concepts
Use the correct function from the itertools module with a for loop and a nested if/else block in order to return all the numbers starting at 20 and up to 31 
with a step of 2. Be careful not to end up with an infinite loop!'''


print("--------------")

import itertools

for n in itertools.count(20,2):
    if n <= 31:
        print(n)
    else: 
        print("Stoped")
        break


'''Exercise 250 - Other Concepts
Use the correct function from the itertools module on line 5, in between the parentheses of list(), in order to return the elements for which the lambda 
function given as an argument returns False.'''

print("--------------")

import itertools

lam = lambda x: x < 5

result = list(itertools.filterfalse(lam, range(10)))

print(result)