from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        pass

    def hello(self):
        print("Hello i make a woof sound")

obj = Dog() # showing error : Can't instantiate abstract class Dog without an implementation for abstract method 'sound'
            #if you want to initiate the dog class you add the Animal class Abstarct sound method .