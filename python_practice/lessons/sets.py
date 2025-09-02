'''
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.
'''

set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"} # creating a set

list1 = [11, 12, 13, 14, 15, 15, 15, 11]
string1 = "aaabcdeeefgg"

print(set1)
print(list1)
set1 = set(list1) # creating a set from a list, removing duplicate elements
print(set1)

set2 = set(string1) #creating a set from a string, removing duplicate and return {'a','b', etc} - sets are unordered collections of elements
print(set2)
print(len(set1), len(set2))
print(11 in set1) # true if 11 is an element of a set
print(10 not in set1) # true if 10 is not and element of a set
set1.add(17)
print(set1)
set1.remove(17)
print(set1)
print("")
print("Frozensets - immutable sets")
frzset1 = frozenset(list1) #defining a frozenset
print(frzset1)
print(type(frzset1))
#proving that frozensets are indeed immutable
#frzset1.add(111)
#frzset1.remove(11)
#same with .pop() and .clear

print("")
set1.add("d")
set1.add("g")
print(set1)
print(set2)
print(set1.intersection(set2)) # returns the common elements of the two sets
print(set1.difference(set2)) # returns the elements that set1 has and set2 doesn't
print(set1.union(set2)) # unifying towo sets with a set result, without duplicates
#set1.pop() # vomoves a random element from set
#set1.clear() # clearing a set = empty set

