#classes can represent real world objects with data and behavior that can be modified and changed

#if we want properties to be blank until we create an instance of the class, we can use instance variables
#instance variables can be set or changed upone the creation of an object/instance
#class variables - pre-set values that come with every instance, but can be changed later

#create a class called Dog.. Dog will have the following properties - name, age, animal
#Dog will always have the class property/variable of animal = "dog"
#name and age will be our instance variables

class Dog:
    #anytime we create a new Dog instance - animal = "dog"
    #class variable
    animal = "dog"

    #instance variables are used in arguments/parameters when creating an instance in order to set properties
    #constructor - initialize the instance variables with some data that the user or other parts of the program provide upon creation

    #constructors are special functions/methods in a class
    #they use some special keywords like self to create instance variables
    #self - an individual instances value or data (its own internal state).  Remember each instance has its own data that is separate from other instances

    # __init__ - constructor keyword in python

    #instance variables
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #we can make other methods/functions that define common behavior between all of the other instances
    #all dogs bark..so lets make a bark method
    def bark(self):
        print("WOOOOOOOFFFFFFF")


#create a new dog instance - two arguments it takes to represent name and age (remember order matters)
dog1 = Dog("Braxton",10)
print(dog1.name)
print(dog1.age)
print(dog1.animal)

dog1.bark()


#what is really cool about instance variables is we can say what TYPE of data we want, but not the actual values
#this is great because it is saying all dogs need a name and an age, but we dont know what that is until it is set
dog2 = Dog("Zilla", 3)
print(dog2.name)
print(dog2.age)
print(dog2.animal)

dog2.bark()