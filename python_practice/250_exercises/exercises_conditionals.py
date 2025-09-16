print("Hello conditionals")

'''Exercise 111 - Conditionals
Considering the code below, write code that prints out True! if x has 50 characters or more.'''

x = "The days of Python 2 are almost over. Python 3 is the king now."

if len(x) >= 50:
    print("True!")


'''Exercise 112 - Conditionals
Considering the code below, write code that prints out True! if x is a string and the first character in the string is T.'''


x = "The days of Python 2 are almost over. Python 3 is the king now."

if x.startswith("T") and type(x) is str:
    print("True2!")



'''Exercise 113 - Conditionals
Considering the code below, write code that prints out True! if at least one of the following conditions occurs:

the string contains the character z

the string contains the character y at least twice'''

x = "The days of Python 2 are almost over. Python 3 is the king now."

if "z" in x or x.count("y") >=2 :
    print("True3!")


'''
Exercise 114 - Conditionals
Considering the code below, write code that prints out True! if the index of the first occurrence of letter f is less than 10 and prints out False! if the same condition is not satisfied.'''

x = "The days of Python 2 are almost over. Python 3 is the king now."


if x.index("f") < 10:
    print("True4!")
else:
    print("False!")
    
if x.find("f") < 10:
    print("True4!")
else:
    print("False!")


'''Exercise 115 - Conditionals
Considering the code below, write code that prints out True! if the last 3 characters of the string are all digits and prints out False! otherwise.

Hint! Use the appropriate method to check if the requested string slice contains digits only.'''

x = "The days of Python 2 are almost over. Python 3 is the king now."

if x[-3].isdigit():
    print("True!")
else:
    print("False!")



'''Exercise 116 - Conditionals
Considering the code below, write code that prints out True! if x has at least 8 elements and the element positioned at index 6 is a floating-point number and prints out False! otherwise.'''

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]


if len(x) >= 8 and type(x[6]) is float:
    print("True4!")
else:
    print("False!")


'''Exercise 117 - Conditionals
Considering the code below, write code that prints out True! if the second string of the first list in x ends with the letter h and the first string of the second list in x also ends with the letter h, and prints out False! otherwise.'''

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]




if str(x[3][1]).endswith("h") and str(x[7][0]).endswith("h"):
    print("True5!")
else:
    print("False!")

if x[3][1].endswith and x[7][0].endswith("h"):
    print("True5!")
else:
    print("False!")

'''Exercise 118 - Conditionals
Considering the code below, write code that prints out True! if one of the following two conditions are satisfied and prints out False! otherwise.

the third string of the first list in x ends with the letter h

the second string of the second list in x also ends with the letter h'''

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]


if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print("True6!")
else:
    print("False!")



'''Exercise 119 - Conditionals
Considering the code below, write code that prints out True! if the largest value among the first 3 elements of the list
is less than or equal to the smallest value among the next 3 elements of the list. Otherwise, print out False!

Hint! Use the appropriate slices to make the comparison.'''

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

#print(x[0:3])
#print(max(x[0:3]))

#print(x[3:6])
#print(min(x[3:6]))

if max(x[0:3]) <= min(x[3:6]):
    print("True7!")
else:
    print("False!")

'''Exercise 120 - Conditionals
Considering the code below, write code that prints out True! if 115 appears at least once inside the list or if it is the first element in the list. 
Otherwise, print out False!

Hint! Use the appropriate method to check if 115 is the first element in the list.'''

x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]

#print(x.count(115))
#print(x.index(115))

if x.count(115) >= 1 or x.index(115) == 0:
    print("True7!")
else:
    print("False!")

'''Exercise 121 - Conditionals
Considering the code below, write code that prints out True! if the value associated with key number 5 is Perl or 
the number of key-value pairs in the dictionary divided by 5 returns a remainder less than 2. Otherwise, print out False!'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


#print(x[5])
#print(len(x) % 5)

if x[5] == "Perl" or (len(x) % 5) < 2:
    print("True8!")
else:
    print("False!")



'''Exercise 122 - Conditionals
Considering the code below, write code that prints out True! if 3 is a key in the dictionary and
the smallest value (alphabetically) in the dictionary is C#. Otherwise, print out False!'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


#print(3 in x.keys())

#print(min(list(x.values())))

#print(max(list(x.values())))

if 3 in x.keys() and min(list(x.values())) == "C#":
    print("True9!")
else:
    print("False!")

if 3 in x and sorted(x.values())[0] == "C#":
    print("True9!")
else:
    print("False!")


'''
Exercise 123 - Conditionals
Considering the code below, write code that prints out True! if the last character of the largest (alphabetically) value in the dictionary is n. 
Otherwise, print out False!'''


x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


#print(list((sorted(x.values()))[-1])[-1])
#print(sorted(x.values())[-1][-1])

#print(max(list(x.values())))

if sorted(x.values())[-1][-1] == "n":
    print("True!")
else:
    print("False!")

