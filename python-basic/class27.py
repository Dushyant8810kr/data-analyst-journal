
"""
class Animal :
    def __init__(self,name,age):
        gender = "Male"             #class attribute : because it can't use the object location it uses the class only so thats why
        self.name = name            #instance attribute : beacuse it is created by the help of object(obj).(it is using the object location)
        self.age = age
    
    def info(self):                 #instance method :- a method which using self keyword as parameter is known as insatnce method
        print("I am a method")      #self target the location of object 

    @classmethod        # cls not targeting any location of object . target on class location directly
    def clmethod(cls):      #class method
        print(f"{cls.gender} is your gender.")

    @staticmethod    #static method do not use (cls,self) type of keywords
    def hello():     #it is not dependent on any thing thats why this method name is static method
        print("hello i am static method")


obj = Animal("lion",12)
obj.info() #targeting the instance method
obj.clmethod()  #targetting the class method
obj.hello()"""
        

#notes:-
"""
1) instance attribute :- an attribute that is created using the self keyword like self.name,self.age....
2) Class attribute :- attribute created inside a class without using self keyword
3) instance method :- a method which using self keyword as parameter is known as insatnce method
4) class method :- class method use @classmethod decorator an do not rely on instance specific data

"""

#make a student management system ask for name,age,number,bloodgroup ,register only 3 students

class registration:
    def __init__(self,name,age,number,blood):
        self.name = name
        self.age = age 
        self.number = number 
        self.blood = blood

    def info(self):
        print(f"Your name is {self.name}\nyour age is {self.age}\nyour number is {self.number}\nyour blood group is {self.blood} ")


student1 = registration("Dushyant kumar",21,8810435223,"A+")
student2 = registration("Jatin",22,9582449328,"AB+")
student3 = registration("Suraj",20,8882131430,"O-")

student1.info()
student2.info()
student3.info()
