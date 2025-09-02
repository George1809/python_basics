'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

#dict1 = {} #creating an empty dictionary

dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}

print(dict1)
print(dict1["IOS"]) # returns value of key ISO
dict1["IOS"] = "12.3" # modifies an existing key - value pair
print(dict1["IOS"])
dict1["RAM"] = "128" # add new key - value pair to the dictionary
dict1["EXT"] = 10
print(dict1)
del dict1["Ports"] # deleting a key-value pair from the dictionary
print(dict1)
print(len(dict1))
print("IOS" in dict1) # veryfies if "IOS" is a key in the dictionary
print("IOSS" not in dict1) # veryfies if "IOSS" is not a key in the dictionary

print("")
print("Dictionaries - methods")
print("")

print(dict1)
print(dict1.keys()) # returns a list having the keys in the dictionary as element
print(dict1.values()) # returns a list having the values in the dictionary as element
print(dict1.items()) # returns a list of tuples, each tuple containing the key and value of each dictionary pair
print(list(dict1.keys())) # returns only the list with the keys in the dictionay
print(list(dict1.values())) # returns only the list with the values in the dictionary
print(list(dict1.items())) # returns only the list with paier key values

print("")
# conversions between data types
str()
int()
float()
list()
tuple()
set()
# bin() # converting to a binary representation
# hex() # converting to a hexadecimal representation
# int(variable, 2) # converting from binary back to decimal
# int(variable, 16) # converting from hexadecimal back to decimal