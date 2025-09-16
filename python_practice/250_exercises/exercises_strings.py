print("Hello")

'''Exercise 1 - Strings
Given the code below, insert the correct negative index on line 3 in order to get the last character in the string.'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-1])

'''Exercise 2 - Strings
Given the code below, insert the correct positive index on line 3 in order to return the comma character from the string.'''

print("," in my_string)
x = my_string.find(",")
print(my_string[x])

'''Exercise 3 - Strings
Given the code below, insert the correct negative index on line 3 in order to return the w character from the string.'''

print(my_string[-10])

'''Exercise 4 - Strings
Given the code below, insert the correct method on line 3 in order to return the index of the B character in the string.'''

print(my_string.index("B"))
print(my_string.find("B"))

'''Exercise 5 - Strings
Given the code below, insert the correct method on line 3 in order to return the number of occurrences of the letter o in the string.'''

print(my_string.count("o"))

'''
Exercise 6 - Strings
Given the code below, insert the correct method on line 3 in order to convert all letters in the string to uppercase.'''

print(my_string.upper())

'''Exercise 7 - Strings
Given the code below, insert the correct method on line 3 in order to get the index at which the substring Bitcoin starts.'''

print(my_string.find("Bitcoin"))
print(my_string[26:])

'''
Exercise 8 - Strings
Given the code below, insert the correct method on line 3 in order to check of the string starts with the letter X.'''

print(my_string.startswith("X"))

'''Exercise 9 - Strings
Given the code below, insert the correct method on line 3 in order to convert all uppercase letters to lowercase and all lowercase letters to uppercase.'''

print(my_string.swapcase()) # invert case, lower to upper and upper to lower

'''Exercise 10 - Strings
Given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard) from the string.'''

print(my_string.replace(" ",""))

'''xercise 11 - Strings
Given the code below, insert the correct method on line 3 in order to replace all the occurrences of letter i with the substring btc.'''

print(my_string.replace("i","btc"))

'''Exercise 12 - Strings
Given the code below, insert the correct method on line 3 in order to split the entire string in two parts, using the comma as a delimiter.'''

print(my_string.split(","))

'''Exercise 13 - Strings
Given the code below, insert the correct method on line 3 in order to join the characters of the string using the & symbol as a delimiter.'''

print("&".join(my_string))

'''Exercise 14 - Strings
Given the code below, insert the correct code on line 4 in order to concatenate my_string with the following string:
'''

my_other_string = "Poor guy!"

print(my_string + my_other_string)
print(my_string, my_other_string)

'''Exercise 15 - Strings
Given the code below, insert the correct method on line 3 in order to convert the first letter of each word in the string to uppercase.'''

print(my_string.title())

'''Exercise 16 - Strings
Given the code below, use string formatting with the % operator on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.'''

print("In %d, someone paid %s %s for two pizzas." % (2010,"10k","Bitcoin"))

'''Exercise 17 - Strings
Given the code below, use string formatting with the format() method on line 3 to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.'''

print("In {}, someone paid {} {} for two pizzas.".format(2010,"10k","Bitcoin"))

'''Given the code below, use slicing and insert the correct code on line 3 in order to return the substring 2010 from the string. Use positive indexes!'''

print(my_string.find("2010"))
print(my_string[3:7])

'''Given the code below, use slicing and insert the correct code on line 3 in order to return the substring Bitcoin from the string. Use negative indexes!'''

print(my_string[-23:-16])

'''Exercise 20 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the first 12 characters in the string. Use a single, positive index!'''

print(my_string[:12])

'''Exercise 21 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 characters of the string. Use a single, negative index!'''

print(my_string[-9:])

'''Exercise 22 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the entire string in reversed order.'''

print(my_string[::-1])

'''Exercise 23 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return every 7th character of the string, starting with the first character.

The final result should be I,n top'''

print(my_string[::7])

'''Exercise 24 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the first 10 characters. Use a single, positive index!'''

print(my_string[10:])

'''Exercise 25 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the last 4 characters. Use a single, negative index!'''

print(my_string[:-4])