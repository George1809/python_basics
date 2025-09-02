'''
For / For Else loops - executes a block of code a number of times, depending on the sequence it iterates on; the "else" clause is optional

With the while loop we can execute a set of statements as long as a condition is true.

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for element in vendors:
    print(element)
else:
    print("The end of the list has been reached")

print("")
#looping through a string


for c in "text":
    print(c)

#while
print("")

x = 1

while x <= 10:
    print(x)
    x += 1
else:
    print("Out of the while loop, x is now greater than 10")

print("")
#nested if, for and while

y = "Cisco"

if "i" in y:
    if len(y) > 3:
        print(y,len(y))
else:
    print("i not in", y)

if "i" not in y:
    if len(y) > 3:
        print(y,len(y))
else:
    print("i not in", y)


print("")
list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
    for j in list2: # for nesting
        print(i,j)
print("")

for i in list1:
    for j in list2: # for nesting
        print(i*j)
print("")

xyz = 1

while xyz <= 10:
    print(xyz)
    print("")
    z = 5
    xyz += 1
    while z <= 10: # while nesting
        print(z)
        z += 1
    print("")

for number in range(10):
    if 5 <= number <= 9: #mixed nesting
        print(number)

print("")
# Break / Continue / Pass

list3 = [4, 5, 6]
list4 = [10, 20, 30]

for i in list3:
    print("pas 1")
    for j in list4:
        print("pas 2")
        if j == 20:
            print("pas 3")
            break 
            '''stops the execution here, ignores the print statement below and
            completely quits THIS "for" loop; however, it doesn't quit the outer "for"
            loop, too!'''
        print(i,j)
        print(i*j)
 
    print("Outside the nested loop")

print("______________________________________")


for i in list3:
    print("pas 1")
    for j in list4:
        print("pas 2")
        if j == 20:
            print("pas 3")
            continue 
            '''ignores the rest of the code below for the current iteration,
            then goes up to the top of the loop (inner "for") and starts the next iteration'''
        print(i,j)
        print(i*j)

    print("Outside the nested loop")



for i in range(10):
    pass 
    '''pass is the equivalent of "do nothing"; it is actually a placeholder 
    for when you just want to write a piece of code that you will treat later'''


