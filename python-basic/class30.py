#Polymorphism:-Polymorphism allowed different classes to define methods with same name but diffrent behaviour.In python it is typically acheived through method overriding

"""
#redefining a function :- In this if a function is already exist and you make 
# a function of same name as before then the first function is deleting(they like remove) then new existing one is there.
def hello():
    print("hello i am a function")

def hello():
    print("hello i am aslo a function")

"""


#In both of the class the Speak function is there and have different work(this concept is known as polymorphism)
"""class Animal:
    name = "lion"

    def speak(self):
        print("hello i roar")


class bird:
    name = "sparrow"

    def speak(self):
        print("hello i tweet")


obj = Animal()
obj2 = bird()

obj.speak()
obj2.speak()
"""

class Animal:
    name = "lion"

    def speak(self):
        print("hello i roar")


class Human:
    name = "Dushyant"

    def speak(self):
        # super().speak : if dont want any type of overriding then you use this.
        print("hello my name is dushyant.")


obj = Human()
obj.speak()

#Imp :-Human speak function override the speak function of their parents class.

#thre are two types of polymorphism :- 1) Overloading(this is not working in pyhton because when you make two functions of same name then the 2nd function overwrite the first function )   2)Overriding