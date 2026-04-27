#Dunder/magic method :- are those mmethods that chnages the 'Objects' behaviour

class Students:
    #1
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    #2
    def __str__(self):
        return f"{self.name} is your name and your marks is {self.marks} "

obj = Students("Dushyant kumar",95)
print(obj)

class shopping:
    def __init__(self,items):
        self.items = items
    
    #3
    def __len__(self):
        return len(self.items)
    
obj = shopping(["watch","Perfume","Pen"])
obj2 = shopping(["apple","Shirt"])

print(len(obj))


class Numbers:
    def __init__(self,numbers):
        self.numbers = numbers
    
    def __add__(self,custom):
        return self.numbers + custom.numbers
    
obj1 = Numbers(12)
obj2 = Numbers(36)
print(obj1 + obj2)
        
        
        