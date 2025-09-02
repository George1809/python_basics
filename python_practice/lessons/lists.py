'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
'''


list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11] # list variable

print(list1)
print(len(list1)) # number of elements in the list
print(list1[1]) # returns the element index position (Juniper), starting from 0
print(list1[0])
list1[0] = "HP" # replacing the first element in the list with the new value 
print(list1[0])
print(list1)
print("")

list2 = [-11, 2, 12]
print(list2)
print(min(list2)) # returns the smallest element, value, in the list
print(max(list2)) # returns the max value in the list

print("")
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
print(list1)
list1.append(100) #add element in the list
list1.append("HP") # add element in the list
print(list1)
del list1[0] # deletes an element in the list
print(list1)
print(list1.pop(0)) # removing an element with pop, no matter is printing, list is modify
print(list1)
print(list1.remove("Avaya")) # removing an element in the list by value not by index
print(list1)
list1.insert(2, "Blaaa")
list1.insert(2, "Blaaa") # insterting an element at a particular index
print(list1)
list1.extend(list2) # appending a list to another list
list2.extend(list1)
print(list1)
print(list2)
print(list1.index(-11)) # returns the index of element -11
print(list1.count("Blaaa")) # returns the number of times element "Blaaa" is in the list

print("")
list3 = [9, 99, 999, 1, 25, 500]
list3.sort() # sorts the elements in ascending order by default and modifies the list
print(list3)
list3.reverse() # sorts the elements in descending order by default and modifies the list
print(list3)
print(sorted(list3)) # sorts ascending but not modify
print(sorted(list3, reverse=True)) # sorts descending and print but not modifies
print(sorted(list3, reverse=False)) # sorts ascending and print but not modifies
print(list3)

print("")
print(list1)
print(list2)
lists_concat = list1+list3 # concatenare 2 liste
print(lists_concat)
print(list1)
print(list1 * 3) # repetition of a list * x

print("")
print("Lists slicing")
print(list1)
print(list1[1:3]) # print from index 1 to 3 but execept 3, only 1 and 2
print(list1[3:]) # prints list starting from index 3
print(list1[-1]) # prints last element
print(list1[-2]) # prints lsecond to last element in the list
print(list1[-9:-1]) # a certain sublist using negative indexes
print(list1[:-5]) # returns the list without the last 5 elements in the list
print(list1[::2]) # element with steps and skips every second element of the list
print(list1[::-1]) # returns list in reverse order
print(-11 in list1) # returns True if -11 is in the list