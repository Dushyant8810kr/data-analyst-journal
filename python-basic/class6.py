#conditional statement :-

#Normal if else condition
age = int(input("Please tell your age - "))

if age>=18:#if this line true then the work inside in if condition works otherwise else statemenrt works
    print("hello you can vote.")
else :
    print("sorry you can't vote.")


# use of 'pass' :-
if age>=18:#if i want to pass the work of if condition then we use "pass" 
    pass
else :
    print("sorry you can't vote.")


#ternary operator :- use when there is only single line conditon(short form of if else condition)
print("vote") if age>=18 else print("not vote")


#elif condition:-(elif ladder)

money = int(input("please give me 10rs or 20rs or 30rs or above"))

if money==10:
    print("I will have a choco bar")

elif money==20:
    print("I will have a mango dolly")

elif money==30:
    print("I will have a cone")

else:
    print("I will have full course meal")


#conditional statement using logical operators:-

a=10
b=40
c=30

if a>b and a>c:
    print("A is the largest number")
elif b>a and b>c:
    print("B is the largest number")
else:
    print("C is the largest number")

    
