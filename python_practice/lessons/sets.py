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
print(set1)

