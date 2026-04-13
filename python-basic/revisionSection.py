#class 2 revision:-
"""
PYTHON REVISION NOTES (Class 2)
1.Print Function :-
print() : is used to display output on screen
print("Hello world")

2. Comments:-
Comments are not executed by Python
# Single line comment
"""" Multi-line comment """"

3. Variables :-
Variables are containers used to store data
a = 10
name = "Dushyant"

4. Variable Naming Rules:-
-> Cannot start with number : (1hello)
-> Cannot contain space : (hello world)
-> Can use underscore _ : (hello_world)
-> Can start with _ : (_name)

5. Naming Conventions:-
camelCase → dushyantKumar
PascalCase → DushyantKumar
snake_case → dushyant_kumar

6. Data Types:-
a = 10
b = 1.5
c = 2j
name = "Dushyant"
x = True

7. Type Checking:-
print(type(a))

8. Important Concepts:-
Python is Case Sensitive: True , true 
Dynamic Typing: a = 10 a = "hello"

9. String Rules
Strings must be inside quotes ("" or '')
 
YOUR MISTAKES (IMPORTANT):-
1. Incomplete Output: Write full output including type
2. Forgot printing types using print(type())
3. Careless spelling mistakes
 EXTRA UNDERSTANDING
"10" is string, 10 is integer
"10" + "20" = "1020", 10 + 20 = 30

"""

#class 3 :-
"""
PYTHON REVISION TEST (Class 2 : Strings, Slicing, Input):-


Section 1: Output Prediction:-

a = "NATURE"
print(a[2])  # T
print(a[-3])  # U

b = "sheriyans coding"
print(b[0:5])  # sher i
print(b[5:10])  # yans (with space)


Section 2: Slicing Logic :-

c = "hello i am data Scientist"
print(c[6:10])  # i am
print("Python"[::-1])  # nohtyP


Section 3: Concepts :-

Strings are immutable → cannot change directly
input() always returns string
Raw string ignores escape sequences


Section 4: Errors :-
a = "Hello"
a[0] = "Y"  # 
Error
age = int(input("Enter age: "))
print(type(name))  # 


Section 5: Boolean:-

name not defined
print(bool(0))    # False
print(bool(" "))  # True
print(bool(""))   # False

Challenge
name = input("Enter your name: ")
print(f"Hello {name}")
YOUR MISTAKES :-

1. Confusion in immutability strings
2. Reverse slicing not understood
3. Boolean concept mistake (' ' vs '')
4. Skipped challenge question

KEY CONCEPTS:-
Immutable → cannot modify string directly
[::-1] → reverse string
Truthy vs Falsy values matte

"""


#class 4 :-
"""
PYTHON REVISION NOTES (Class 4):-

1. Arithmetic Operators
Operator Meaning
+
Addition
Example
12 + 34 = 46
*
/
//
**
%

2. BODMAS Rule:-
print(10 + 2 * 5)
print((10 + 2) * 5)

3. Division Difference:-
print(12 / 5)   # 2.4
print(12 // 5)  # 2

4. Assignment Operators:-
a = 10
a = a + 5
a += 5

5. String Operations :-
print("hello" + " world")
print("hello" * 3)

6. Invalid Operation :-
print("hello" + 3)  # Error

7. Special Case:-
print("5" * 3)  # 555

8. Modulo Usage:-
print(10 % 2)
print(7 % 2)

YOUR MISTAKES :-
Subtraction
Multiplication
Division
12 - 34 = -22
12 * 34 = 408
12 / 5 = 2.4
Floor Division 12 // 5 = 2
Power
Modulo:-
1. Float vs Integer confusion (/ always float)
2. Incomplete concept explanation
3. Did not follow input requirement
5 ** 2 = 25
17 % 5 = 2

4. Weak explanation style:-
EXTRA UNDERSTANDING
print(5 + 2 * 3 ** 2)
 TASK
Revise and practice BODMAs

"""


#class 5 :-

