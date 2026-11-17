#classes are like combining features of a dictionary and a function or group of function
#what is class - a class is a blueprint for an object that contains some data (attribute/properties) and functions(methods)

#functions and methods - pretty much the same thing.  The only difference is that methods belong to an object, and functions do not need an object to work or be callable (like the print function)

#instance - spawn or copy of a class. Concrete manifestation of a class.  It allows us to take a blueprint and make an actual object out of it

#think of a blueprint for a house, and the using those blueprints to build the house.  The built house would be like an instance

#objects that are associated with classes represent bundled data that defines what an object represents (often something in the real world)

#to us a class we first must define it like a function
#we just use they keyword class
#example - a person with a name and age
#we will use class variables at first so this will not useful until we use instance variables

class Person:
    #properties
    name = "Zach"
    age = 41

#we need to create instances of a class to use it.  Right now it is similar to a defined function in that we havent actually used it yet

#create an instance variable = classname()
instance1 = Person()

#access instance1s properties by using dot notation
print(instance1.name)
print(instance1.age)

#instances maintain their own state...which means that if we create instance2 and change its data, that will not affect instance1
instance2 = Person()
#change the variables also with dot notation
instance2.name = "Tim"
instance2.age = 50

print(instance2.name)
print(instance2.age)

print(instance1.name)
print(instance1.age)