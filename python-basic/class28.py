#Inheritance :- Inheritance is the mechanism by which a class (child) can use the property and methods of another class(parent).
class Animal:       #parent class , super class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"your name is {self.name} and your age is {self.age}")

class Human(Animal):        #child class , sub class
    def __init__(self, name, age,number,group):
        super().__init__(name, age)             # super() is connected with the Animal(parent) class (for initialisation purpose)
        self.number = number
        self.group = age

class Robot(Human):
    def __init__(self, name, age, number, group,imei):
        super().__init__(name, age, number, group)
        self.imei = imei

obj1 = Animal("Lion",12)
obj2 = Human("Dushynat",24,8810435223,"AB+")
obj3 = Robot("Chitti",3,1234567890,"NA","gduov#21")

"""
Type of inheritance :-
#1 single level inheritance :- one class inherits from another
#2 multilevel inhertance    :- class inherits from a class that already inherits from another class.

#3 Multiple inheritance :- a class inherits from multiple parents class
class Animal:
    name = "Lion"

class Human:
    name = "Dushyant"

class Robot(Human,Animal):
    pass
    

#4 Heierchical inheritance :- multiple classes inherit from single parent class.
class Animal:
    name = "lion"

class Human(Animal):
    pass

class Robot(Animal):
    pass
"""