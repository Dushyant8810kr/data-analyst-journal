#Encapsulation :
"""
class Animal:
    name = "Lion"

    def speak(self):
        print("hello i will roar")

obj = Animal()
"""
# obj.name = "Zebra"   : by this we can change an attribute of class very easily.
# print(obj.name)      : Zebra

#like above we easily access the attributes and methods easily so we make an restriction for this in that scenerio the Encapsulation concept will come

#Encapsultion means building data(attributes) and methods into one unit(class).
#It also involves controlling access to these attributes using access modifiers.


#type of Access modifiers :-
#1) public : Accessible Anywhere. until now we were using public attributes and methods

#2) Protected : Accessible in the class and subclass.By the use of protected modifiers we access the methods and attributes in python but can't change them(as in c++ , Java we cant acess te protected modifiers)
"""
class Animal:
    _name = "Lion"

    def _speak(self):
        print("hello i will roar")

obj = Animal()
"""

#3) Private : by the use of private modifiers in attributes and methods we cant access them they showing an error.
"""
#Example 1 :-
class Animal:
    __name = "Lion"

    def __speak(self):
        print("hello i will roar")

obj = Animal()
print(obj.name) #AttributeError: 'Animal' object has no attribute 'name'
"""

#Example 2:
"""
class Animal:
    __name = "Lion"

    def __speak(self):
        print("hello i will roar")


class Human(Animal):
    def say(self):
        print(f"Hello my name is {super().name} ")
obj = Human()
print(obj.name) #AttributeError: 'Human' object has no attribute 'name'
"""