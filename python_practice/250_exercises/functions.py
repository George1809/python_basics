print("Hello functions")

'''Exercise 171 - Functions
Implement a function called my_func() that simply prints out Hello Python! to the screen and call the function.'''

print("----------------")

def my_func():
    print("Hello Python!")

my_func()

'''Exercise 172 - Functions
Implement a function called my_func() that creates a variable add which stores the result of adding 10 and 20, and prints out the value of add. 
Don't forget to also call the function!'''


print("----------------")

def my_func():
    add = 10 +20
    return add

print(my_func())

def my_func():
    add = 10 +20
    print(add)

my_func()


'''Exercise 173 - Functions
Implement a function called my_func() that takes a single parameter x and multiplies it with 10, also returning the result when the function is called.'''



print("----------------")

def my_func(x):
    res = x * 10
    print(res)

my_func(4)


'''Exercise 174 - Functions
Implement a function called my_func() that takes two parameters x and y and divides x by y, also returning the result when the function is called.'''


print("----------------")

def my_func(x, y):
    return x / y

rez = my_func(11,5)
print(rez)

'''Exercise 175 - Functions
Implement a function called my_func() that takes 3 parameters x, y and z and raises x to the power of y then adds z, also returning the result 
when the function is called.'''

print("----------------")

def my_func(x, y, z):
    return x ** y + z

result = my_func(3,3,3)
print(result)


'''Exercise 176 - Functions
Implement a function called my_func() that takes a single parameter x and multiplies it with each element of range(5), also adding each multiplication result 
to a new (initially empty) list called my_new_list. Finally, the list should be printed out to the screen after the function is called.'''


print("----------------")




def my_func(x):
    my_new_list=[]
    for i in range(5):
        my_new_list.append(i * x)

    return my_new_list

result = my_func(2)
print(result)

'''Exercise 177 - Functions
Implement a function called my_func() that takes a single parameter x (a string) and turns each character of the string to uppercase, also returning the result 
when the function is called.'''


print("----------------")


def my_func(x):
    return x.upper()

result = my_func("Satoshi Nakamoto")
print(result)

'''Exercise 178 - Functions
Implement a function called my_func() that takes a single parameter x (a list) and eliminates all duplicates from the list, 
also returning the result when the function is called.'''

print("----------------")

def my_func(x):
    return list(set(x))


result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)


'''Exercise 179 - Functions
Implement a function called my_func() that takes a single parameter x (a tuple) and for each element of the tuple that is greater than 4 it raises that element 
to the power of 2, also adding it to a new (initially empty) list called my_new_list. Finally, the code returns the result when the function is called.'''

print("----------------")

def my_func(x):
    my_new_list = []
    for i in x:
        if i > 4:            
            my_new_list.append(i ** 2)

    return my_new_list

result = my_func((2, 3, 5, 6, 4, 8, 9))
print(result)

'''Exercise 180 - Functions
Implement a function called my_func() that takes a single parameter x (a dictionary) and multiplies the number of elements in the dictionary with the largest 
key in the dictionary, also returning the result when the function is called.'''

print("----------------")

def my_func(x):
    return len(x) * max(x)
    #return len(x) * sorted(x.keys())[-1]


result = my_func({1: 3, 2: 3, 4: 5, 5: 9, 6: 8, 3: 7, 7: 0})
print(result)


'''Exercise 181 - Functions
Implement a function called my_func() that takes a single positional parameter x and a default parameter y which is equal to 10 and multiplies the two, 
also returning the result when the function is called.'''

print("----------------")


def my_func(x, y=10):
    return x * y
    

result = my_func(5)
print(result)


'''
Exercise 182 - Functions
Implement a function called my_func() that takes a single positional parameter x and two default parameters y and z which are equal to 100 and 200 respectively, 
and adds them together, also returning the result when the function is called.'''

print("----------------")

def my_func(x, y=100, z=200):
    return y+z+x

result = my_func(50)
print(result)


'''Exercise 183 - Functions
Implement a function called my_func() that takes two default parameters x (a list) and y (an integer), and returns the element in x positioned at index y, 
also printing the result to the screen when called.'''

print("----------------")


def my_func(*args, y):
    
    first = args
    return first[y]


result = my_func(5, 6,7,7,8,list(range(2,25,2)), y=5)
print(result) #result should be 10


'''Exercise 184 - Functions
Implement a function called my_func() that takes a positional parameter x and a variable-length tuple of parameters and returns the result of multiplying x 
with the second element in the tuple, also returning the result when the function is called.

'''

print("----------------")

def my_func(x, * args):

    second = args
    return x * second[1]

result = my_func(5, 10, 20, 30, 50)
print(result)

'''Exercise 185 - Functions
Implement a function called my_func() that takes a positional parameter x and a variable-length dictionary of (keyword) parameters and returns the result of 
multiplying x with the largest value in the dictionary, also returning the result when the function is called.

'''


print("----------------")

def my_func(x, **kwargs):

    return x * max(kwargs.values())


result = my_func(10, val1 = 10, val2 = 15, val3 = 20, val4 = 25, val5 = 30)
print(result)


'''Exercise 186 - Functions
Add the correct line(s) of code inside the function in order to get 200 as a result of calling my_func() and have the result printed out to the screen.'''

print("----------------")


var = 10

def my_func(x):
    
    print(x * var)
	
my_func(20)


'''Exercise 187 - Functions
Add the correct line(s) of code inside the function in order to get 100 as a result of calling my_func() and have the result printed out to the screen.'''

print("----------------")

var = 10

def my_func(x):

    #global var
    var = 5
    print(x * var)
	
my_func(20)
print(var)

'''Exercise 188 - Functions
Make the necessary adjustment inside the function in order to get 120 as a result of calling my_func() and have the result printed out to the screen.'''

print("----------------")


def my_func(x):
    var = 12
    print(x * var)
    
	
my_func(10)


'''Exercise 189 - Functions
Add the necessary line of code inside the function in order to get 80 as a result of calling my_func() and have the result printed out to the screen.'''

print("----------------")

var = 8

def my_func(x):
    global var
    print(x * var)
    var = 12
	
my_func(10)


'''Exercise 190 - Functions
Write code that will import only the pi variable from the math module and then it will format it in order to have only 4 digits after the floating point. 
Of course, print out the result to the screen using the print() function.'''

print("----------------")

import math

def my_func():
    print(round(math.pi,4))


my_func()

print("%.4f" % math.pi)