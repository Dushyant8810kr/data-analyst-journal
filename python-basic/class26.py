#like in functions we take parameters but in class we dont take any type of parameters
#so we make constructor for it
"""
class factory(material,zip,xyz):
    pass

factory()
"""



"""
class Factory:
    def __init__(self,material,zips,pockets):                  #self targeting the location of obj
        print("hello i wil run no matter what!!")              #__init__ is an initialize method

obj = Factory() """



class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips     = zips
        self.pockets  = pockets
    def showDetails(self):
        print(self.material,self.zips,self.pockets)

Reebok = Factory("leather",3,3) 
Campus = Factory("nylon",2,2) 
print(Reebok.material) 

Reebok.showDetails()