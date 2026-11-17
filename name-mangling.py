#privating variables in other languages allow us to encapsulate data
#hide things behind the scenes where you cannot access variables/properties, without using a method/function
#the reason for this is because it allows for easier troubleshooting and class properties to be accessed in a certain way
#for example - you want to set a value to a property but need to check to see if its a number first.  This would be a good use of encapsulation


#python uses name mangling where the interpreter automatically renames the class propertie to start with two leading underscores so it cannot be accessed with a function/method

class BankAccount:
    def __init__(self,balance):
        #to name mangle we use __ before the self.property_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,value):
        if float(value):
            self.__balance = value
        else:
            print("value is not a number")


myaccount = BankAccount(100.00)
print(myaccount.get_balance())
myaccount.set_balance("asdfadsf")
print(myaccount.get_balance())