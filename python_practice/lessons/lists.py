list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11] # list variable

print(list1)
print(len(list1)) # number of elements in the list
print(list1[1]) # returns the element index position (Juniper), starting from 0
print(list1[0])
list1[0] = "HP" # replacing the first element in the list with the new value 
print(list1[0])
print(list1)

list2 = [-11, 2, 12]
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
