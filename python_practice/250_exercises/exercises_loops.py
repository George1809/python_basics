print("Hello Loops")


'''Exercise 136 - Loops
Write a for loop that iterates over the x list and prints out all the elements of the list.'''

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for g in x:
    print(g)

'''Exercise 137 - Loops
Write a for loop that iterates over the x list and prints out the remainders of each element of the list divided by 3.'''

print("---------")
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for g in x:
    rez = g % 3
    print(rez)

'''Exercise 138 - Loops
Write a for loop that iterates over the x list and prints out all the elements of the list in reversed order and multiplied by 10.'''

print("---------")
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

#print(x[::-1])

for h in x[::-1]:
    print(h * 10)

#for i in sorted(x, reverse = True):
#	print(i * 10)

'''
Exercise 139 - Loops
Write a for loop that iterates over the x list and prints out all the elements of the list divided by 2 and the string Great job! after the list is exhausted.'''

print("---------")
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for div in x:
    print(div % 2, "Great job!")


for i in x:
    print(i / 2)
else:
    print("Great job!")

'''Exercise 140 - Loops
Write a for loop that iterates over the x list and prints out the index of each element.'''

print("---------")
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

#print(x.index(10))


for idx in x:
    print(x.index(idx))

'''
Exercise 141 - Loops
Write a while loop that prints out the value of x squared while x is less than or equal to 5. Be careful not to end up with an infinite loop!'''

print("---------")
x = 0

while x <= 5:
    print(x ** 2)
    x +=1

'''Exercise 142 - Loops
Write a while loop that prints out the value of x times 10 while x is less than or equal to 4 and then prints out Done! when x becomes larger than 4. 
Be careful not to end up with an infinite loop!'''

print("---------")
x = 0

while x <= 4:
    print(x * 10)
    x += 1
print("Done!")

'''Exercise 143 - Loops
Write a while loop that prints out the value of x plus 10 while x is less than or equal to 15 and the remainder of x divided by 5 is 0. 
Be careful not to end up with an infinite loop!'''

print("---------")
x = 10

while x <= 15 and x % 5 == 0:
    print(x + 10)
    x += 1

'''Exercise 144 - Loops
Write a while loop that prints out the absolute value of x while x is negative. Be careful not to end up with an infinite loop!'''

print("---------")
x = -7

while x < 0:
    print(abs(x))
    x += 1

'''Exercise 145 - Loops
Write a while loop that prints out the value of x times y while x is greater than or equal to 5 and less than 10, and prints out the result of x 
divided by y when x becomes 10. Be careful not to end up with an infinite loop!'''

print("---------")
x = 5
y = 2


while x >= 5 and x < 10:
    z = x * 2
    print(z)
    x += 1
print(x % y)

'''Exercise 146 - Loops
Write code that will iterate over the x list and multiply by 10 only the elements that are greater than 20 and print them out to the screen.

Hint: use nesting!'''

print("---------")
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in x:
    if i > 20:
        print(i * 10)

'''Exercise 147 - Loops
Write code that will iterate over the x and y lists and multiply each element of x with each element of y, also printing the results to the screen.

Hint: use nesting!'''


print("---------")
x = [2, 4, 6]
y = [5, 10]

for i in x:
    for j in y:
        print(i * j)

'''Exercise 148 - Loops
Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than 12, 
also printing the results to the screen.

Hint: use nesting!'''

print("---------")
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for g in x:
    for h in y:
        if h < 12:
            print(g * h)

'''Exercise 149 - Loops
Write code that will iterate over the x and y lists and multiply each element of x that is greater than 5 with each element of y that is less than 12, 
also printing the results to the screen. Hint: use nesting!'''

print("---------")
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for t in x:
    for e in y:       
        if t > 5 and e < 12:
            print(t * e)
            
'''Exercise 150 - Loops
Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than or equal to 10, 
also printing the results to the screen. For y's elements that are greater than 10, multiply each element of x with y squared.

Hint: use nesting!'''

print("---------")
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for t in x:
    for e in y:
        if e <= 10:
            print(t*e)
        else:
            print(t * e**2)


