print("Hello Classes")


'''Exercise 231 - Classes
Write a class called ClassOne starting on line 1 containing:

The __init__ method with two parameters p1 and p2. Define the corresponding attributes inside the __init__ method.

A method called square that takes one parameter p3 and prints out the value of p3 squared.'''

print("----------------")

class ClassOne():
    def __init__(self,p1,p2):
        self.var_p1 = p1
        self.var_p2 = p2

    def square(self, p3):
        self.var_p3 = p3
        print(p3 ** 2)

    

p = ClassOne(1, 2)
print(type(p))
p.square(5)

print(p.var_p1, p.var_p2, p.var_p3)


'''Exercise 232 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to access the p1 attribute for the current instance of the class 
and print its value to the screen.'''

print("----------------")



class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

print(p.p1)
print(p.p2)
p.square(2)


'''Exercise 233 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to call the square() method for the current instance of 
the class using 10 as an argument and print the result to the screen.'''


print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

p.square(10)

'''Exercise 234 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to set the value of the p2 attribute to 5 
for the current instance of the class, without using a function.'''

print("----------------")


class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

setattr(p,"p1", 5)
setattr(p,"p2", 57)
#p.p2 = 5 # another way to set a new value for an attribute


print(p.p1)
print(p.p2)


'''Exercise 235 - Classes
Considering the ClassOne class and the p object, write code on lines 11 and 12 in order to set the value of the p2 attribute to 50 for the current 
instance of the class using a function, and then get the new value of p2, again using a function, and print it out to the screen as well.'''

print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

setattr(p, "p2", 50)
print(getattr(p,"p2"))


'''Exercise 236 - Classes
Considering the ClassOne class and the p object, write code on line 11 in order to check if p2 is an attribute of p, 
using a function, also printing the result to the screen.'''

print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

print(hasattr(p, "p2"))


'''
Exercise 237 - Classes
Considering the ClassOne class and the p object, write code on line 11 to check if p is indeed an instance of the ClassOne class, 
using a function, also printing the result to the screen.'''

print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)

print(isinstance(p, ClassOne))


'''Exercise 238 - Classes
Considering the ClassOne class, write code starting on line 9 to create a child class called ClassTwo that inherits from ClassOne and also has its 
own method called times10() that takes a single parameter x and prints out the result of multiplying x by 10.'''

print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self, x):
        print(x * 10)


y = ClassTwo(10, 20)
print(y.p1)

'''Exercise 239 - Classes
Considering the ClassOne and ClassTwo classes, where the latter is a child of the former, write code on line 15 in order to call the times10() method 
from the child class having x equal to 45, also printing the result to the screen.'''

print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self, x):
        return x * 10
        
obj = ClassTwo(15, 25)

result = obj.times10(45)

print(result)


'''
Exercise 240 - Classes
Considering the ClassOne and ClassTwo classes, write code on line 13 to verify that ClassTwo is indeed a child of ClassOne, 
also printing the result to the screen.'''

print("----------------")

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

class ClassTwo(ClassOne):
    def times10(self, x):
        return x * 10
    
print(issubclass(ClassTwo,ClassOne))
print(issubclass(ClassOne,ClassTwo))

