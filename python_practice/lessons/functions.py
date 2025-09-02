def my_funct(x,y): #defining a function that takes two parameters
    sum = x + y
    return sum # this statement is used to exit a function and return something when the function is called - return save the value


rez = my_funct(1,2)
print(rez)
print(rez * 4)
print("Suma este", rez)


def function_1(x, y, z = 3): #specifying a default parameter value in a function definition
    ceva = x
    ceva2 = y
    ceva3 = z
    return ceva, ceva2, ceva3

rez = function_1(1,55)

print(rez)
print(rez[0])
print(rez[1])
print(rez[2])

print("")

# *args → all extra positional elements in a tuple.
# **kwargs → all extra keyword elements in a dict.

def function_2(x, *args): #specifying a variable number of positional parameters in a function definition; args is a tuple
    primul = x
    al_doilea = args # args takes more parameter value
    return primul, al_doilea 

rez1 = function_2(1,2,3,4,5,6,7,8,9,10,11)
print(rez1)
print(rez1[0]) 
print(rez1[1]) # save index of rezulted tuple
print(rez1[1][1]) # save number by index from a rezulted tuple for args

print("")

def function_3(x, **kwargs): #specifying a variable number of keyword parameters in a function definition; args is a tuple
    first = x
    second = kwargs # args takes more parameter value
    return first, second

rez2 = function_3(2, bla="trei", h=10, y="Wow") 
print(rez2)
separate1 = rez2[0]
separate2 = rez2[1]
print(separate1)
print(separate2)

print("")

#global my_var #"importing" a variable in the global namespace to the local namespace of a function

x = 10

def function_global_variable(y):
    #global x 
    x = 4
    sum = x + y
    return sum

rez3 = function_global_variable(10)
print(rez3)


print(x)