'''Exercise 124 - Conditionals
Considering the code below, write code that prints out True! if the largest key in the dictionary divided by the second largest key in the dictionary returns
 a remainder equal to the smallest key in the dictionary. Otherwise, print out False!'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


#print(list(x.keys()))
#print(max(x.keys()))
#print(sorted(x.keys())[-2])
#print(min(x.keys()))

if max(x.keys()) % sorted(x.keys())[-2] == min(x.keys()):
    print("True10!")
else:
    print("False!")

if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print("True10!")
else:
    print("False!")

'''Exercise 125 - Conditionals
Considering the code below, write code that prints out True! if the sum of all the keys in the dictionary is less than the number 
of characters of the string obtained by concatenating the values associated with the first 5 keys in the dictionary. Otherwise, print out False!'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

#print(sum(x.keys()))

#print(len("".join(list(x.values())[0:5])))

if sum(x.keys()) < len("".join(list(x.values())[0:5])):
    print("True!")
else:
    print("False!")

if sum(x) < len(x[1] + x[2] + x[3] + x[4] + x[5]):
    print("True!")
else:
    print("False!")


'''Exercise 126 - Conditionals
Considering the code below, write code that prints out True! if the 3rd element of the first range is less than 2, prints out False! if the 5th element 
of the first range is 5, and prints out None! otherwise.'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

#print(x)
#print(x[0][2]) 
#print(x[0][4])


if x[0][2] < 2:
    print("True")
elif x[0][4] == 5:
    print("False!")
else:
    print("None")

'''Exercise 127 - Conditionals
Considering the code below, write code that prints out True! if the 3rd element of the 3rd range is less than 6, prints out False! if the 1st element 
of the second range is 5, and prints out None! otherwise.'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

#print(x[2][2])

if x[2][2] < 6:
    print("True")
elif x[1][0] == 5:
    print("False!")
else:
    print("None")


'''Exercise 128 - Conditionals
Considering the code below, write code that prints out True! if the last element of the first range is greater than 3, prints out False!
 if the last element of the second range is less than 9, and prints out None! otherwise.'''    

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

#print(x)
#print(x[0][-1])

if x[0][-1] > 3:
    print("True")
elif x[1][-1] < 9:
    print("False!")
else:
    print("None")

'''Exercise 129 - Conditionals
Considering the code below, write code that prints out True! if the length of the first range is greater than or equal to 5, prints out False!
if the length of the second range is 4, and prints out None! otherwise.'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if len(x[0]) >= 5:
    print("True")
elif len(x[1]) == 4:
    print("False!")
else:
    print("None")

'''Exercise 130 - Conditionals
Considering the code below, write code that prints out True! if the sum of all the elements of the first range is greater than the sum 
of all the elements of the third range, prints out False! if the largest element of the second range is greater than the largest element 
of the third range, and prints out None! otherwise.'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

#print(x)
#print(sum(x[0]), sum(x[2]))
#print(max(x[1]), max(x[2]))

if sum(x[0]) > sum(x[2]):
    print("True")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None")


'''Exercise 131 - Conditionals
Considering the code below, write code that prints out True! if the largest element of the first range minus the second element of the 3rd range is equal 
to the first element of the first range, prints out False! if the length of the first range minus the length of the 2nd range is equal to the first element 
of the 3rd range, prints out Maybe! if the sum of all the elements of the 3rd range divided by 2 returns a remainder of 0, and prints out None! otherwise.'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

#print(x)

if max(x[0]) - x[2][1] == x[0][0]:
    print("True!")
elif len(x[0]) - len(x[1]) == x[2][0]:
    print("False")
elif sum(x[2]) % 2 == 0:
    print("Maybe")
else:
    print("None")

'''Exercise 132 - Conditionals
Considering the code below, write code that prints out True! if the sum of the last 3 elements of the first range plus the sum of the last 3 elements 
of the 3rd range is equal to the sum of the last 3 elements of the 2nd range, and prints out False! if the length of the first range times 2 is
less than the sum of all the elements of the 3rd range.'''

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

#print(x)
#print(x[0][-3:],x[2][-3:], (x[1][-3:]))
#print(sum(x[0][-3:]),sum(x[2][-3:]), sum(x[1][-3:]))

if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print("True")
elif len(x[0]) * 2 < sum(x[2]):
    print("False")

'''
Exercise 133 - Conditionals
Considering the code below, write code that prints out True! if the 2nd character of the value at key 1 is also present in the value at key 4, 
and prints out False! otherwise.'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


#print(x[1][1] in x[4])


if x[1][1] in x[4]:
    print("True!")
else:
    print("False!")

'''Exercise 134 - Conditionals
Considering the code below, write code that prints out True! if the second to last character of the value at key 3 is the first character of 
the value at key 5, and prints out False! otherwise.'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}


print(x[3][-2].upper(), x[5].startswith("P"))


if x[3][-2] == x[5].startswith("P"):
    print("True")
else:
    print("False")

if x[3][-2] == x[5][0]:
    print("True!")
else:
    print("False!")

if x[3][-2].upper() == x[5][0]:
    print("True!")
else:
    print("False!")

'''
Exercise 135 - Conditionals
Considering the code below, write code that prints out True! if the number of characters of the smallest value 
in the dictionary is equal to the number of occurrences of letter a in the value at key 3, and prints out False! otherwise.'''

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

#print(min(x.values()))

#print(len(min(x.values())))
#print(x[3].count("a"))

if len(min(x.values())) == x[3].count("a"):
    print("True!")
else:
    print("False!")