#we use class (Blueprint) to create an object

class Factory:
    a = "Hello i am an attribute"
    def hello(s):
        print("Hello i am a method")

obj = Factory()     #if you have a class and you call a class inside a variable then variable is known as object.
                    #this obj is capturing or points towards the location of Factory() and it can access the whole class till now.

obj2 = Factory()

print(obj.a)   # Hello i am an attribute
obj2.hello()   # Hello i am a method