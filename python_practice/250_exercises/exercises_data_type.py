print("Hello Data type")

'''Exercise 101 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a string.'''

value = 10

conv = str(value)

print(type(conv))

'''Exercise 102 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to an integer.'''

value = "10"

conv = int(value)

print(type(conv))

'''Exercise 103 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a floating-point number.'''

value = 10

conv = float(value)

print(type(conv))

'''Exercise 104 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a list.'''

value = "Hello!"

conv = list(value)

print(type(conv))

'''Exercise 105 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a tuple.'''

value = [1, 2, 3, 10, 20, 30]

conv = tuple(value)

print(type(conv))

'''
Exercise 106 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a frozen set.'''

value = (10, 20, 40, 10, 25, 30, 45)

conv = frozenset(value)

print(type(conv))

'''Exercise 107 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a binary representation.'''

value = 10

conv = bin(value)

print(conv)

'''
Exercise 108 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value to a hexadecimal representation.'''

value = 10

conv = hex(value)

print(conv)

'''Exercise 109 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value from binary to decimal notation.'''

value = '0b1010'

conv = int(value, 2)

print(conv)

'''Exercise 110 - Data Type Conversions
Given the code below, use the correct function on line 3 in order to convert value from hexadecimal to decimal notation.'''

value = '0xa'

conv = int(value,16)

print(conv)