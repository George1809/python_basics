print("Hello Dictionaries")

'''
Exercise 86 - Dictionaries
Given the code below, use the correct code on line 3 in order to return the value associated with key 4. Do not use a method as a solution for this exercise!'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

value = crypto[4]

print(value)

'''Exercise 87 - Dictionaries
Given the code below, use the correct code on line 3 in order to return the value associated with key 4. This time, use a method as a solution for this exercise!'''


crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

value = crypto.get(4)

print(value)

'''Exercise 88 - Dictionaries
Given the code below, use the correct code on line 3 in order to update the value associated with key 4 to "Cardano".'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto[4] = "Cardano"

print(crypto[4])

'''Exercise 89 - Dictionaries
Given the code below, use the correct code on line 3 in order to add a new key-value pair to the dictionary: 6: "Monero"'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto[6] = "Monero"

print(crypto[6])

'''Exercise 90 - Dictionaries
Given the code below, use the correct code on line 3 in order to return the number of key-value pairs in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

number = len(crypto)

print(number)

'''Exercise 91 - Dictionaries
Given the code below, use the correct code on line 3 in order to delete the key-value pair associated with key 3. Do not use a method as a solution for this exercise!'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

del crypto[3]

print(crypto)

'''Exercise 92 - Dictionaries
Given the code below, use the correct code on line 3 in order to delete the key-value pair associated with key 3. This time, use a method as a solution for this exercise!'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.pop(3)

print(crypto)

'''Exercise 93 - Dictionaries
Given the code below, use the correct code on line 3 in order to verify that 7 is not a key in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

check = 7 not in crypto

print(check)

'''Exercise 94 - Dictionaries
Given the code below, use the correct method on line 3 in order to delete all the elements in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.clear()

print(crypto)

'''Exercise 95 - Dictionaries
Given the code below, use the correct code on line 3 in order to get a list of tuples, where each tuple represents a key-value pair in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

result = crypto.items()

print(list(result))

'''Exercise 96 - Dictionaries
Given the code below, use the correct function on line 3 in order to get the sum of all the keys in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

add = sum(crypto)

print(add)

'''Exercise 97 - Dictionaries
Given the code below, use the correct method on line 3 in order to get a list of all the values in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

val = crypto.values()

print(list(val))

'''Exercise 98 - Dictionaries
Given the code below, use the correct function on line 3 in order to get the smallest key in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

key = min(crypto)

print(key)


'''Exercise 99 - Dictionaries
Given the code below, use the correct method on line 3 in order to get a list of all the keys in the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

keys = crypto.keys()

print(list(keys))

'''
Exercise 100 - Dictionaries
Given the code below, use the correct method on line 3 in order to return and remove an arbitrary key-value pair from the dictionary.'''

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

crypto.popitem()
crypto.popitem()

print(len(crypto))