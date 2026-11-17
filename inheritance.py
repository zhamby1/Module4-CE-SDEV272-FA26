#inheritance is the ability to inherit liek actions, data or functions from a base/parent class to a derived/child class
#it is called a is-a relationship.  For instance parent class called animal and a child class called Dog where dog is an animal
#it can inherit all the functions and data properties while at the same time modifying or updating those things to give it additional features
#URL for code https://www.youtube.com/watch?v=u1be7Vele5o

# Inheritance = Allows a class to inherit attributes and methods from another class
#                         Helps with code reusability and extensibility
#                         class Child(Parent)


#this is more a form of polymorphism - we can use the same name for inherited class methods/functions but they perform different implementations
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.speak()