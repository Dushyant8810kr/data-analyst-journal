#exception handling :-
#When we run a program in python there a various exception that can be raised.(ex:-syntax error ,name error ,zero division error etc.)

#exceptions are raised when the program is syntactically correct,but the code results in an error.this error doesnot stops the execution of program,however,it changes the normal flow of the program.
#so you cant handle the syntax error.But if there is no syntax error you can handle them.

#1:-
"""
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

try:            #"try" will catch the exception if any and pass to "except".
    print(a/b)
except Exception as err:        #except will deal with this exception.you can have customs exception or universal catcher.
    print(f"Sorry an error occured as {err}")
else:
    print("there was no errors.")                       #else will be excuted if no exception occurs or it wont be executed.
finally:
    print("I will execute no matter what.")             #thia will definately runs no what happens.
print(a + b)

"""

#2 :-
try:
    age = int(input("Enter your age :"))
    if age <18 :
        raise Exception("You must be 18+")          #raise a custom error as you need.
    print("access granted")
except Exception as e:
    print("Error:",e)