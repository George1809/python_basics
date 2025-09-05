#List / Set / Dictionary comprehensions


list1 = []

for i in range(10):
    j = i ** 2
    print(j)
    list1.append(j)

print(list1)

print("---------------------------------------------------------")

list2 = []

for i in range(10):
    list2 += [i]
    print(i)

print(list2)

print("----------------------------------------------------------")

list3 = [x ** 2 for x in range(10)]
print(list3)
list4 = [x  ** 2 for x in range(10) if x >5] # with conditional stataments
print(list4)
set1 = {x **2 for x in range(10)} # set comprehension
print(set1)
dict1 = {x:x * 2 for x in range(10)} # dictionary comprehension
print(dict1)

print("----------------------------------------------------------")


x = 1
list_w = []
while x < 10:
    list_w += [x]
    x +=1

print(list_w)

print("----------------------------------------------------------")

# Lambda functions - anonymous functions

# lambda arg1, arg2, ..., arg n: an expression using the arguments #general syntax
a = lambda x, y: x * y # defining a lambda function
b = a(20,10)
print(b)