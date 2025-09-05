class my_class(object): #creating a class which inherts from the default "object" class
    #class constructor; initializing some variables and the method is called whenever you create a new instance of the class
    def __init__(self, routername, model, serialno, ios): 
        self.router_name = routername # "self" is a reference to the current instance of the class - attribute
        self.model_device = model # attribute
        self.serial_no = serialno # attribute
        self.d_ios = ios # attribute

    def print_router(self, manuf_date):
        self.created_date = manuf_date
        print("The router name is: ", self.router_name)
        print("The router model is: ", self.model_device)
        print("The serial number of: ", self.serial_no)
        print("The IOS version is: ", self.d_ios)
        print("The model and date combined: ", self.model_device, self.created_date)

router1 = my_class('R1', '2600', '123456', '12.4') 
#creating an object by simply calling the class name and entering the arguments required by the __init__ method in between parentheses
router1.print_router("21.05.2025") # accessing a function (actually called method) from within the class
print("------------------------------------------------------------------------------------------------")
router1.print_router("18.09.1986")
print(router1.serial_no)

print("")

print(getattr(router1, "d_ios")) #getting the value of an attribute
print(setattr(router1, "d_ios", "12.1")) #setting the value of an attribute
print(getattr(router1, "d_ios"))
print(hasattr(router1, "d_ios")) #checking if an object attribute exists
print(delattr(router1, "d_ios")) # deleting an attribute

print (isinstance(router1, my_class)) # verifying if an object is an instance of a particular class

class my_new_class(my_class): # creating a new class (child) inheriting from the my_class parent class
    pass

print(issubclass(my_new_class, my_class)) # returns True or False; checking if a class is the child of another class