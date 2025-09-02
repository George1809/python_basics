'''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable. Immutable lists (their contents cannot be changed by adding,
removing or replacing elements)

Tuples are written with round brackets.
'''

my_tuple = (1,2,3,4)

print(len(my_tuple)) # returns the number of elements in the tuple
#slicing
print(my_tuple[0]) # returns first element
print(my_tuple[-1]) # returns last element in the tuple
print(my_tuple[0:2]) # returns starting from 0 to 2, but without index 2
print(my_tuple[:2]) # returns all elements without the last two elements in the tuple
print(my_tuple[1:]) # returns all starting from index 1
print(my_tuple[:]) # returns all elements
print(my_tuple[-2:]) # returns last 2 negati indexes
print(my_tuple[::-1]) # returns reverse tuple, with step element added
print(my_tuple[::2]) # returns tuple skiping and element

print("")
#Tuples - tuple assignment / packing and unpacking
tuple1 = ("Cisco", "2600", "12.4")
(vendor, model, ios) = tuple1 #vendor will be mapped to "Cisco" and so are the rest of the elements with their corresponding values; both tuples should have the same number of elements

print(vendor + " " + model + " " + ios)

(a, b, c) = (1, 2, 3) #assigning values in a tuple to variables in another tuple
print(a,b,c)
print(min(tuple1)) # returns min value Unicode
print(max(tuple1)) # returns max value Unicode
tp = tuple1 + (5,6,7) # tuple concatenation
print(tp)
tp1 = tuple1 * 10 # tuple multipication
print(tp1)
print("2600" in tuple1) # true if 2600 in tuple
print(784 not in tuple1) # true if that value is not in tuple
#del duple1 # deleting a tuple

print("")
print("")
print("Ranges")
print("Define a range")
r = range(10) # define a range
print("")
print(r)
print(list(r)) # converting a range to a list
print(r)
print(list(r)[2:5]) # converting a range to a list and slicing it