#map() - takes a function and a sequence as arguments and applies the function to all the elements of the sequence, returning a list as the result

def product10(a):
    return a * 10

list1 = range(11)

a = map(product10, list1) # applying the product10() function to each element of the list1

print(list(a))


def product10(a):
    return a * 10

rez = map(product10, [1, 2, 3, 4])
print(list(rez))


def multiply(x, y):
    return x * y

rez = map(multiply, [1, 2, 3], [10, 20, 30])
print(list(rez))


def sum3(a, b, c):
    return a + b + c

rez = map(sum3, [1, 2], [10, 20], [100, 200])
print(list(rez))


b = map((lambda a: a * 10), list1)
print(list(b))


#filter() - takes a function and a sequence as arguments and extracts all the elements in the list for which the function returns True

c = filter(lambda a: a > 5, list1)
print(list(c))