'''Exercise 151 - Loops
Write code that will print out each character in x doubled if that character is also inside y.

Hint: use nesting!'''


print("---------")
x = "cryptocurrency"
y = "blockchain"


for c in x:
    for d in y:
        if c == d: 
            print(c, d)

for c in x:
    if c in y:
        print(c * 2)

'''
Exercise 152 - Loops
Write code that will iterate over the range generated by range(9) and for each element that is between 3 and 7 inclusively print out the result of multiplying 
that element by the second element in the same range.

Hint: use nesting!'''


print("---------")
my_range = range(9)


for r in my_range:
    if r >= 3 and r <= 7:
        print(r*my_range[1])

for r in my_range:
    if r >= 3 and r <= 7:
       print(r*list(my_range)[1])

for i in my_range:
    if 3 <= i <= 7:
        print(i * my_range[1])

'''Exercise 153 - Loops
Write code that will iterate over the range starting at 1, up to but not including 11, with a step of 2, and for each element that is between 3 and 8 
inclusively print out the result of multiplying that element by the last element in the same range. For any other element of the range (outside [3-8]) 
print Outside!

Hint: use nesting!''' 

my_range = range(1,11,2)

print(list(my_range))

for r in my_range:
    if 3 <= r <= 8:
        print(r * my_range[-1])
    else:
        print("Outside")

print("")

for i in range(1,11,2):
    if 3 <= i <= 8:
        print(i * range(1,11,2)[-1])
    else:
        print("Outside!")

'''Exercise 154 - Loops
Write code that will iterate over the range starting at 5, up to but not including 25, with a step of 5, and for each element that is between 10 and 21 
inclusively print out the result of multiplying that element by the second to last element of the same range. For any other element of the range 
(outside [10-21]) print Outside! Finally, after the entire range is exhausted print out The end!

Hint: use nesting!'''

print("---------")
my_range = range(5,25,5)


print(list(my_range))


for geo in my_range:
    if 10 <= geo <= 21:
        print(geo * my_range[-2])
    else:
        print(geo, "Outside!")

print("")

for geo in range(5,25,5):
    if 10 <= geo <= 21:
        print(geo * range(5,25,5)[-2])
    else:
        print(geo, "Outside!")


'''Exercise 155 - Loops
Write a while loop that prints out the value of x times 11 while x is less than or equal to 11.  When x becomes equal to 10, print out x is 10! 
Be careful not to end up with an infinite loop!'''

print("---------")
x = 5

while x <= 11:
    if x == 10:
        print("x is 10")
    else:
        print(x * 11)
    
    x +=1

# while x <= 11:
#    if x == 10:
#        print("x is 10!")
#        x = x + 1
#    else:
#        print(x * 11)
#        x = x + 1

'''Exercise 156 - Loops
Insert a break statement where necessary in order to obtain the following result:

1
1
100
20
10'''

print("---------")
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        print(i, j)

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            break
        print(i)
    print(j)


'''Exercise 157 - Loops
Insert a break statement where necessary in order to obtain the following result:

1
10
20
2
10'''

print("---------")
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i*j)
        print(i)
        break
    print(j)


'''Exercise 158 - Loops
Insert a break statement where necessary in order to obtain the following result:

1
1
100
10'''


print("---------")

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            break
        print(i)
    print(j)

print("")

for i in x:
    for j in y:
        if i % 2 == 0:
            break
            print(i * j)
        print(i)
    print(j)

'''Exercise 159 - Loops
Insert a continue statement where necessary in order to obtain the following result:

1
1
100
20
200
100'''


print("---------")
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            continue
        print(i)
    print(j)


'''Exercise 160 - Loops
Insert a continue statement where necessary in order to obtain the following result:

1
1
100
100'''

print("---------")
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 != 0:
            print(i)  
            continue
    if j % 2 == 0:
        print(j)
        continue


for i in x:
    for j in y:
        if i % 2 == 0:
            continue
            print(i * j)
        print(i)
    print(j)