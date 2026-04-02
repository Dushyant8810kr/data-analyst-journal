"""Function is a block of code in which we write a code that perform a particuklar task .
like to find factorial,addition,multiplication etc. and we use this block of code by calling"""

# there are two types of function : 1. Inbuilt and 2. made by user

"""
#1

def Greet(): # Defining the fUnction
    print("Hello greeting from  Dushyant!!") #print work is simple and that is to print the thing in terminal
                                             # to provide the output to the terminal use only print function(IMP***)
Greet() #calling the Function

"""


"""
#2

def Greet():
    return "Hello Greetings from Dushyant" # Return is used to transfer the result at the place from where it is called.

print(Greet())

"""

"""
#3

def addition(a,b): # a,b are the "PARAMETER" which accepts the value form function calling
    print(a + b)

addition(12,45) # 12,45  both are the ARGUMENTS which is going to "addtition function"
addition(10,35)
addition(20,1)

"""

"""
#4

def pallindrome(x):
    rev = 0
    copy = x
    while x>0:
        rev = (rev*10) + (x%10)
        x//=10
    
    if rev == copy :
        return True
    else :
        return False
    
print(pallindrome(121)) #True
print(pallindrome(196)) #False

"""


#Imp :- functions are the thing in programming which increase the Reusability of a code


"""

#5
def addition(a,b,c):
    print(a+b+c)

# addition(b=12,56)   positional argument can't appear after keyword argument(at 56 there is an error) we write this like print(b=12,a=56)

#addition(56,b=12,c=10) 

"""

def addition (a,b=67,c=14): #here in this the value of b= 67 is overwrite by 10 and c=14 is overwrite by 20 
    print(a+b+c)            # default value of a parameter can be set at last not like this -> def addition(a,b=67,c)

addition(10,10,20)