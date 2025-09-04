# Files - opening and reading a file

my_file = open("/workspace/files/test_awk.txt", "r") # "r" is the file access mode for reading and it is the default mode when opening a file - opening an object

print(my_file.mode) #checking the mode in which a file has been opened
#print(my_file.read()) # method that returns the entire content of a file in the form of a string
print(my_file.read(5)) # returns only the first 5 characters (bytes) in the files - the next read, continues from the last read
print(my_file.read(5)) # returns next 5 characters
print(my_file.read(5)) # returns next 5 characters
(my_file.seek(0)) # moves the cursor at the begining of the file
print(my_file.read(5)) # return first 5 characters
print(my_file.read(17)) # return first 5 characters
print(my_file.tell()) # checking the current position of the cursor inside the file
print(my_file.readline()) # returns the file content one line a the time, each time the method is used
print(my_file.readline()) # new line
print(my_file.readline()) # new line
print(my_file.readline()) # new line

print(my_file.tell()) # checking the current position of the cursor inside the file

lines = my_file.readlines() # returns a list where each element is a line in the file
print(lines)
print("")

print(my_file.tell()) # checking the current position of the cursor inside the file
print(my_file.read(5)) # nothing to print, end of the file
print(lines[0:2]) 

print("")
my_file.close() # closing file

#Files - writing and appending to a file

new_file = open("/workspace/files/newfile.txt", "w")
'''opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and
overrides the file if the file already exists; remember to close the file after writing to it to save the changes!'''

new_file.writelines(["Avem aici prinul rand\n", "Avem aici al doilea rand\n", "Avem aici al treilea rand\n"])
# this method takes a sequence of strings as an argument and writes thoese strings to the file
new_file.close()

my_new_file = open("/workspace/files/newfile.txt", "r")
print(my_new_file.read())
my_new_file.close

print("------------------------------------------------------------------------------------------------------------")

#new writing - overwriting
new_file = open("/workspace/files/newfile.txt", "w")

new_file.writelines(["Avem aici primul rand\n", "Avem aici al doilea rand\n", "Avem aici al treilea rand\n"])
# this method takes a sequence of strings as an argument and writes thoese strings to the file
new_file.close()

my_new_file = open("/workspace/files/newfile.txt", "r")
print(my_new_file.read())
my_new_file.close

print("------------------------------------------------------------------------------------------------------------")


new_file = open("/workspace/files/newfile.txt", "a") # open file again
new_file.writelines(["Avem aici al patrulea rand\n", "Avem aici al cincilea rand\n"]) # appending text to the file
new_file.close()

my_new_file = open("/workspace/files/newfile.txt", "r")
print(my_new_file.read())
my_new_file.close

print("------------------------------------------------------------------------------------------------------------")

newfile = open("/workspace/files/newfile.txt", "w+") #opens a file for both writing and reading at the same time, but "w+ truncate the file and star over"
newfile.writelines(["Prima linie\n", "Linia 2"])
newfile.seek(0)
print(newfile.read())
newfile.close

print("------------------------------------------------------------------------------------------------------------")


with open("/workspace/files/newfile.txt", "r") as f: #using the with-as solution, the files gets closed automatically, without needing the close() method
    print(f.read())


#Truncating files - the file should be open for reading AND writing, not just reading!
# f = open("/workspace/files/newfile.txt", "r+")
# f.truncate() #this deletes all the content inside the file
#Truncating files - the file should be open for reading AND writing, not just reading!
#f = open("/workspace/files/", "r+")
#f.truncate(1) #this will keep the first 10 characters in the file and delete the rest