"""
PYTHON REVISION NOTES (Comparison & Logical Operators):-

1. Comparison Operators:-
Operator Meaning
Example:-
==
Equal to
12 == 12 → True
!=
>
<
>=
<=


2. Boolean Results:-
print(12 == 12)
print(12 != 12)

3. Logical Operators :-
AND → all conditions true
OR → any one condition true
NOT → reverse result
print(10 > 5 and 20 > 10)
print(10 > 5 or 20 < 10)
print(not True)

4. Chained Comparison (Important):-
Not equal
Greater than
Less than
12 != 12 → False
10 > 5 → True
5 < 10 → True
Greater or equal 10 >= 10 → True
Less or equal
print(10 > 5 == True)
# means (10 > 5) and (5 == True)

5. Even Odd Logic:-
a = int(input())
if a % 2 == 0:
    print('Even')
else:
    print('Odd')
    
YOUR MISTAKES:-
1. Confusion in chained comparison
2. Weak explanation clarity
3. Minor formatting mistakes
 SUMMARY
Operator Rule
5 <= 10 → True
AND
All True



"""


#class 6:-
"""
PYTHON REVISION NOTES (Conditional Statements):-

1. if-else Statement
age = int(input("Enter age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

2. pass Keyword:-
if age >= 18:
    pass
else:
    print("Not allowed")

3. Ternary Operator :-
print("Vote") if age >= 18 else print("Not Vote")

4. elif Ladder :-
money = int(input("Enter money: "))
if money == 10:
    print("Choco bar")
elif money == 20:
    print("Mango dolly")
elif money == 30:
    print("Cone")
else:
    print("Meal")

5. Logical Conditions :-
a = 10
b = 40
c = 30
if a > b and a > c:
    print("A is largest")
elif b > a and b > c:
    print("B is largest")
else:
    print("C is largest")

YOUR MISTAKES:-
1. Wrong condition range (used 55 instead of 50)
2. Unnecessary conditions like <=100
3. Need cleaner logic writing
 
SUMMARY
Concept Key Point:-
if-else ->decision making
elif    ->ladder checking
pass    ->do nothing
ternary ->short form

"""

#class 8 :-
"""
PYTHON REVISION NOTES (Loops)
1. Loops :-
Loops are used to perform repetitive tasks.

2. Types of Loops:-
for loop → when number of iterations is known
while loop → when condition is known

3. range() Function :-
range(start, stop, step)
Example:
for i in range(5):
    print(i)  # 0 to 4

4. Examples:-
# 10 to 40
for i in range(10, 41):
    print(i)
# -10 to 20
for i in range(-10, 21):
    print(i)
# 34 to 5
for i in range(34, 4, -1):
    print(i)

5. Table Program:-
n = int(input("Enter number: "))
for i in range(n, n*10+1, n):
    print(i)

6. String Loop:-
s = "Dushyant"
for i in s:
    print(i)
for i in range(len(s)):
    print(s[i])

YOUR MISTAKES :-
1. Forgot that range(5) starts from 0
2. Confusion in step direction
3. Skipped some questions

SUMMARY:-
Concept -> Key Point
range   -> stop  excluded
default start   -> 0
step    -> direction matters
string loop -> value vs index

"""

#class 12 :-
"""
PYTHON REVISION NOTES (Functions):-
1. What is Function?
A function is a block of code used to perform a specific task and can be reused.

2. Types of Functions:-
1. Inbuilt functions (print, len, etc.)
2. User-defined functions

3. Function Syntax:-
def greet():
    print("Hello")
greet()

4. print vs return:-
def f():
    print(10)
def g():
    return 10
print() → only displays output
return → sends value back to caller

5. Parameters & Arguments:-
def add(a, b):  # parameters
    return a + b
add(10, 20)  # arguments

6. Default Arguments:-
def add(a, b=10):
    return a + b
 Rule: Default arguments must come after non-default arguments
def add(a, b=10):
    print(a + b)
add(5)      # 15
add(5, 20)  # 25

7. Example: Even/Odd Function:-
def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd" 

8. Factorial Function:-
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

YOUR MISTAKES:-
1. Confusion between print and return
2. Function stops after first return
3. Weak explanation of errors

SUMMARY:-
Concept -> Key Point
functionn -> reusability
return    -> gives value
print     -> just displays
default arg-> must be last"""