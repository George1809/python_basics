print("Hello files")


'''Exercise 191 - Files
Add the necessary code in between print's parentheses in order to read the content of test.txt as a string and have the result printed out to the screen.'''


print("---------------")

f = open("/workspace/files/test_awk.txt", "r")

print(f.read())
f.close()


'''Exercise 192 - Files
Add the necessary code in between print's parentheses in order to read the content of test.txt as a list where each element of the list is a row in the file, 
and have the result printed out to the screen.'''

print("---------------")


f = open("/workspace/files/test_awk.txt", "r")

print(f.readlines())
f.close()

'''Exercise 193 - Files
Add the necessary code on line 5 in order to bring back the cursor at the very beginning of test.txt before reading from the file once again.'''

print("---------------")

f = open("/workspace/files/test_awk.txt", "r")

f.read()

f.seek(0)

print(f.read())
f.close()

'''
Exercise 194 - Files
Add the necessary code on line 5 (in between the parentheses of print()) in order to get the current position of the cursor inside test.txt 
and have the result printed out to the screen.'''

print("---------------")

f = open("/workspace/files/test_awk.txt", "r")

f.read(5)

print(f.tell())
f.close()

'''Exercise 195 - Files
Add the necessary code on line 5 (in between the parentheses of print()) in order to get the current mode in which test.txt is open (read, write etc.) 
and have the result printed out to the screen.'''

print("---------------")

f = open("/workspace/files/test_awk.txt", "r")

f.read(5)

print(f.mode)

f.close()

'''Exercise 196 - Files
Add the necessary file access mode on line 1 in order to open test.txt for appending and reading at the same time.'''

print("---------------")

f = open("/workspace/files/test_awk.txt", "a+")

print(f.mode)
f.close()


'''Exercise 197 - Files
Add the necessary code on lines 3 and 4 in order to write the string python to test.txt and have the result of reading the file printed out to the screen.'''

print("---------------")

f = open("/workspace/files/test.txt", "w")

#f.write("python")
f.writelines(["Prima linie din exercitiu\n","A doua linie din exercitiu\n"])
f.close()

f = open("/workspace/files/test.txt", "r")

print(f.read())

f.close()

'''Exercise 198 - Files
Add the necessary code on lines 3 and 4 in order to write a list of strings ['python', ' ', 'and', ' ', 'java'] to test.txt and 
have the result of reading the file printed out to the screen.'''

print("---------------")


f = open("/workspace/files/test.txt", "w")

f.writelines(['python', ' ', 'and', ' ', 'java'])
f.close()

f = open("/workspace/files/test.txt", "r")

print(f.read())
f.close()

'''Exercise 199 - Files
Add the necessary code starting at line 1 in order to write the string python and also close test.txt properly using the with statement.'''

print("---------------")

with open("/workspace/files/test.txt", "w") as f:
    f.write("python")

f = open("/workspace/files/test.txt", "r")

print(f.read())
f.close()


'''Exercise 200 - Files
Add the necessary code on lines 4 and 5 in order to delete the entire content of test.txt.'''

with open("/workspace/files/test.txt", "w") as f:
    f.write("python")

#f = open("/workspace/files/test.txt", "r+")
#f.truncate()
#f.close()

f = open("/workspace/files/test.txt", "r")

print(f.read())
f.close()