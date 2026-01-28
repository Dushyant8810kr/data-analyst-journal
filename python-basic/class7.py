#Question1:-
"""a= float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print("{a} is equal to {b}")"""


#Question2:-
"""gen= input("Enter your gender 'm' for male and 'f'for female: ")

if gen=='m':
    print("Hello sir")
else:
    print("Hello mam")"""


#Question3:-
"""gen= input("Enter your gender 'm' for male and 'f'for female: ")

if gen=='m' and gen == "M":
    print("Hello sir")
elif gen=="f" and gen=="F":
    print("Hello mam")
else:
    print("wrong input plase put valid input from m or f")"""


#Question4:-
"""num=int(input("Enter a number: "))

if num%2==0 :
    print("Number is even")
else:
    print("Number is odd")"""


#Question5:-
"""name=input("Enter your name: ")
age=int(input("Enter your age: "))

if age>=18:
    print(f"Hello {name} you can vote")
else:
    print(f" Hello {name} you can't vote")
    print(f"{18-age} year/years left for vote")"""

#question6:-
"""a=int(input("Enter your day(1-7): "))
if a==1:
    print("monday it is")
elif a==2:
    print("tuesday it is")
elif a==3:
    print("wednesday it is")
elif a==4:
    print("thursday it is")
elif a==5:
    print("friday it is")
elif a==6:
    print("saturday it is")
elif a==7:
    print("sunday it is")
else:
    print("sorry invalid input")"""

#Question7;-
"""a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))

if a==b and b==c:
    print("all 3 no.s are equals")
elif a==b or b==c or c==a:
    print("any 2 no.s are equal")
elif a>b and a>c:
    print(f"{a} is greatest")
elif b>a and b>c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")"""


#Question8:-(leap year)
#if year is divisible by 100 then the year is a century year and also divisible by 400 then it is a leap year.

"""year=int(input("please enter your year: "))

if year%100 and year%400:
    print("its a leap year")
elif year%100!=0 and year%4:
    print("its a leap year")
else:
    print("its not a leap year")"""


#Question9:-(shop discount calculator)

"""amt=float(input("Enter your purchase amount: "))

if amt>=1000 and amt<=4999:
    print(f"Your purchase amount is : ",amt-(amt*0.1))
elif amt>=5000:
    print(f"Your purchase amount is : ",amt-(amt*0.2))
else:
    print("Not any discount on purchase amount")"""


#Question10:-(consonant or vowels)
"""char = input("Enter your charcter: ")

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' :   # char in "aeiouAEIOU"
    print("Input char. is vowel")
else:
    print("input char. is consonant")"""





    
    



